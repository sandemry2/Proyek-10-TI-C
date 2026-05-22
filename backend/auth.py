from backend.file_handler import load_users

def login():

    users = load_users()

    print("=" * 40)
    print("LOGIN SISTEM EKOSISTEM")
    print("=" * 40)

    username = input("Username : ")
    password = input("Password : ")

    for user in users:

        if (
            user["username"] == username
            and
            user["password"] == password
        ):

            print("\nLogin berhasil!")
            return True

    print("\nLogin gagal!")
    return False
