import sqlite3

def read_processed_keys(db_name='keys.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('SELECT key FROM processed_keys')
    keys = cursor.fetchall()
    conn.close()
    return [key[0] for key in keys]

def delete_processed_key(key, db_name='keys.db'):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    cursor.execute('DELETE FROM processed_keys WHERE key = ?', (key,))
    conn.commit()
    conn.close()

def main():
    while True:
        print("\nOptions:")
        print("1. Read processed keys")
        print("2. Delete a processed key")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            processed_keys = read_processed_keys()
            print("\nProcessed Keys:")
            for i, key in enumerate(processed_keys, 1):
                print(f"{i}. {key}")
        elif choice == '2':
            processed_keys = read_processed_keys()
            print("\nProcessed Keys:")
            for i, key in enumerate(processed_keys, 1):
                print(f"{i}. {key}")
            key_index = int(input("Enter the number of the key to delete: ")) - 1
            if 0 <= key_index < len(processed_keys):
                delete_processed_key(processed_keys[key_index])
                print(f"Key '{processed_keys[key_index]}' deleted.")
            else:
                print("Invalid number.")
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
