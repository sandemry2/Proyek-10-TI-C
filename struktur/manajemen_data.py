"""
structures/manajemen_data.py — Anggota 2
════════════════════════════════════════
Implementasi struktur data dasar:
  - List       : daftar spesies dan populasi satwa
  - Tuple      : koordinat geografis habitat (read-only)
  - Set        : kumpulan spesies unik tanpa duplikasi
  - Dictionary : database satwa berindeks Chip ID
"""

# Class Satwa dibuat di structures/satwa.py karena backend/models.py
# milik Anggota 1 hanya berisi User, Ranger, dan Habitat.
from struktur.satwa import Satwa


# ════════════════════════════════════════
#  1. LIST — Daftar spesies & populasi
# ════════════════════════════════════════

class ManajemenPopulasi:
    """
    Mengelola daftar satwa menggunakan List Python.
    Mendukung tambah, hapus, tampilkan, dan filter berdasarkan zona.
    """

    def __init__(self):
        self._data: list = []   # list of Animal objects

    # ── CRUD ────────────────────────────────────────────────────────
    def tambah_satwa(self, satwa) -> bool:
        """Tambah satwa ke daftar. Cek duplikat Chip ID terlebih dahulu."""
        for s in self._data:
            if s.chip_id == satwa.chip_id:
                print(f"  [!] Chip ID '{satwa.chip_id}' sudah terdaftar.")
                return False
        self._data.append(satwa)
        return True

    def hapus_satwa(self, chip_id: str) -> bool:
        """Hapus satwa berdasarkan Chip ID."""
        for i, s in enumerate(self._data):
            if s.chip_id == chip_id:
                nama = s.nama
                self._data.pop(i)
                print(f"  [✓] {nama} ({chip_id}) berhasil dihapus.")
                return True
        print(f"  [!] Chip ID '{chip_id}' tidak ditemukan.")
        return False

    def perbarui_zona(self, chip_id: str, zona_baru: str) -> bool:
        """Perbarui zona habitat satwa."""
        for s in self._data:
            if s.chip_id == chip_id:
                lama = s.zona
                s.zona = zona_baru
                print(f"  [✓] Zona {s.nama} diperbarui: {lama} → {zona_baru}")
                return True
        print(f"  [!] Chip ID '{chip_id}' tidak ditemukan.")
        return False

    # ── Filter ──────────────────────────────────────────────────────
    def filter_zona(self, zona: str) -> list:
        """Kembalikan list satwa yang ada di zona tertentu."""
        return [s for s in self._data if s.zona.lower() == zona.lower()]

    def filter_status(self, status: str) -> list:
        """Kembalikan list satwa berdasarkan status kepunahan."""
        return [s for s in self._data if s.status_kepunahan.upper() == status.upper()]

    def get_semua(self) -> list:
        return self._data[:]

    def jumlah(self) -> int:
        return len(self._data)

    # ── Tampilkan ────────────────────────────────────────────────────
    def tampilkan_semua(self):
        print(f"\n  📋 DAFTAR SELURUH SATWA (List)")
        print(f"  {'─'*60}")
        if not self._data:
            print("  (Belum ada data satwa)")
            return
        print(f"  {'No':<4} {'Chip ID':<8} {'Nama':<15} {'Spesies':<22} {'Zona':<8} {'Status'}")
        print(f"  {'─'*60}")
        for i, s in enumerate(self._data, 1):
            print(f"  {i:<4} {s.chip_id:<8} {s.nama:<15} {s.spesies:<22} {s.zona:<8} {s.status_kepunahan}")
        print(f"  {'─'*60}")
        print(f"  Total: {self.jumlah()} satwa")

    def tampilkan_per_zona(self):
        """Tampilkan ringkasan jumlah satwa per zona."""
        ringkasan: dict = {}
        for s in self._data:
            ringkasan[s.zona] = ringkasan.get(s.zona, 0) + 1

        print(f"\n  🗂️  POPULASI PER ZONA (List + Dictionary)")
        print(f"  {'─'*30}")
        for zona, jumlah in sorted(ringkasan.items()):
            bar = "█" * jumlah
            print(f"  {zona:<10} {bar} {jumlah} satwa")
        print(f"  {'─'*30}")
        print(f"  Total zona aktif: {len(ringkasan)}")


# ════════════════════════════════════════
#  2. TUPLE — Koordinat habitat (immutable)
# ════════════════════════════════════════

class KoordinatHabitat:
    """
    Menyimpan koordinat geografis setiap habitat menggunakan Tuple.
    Tuple dipilih karena koordinat bersifat tetap (immutable).
    """

    def __init__(self):
        # Format: nama_habitat -> (latitude, longitude, ketinggian_mdpl)
        self._koordinat: dict = {}

    def tambah_koordinat(self, nama_habitat: str, lat: float, lon: float, ketinggian: int):
        """Simpan koordinat habitat. Disimpan sebagai tuple (immutable)."""
        koordinat = (lat, lon, ketinggian)   # ← TUPLE
        self._koordinat[nama_habitat] = koordinat
        print(f"  [✓] Koordinat '{nama_habitat}' disimpan: {koordinat}")

    def get_koordinat(self, nama_habitat: str) -> tuple:
        """Kembalikan koordinat habitat sebagai tuple."""
        return self._koordinat.get(nama_habitat, None)

    def hitung_jarak_kasar(self, habitat_a: str, habitat_b: str) -> float:
        """
        Estimasi jarak dua habitat menggunakan rumus Euclidean sederhana
        (bukan jarak sesungguhnya, hanya untuk ilustrasi).
        """
        koord_a = self.get_koordinat(habitat_a)
        koord_b = self.get_koordinat(habitat_b)
        if not koord_a or not koord_b:
            print("  [!] Salah satu habitat tidak memiliki koordinat.")
            return -1.0
        delta_lat = koord_a[0] - koord_b[0]
        delta_lon = koord_a[1] - koord_b[1]
        return round((delta_lat**2 + delta_lon**2) ** 0.5, 4)

    def tampilkan_semua(self):
        print(f"\n  📍 KOORDINAT HABITAT (Tuple)")
        print(f"  {'─'*55}")
        print(f"  {'Nama Habitat':<25} {'Latitude':>10} {'Longitude':>11} {'Tinggi (mdpl)':>14}")
        print(f"  {'─'*55}")
        if not self._koordinat:
            print("  (Belum ada koordinat)")
            return
        for nama, (lat, lon, tnggi) in self._koordinat.items():
            print(f"  {nama:<25} {lat:>10.4f} {lon:>11.4f} {tnggi:>14}")
        print(f"  {'─'*55}")


