"""
═════════════════════════════════════
Galeri foto satwa menggunakan Double Linked List (DLL).
Setiap foto = satu node, bisa navigasi maju (next) dan mundur (prev).

Struktur DLL: None ← Node1 ↔ Node2 ↔ ... ↔ NodeN → None

Persistensi:
  - galeri_foto.json dibaca saat program dibuka → dimuat ke DLL
  - Setiap tambah/hapus → galeri_foto.json diperbarui
"""

import json
import os


# ════════════════════════════════════════
#  PATH FILE
# ════════════════════════════════════════

BASE_DIR   = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)

FILE_GALERI = os.path.join(BASE_DIR, "data", "galeri_foto.json")


# ════════════════════════════════════════
#  HELPER BACA / TULIS JSON
# ════════════════════════════════════════

def _baca_json(path: str) -> list:
    if not os.path.exists(path):
        return []
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data if isinstance(data, list) else []
    except (json.JSONDecodeError, IOError):
        return []


def _tulis_json(path: str, data: list):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


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
            'nama_file' : str
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

    DLL dipilih karena:
    - Navigasi maju: node.next  (seperti gulir ke foto berikutnya)
    - Navigasi mundur: node.prev (seperti gulir ke foto sebelumnya)
    - Hapus dari tengah: O(1) karena bisa langsung hubungkan prev dan next
      tanpa traverse ulang dari HEAD

    Perbedaan dengan SLL: SLL hanya punya pointer 'next',
    sehingga untuk mundur harus traverse ulang dari HEAD — tidak efisien.
    """

    def __init__(self):
        self.head         = None
        self.tail         = None
        self.kursor       = None    # node yang sedang ditampilkan
        self.jumlah       = 0
        self._id_counter  = 1
        self._load_json()           # muat data dari JSON saat dibuat


    # ════════════════════════════════════════
    #  PERSISTENSI JSON
    # ════════════════════════════════════════

    def _load_json(self):
        """
        Baca galeri_foto.json dan masukkan setiap item ke DLL.
        Data dibaca dari depan ke belakang (urutan asli terjaga)
        karena DLL tambah di TAIL — berbeda dengan SLL yang tambah di HEAD.

        Juga lanjutkan _id_counter dari ID tertinggi yang ada
        agar ID foto baru tidak bentrok dengan yang sudah ada.
        """
        data_list = _baca_json(FILE_GALERI)

        if not data_list:
            return

        max_id = max(item.get("id_foto", 0) for item in data_list)
        self._id_counter = max_id + 1

        for item in data_list:
            self._tambah_internal(item)

    def _save_json(self):
        """
        Traverse DLL dari HEAD ke TAIL, kumpulkan semua data,
        tulis ke galeri_foto.json.
        Dipanggil setiap kali ada perubahan (tambah/hapus).
        """
        data_list = []
        node = self.head
        while node:
            data_list.append(node.data)
            node = node.next
        _tulis_json(FILE_GALERI, data_list)

    def _tambah_internal(self, data: dict):
        """
        Insert node di TAIL tanpa menyimpan ke JSON.
        Dipakai saat load dari file agar tidak tulis ulang saat membaca.
        """
        node = NodeFoto(data)

        if self.tail is None:
            # DLL kosong — node ini jadi satu-satunya
            self.head   = node
            self.tail   = node
            self.kursor = node
        else:
            # Sambungkan node baru ke tail lama
            node.prev       = self.tail   # node baru tahu siapa pendahulunya
            self.tail.next  = node        # tail lama tahu siapa penggantinya
            self.tail       = node        # tail digeser ke node baru

        self.jumlah += 1


    # ════════════════════════════════════════
    #  TAMBAH FOTO
    # ════════════════════════════════════════

    def tambah_foto(self, chip_id: str, nama: str, spesies: str,
                    nama_file: str, deskripsi: str, tanggal: str,
                    zona: str, tampilkan_pesan: bool = True):
        """
        Tambah foto baru di TAIL (belakang DLL).
        Foto terbaru selalu ada di paling akhir.
        Setelah insert, galeri disimpan ke JSON.
        """
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

        self._tambah_internal(data)
        self._id_counter += 1
        self._save_json()   # simpan perubahan ke file

        if tampilkan_pesan:
            print(f"  [✓] Foto '{nama_file}' ({nama}) ditambahkan ke galeri (#{data['id_foto']}).")


    # ════════════════════════════════════════
    #  HAPUS FOTO
    # ════════════════════════════════════════

    def hapus_foto(self, id_foto: int) -> bool:
        """
        Hapus node berdasarkan ID.
        Karena DLL punya pointer prev dan next, penghapusan bisa
        langsung tanpa traverse ulang — cukup sambungkan ulang
        node sebelum dan sesudah node yang dihapus.
        Setelah hapus, galeri disimpan ke JSON.
        """
        node = self.head
        while node:
            if node.data["id_foto"] == id_foto:

                # Sambungkan prev ke next, lewati node ini
                if node.prev:
                    node.prev.next = node.next
                else:
                    self.head = node.next   # node ini adalah HEAD

                if node.next:
                    node.next.prev = node.prev
                else:
                    self.tail = node.prev   # node ini adalah TAIL

                # Pindahkan kursor kalau node yang dihapus adalah kursor
                if self.kursor == node:
                    self.kursor = node.next or node.prev

                self.jumlah -= 1
                self._save_json()   # simpan perubahan ke file
                print(f"  [✓] Foto #{id_foto} dihapus dari galeri.")
                return True

            node = node.next

        print(f"  [!] Foto #{id_foto} tidak ditemukan.")
        return False


    # ════════════════════════════════════════
    #  NAVIGASI KURSOR
    # ════════════════════════════════════════

    def tampilkan_kursor(self):
        """Tampilkan foto yang sedang aktif (kursor)."""
        if self.kursor is None:
            print("  [!] Galeri kosong.")
            return
        d      = self.kursor.data
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
        """Geser kursor ke foto berikutnya (node.next)."""
        if self.kursor and self.kursor.next:
            self.kursor = self.kursor.next
            print(f"  [▶] Foto berikutnya: #{self.kursor.data['id_foto']} — {self.kursor.data['nama_file']}")
        else:
            print("  [!] Sudah di foto terakhir.")

    def mundur(self):
        """Geser kursor ke foto sebelumnya (node.prev)."""
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
        pos  = 1
        while node and node != self.kursor:
            node = node.next
            pos += 1
        return pos


    # ════════════════════════════════════════
    #  TAMPILKAN SEMUA
    # ════════════════════════════════════════

    def tampilkan_semua(self, arah: str = "maju"):
        """
        Tampilkan semua foto.
        arah='maju'   → traverse HEAD ke TAIL (node.next)
        arah='mundur' → traverse TAIL ke HEAD (node.prev)
        Ini keunggulan DLL — SLL tidak bisa traverse mundur.
        """
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
                d     = node.data
                aktif = " ◄ AKTIF" if node == self.kursor else ""
                print(f"  {d['id_foto']:<5} {d['nama_file']:<25} {d['nama']:<14} {d['tanggal']:<12} {d['zona']}{aktif}")
                node  = node.prev
        else:
            node = self.head
            while node:
                d     = node.data
                aktif = " ◄ AKTIF" if node == self.kursor else ""
                print(f"  {d['id_foto']:<5} {d['nama_file']:<25} {d['nama']:<14} {d['tanggal']:<12} {d['zona']}{aktif}")
                node  = node.next

        print(f"  {'─'*60}")
        print(f"  Total: {self.jumlah} foto")

    # ════════════════════════════════════════
    #  LOAD DATA AWAL (dari data_dummy)
    # ════════════════════════════════════════

    def load_data(self, data_galeri: list):
        """
        Isi galeri dari list dict (dipanggil dari data_dummy_ekosistem.py).
        Hanya dipakai jika JSON kosong — tidak menimpa data yang sudah ada.
        """
        if self.jumlah > 0:
            # Sudah ada data dari JSON, skip data dummy
            return

        for foto in data_galeri:
            self.tambah_foto(
                foto["chip_id"],
                foto["nama"],
                foto["spesies"],
                foto["nama_file"],
                foto["deskripsi"],
                foto["tanggal"],
                foto["zona"],
                tampilkan_pesan=False
            )


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
            chip  = input("  Chip ID satwa  : ").strip()
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
            a    = input("  Pilih: ").strip()
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