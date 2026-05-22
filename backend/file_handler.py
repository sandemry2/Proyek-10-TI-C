import os

# Path ke users.txt selalu relatif dari root project (folder tempat main.py berada)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
USERS_FILE = os.path.join(BASE_DIR, "data", "users.txt")


def load_users():
    users = []
    try:
        with open(USERS_FILE, "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                data = line.split(",")
                if len(data) >= 2:
                    user = {
                        "username": data[0].strip(),
                        "password": data[1].strip()
                    }
                    users.append(user)
    except FileNotFoundError:
        print(f"  [!] File users tidak ditemukan: {USERS_FILE}")
    return users


def save_user(username, password):
    with open(USERS_FILE, "a") as file:
        file.write(f"\n{username},{password}")
