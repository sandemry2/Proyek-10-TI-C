"""
structures/dll_galeri.py — Anggota 3
═════════════════════════════════════
Galeri foto satwa menggunakan Double Linked List (DLL).
Setiap foto = satu node, bisa navigasi maju (next) dan mundur (prev).

Struktur DLL: None ← Node1 ↔ Node2 ↔ ... ↔ NodeN → None
"""

from tabulate import tabulate

# ════════════════════════════════════════
#  NODE
# ════════════════════════════════════════

class NodeFoto:
    def __init__(self, data: dict):
        """
        data: dict berisi info satu foto
          {
            'id_foto'   : int
            'chip_id'   : str,
            'nama'      : str,
            'spesies'   : str,
            'nama_file' : str   — misal: "raja_makan_2025.jpg"
            'deskripsi' : str
            'tanggal'   : str
            'zona'      : str
          }
        """
        self.data = data
        self.prev = None    # pointer ke node sebelumnya
        self.next = None    # pointer ke node berikutnya


# ════════════════════════════════════════
#  DOUBLE LINKED LIST
# ════════════════════════════════════════

class DLLGaleri:
    """
    Galeri foto satwa dengan navigasi dua arah (maju/mundur).
    Mendukung tambah foto, hapus, dan slideshow.
    """

    def __init__(self):
        self.head    = None     # foto pertama
        self.tail    = None     # foto terakhir
        self.kursor  = None     # foto yang sedang dilihat
        self.jumlah  = 0
        self._id_counter = 1

    # ── Tambah foto (di belakang) ─────────────────────────────────────
    def tambah_foto(self, chip_id: str, nama: str, spesies: str,
                    nama_file: str, deskripsi: str, tanggal: str, zona: str):
        data = {
            "id_foto"   : self._id_counter,
            "chip_id"   : chip_id,
            "nama"      : nama,
            "spesies"   : spesies,
            "nama_file" : nama_file,
            "deskripsi" : deskripsi,
            "tanggal"   : tanggal,
            "zona"      : zona
        }
        node = NodeFoto(data)

        if self.tail is None:
            self.head = self.tail = node
            self.kursor = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.jumlah += 1
        self._id_counter += 1
        print(f"  [✓] Foto '{nama_file}' ({nama}) ditambahkan ke galeri (#{data['id_foto']}).")

    # ── Hapus foto berdasarkan ID ──────────────────────────────────────
    def hapus_foto(self, id_foto: int) -> bool:
        node = self.head
        while node:
            if node.data["id_foto"] == id_foto:
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.head = node.next
                if node.next:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev
                # Pindahkan kursor jika yang dihapus adalah kursor
                if self.kursor == node:
                    self.kursor = node.next or node.prev
                self.jumlah -= 1
                print(f"  [✓] Foto #{id_foto} dihapus dari galeri.")
                return True
            node = node.next
        print(f"  [!] Foto #{id_foto} tidak ditemukan.")
        return False

    # ── Navigasi ──────────────────────────────────────────────────────
    def tampilkan_kursor(self):
        """Tampilkan foto yang sedang aktif (kursor)."""
        if self.kursor is None:
            print("  [!] Galeri kosong.")
            return
        d = self.kursor.data
        posisi = self._posisi_kursor()
        print(f"\n  🖼️  GALERI FOTO  [{posisi}/{self.jumlah}]")
        print(f"  {'═'*42}")
        print(f"  ID Foto     : #{d['id_foto']}")
        print(f"  File        : {d['nama_file']}")
        print(f"  Satwa       : {d['nama']} ({d['spesies']})")
        print(f"  Zona        : {d['zona']}")
        print(f"  Tanggal     : {d['tanggal']}")
        print(f"  Deskripsi   : {d['deskripsi']}")
        print(f"  {'─'*42}")
        prev_info = f"◀ #{self.kursor.prev.data['id_foto']}" if self.kursor.prev else "◀ (awal)"
        next_info = f"#{self.kursor.next.data['id_foto']} ▶" if self.kursor.next else "(akhir) ▶"
        print(f"  {prev_info:<18}  {next_info:>18}")
        print(f"  {'═'*42}")

    def maju(self):
        """Geser ke foto berikutnya."""
        if self.kursor and self.kursor.next:
            self.kursor = self.kursor.next
            print(f"  [▶] Foto berikutnya: #{self.kursor.data['id_foto']} — {self.kursor.data['nama_file']}")
        else:
            print("  [!] Sudah di foto terakhir.")

    def mundur(self):
        """Geser ke foto sebelumnya."""
        if self.kursor and self.kursor.prev:
            self.kursor = self.kursor.prev
            print(f"  [◀] Foto sebelumnya: #{self.kursor.data['id_foto']} — {self.kursor.data['nama_file']}")
        else:
            print("  [!] Sudah di foto pertama.")

    def ke_awal(self):
        self.kursor = self.head
        print("  [⏮] Kembali ke foto pertama.")

    def ke_akhir(self):
        self.kursor = self.tail
        print("  [⏭] Loncat ke foto terakhir.")

    def _posisi_kursor(self) -> int:
        node = self.head
        pos = 1
        while node and node != self.kursor:
            node = node.next
            pos += 1
        return pos

    # ── Tampilkan semua foto (daftar) ─────────────────────────────────
    def tampilkan_semua(self, arah: str = "maju"):
        print(f"\n  🗂️  DAFTAR GALERI FOTO (DLL — arah: {arah})")
        print(f"  {'─'*60}")
        if self.head is None:
            print("  (Galeri kosong)")
            print(f"  {'─'*60}")
            return

        print(f"  {'ID':<5} {'Nama File':<25} {'Satwa':<14} {'Tanggal':<12} {'Zona'}")
        print(f"  {'─'*60}")

        if arah == "mundur":
            node = self.tail
            while node:
                d = node.data
                aktif = " ◄ AKTIF" if node == self.kursor else ""
                print(f"  {d['id_foto']:<5} {d['nama_file']:<25} {d['nama']:<14} {d['tanggal']:<12} {d['zona']}{aktif}")
                node = node.prev
        else:
            node = self.head
            while node:
                d = node.data
                aktif = " ◄ AKTIF" if node == self.kursor else ""
                print(f"  {d['id_foto']:<5} {d['nama_file']:<25} {d['nama']:<14} {d['tanggal']:<12} {d['zona']}{aktif}")
                node = node.next
        print(f"  {'─'*60}")
        print(f"  Total: {self.jumlah} foto")


