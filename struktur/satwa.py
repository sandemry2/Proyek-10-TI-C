class Satwa:
    """
    Class Satwa — digunakan oleh ManajemenPopulasi, DatabaseSatwa, dan struktur lainnya.
    Kompatibel dengan data dari data_dummy_ekosistem.py (class Animal).
    """
    def __init__(self, chip_id, nama, spesies, usia, berat_kg, zona, status_kepunahan, jenis_kelamin):
        self.chip_id          = chip_id
        self.nama             = nama
        self.spesies          = spesies
        self.usia             = usia
        self.berat_kg         = berat_kg
        self.zona             = zona
        self.status_kepunahan = status_kepunahan
        self.jenis_kelamin    = jenis_kelamin

    def tampilkan_info(self):
        print(f"  Chip ID    : {self.chip_id}")
        print(f"  Nama       : {self.nama}")
        print(f"  Spesies    : {self.spesies}")
        print(f"  Usia       : {self.usia} tahun")
        print(f"  Berat      : {self.berat_kg} kg")
        print(f"  Zona       : {self.zona}")
        print(f"  Status     : {self.status_kepunahan}")
        print(f"  Kelamin    : {self.jenis_kelamin}")

    def info(self):
        return (f"[{self.chip_id}] {self.nama} ({self.spesies}) | "
                f"{self.usia} thn | {self.berat_kg} kg | {self.zona} | {self.status_kepunahan}")

    def __repr__(self):
        return f"Satwa({self.chip_id}, {self.nama})"
