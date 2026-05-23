"""
══════════════════════════════════
Log penampakan satwa menggunakan Single Linked List (SLL).
Setiap penampakan disimpan sebagai node yang terhubung ke node berikutnya.

Struktur SLL: Head → Node1 → Node2 → ... → NodeN → None
"""

from tabulate import tabulate
from datetime import datetime


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
            'petugas'   : str   — nama petugas yang mencatat
            'waktu'     : str
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
    """

    def __init__(self):
        self.head = None
        self.jumlah = 0
        self._id_counter = 1

    # ── Tambah log (insert di depan) ─────────────────────────────────
    def tambah_log(self, chip_id: str, nama: str, spesies: str,
                   zona: str, lokasi: str, aktivitas: str, petugas: str):
        data = {
            "id_log"    : self._id_counter,
            "chip_id"   : chip_id,
            "nama"      : nama,
            "spesies"   : spesies,
            "zona"      : zona,
            "lokasi"    : lokasi,
            "aktivitas" : aktivitas,
            "petugas"   : petugas,
            "waktu"     : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        node = NodeLog(data)
        node.next = self.head
        self.head = node
        self.jumlah += 1
        self._id_counter += 1
        print(f"  [✓] Log #{data['id_log']} dicatat: {nama} terlihat di {lokasi}.")

    # ── Hapus log berdasarkan ID ──────────────────────────────────────
    def hapus_log(self, id_log: int) -> bool:
        if self.head is None:
            print("  [!] Log kosong.")
            return False

        # Kasus: node pertama
        if self.head.data["id_log"] == id_log:
            self.head = self.head.next
            self.jumlah -= 1
            print(f"  [✓] Log #{id_log} berhasil dihapus.")
            return True

        node = self.head
        while node.next:
            if node.next.data["id_log"] == id_log:
                node.next = node.next.next
                self.jumlah -= 1
                print(f"  [✓] Log #{id_log} berhasil dihapus.")
                return True
            node = node.next

        print(f"  [!] Log #{id_log} tidak ditemukan.")
        return False

    # ── Cari log berdasarkan chip_id ──────────────────────────────────
    def cari_by_chip(self, chip_id: str) -> list:
        hasil = []
        node = self.head
        while node:
            if node.data["chip_id"].lower() == chip_id.lower():
                hasil.append(node.data)
            node = node.next
        return hasil

    # ── Cari log berdasarkan zona ──────────────────────────────────────
    def cari_by_zona(self, zona: str) -> list:
        hasil = []
        node = self.head
        while node:
            if node.data["zona"].lower() == zona.lower():
                hasil.append(node.data)
            node = node.next
        return hasil

    # ── Tampilkan semua log ───────────────────────────────────────────
    def tampilkan(self):
        print(f"\n  📒 LOG PENAMPAKAN SATWA (Single Linked List) — {self.jumlah} entri")
        print(f"  {'─'*65}")
        if self.head is None:
            print("  (Belum ada log)")
            print(f"  {'─'*65}")
            return

        print(f"  {'ID':<5} {'Chip ID':<9} {'Nama':<13} {'Lokasi':<18} {'Aktivitas':<18} {'Waktu'}")
        print(f"  {'─'*65}")
        node = self.head
        while node:
            d = node.data
            print(f"  {d['id_log']:<5} {d['chip_id']:<9} {d['nama']:<13} "
                  f"{d['lokasi']:<18} {d['aktivitas']:<18} {d['waktu']}")
            node = node.next
        print(f"  {'─'*65}")

    def tampilkan_detail(self, id_log: int):
        node = self.head
        while node:
            if node.data["id_log"] == id_log:
                d = node.data
                print(f"\n  📋 Detail Log #{id_log}")
                print(f"  {'─'*40}")
                for k, v in d.items():
                    print(f"  {k:<14}: {v}")
                print(f"  {'─'*40}")
                return
            node = node.next
        print(f"  [!] Log #{id_log} tidak ditemukan.")

    # ── Hitung total penampakan per satwa ─────────────────────────────
    def statistik_penampakan(self):
        frekuensi = {}
        node = self.head
        while node:
            nama = node.data["nama"]
            frekuensi[nama] = frekuensi.get(nama, 0) + 1
            node = node.next

        print(f"\n  📊 STATISTIK PENAMPAKAN")
        print(f"  {'─'*30}")
        for nama, count in sorted(frekuensi.items(), key=lambda x: -x[1]):
            bar = "▪" * count
            print(f"  {nama:<15} {bar} ({count}x)")
        print(f"  {'─'*30}")


# ════════════════════════════════════════
#  MENU
# ════════════════════════════════════════

def menu_log(sll: SLLLog, daftar_satwa: list, ranger_aktif):
    while True:
        print(f"\n  ╔══ LOG PENAMPAKAN SATWA {'═'*17}")
        print(f"  ║  1. Catat penampakan baru")
        print(f"  ║  2. Tampilkan semua log")
        print(f"  ║  3. Cari log berdasarkan Chip ID")
        print(f"  ║  4. Cari log berdasarkan Zona")
        print(f"  ║  5. Lihat detail log")
        print(f"  ║  6. Hapus log")
        print(f"  ║  7. Statistik penampakan")
        print(f"  ║  0. Kembali")
        print(f"  ╚{'═'*40}")
        pilihan = input("  Pilih: ").strip()

        if pilihan == "1":
            chip = input("  Chip ID satwa : ").strip()
            satwa = next((s for s in daftar_satwa if s.chip_id == chip), None)
            if not satwa:
                print(f"  [!] Chip ID '{chip}' tidak ditemukan.")
            else:
                lokasi    = input("  Lokasi spesifik : ").strip()
                aktivitas = input("  Aktivitas satwa  : ").strip()
                nama_petugas = ranger_aktif.nama_lengkap if ranger_aktif else "Tidak diketahui"
                sll.tambah_log(chip, satwa.nama, satwa.spesies,
                               satwa.zona, lokasi, aktivitas, nama_petugas)

        elif pilihan == "2":
            sll.tampilkan()
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "3":
            chip = input("  Chip ID: ").strip()
            hasil = sll.cari_by_chip(chip)
            if hasil:
                print(f"\n  Ditemukan {len(hasil)} log untuk Chip ID {chip}:")
                for d in hasil:
                    print(f"  #{d['id_log']} — {d['lokasi']} | {d['aktivitas']} | {d['waktu']}")
            else:
                print(f"  [!] Tidak ada log untuk Chip ID {chip}.")
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "4":
            zona = input("  Zona (misal: Zona A): ").strip()
            hasil = sll.cari_by_zona(zona)
            if hasil:
                print(f"\n  {len(hasil)} penampakan di {zona}:")
                for d in hasil:
                    print(f"  #{d['id_log']} — {d['nama']} | {d['aktivitas']} | {d['waktu']}")
            else:
                print(f"  [!] Tidak ada log di {zona}.")
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "5":
            try:
                id_log = int(input("  Nomor log: ").strip())
                sll.tampilkan_detail(id_log)
            except ValueError:
                print("  [!] Masukkan angka yang valid.")
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "6":
            try:
                id_log = int(input("  Nomor log yang akan dihapus: ").strip())
                sll.hapus_log(id_log)
            except ValueError:
                print("  [!] Masukkan angka yang valid.")

        elif pilihan == "7":
            sll.statistik_penampakan()
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "0":
            break
        else:
            print("  [!] Pilihan tidak valid.")