# ════════════════════════════════════════
#  MENU
# ════════════════════════════════════════

def menu_galeri(dll: DLLGaleri, daftar_satwa: list):
    while True:
        print(f"\n  ╔══ GALERI FOTO SATWA (DLL) {'═'*14}")
        print(f"  ║  1. Tampilkan foto saat ini")
        print(f"  ║  2. Foto berikutnya  (▶ next)")
        print(f"  ║  3. Foto sebelumnya  (◀ prev)")
        print(f"  ║  4. Ke foto pertama  (⏮)")
        print(f"  ║  5. Ke foto terakhir (⏭)")
        print(f"  ║  6. Tambah foto baru")
        print(f"  ║  7. Tampilkan semua foto")
        print(f"  ║  8. Hapus foto")
        print(f"  ║  0. Kembali")
        print(f"  ╚{'═'*40}")
        pilihan = input("  Pilih: ").strip()

        if pilihan == "1":
            dll.tampilkan_kursor()
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "2":
            dll.maju()
            dll.tampilkan_kursor()
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "3":
            dll.mundur()
            dll.tampilkan_kursor()
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "4":
            dll.ke_awal()
            dll.tampilkan_kursor()
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "5":
            dll.ke_akhir()
            dll.tampilkan_kursor()
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "6":
            chip = input("  Chip ID satwa  : ").strip()
            satwa = next((s for s in daftar_satwa if s.chip_id == chip), None)
            if not satwa:
                print(f"  [!] Chip ID '{chip}' tidak ditemukan.")
            else:
                nama_file = input("  Nama file foto : ").strip()
                deskripsi = input("  Deskripsi      : ").strip()
                tanggal   = input("  Tanggal (YYYY-MM-DD): ").strip()
                dll.tambah_foto(chip, satwa.nama, satwa.spesies,
                                nama_file, deskripsi, tanggal, satwa.zona)

        elif pilihan == "7":
            print("  Arah tampilan: 1. Maju (default)  2. Mundur")
            a = input("  Pilih: ").strip()
            arah = "mundur" if a == "2" else "maju"
            dll.tampilkan_semua(arah)
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "8":
            try:
                id_foto = int(input("  ID foto yang akan dihapus: ").strip())
                dll.hapus_foto(id_foto)
            except ValueError:
                print("  [!] Masukkan angka yang valid.")

        elif pilihan == "0":
            break
        else:
            print("  [!] Pilihan tidak valid.")
