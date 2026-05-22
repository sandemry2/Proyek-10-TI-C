class User:

    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

    def info(self):
        return f"{self.username} ({self.role})"


class Ranger:

    def __init__(self, nama, zona):
        self.nama = nama
        self.zona = zona

    def patroli(self):
        return f"{self.nama} patroli di {self.zona}"


class Habitat:

    def __init__(self, nama, kondisi):
        self.nama = nama
        self.kondisi = kondisi

    def info(self):
        return f"{self.nama} - {self.kondisi}"
