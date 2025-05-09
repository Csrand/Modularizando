# user.py

import storage

def create_user(name, email):
    user = {"name": name,"email":email}
    storage.save(user)


def list_users():
    users = storage.load_all()
    for user in users:
        print(f"{user['name']} - {user['email']}")


def delete_user_by_email(email):
        storage.delete_by_email(email)



