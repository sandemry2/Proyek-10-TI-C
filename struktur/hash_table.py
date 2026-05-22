"""
═════════════════════════════════════
Hash Table manual untuk pencarian data medis satwa.
Implementasi: Separate Chaining (tiap bucket = linked list)
"""


# ════════════════════════════════════════
#  Node untuk chaining
# ════════════════════════════════════════

class NodeMedis:
    def __init__(self, chip_id: str, data_medis: dict):
        self.chip_id = chip_id
        self.data_medis = data_medis   # dict berisi info medis
        self.next = None               # pointer ke node berikutnya (chaining)


# ════════════════════════════════════════
#  Hash Table
# ════════════════════════════════════════

class HashTableMedis:
    """
    Hash Table untuk menyimpan dan mencari data medis satwa.

    Cara kerja:
      1. chip_id di-hash → index bucket
      2. Jika terjadi collision → node baru ditambahkan di depan (chaining)
      3. Pencarian: hash chip_id → cek bucket → traverse linked list
    """

    def __init__(self, ukuran: int = 16):
        self.ukuran = ukuran
        self.bucket = [None] * self.ukuran   # array of NodeMedis
        self.jumlah_data = 0

    # ── Hash function ────────────────────────────────────────────────
    def _hash(self, chip_id: str) -> int:
        """
        Hash function sederhana:
        Jumlahkan nilai ASCII setiap karakter × posisi, modulo ukuran tabel.
        """
        nilai = 0
        for i, karakter in enumerate(chip_id):
            nilai += ord(karakter) * (i + 1)
        return nilai % self.ukuran

    # ── Insert ───────────────────────────────────────────────────────
    def simpan(self, chip_id: str, data_medis: dict) -> bool:
        """
        Simpan data medis satwa.
        Jika chip_id sudah ada, data diperbarui.
        """
        index = self._hash(chip_id)
        node = self.bucket[index]

        # Cek apakah chip_id sudah ada → update
        while node:
            if node.chip_id == chip_id:
                node.data_medis = data_medis
                print(f"  [✓] Data medis '{chip_id}' diperbarui (index bucket: {index})")
                return True
            node = node.next

        # Belum ada → insert di depan (chaining)
        node_baru = NodeMedis(chip_id, data_medis)
        node_baru.next = self.bucket[index]
        self.bucket[index] = node_baru
        self.jumlah_data += 1
        print(f"  [✓] Data medis '{chip_id}' disimpan (index bucket: {index})")
        return True

    # ── Search ───────────────────────────────────────────────────────
    def cari(self, chip_id: str) -> dict:
        """
        Cari data medis berdasarkan Chip ID.
        Return: dict data medis, atau None jika tidak ditemukan.
        Kompleksitas rata-rata: O(1)
        """
        index = self._hash(chip_id)
        node = self.bucket[index]

        while node:
            if node.chip_id == chip_id:
                return node.data_medis
            node = node.next

        return None

    # ── Delete ───────────────────────────────────────────────────────
    def hapus(self, chip_id: str) -> bool:
        index = self._hash(chip_id)
        node = self.bucket[index]
        sebelumnya = None

        while node:
            if node.chip_id == chip_id:
                if sebelumnya:
                    sebelumnya.next = node.next
                else:
                    self.bucket[index] = node.next
                self.jumlah_data -= 1
                print(f"  [✓] Data medis '{chip_id}' dihapus.")
                return True
            sebelumnya = node
            node = node.next

        print(f"  [!] Chip ID '{chip_id}' tidak ditemukan.")
        return False

    # ── Tampilkan satu ───────────────────────────────────────────────
    def tampilkan_data_medis(self, chip_id: str):
        data = self.cari(chip_id)
        print(f"\n  💊 DATA MEDIS — Chip ID: {chip_id}")
        print(f"  {'─'*40}")
        if not data:
            print(f"  [!] Data tidak ditemukan.")
            return
        for kunci, nilai in data.items():
            print(f"  {kunci:<20} : {nilai}")
        print(f"  {'─'*40}")

    # ── Tampilkan seluruh tabel ───────────────────────────────────────
    def tampilkan_tabel(self):
        print(f"\n  🏥 HASH TABLE DATA MEDIS")
        print(f"  Ukuran tabel : {self.ukuran} bucket")
        print(f"  Jumlah data  : {self.jumlah_data}")
        print(f"  Load factor  : {self.jumlah_data / self.ukuran:.2f}")
        print(f"  {'─'*45}")

        for i, node in enumerate(self.bucket):
            if node:
                rantai = []
                while node:
                    rantai.append(f"{node.chip_id}({node.data_medis.get('status', '?')})")
                    node = node.next
                print(f"  Bucket[{i:02d}] → " + " → ".join(rantai))

        print(f"  {'─'*45}")

    # ── Tampilkan visualisasi collision ──────────────────────────────
    def tampilkan_statistik(self):
        terisi = sum(1 for b in self.bucket if b)
        maks_chain = 0
        for node in self.bucket:
            panjang = 0
            while node:
                panjang += 1
                node = node.next
            maks_chain = max(maks_chain, panjang)

        print(f"\n  📊 STATISTIK HASH TABLE")
        print(f"  {'─'*35}")
        print(f"  Total bucket        : {self.ukuran}")
        print(f"  Bucket terisi       : {terisi}")
        print(f"  Bucket kosong       : {self.ukuran - terisi}")
        print(f"  Rantai terpanjang   : {maks_chain} node")
        print(f"  {'─'*35}")
