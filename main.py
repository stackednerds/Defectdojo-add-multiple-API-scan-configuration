import requests
import urllib3
import sqlite3

# Suppress only the single InsecureRequestWarning from urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Global constants
SONARQUBE_API_URL = "https://URL/api/projects/search"
SONARQUBE_API_TOKEN = ""
DD_POST_API_URL = "http://URL/api/v2/product_api_scan_configurations/"
DD_POST_API_TOKEN = ""

class Database:
    def __init__(self, db_name='keys.db'):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS processed_keys (key TEXT PRIMARY KEY)''')
        self.conn.commit()

    def is_key_processed(self, key):
        self.cursor.execute('SELECT 1 FROM processed_keys WHERE key = ?', (key,))
        return self.cursor.fetchone() is not None

    def mark_key_as_processed(self, key):
        self.cursor.execute('INSERT INTO processed_keys (key) VALUES (?)', (key,))
        self.conn.commit()

    def close(self):
        self.conn.close()

def get_data():
    headers = {
        "Authorization": SONARQUBE_API_TOKEN
    }
    
    try:
        res = requests.get(SONARQUBE_API_URL, headers=headers, verify=False)
        data = res.json()
        keys = [component['key'] for component in data['components']]
        print(keys)
        return keys
        
    except Exception as e:
        print('Error:', e)
        return

def post_data(key):
    headers = {
        "Authorization": DD_POST_API_TOKEN,
        "Content-Type": "application/json"
    }
    
    payload = {
        "service_key_1": key,
        "service_key_2": "",
        "service_key_3": "",
        "product": 1,
        "tool_configuration": 3
    }
    
    try:
        res = requests.post(DD_POST_API_URL, headers=headers, json=payload, verify=False)
        print(res.json())
        return res.json()
        
    except Exception as e:
        print('Error:', e)
        return

def main():
    db = Database()
    keys = get_data()
    if keys:
        for key in keys:
            if not db.is_key_processed(key):
                post_data(key)
                db.mark_key_as_processed(key)
    db.close()

if __name__ == "__main__":
    main()
