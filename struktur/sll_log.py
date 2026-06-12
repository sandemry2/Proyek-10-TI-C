"""
══════════════════════════════════
Log penampakan satwa menggunakan Single Linked List (SLL).
Setiap penampakan disimpan sebagai node yang terhubung ke node berikutnya.

Struktur SLL: Head → Node1 → Node2 → ... → NodeN → None

Persistensi: setiap perubahan (tambah/hapus/edit) langsung disimpan
ke log_penampakan.json, dan saat program dibuka kembali data dimuat
dari JSON ke dalam linked list.
"""

from datetime import datetime
import json
import os


# ════════════════════════════════════════
#  PATH FILE
# ════════════════════════════════════════

# Ikuti pola yang sama dengan file_handler.py:
# BASE_DIR = dua folder di atas file ini (root proyek)
BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

FILE_LOG = os.path.join(BASE_DIR, "data", "log_penampakan.json")


# ════════════════════════════════════════
#  NODE
# ════════════════════════════════════════

class NodeLog:
    def __init__(self, data: dict):
        """
        data: dict berisi satu catatan penampakan
          {
            'id_log'    : int   — nomor urut otomatis
            'chip_id'   : str,
            'nama'      : str,
            'spesies'   : str,
            'zona'      : str,
            'lokasi'    : str   — deskripsi lokasi spesifik
            'aktivitas' : str   — apa yang dilakukan satwa
            'waktu'     : str   — timestamp otomatis
          }
        """
        self.data = data
        self.next = None    # pointer ke node berikutnya


# ════════════════════════════════════════
#  SINGLE LINKED LIST
# ════════════════════════════════════════

