"""
═════════════════════════════════════
Algoritma pencarian satwa:
  - Linear Search  : cari berdasarkan nama / zona / spesies
  - Binary Search  : cari berdasarkan Chip ID (data harus terurut)
"""


# ════════════════════════════════════════
#  LINEAR SEARCH
# ════════════════════════════════════════

class LinearSearch:
    """
    Mencari satwa dengan memeriksa setiap elemen satu per satu.
    Tidak membutuhkan data terurut.
    Kompleksitas: O(n)
    """

    @staticmethod
    def cari_by_chip_id(daftar_satwa: list, chip_id: str):
        """Cari satu satwa berdasarkan Chip ID. Return objek atau None."""
        for satwa in daftar_satwa:
            if satwa.chip_id.lower() == chip_id.lower():
                return satwa
        return None

    @staticmethod
    def cari_by_nama(daftar_satwa: list, nama: str) -> list:
        """Cari satwa berdasarkan nama (partial match). Return list hasil."""
        hasil = []
        for satwa in daftar_satwa:
            if nama.lower() in satwa.nama.lower():
                hasil.append(satwa)
        return hasil

    @staticmethod
    def cari_by_zona(daftar_satwa: list, zona: str) -> list:
        """Cari semua satwa di zona tertentu."""
        return [s for s in daftar_satwa if s.zona.lower() == zona.lower()]

    @staticmethod
    def cari_by_spesies(daftar_satwa: list, spesies: str) -> list:
        """Cari satwa berdasarkan nama spesies (partial match)."""
        return [s for s in daftar_satwa if spesies.lower() in s.spesies.lower()]

    @staticmethod
    def cari_by_status(daftar_satwa: list, status: str) -> list:
        """Cari satwa berdasarkan status kepunahan (CR/EN/VU/NT/LC)."""
        return [s for s in daftar_satwa if s.status_kepunahan.upper() == status.upper()]

    @staticmethod
    def cari_rentang_usia(daftar_satwa: list, min_usia: int, maks_usia: int) -> list:
        """Cari satwa dalam rentang usia tertentu."""
        return [s for s in daftar_satwa if min_usia <= s.usia <= maks_usia]


# ════════════════════════════════════════
#  BINARY SEARCH
# ════════════════════════════════════════

class BinarySearch:
    """
    Pencarian cepat berdasarkan Chip ID yang sudah diurutkan.
    Kompleksitas: O(log n)

    PENTING: daftar satwa HARUS diurutkan berdasarkan chip_id terlebih dahulu.
    Gunakan metode urutkan() sebelum mencari.
    """

    @staticmethod
    def urutkan_by_chip_id(daftar_satwa: list) -> list:
        """
        Urutkan daftar satwa berdasarkan Chip ID menggunakan Insertion Sort.
        (Tidak menggunakan sorted() bawaan Python)
        """
        data = daftar_satwa[:]
        for i in range(1, len(data)):
            kunci = data[i]
            j = i - 1
            while j >= 0 and data[j].chip_id > kunci.chip_id:
                data[j + 1] = data[j]
                j -= 1
            data[j + 1] = kunci
        return data

    @staticmethod
    def cari(daftar_terurut: list, chip_id: str):
        """
        Binary search untuk menemukan satwa berdasarkan Chip ID.
        Parameter daftar_terurut HARUS sudah diurut berdasarkan chip_id.
        Return: objek Animal, atau None jika tidak ditemukan.
        """
        kiri = 0
        kanan = len(daftar_terurut) - 1
        langkah = 0

        while kiri <= kanan:
            tengah = (kiri + kanan) // 2
            langkah += 1
            chip_tengah = daftar_terurut[tengah].chip_id

            if chip_tengah == chip_id:
                print(f"  [✓] Ditemukan pada langkah ke-{langkah} (index: {tengah})")
                return daftar_terurut[tengah]
            elif chip_tengah < chip_id:
                kiri = tengah + 1
            else:
                kanan = tengah - 1

        print(f"  [!] Chip ID '{chip_id}' tidak ditemukan setelah {langkah} langkah.")
        return None


# ════════════════════════════════════════
#  TAMPILKAN HASIL PENCARIAN
# ════════════════════════════════════════

