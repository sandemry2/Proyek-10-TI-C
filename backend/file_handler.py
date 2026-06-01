"""
FILE HANDLER
Fungsi:
1. Load & save user login
2. Load & save antrean medis

Dipakai untuk menyimpan data dinamis agar tidak hilang
saat program ditutup.
"""

import os
import json


# ====================================================
# PATH FILE
# ====================================================

BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

USERS_FILE = os.path.join(
    BASE_DIR,
    "data",
    "users.txt"
)

ANTREAN_FILE = os.path.join(
    BASE_DIR,
    "data",
    "antrean_medis.json"
)


# ====================================================
# USER LOGIN
# ====================================================

def load_users():
    """
    Membaca semua akun user
    dari users.txt
    """

    users = []

    try:
        with open(USERS_FILE, "r") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                data = line.split(",")

                if len(data) >= 2:

                    users.append({
                        "username": data[0],
                        "password": data[1]
                    })

    except FileNotFoundError:
        print("[!] users.txt belum ada")

    return users


def save_user(username, password):
    """
    Menyimpan user baru
    """

    with open(USERS_FILE, "a") as file:
        file.write(f"\n{username},{password}")


# ====================================================
# ANTREAN MEDIS
# ====================================================

FILE_ANTREAN = "data/antrean_medis.json"


def load_antrean():
    """Membaca data antrean dari file JSON"""

    if not os.path.exists(FILE_ANTREAN):
        return []

    try:
        with open(FILE_ANTREAN, "r", encoding="utf-8") as file:
            return json.load(file)

    except:
        return []


def save_antrean(data):
    """
    Menyimpan antrean medis
    ke file JSON
    """

    with open(ANTREAN_FILE, "w") as file:

        json.dump(
            data,
            file,
            indent=4
        )