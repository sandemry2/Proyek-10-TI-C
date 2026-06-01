"""
struktur/tree_taksonomi.py — Anggota 4
═══════════════════════════════════════
Implementasi Tree untuk taksonomi biologis satwa.
Data diambil dari taksonomi_tree (nested dict) di data_dummy_ekosistem.py

Struktur Tree: setiap node mewakili satu tingkat taksonomi
  Animalia → Chordata → Mammalia → Carnivora → Felidae → [spesies]
"""


# ════════════════════════════════════════
#  NODE
# ════════════════════════════════════════

class NodeTaksonomi:
    def __init__(self, nama: str, tingkat: str):
        """
        nama    : nama takson (misal: "Mammalia", "Felidae")
        tingkat : level taksonomi (Kingdom/Filum/Kelas/Ordo/Famili/Genus/Spesies)
        """
        self.nama    = nama
        self.tingkat = tingkat
        self.anak    = []      # list of NodeTaksonomi

    def tambah_anak(self, node: 'NodeTaksonomi'):
        self.anak.append(node)

    def adalah_daun(self) -> bool:
        return len(self.anak) == 0


# ════════════════════════════════════════
#  TREE
# ════════════════════════════════════════

URUTAN_TINGKAT = ["Kingdom", "Filum", "Kelas", "Ordo", "Famili", "Genus", "Spesies"]

class TreeTaksonomi:
    """
    Pohon taksonomi biologis satwa.
    Dibangun dari nested dict taksonomi_tree di data_dummy_ekosistem.
    """

    def __init__(self):
        self.akar = None
        self.jumlah_node  = 0
        self.jumlah_spesies = 0

    # ── Bangun tree dari nested dict ─────────────────────────────────
    def bangun_dari_dict(self, data: dict):
        """
        Bangun tree dari taksonomi_tree (nested dict dari data_dummy).
        Contoh:
          {"Animalia": {"Chordata": {"Mammalia": {"Carnivora": {"Felidae": [...]}}}}}
        """
        nama_root = list(data.keys())[0]
        self.akar = NodeTaksonomi(nama_root, "Kingdom")
        self.jumlah_node = 1
        self._rekursif_bangun(self.akar, data[nama_root], 1)

    def _rekursif_bangun(self, node_induk: NodeTaksonomi, data, kedalaman: int):
        tingkat = URUTAN_TINGKAT[min(kedalaman, len(URUTAN_TINGKAT)-1)]

        if isinstance(data, list):
            # Data adalah list spesies (daun)
            for nama_spesies in data:
                node = NodeTaksonomi(nama_spesies, "Spesies")
                node_induk.tambah_anak(node)
                self.jumlah_node += 1
                self.jumlah_spesies += 1
        elif isinstance(data, dict):
            for nama, isi in data.items():
                node = NodeTaksonomi(nama, tingkat)
                node_induk.tambah_anak(node)
                self.jumlah_node += 1
                self._rekursif_bangun(node, isi, kedalaman + 1)

    # ── Tampilkan pohon (DFS) ─────────────────────────────────────────
    def tampilkan(self, node: NodeTaksonomi = None, prefix: str = "", is_last: bool = True):
        if node is None:
            if self.akar is None:
                print("  [!] Tree belum dibangun.")
                return
            print(f"\n  🌳 POHON TAKSONOMI BIOLOGIS")
            print(f"  {'─'*45}")
            print(f"  {self.akar.tingkat:10s}: {self.akar.nama}")
            node = self.akar

        for i, anak in enumerate(node.anak):
            is_anak_terakhir = (i == len(node.anak) - 1)
            konektor = "└── " if is_anak_terakhir else "├── "
            warna_tingkat = {"Filum":"[F]","Kelas":"[K]","Ordo":"[O]",
                             "Famili":"[Fm]","Genus":"[G]","Spesies":"[Sp]"}
            label = warna_tingkat.get(anak.tingkat, "")
            print(f"  {prefix}{konektor}{label} {anak.nama}")
            ekstensi = "    " if is_anak_terakhir else "│   "
            self.tampilkan(anak, prefix + ekstensi, is_anak_terakhir)

    # ── Cari spesies (DFS rekursif) ───────────────────────────────────
    def cari(self, kata_kunci: str) -> list:
        """Cari node yang namanya mengandung kata_kunci. Return list jalur."""
        hasil = []
        if self.akar:
            self._rekursif_cari(self.akar, kata_kunci.lower(), [], hasil)
        return hasil

    def _rekursif_cari(self, node: NodeTaksonomi, target: str,
                       jalur: list, hasil: list):
        jalur_baru = jalur + [f"{node.tingkat}: {node.nama}"]
        if target in node.nama.lower():
            hasil.append(jalur_baru[:])
        for anak in node.anak:
            self._rekursif_cari(anak, target, jalur_baru, hasil)

    def tampilkan_hasil_cari(self, kata_kunci: str):
        hasil = self.cari(kata_kunci)
        print(f"\n  🔍 Pencarian taksonomi: '{kata_kunci}'")
        print(f"  {'─'*45}")
        if not hasil:
            print("  Tidak ditemukan dalam pohon taksonomi.")
            return
        for jalur in hasil:
            print("  " + " → ".join(jalur))
        print(f"\n  Ditemukan: {len(hasil)} node")

    # ── Statistik tree ────────────────────────────────────────────────
    def statistik(self):
        print(f"\n  📊 STATISTIK POHON TAKSONOMI")
        print(f"  {'─'*35}")
        print(f"  Total node      : {self.jumlah_node}")
        print(f"  Total spesies   : {self.jumlah_spesies}")
        print(f"  {'─'*35}")
        # Hitung per tingkat
        per_tingkat = {}
        if self.akar:
            self._hitung_per_tingkat(self.akar, per_tingkat)
        for t in URUTAN_TINGKAT:
            if t in per_tingkat:
                print(f"  {t:<12}: {per_tingkat[t]} node")

    def _hitung_per_tingkat(self, node: NodeTaksonomi, hasil: dict):
        hasil[node.tingkat] = hasil.get(node.tingkat, 0) + 1
        for anak in node.anak:
            self._hitung_per_tingkat(anak, hasil)


# ════════════════════════════════════════
#  MENU
# ════════════════════════════════════════

def menu_taksonomi(tree: TreeTaksonomi):
    while True:
        print(f"\n  ╔══ TAKSONOMI BIOLOGIS (Tree) {'═'*11}")
        print(f"  ║  1. Tampilkan pohon taksonomi")
        print(f"  ║  2. Cari spesies / takson")
        print(f"  ║  3. Statistik pohon")
        print(f"  ║  0. Kembali")
        print(f"  ╚{'═'*40}")
        pilih = input("  Pilih: ").strip()

        if pilih == "1":
            tree.tampilkan()
            input("\n  Tekan Enter untuk lanjut...")
        elif pilih == "2":
            kata = input("  Kata kunci: ").strip()
            tree.tampilkan_hasil_cari(kata)
            input("\n  Tekan Enter untuk lanjut...")
        elif pilih == "3":
            tree.statistik()
            input("\n  Tekan Enter untuk lanjut...")
        elif pilih == "0":
            break
        else:
            print("  [!] Pilihan tidak valid.")