def tampilkan_hasil(daftar_satwa: list, judul: str):
    print(f"\n  🔍 {judul}")
    print(f"  {'─'*60}")
    if not daftar_satwa:
        print("  Tidak ada satwa yang cocok dengan kriteria pencarian.")
        print(f"  {'─'*60}")
        return
    print(f"  {'No':<4} {'Chip ID':<10} {'Nama':<15} {'Spesies':<22} {'Zona':<8} {'Status'}")
    print(f"  {'─'*60}")
    for i, s in enumerate(daftar_satwa, 1):
        print(f"  {i:<4} {s.chip_id:<10} {s.nama:<15} {s.spesies:<22} {s.zona:<8} {s.status_kepunahan}")
    print(f"  {'─'*60}")
    print(f"  Ditemukan: {len(daftar_satwa)} satwa")


# ════════════════════════════════════════
#  MENU SEARCHING (dipanggil dari main/menu)
# ════════════════════════════════════════

def menu_pencarian(daftar_satwa: list):
    """
    Menu interaktif pencarian satwa.
    daftar_satwa: list of Animal objects (dari database / dummy data)
    """
    while True:
        print(f"\n  ╔══ PENCARIAN SATWA {'═'*22}")
        print(f"  ║  [LINEAR SEARCH]")
        print(f"  ║  1. Cari berdasarkan Chip ID")
        print(f"  ║  2. Cari berdasarkan Nama")
        print(f"  ║  3. Cari berdasarkan Zona")
        print(f"  ║  4. Cari berdasarkan Spesies")
        print(f"  ║  5. Cari berdasarkan Status Kepunahan")
        print(f"  ║  6. Cari berdasarkan Rentang Usia")
        print(f"  ║  [BINARY SEARCH]")
        print(f"  ║  7. Cari Chip ID (Binary Search)")
        print(f"  ║  0. Kembali")
        print(f"  ╚{'═'*40}")
        pilihan = input("  Pilih: ").strip()

        if pilihan == "1":
            chip = input("  Chip ID: ").strip()
            hasil = LinearSearch.cari_by_chip_id(daftar_satwa, chip)
            if hasil:
                tampilkan_hasil([hasil], f"Hasil pencarian Chip ID: {chip}")
            else:
                print(f"  [!] Chip ID '{chip}' tidak ditemukan.")

        elif pilihan == "2":
            nama = input("  Nama satwa: ").strip()
            hasil = LinearSearch.cari_by_nama(daftar_satwa, nama)
            tampilkan_hasil(hasil, f"Hasil pencarian nama: '{nama}'")

        elif pilihan == "3":
            zona = input("  Zona (contoh: Zona A): ").strip()
            hasil = LinearSearch.cari_by_zona(daftar_satwa, zona)
            tampilkan_hasil(hasil, f"Satwa di {zona}")

        elif pilihan == "4":
            spesies = input("  Nama spesies: ").strip()
            hasil = LinearSearch.cari_by_spesies(daftar_satwa, spesies)
            tampilkan_hasil(hasil, f"Spesies: '{spesies}'")

        elif pilihan == "5":
            print("  Status: CR / EN / VU / NT / LC")
            status = input("  Status: ").strip()
            hasil = LinearSearch.cari_by_status(daftar_satwa, status)
            tampilkan_hasil(hasil, f"Status kepunahan: {status.upper()}")

        elif pilihan == "6":
            try:
                min_u = int(input("  Usia minimal (tahun): ").strip())
                maks_u = int(input("  Usia maksimal (tahun): ").strip())
                hasil = LinearSearch.cari_rentang_usia(daftar_satwa, min_u, maks_u)
                tampilkan_hasil(hasil, f"Usia {min_u}–{maks_u} tahun")
            except ValueError:
                print("  [!] Masukkan angka yang valid.")

        elif pilihan == "7":
            chip = input("  Chip ID: ").strip()
            print("  Mengurutkan data terlebih dahulu...")
            terurut = BinarySearch.urutkan_by_chip_id(daftar_satwa)
            hasil = BinarySearch.cari(terurut, chip)
            if hasil:
                tampilkan_hasil([hasil], f"Binary Search — Chip ID: {chip}")

        elif pilihan == "0":
            break
        else:
            print("  [!] Pilihan tidak valid.")
