"""
══════════════════════════════════
Log penampakan satwa menggunakan Single Linked List (SLL).
Setiap penampakan disimpan sebagai node yang terhubung ke node berikutnya.

Struktur SLL: Head → Node1 → Node2 → ... → NodeN → None
"""

from tabulate import tabulate
from datetime import datetime
import json
import os


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

    FILE_LOG = "data/log.penampakan.json"

    def __init__(self):
        self.head = None
        self.jumlah = 0
        self._id_counter = 1
        self.load_json()

    # ── Tambah log (insert di depan) ─────────────────────────────────
    def tambah_log(self, chip_id: str, nama: str, spesies: str,
                   zona: str, lokasi: str, aktivitas: str):
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

    # ── Hitung total penampakan per satwa ─────────────────────────────
    def statistik_penampakan(self):

        total_zona = {}
        total_satwa = {}

        node = self.head

        while node:

            zona = node.data["zona"]
            nama = node.data["nama"]

            total_zona[zona] = total_zona.get(zona, 0) + 1
            total_satwa[nama] = total_satwa.get(nama, 0) + 1

            node = node.next

        print("\n  📊 STATISTIK PENAMPAKAN")
        print("  " + "─"*40)

        print("\n  Penampakan per Zona:")

        for zona, jumlah in sorted(
            total_zona.items(),
            key=lambda x: x[1],
            reverse=True
        ):
            print(f"  {zona:<10} : {jumlah} kali")

        print("\n  Satwa Paling Sering Muncul:")

        for nama, jumlah in sorted(
            total_satwa.items(),
            key=lambda x: x[1],
            reverse=True
        )[:5]:
            print(f"  {nama:<15} : {jumlah} kali")

        print("  " + "─"*40)

    # ── Edit log berdasarkan ID ──────────────────────────────────
    def edit_log(self, id_log: int, lokasi_baru=None, aktivitas_baru=None):

        node = self.head

        while node:

            if node.data["id_log"] == id_log:

                if lokasi_baru:
                    node.data["lokasi"] = lokasi_baru

                if aktivitas_baru:
                    node.data["aktivitas"] = aktivitas_baru

                print(f"  [✓] Log #{id_log} berhasil diperbarui.")
                return True

            node = node.next

        print(f"  [!] Log #{id_log} tidak ditemukan.")
        return False
    
    def load_json(self):

        if not os.path.exists(self.FILE_LOG):
            return

        with open(self.FILE_LOG, "r", encoding="utf-8") as file:

            data = json.load(file)

        print(f"[DEBUG] {len(data)} log berhasil dibaca")

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

        # ======================================================
        # 1. Tambah Log
        # ======================================================

        if pilihan == "1":

            chip = input("  Chip ID satwa : ").strip()

            satwa = next(
                (s for s in daftar_satwa if s.chip_id == chip),
                None
            )

            if not satwa:
                print(f"  [!] Chip ID '{chip}' tidak ditemukan.")

            else:

                lokasi = input(
                    "  Lokasi spesifik : "
                ).strip()

                aktivitas = input(
                    "  Aktivitas satwa : "
                ).strip()


                sll.tambah_log(
                    chip,
                    satwa.nama,
                    satwa.spesies,
                    satwa.zona,
                    lokasi,
                    aktivitas,
                )

        # ======================================================
        # 2. Tampilkan Semua Log
        # ======================================================

        elif pilihan == "2":

            sll.tampilkan()

            input(
                "\n  Tekan Enter untuk lanjut..."
            )

        # ======================================================
        # 3. Cari Berdasarkan Chip ID
        # ======================================================

        elif pilihan == "3":

            chip = input(
                "  Chip ID: "
            ).strip()

            hasil = sll.cari_by_chip(chip)

            if hasil:

                print(
                    f"\n  Ditemukan {len(hasil)} log untuk Chip ID {chip}:"
                )

                for d in hasil:

                    print(
                        f"  #{d['id_log']} | "
                        f"{d['nama']} | "
                        f"{d['aktivitas']} | "
                        f"{d['lokasi']} | "
                        f"{d['waktu']}"
                    )

            else:

                print(
                    f"  [!] Tidak ada log untuk Chip ID {chip}."
                )

            input(
                "\n  Tekan Enter untuk lanjut..."
            )

        # ======================================================
        # 4. Edit Log
        # ======================================================

        elif pilihan == "4":

            try:

                id_log = int(
                    input("  ID Log: ")
                )

                lokasi_baru = input(
                    "  Lokasi baru (kosongkan jika tidak diubah): "
                ).strip()

                aktivitas_baru = input(
                    "  Aktivitas baru (kosongkan jika tidak diubah): "
                ).strip()

                sll.edit_log(
                    id_log,
                    lokasi_baru if lokasi_baru else None,
                    aktivitas_baru if aktivitas_baru else None
                )

            except ValueError:

                print(
                    "  [!] ID log harus berupa angka."
                )

        # ======================================================
        # 5. Hapus Log
        # ======================================================

        elif pilihan == "5":

            try:

                id_log = int(
                    input(
                        "  Nomor log yang akan dihapus: "
                    ).strip()
                )

                sll.hapus_log(id_log)

            except ValueError:

                print(
                    "  [!] Masukkan angka yang valid."
                )

        # ======================================================
        # 6. Statistik
        # ======================================================

        elif pilihan == "6":

            sll.statistik_penampakan()

            input(
                "\n  Tekan Enter untuk lanjut..."
            )

        # ======================================================
        # 0. Keluar
        # ======================================================

        elif pilihan == "0":

            break

        else:

            print(
                "  [!] Pilihan tidak valid."
            )