# ════════════════════════════════════════
#  3. SET — Spesies unik
# ════════════════════════════════════════

class SpesiesUnik:
    """
    Menyimpan daftar spesies yang ada di konservasi menggunakan Set.
    Set otomatis menghilangkan duplikasi.
    """

    def __init__(self):
        self._spesies: set = set()

    def tambah_dari_daftar(self, daftar_satwa: list):
        """Ekstrak spesies unik dari list satwa."""
        sebelum = len(self._spesies)
        for s in daftar_satwa:
            self._spesies.add(s.spesies)
        sesudah = len(self._spesies)
        print(f"  [✓] {sesudah - sebelum} spesies baru ditambahkan. Total: {sesudah} spesies unik.")

    def tambah_manual(self, nama_spesies: str):
        if nama_spesies in self._spesies:
            print(f"  [!] '{nama_spesies}' sudah ada dalam set.")
        else:
            self._spesies.add(nama_spesies)
            print(f"  [✓] '{nama_spesies}' ditambahkan.")

    def hapus(self, nama_spesies: str):
        self._spesies.discard(nama_spesies)
        print(f"  [✓] '{nama_spesies}' dihapus dari set.")

    def ada(self, nama_spesies: str) -> bool:
        return nama_spesies in self._spesies

    def gabung(self, set_lain: 'SpesiesUnik') -> set:
        """Union dua set spesies."""
        return self._spesies | set_lain._spesies

    def irisan(self, set_lain: 'SpesiesUnik') -> set:
        """Intersection — spesies yang ada di kedua konservasi."""
        return self._spesies & set_lain._spesies

    def tampilkan(self):
        print(f"\n  🧬 SPESIES UNIK (Set) — Total: {len(self._spesies)}")
        print(f"  {'─'*40}")
        if not self._spesies:
            print("  (Set kosong)")
            return
        for i, sp in enumerate(sorted(self._spesies), 1):
            print(f"  {i:>3}. {sp}")
        print(f"  {'─'*40}")

# ═══════════════════════════════
#  4. DICTIONARY — Database satwa by Chip ID
# ════════════════════════════════════════

class DatabaseSatwa:
    """
    Database utama satwa menggunakan Dictionary.
    Key: chip_id (str), Value: objek Animal.
    Operasi O(1) untuk insert, lookup, dan delete.
    """

    def __init__(self):
        self._db: dict = {}

    def muat_dari_list(self, daftar_satwa: list):
        """Isi dictionary dari list satwa sekaligus."""
        for s in daftar_satwa:
            self._db[s.chip_id] = s
        print(f"  [✓] {len(daftar_satwa)} satwa dimuat ke database dictionary.")

    def tambah(self, satwa) -> bool:
        if satwa.chip_id in self._db:
            print(f"  [!] Chip ID '{satwa.chip_id}' sudah ada di database.")
            return False
        self._db[satwa.chip_id] = satwa
        return True

    def hapus(self, chip_id: str) -> bool:
        if chip_id in self._db:
            del self._db[chip_id]
            print(f"  [✓] Chip ID '{chip_id}' dihapus dari database.")
            return True
        print(f"  [!] Chip ID '{chip_id}' tidak ditemukan.")
        return False

    def cari(self, chip_id: str):
        """Kembalikan objek Animal atau None jika tidak ada."""
        return self._db.get(chip_id, None)

    def ada(self, chip_id: str) -> bool:
        return chip_id in self._db

    def semua_chip_id(self) -> list:
        return list(self._db.keys())

    def jumlah(self) -> int:
        return len(self._db)

    def tampilkan(self):
        print(f"\n  🗄️  DATABASE SATWA (Dictionary) — {self.jumlah()} entri")
        print(f"  {'─'*60}")
        if not self._db:
            print("  (Database kosong)")
            return
        print(f"  {'Chip ID':<10} {'Nama':<15} {'Spesies':<22} {'Zona':<8} {'Status'}")
        print(f"  {'─'*60}")
        for chip_id, s in self._db.items():
            print(f"  {chip_id:<10} {s.nama:<15} {s.spesies:<22} {s.zona:<8} {s.status_kepunahan}")
        print(f"  {'─'*60}")

    def tampilkan_satu(self, chip_id: str):
        satwa = self.cari(chip_id)
        if satwa:
            print(f"\n  🔎 Data satwa Chip ID: {chip_id}")
            try:
                satwa.tampilkan_info()
            except AttributeError:
                # fallback jika method tampilkan_info tidak ada di models.py Anggota 1
                print(f"  Nama    : {satwa.nama}")
                print(f"  Spesies : {satwa.spesies}")
                print(f"  Zona    : {satwa.zona}")
        else:
            print(f"  [!] Chip ID '{chip_id}' tidak ditemukan di database.")
