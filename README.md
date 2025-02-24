# Defectdojo-add-multiple-API-scan-configuration

## Overview

This script automates the process of adding multiple API scan configurations in DefectDojo for SonarQube projects. Since each SonarQube project requires a separate API scan configuration, manually adding them is time-consuming. This automation fetches project keys from SonarQube, checks if they have been processed before, and submits them to DefectDojo automatically.

## Files & Purpose

1. **main.py** (Core Script)
   - Fetches SonarQube project keys via API.
   - Checks if the key has already been processed using an SQLite database.
   - Submits API requests to DefectDojo to add API scan configurations.
   - Stores processed keys in the database to prevent duplicates.

2. **readdb.py** (Optional Utility)
   - Reads all processed keys from the database.
   - Allows users to delete specific keys if needed.
   - Provides a simple menu to manage stored keys.

## How It Works

1. The script fetches a list of SonarQube project keys.
2. It checks each key in a local SQLite database to avoid duplicate processing.
3. If a key is new, it submits an API request to add an API scan configuration in DefectDojo.
4. The key is then stored in the database as processed.
5. Users can view or delete processed keys using `readdb.py` (optional).

## How to Use

### 1. Setup

Install dependencies:
```sh
pip install requests urllib3
```

Update SonarQube & DefectDojo API URLs and Tokens inside `main.py`.

### 2. Run the Script

To automate API scan configuration addition, run:
```sh
python main.py
```

To view or manage processed keys (optional), run:
```sh
python readdb.py
```
- 1 → View processed keys.
- 2 → Delete a specific key.
- 3 → Exit.

## Key Benefits

- ✅ Saves time by automating bulk API scan configurations.
- ✅ Prevents duplicate processing using a local database.
- ✅ Easy to manage and track processed keys.

This README provides a clear overview of how the script works and how to use it efficiently. 🚀
