#storage.py

import json
import os

DB_FILE = 'users.json'


def delete_by_email(email):
    users = load_all()
    users = [user for user in users if user["email"] != email]
    with open(DB_FILE, 'w') as f:
        json.dump(users, f, indent=2)


def save(user):
    users = load_all()
    users.append(user)
    with open(DB_FILE, 'w') as f:
        json.dump(users, f, indent=2)

def load_all():
    if not os.path.exists(DB_FILE):
        return[]
    with open(DB_FILE, 'r') as f:
        return json.load(f)