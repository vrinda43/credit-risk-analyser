import json
import os
from config.settings import DATA_FILE

def ensure_data_file_exists():
    """
    Creates the data folder and applicants.json file if they do not exist.
    """
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w') as f:
            json.dump([], f)

def load_all_applicants():
    """
    Reads all applicant records from the JSON file.
    """
    ensure_data_file_exists()
    try:
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

def save_applicant_record(record):
    """
    Appends a new applicant record to the JSON file.
    """
    records = load_all_applicants()
    records.append(record)
    with open(DATA_FILE, 'w') as f:
        json.dump(records, f, indent=4)
    return True

def delete_applicant(applicant_name):
    """
    Deletes an applicant record by name.
    """
    records = load_all_applicants()
    updated_records = [r for r in records if r['name'].lower() != applicant_name.lower()]
    if len(records) == len(updated_records):
        return False
    with open(DATA_FILE, 'w') as f:
        json.dump(updated_records, f, indent=4)
    return True