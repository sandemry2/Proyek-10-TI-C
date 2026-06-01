"""
Antrean pemeriksaan medis satwa menggunakan Queue.
Implementasi: Linked List (bukan list Python biasa)

Konsep Queue: FIFO — First In, First Out
  Enqueue → masuk dari belakang (tail)
  Dequeue → keluar dari depan (head)
"""
from tabulate import tabulate
from datetime import datetime
from backend.file_handler import load_antrean, save_antrean


# ════════════════════════════════════════
#  NODE
# ════════════════════════════════════════

class NodeAntrean:
    def __init__(self, data: dict):
        """
        data: dict berisi info satwa yang akan diperiksa
          {
            'chip_id'  : str,
            'nama'     : str,
            'spesies'  : str,
            'zona'     : str,
            'keluhan'  : str,
            'prioritas': str  — "Darurat" / "Normal"
            'waktu'    : str  — otomatis diisi
          }
        """
        self.data = data
        self.next = None


# ════════════════════════════════════════
#  QUEUE
# ════════════════════════════════════════

class QueueMedis:
    """
    Antrean pemeriksaan kesehatan satwa.
    Satwa dengan prioritas 'Darurat' akan dimasukkan ke depan antrean.
    """

    def __init__(self):

        self.head = None
        self.tail = None
        self.ukuran = 0

        # Rekam medis
        self.rekam_medis = []

        # Ambil data antrean dari file
        self.data_file = load_antrean()

        # Masukkan ke linked list
        for item in self.data_file:
            self.enqueue(
                item["chip_id"],
                item["nama"],
                item["spesies"],
                item["zona"],
                item["keluhan"],
                item["prioritas"],
                item["waktu"],
                simpan=False
            )

    # ── Antrean medis ─────────────────────────
    def __len__(self):
        return self.ukuran
            
    # ── Enqueue normal (masuk dari belakang) ─────────────────────────
    def enqueue(self, chip_id: str, nama: str, spesies: str,
            zona: str, keluhan: str,
            prioritas: str = "Normal",
            waktu=None,
            simpan=True):

        data = {
            "chip_id": chip_id,
            "nama": nama,
            "spesies": spesies,
            "zona": zona,
            "keluhan": keluhan,
            "prioritas": prioritas,
            "waktu": waktu or datetime.now().strftime("%H:%M:%S")
        }

        node = NodeAntrean(data)

        if prioritas == "Darurat":
            # Masuk ke depan antrean
            node.next = self.head
            self.head = node

            if self.tail is None:
                self.tail = node

            print(f"  [🚨] {nama} masuk antrean DARURAT (posisi 1).")

        else:
            # Masuk ke belakang antrean
            if self.tail:
                self.tail.next = node

            self.tail = node

            if self.head is None:
                self.head = node

            print(f"  [✓] {nama} masuk antrean (posisi {self.ukuran + 1}).")

        self.ukuran += 1

        # simpan ke file hanya jika antrean baru ditambah user
        if simpan:
            self.simpan_file()

    def simpan_file(self):

        data = []

        node = self.head

        while node:
            data.append(node.data)
            node = node.next

        save_antrean(data)

    # ── Dequeue (keluar dari depan) ──────────────────────────────────
    def dequeue(self) -> dict:
        """Keluarkan satwa paling depan untuk diperiksa."""
        if self.kosong():
            print("  [!] Antrean kosong. Tidak ada satwa yang perlu diperiksa.")
            return None

        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.ukuran -= 1

        print(f"\n  [🏥] Memanggil: {data['nama']} ({data['chip_id']}) — {data['keluhan']}")

        self.simpan_file()

        return data
    
    # ── Peek (lihat depan tanpa dikeluarkan) ────────────────────────
    def peek(self) -> dict:
        if self.kosong():
            print("  [!] Antrean kosong.")
            return None
        return self.head.data

    def kosong(self) -> bool:
        return self.head is None

    def panjang(self) -> int:
        return self.ukuran

    # ── Tampilkan antrean ─────────────────────────────────────────────
    def tampilkan(self):
        print(f"\n  🏥 ANTREAN PEMERIKSAAN MEDIS")
        print(f"  {'─'*55}")
        if self.kosong():
            print("  (Antrean kosong)")
            print(f"  {'─'*55}")
            return

        print(f"  {'No':<4} {'Chip ID':<9} {'Nama':<14} {'Keluhan':<20} {'Prioritas':<10} {'Waktu'}")
        print(f"  {'─'*55}")
        node = self.head
        nomor = 1
        while node:
            d = node.data
            prio_label = "🚨 Darurat" if d['prioritas'] == "Darurat" else "Normal"
            print(f"  {nomor:<4} {d['chip_id']:<9} {d['nama']:<14} {d['keluhan']:<20} {prio_label:<10} {d['waktu']}")
            node = node.next
            nomor += 1
        print(f"  {'─'*55}")
        print(f"  Total antrean: {self.ukuran} satwa")

    # ── Simpan Rekam Medis ─────────────────────────────────────────────
    def simpan_rekam_medis(self, data_satwa, diagnosis, tindakan):
        rekam = {
            "chip_id": data_satwa["chip_id"],
            "nama": data_satwa["nama"],
            "spesies": data_satwa["spesies"],
            "keluhan": data_satwa["keluhan"],
            "diagnosis": diagnosis,
            "tindakan": tindakan,
            "tanggal": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        }

        self.rekam_medis.append(rekam)

        print(f"  [✓] Rekam medis {data_satwa['nama']} berhasil disimpan.")


    # ── Tampilkan rekam medis ─────────────────────────────────────────────

    def tampilkan_rekam_medis(self):
        print("\n  📋 REKAM MEDIS SATWA")
        print(f"  {'─'*80}")

        if not self.rekam_medis:
            print("  (Belum ada rekam medis)")
            return

        for i, r in enumerate(self.rekam_medis, 1):
            print(f"\n  Rekam #{i}")
            print(f"  Chip ID   : {r['chip_id']}")
            print(f"  Nama      : {r['nama']}")
            print(f"  Spesies   : {r['spesies']}")
            print(f"  Keluhan   : {r['keluhan']}")
            print(f"  Diagnosis : {r['diagnosis']}")
            print(f"  Tindakan  : {r['tindakan']}")
            print(f"  Tanggal   : {r['tanggal']}")

        print(f"\n  Total rekam medis: {len(self.rekam_medis)}")