class SLLLog:
    """
    Log penampakan satwa harian menggunakan Single Linked List.
    Log baru ditambahkan di depan (head insertion) agar log terbaru
    selalu muncul pertama.

    Setiap perubahan langsung disimpan ke log_penampakan.json.
    Saat program dibuka, data JSON dimuat kembali ke linked list.
    """

    def __init__(self):
        self.head = None
        self.jumlah = 0
        self._id_counter = 1
        self._load_json()   # muat data dari JSON saat objek dibuat


    # ════════════════════════════════════════
    #  PERSISTENSI JSON
    # ════════════════════════════════════════

    def _load_json(self):

        if not os.path.exists(FILE_LOG):
            return

        try:
            with open(FILE_LOG, "r", encoding="utf-8") as f:
                data_list = json.load(f)

            if not isinstance(data_list, list) or len(data_list) == 0:
                return

            # Cari id_counter tertinggi agar ID tidak mulai dari 1 lagi
            max_id = max(item.get("id_log", 0) for item in data_list)
            self._id_counter = max_id + 1

            # Masukkan dari belakang supaya urutan tetap terjaga
            # (tambah_log insert di HEAD, jadi item terakhir masuk = jadi HEAD)
            for item in reversed(data_list):
                node = NodeLog(item)
                node.next = self.head
                self.head = node
                self.jumlah += 1

        except (json.JSONDecodeError, KeyError, TypeError):
            print("  [!] Gagal memuat log_penampakan.json. Mulai dengan log kosong.")


    def _save_json(self):
        """
        Tulis seluruh isi linked list ke log_penampakan.json.
        Dipanggil setiap kali ada perubahan (tambah/hapus/edit).

        Cara kerja: traverse SLL dari head ke tail,
        kumpulkan semua data ke list Python, lalu dump ke JSON.
        Karena head adalah log TERBARU, hasil JSON juga urut terbaru dulu.
        """

        data_list = []
        node = self.head

        while node:
            data_list.append(node.data)
            node = node.next

        try:
            # Buat folder data/ kalau belum ada
            os.makedirs(os.path.dirname(FILE_LOG), exist_ok=True)

            with open(FILE_LOG, "w", encoding="utf-8") as f:
                json.dump(data_list, f, indent=4, ensure_ascii=False)

        except IOError as e:
            print(f"  [!] Gagal menyimpan log: {e}")


    # ════════════════════════════════════════
    #  OPERASI LINKED LIST
    # ════════════════════════════════════════

    def tambah_log(self, chip_id: str, nama: str, spesies: str,
                   zona: str, lokasi: str, aktivitas: str):
        """
        Tambah log baru di depan (head insertion).
        Log terbaru selalu jadi HEAD — muncul pertama saat ditampilkan.
        Setelah insert, langsung simpan ke JSON.
        """
        data = {
            "id_log"    : self._id_counter,
            "chip_id"   : chip_id,
            "nama"      : nama,
            "spesies"   : spesies,
            "zona"      : zona,
            "lokasi"    : lokasi,
            "aktivitas" : aktivitas,
            "waktu"     : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        node = NodeLog(data)
        node.next = self.head   # node baru menunjuk ke head lama
        self.head = node        # head digeser ke node baru
        self.jumlah += 1
        self._id_counter += 1

        self._save_json()       # simpan perubahan ke file

        print(f"  [✓] Log #{data['id_log']} dicatat: {nama} terlihat di {lokasi}.")


    def hapus_log(self, id_log: int) -> bool:
        """
        Hapus node dengan id_log tertentu dari linked list.
        Setelah hapus, simpan ke JSON.
        """
        if self.head is None:
            print("  [!] Log kosong.")
            return False

        # Kasus: node pertama (HEAD) yang dihapus
        if self.head.data["id_log"] == id_log:
            self.head = self.head.next
            self.jumlah -= 1
            self._save_json()
            print(f"  [✓] Log #{id_log} berhasil dihapus.")
            return True

        # Kasus: cari di tengah atau akhir
        node = self.head
        while node.next:
            if node.next.data["id_log"] == id_log:
                node.next = node.next.next  # bypass node yang dihapus
                self.jumlah -= 1
                self._save_json()
                print(f"  [✓] Log #{id_log} berhasil dihapus.")
                return True
            node = node.next

        print(f"  [!] Log #{id_log} tidak ditemukan.")
        return False


    def edit_log(self, id_log: int, lokasi_baru=None, aktivitas_baru=None):
        """
        Edit lokasi atau aktivitas log berdasarkan ID.
        Setelah edit, simpan ke JSON.
        """
        node = self.head

        while node:
            if node.data["id_log"] == id_log:

                if lokasi_baru:
                    node.data["lokasi"] = lokasi_baru

                if aktivitas_baru:
                    node.data["aktivitas"] = aktivitas_baru

                self._save_json()   # simpan perubahan
                print(f"  [✓] Log #{id_log} berhasil diperbarui.")
                return True

            node = node.next

        print(f"  [!] Log #{id_log} tidak ditemukan.")
        return False


    # ════════════════════════════════════════
    #  OPERASI BACA (tidak ubah data)
    # ════════════════════════════════════════

    def cari_by_chip(self, chip_id: str) -> list:
        """Kembalikan semua log milik chip_id tertentu sebagai list dict."""
        hasil = []
        node = self.head
        while node:
            if node.data["chip_id"].lower() == chip_id.lower():
                hasil.append(node.data)
            node = node.next
        return hasil


    def tampilkan(self):
        """Tampilkan seluruh isi linked list dari HEAD ke TAIL."""
        print(f"\n  📒 LOG PENAMPAKAN SATWA (Single Linked List) — {self.jumlah} entri")
        print(f"  {'─'*70}")

        if self.head is None:
            print("  (Belum ada log)")
            print(f"  {'─'*70}")
            return

        print(f"  {'ID':<5} {'Chip ID':<9} {'Nama':<13} {'Lokasi':<18} {'Aktivitas':<18} {'Waktu'}")
        print(f"  {'─'*70}")

        node = self.head
        while node:
            d = node.data
            print(
                f"  {d['id_log']:<5} {d['chip_id']:<9} {d['nama']:<13} "
                f"{d['lokasi']:<18} {d['aktivitas']:<18} {d['waktu']}"
            )
            node = node.next

        print(f"  {'─'*70}")


    def statistik_penampakan(self):
        """Ringkasan penampakan per zona dan per satwa."""
        total_zona  = {}
        total_satwa = {}

        node = self.head
        while node:
            zona = node.data["zona"]
            nama = node.data["nama"]
            total_zona[zona]   = total_zona.get(zona, 0) + 1
            total_satwa[nama]  = total_satwa.get(nama, 0) + 1
            node = node.next

        print("\n  📊 STATISTIK PENAMPAKAN")
        print("  " + "─" * 40)

        print("\n  Penampakan per Zona:")
        for zona, jumlah in sorted(total_zona.items(), key=lambda x: x[1], reverse=True):
            print(f"  {zona:<10} : {jumlah} kali")

        print("\n  Satwa Paling Sering Muncul:")
        for nama, jumlah in sorted(total_satwa.items(), key=lambda x: x[1], reverse=True)[:5]:
            print(f"  {nama:<15} : {jumlah} kali")

        print("  " + "─" * 40)


# ════════════════════════════════════════
#  MENU
# ════════════════════════════════════════

def menu_log(sll: SLLLog, daftar_satwa: list):

    while True:

        print(f"\n  ╔══ LOG PENAMPAKAN SATWA {'═'*17}")
        print(f"  ║  1. Catat penampakan baru")
        print(f"  ║  2. Tampilkan semua log")
        print(f"  ║  3. Cari log berdasarkan Chip ID")
        print(f"  ║  4. Edit log")
        print(f"  ║  5. Hapus log")
        print(f"  ║  6. Statistik penampakan")
        print(f"  ║  0. Kembali")
        print(f"  ╚{'═'*40}")

        pilihan = input("  Pilih: ").strip()

        if pilihan == "1":
            chip = input("  Chip ID satwa  : ").strip()
            satwa = next((s for s in daftar_satwa if s.chip_id == chip), None)

            if not satwa:
                print(f"  [!] Chip ID '{chip}' tidak ditemukan.")
            else:
                lokasi    = input("  Lokasi spesifik : ").strip()
                aktivitas = input("  Aktivitas satwa : ").strip()
                sll.tambah_log(
                    chip,
                    satwa.nama,
                    satwa.spesies,
                    satwa.zona,
                    lokasi,
                    aktivitas
                )

        elif pilihan == "2":
            sll.tampilkan()
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "3":
            chip  = input("  Chip ID: ").strip()
            hasil = sll.cari_by_chip(chip)

            if hasil:
                print(f"\n  Ditemukan {len(hasil)} log untuk Chip ID {chip}:")
                for d in hasil:
                    print(
                        f"  #{d['id_log']} | "
                        f"{d['nama']} | "
                        f"{d['aktivitas']} | "
                        f"{d['lokasi']} | "
                        f"{d['waktu']}"
                    )
            else:
                print(f"  [!] Tidak ada log untuk Chip ID {chip}.")

            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "4":
            try:
                id_log         = int(input("  ID Log         : "))
                lokasi_baru    = input("  Lokasi baru    (kosongkan jika tidak diubah): ").strip()
                aktivitas_baru = input("  Aktivitas baru (kosongkan jika tidak diubah): ").strip()
                sll.edit_log(
                    id_log,
                    lokasi_baru    if lokasi_baru    else None,
                    aktivitas_baru if aktivitas_baru else None
                )
            except ValueError:
                print("  [!] ID log harus berupa angka.")

        elif pilihan == "5":
            try:
                id_log = int(input("  Nomor log yang akan dihapus: ").strip())
                sll.hapus_log(id_log)
            except ValueError:
                print("  [!] Masukkan angka yang valid.")

        elif pilihan == "6":
            sll.statistik_penampakan()
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "0":
            break

        else:
            print("  [!] Pilihan tidak valid.")