# ════════════════════════════════════════
#  MENU
# ════════════════════════════════════════

def menu_antrean(queue: QueueMedis, daftar_satwa: list):
    while True:
        print(f"\n  ╔══ ANTREAN PEMERIKSAAN MEDIS {'═'*12}")
        print(f"  ║  1. Tambah ke antrean")
        print(f"  ║  2. Panggil satwa berikutnya (Dequeue)")
        print(f"  ║  3. Lihat antrean saat ini")
        print(f"  ║  4. Lihat satwa paling depan (Peek)")
        print(f"  ║  5. Lihat rekam medis")
        print(f"  ║  0. Kembali")
        print(f"  ╚{'═'*40}")
        pilihan = input("  Pilih: ").strip()

        if pilihan == "1":
            chip = input("  Chip ID satwa  : ").strip()
            # Cari dari daftar satwa
            satwa = next((s for s in daftar_satwa if s.chip_id == chip), None)
            if not satwa:
                print(f"  [!] Chip ID '{chip}' tidak ditemukan.")
            else:
                keluhan  = input("  Keluhan        : ").strip()
                print("  Prioritas: 1. Normal  2. Darurat")
                p = input("  Pilih          : ").strip()
                prioritas = "Darurat" if p == "2" else "Normal"
                queue.enqueue(chip, satwa.nama, satwa.spesies, satwa.zona, keluhan, prioritas)

        elif pilihan == "2":
            hasil = queue.dequeue()

            if hasil:
                print(f"\n  Pemeriksaan untuk {hasil['nama']}")

                diagnosis = input("  Diagnosis : ")
                tindakan = input("  Tindakan  : ")

                queue.simpan_rekam_medis(
                    hasil,
                    diagnosis,
                    tindakan
                )

        elif pilihan == "3":
            queue.tampilkan()
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "4":
            depan = queue.peek()
            if depan:
                print(f"\n  Satwa berikutnya: {depan['nama']} ({depan['chip_id']}) — {depan['keluhan']}")
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "5":
            queue.tampilkan_rekam_medis()
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "0":
            break
        else:
            print("  [!] Pilihan tidak valid.")

        