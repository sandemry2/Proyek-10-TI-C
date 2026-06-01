"""
══════════════════════════════════════
Implementasi Graph untuk peta habitat dan jalur migrasi satwa.
Data diambil dari peta_migrasi (adjacency list) di data_dummy_ekosistem.py

Representasi: Adjacency List dengan bobot jarak (km)
"""

from collections import deque


# ════════════════════════════════════════
#  GRAPH
# ════════════════════════════════════════

class GraphMigrasi:
    """
    Peta habitat dan jalur migrasi antar zona menggunakan Graph berbobot.
    Dibangun dari dict peta_migrasi di data_dummy_ekosistem.
    """

    def __init__(self):
        self.adjacency = {}    # {zona: [(tetangga, jarak_km), ...]}
        self.jumlah_zona  = 0
        self.jumlah_jalur = 0

    # ── Bangun dari dict peta_migrasi ─────────────────────────────────
    def bangun_dari_dict(self, peta: dict):
        """
        Bangun graph dari peta_migrasi.
        Format: {"Zona A": [("Zona B", 12.5), ...], ...}
        """
        self.adjacency = {zona: list(jalur) for zona, jalur in peta.items()}
        self.jumlah_zona = len(self.adjacency)
        # Hitung jumlah jalur unik (tiap edge dihitung sekali)
        total = sum(len(v) for v in self.adjacency.values())
        self.jumlah_jalur = total // 2

    # ── Tampilkan adjacency list ──────────────────────────────────────
    def tampilkan_peta(self):
        print(f"\n  🗺️  PETA HABITAT & JALUR MIGRASI (Graph)")
        print(f"  {'─'*50}")
        print(f"  Zona     : {self.jumlah_zona} zona")
        print(f"  Jalur    : {self.jumlah_jalur} jalur migrasi")
        print(f"  {'─'*50}")
        for zona, jalur in self.adjacency.items():
            koneksi = ", ".join(f"{t}({j}km)" for t, j in jalur)
            print(f"  {zona:<10} → {koneksi}")
        print(f"  {'─'*50}")

    # ── BFS: Jalur terpendek (jumlah hop minimum) ────────────────────
    def bfs_jalur_terpendek(self, asal: str, tujuan: str) -> list:
        """
        Cari jalur dengan jumlah zona singgah paling sedikit (BFS).
        Return list nama zona, atau None jika tidak ada jalur.
        """
        if asal not in self.adjacency or tujuan not in self.adjacency:
            return None
        if asal == tujuan:
            return [asal]

        dikunjungi = {asal}
        antrian = deque([[asal]])

        while antrian:
            jalur = antrian.popleft()
            zona_sekarang = jalur[-1]
            for tetangga, _ in self.adjacency[zona_sekarang]:
                if tetangga == tujuan:
                    return jalur + [tetangga]
                if tetangga not in dikunjungi:
                    dikunjungi.add(tetangga)
                    antrian.append(jalur + [tetangga])
        return None

    # ── Dijkstra: Jalur terdekat berdasarkan jarak km ─────────────────
    def dijkstra_jarak_terpendek(self, asal: str, tujuan: str):
        """
        Cari jalur dengan total jarak paling pendek (Dijkstra sederhana).
        Return (jalur, total_jarak) atau (None, -1).
        """
        if asal not in self.adjacency or tujuan not in self.adjacency:
            return None, -1

        # Inisialisasi jarak
        jarak = {zona: float('inf') for zona in self.adjacency}
        jarak[asal] = 0
        sebelumnya = {zona: None for zona in self.adjacency}
        belum_dikunjungi = set(self.adjacency.keys())

        while belum_dikunjungi:
            # Pilih zona dengan jarak terkecil
            zona_min = min(belum_dikunjungi, key=lambda z: jarak[z])
            if jarak[zona_min] == float('inf'):
                break
            if zona_min == tujuan:
                break
            belum_dikunjungi.remove(zona_min)

            for tetangga, bobot in self.adjacency[zona_min]:
                if tetangga in belum_dikunjungi:
                    jarak_baru = jarak[zona_min] + bobot
                    if jarak_baru < jarak[tetangga]:
                        jarak[tetangga] = jarak_baru
                        sebelumnya[tetangga] = zona_min

        # Rekonstruksi jalur
        if jarak[tujuan] == float('inf'):
            return None, -1

        jalur = []
        zona = tujuan
        while zona is not None:
            jalur.insert(0, zona)
            zona = sebelumnya[zona]
        return jalur, round(jarak[tujuan], 1)

    # ── DFS: Semua zona yang terhubung dari suatu zona ────────────────
    def dfs_terhubung(self, awal: str) -> list:
        """
        Cari semua zona yang dapat dicapai dari zona awal (DFS rekursif).
        Return list nama zona.
        """
        if awal not in self.adjacency:
            return []
        dikunjungi = []
        self._dfs_rekursif(awal, set(), dikunjungi)
        return dikunjungi

    def _dfs_rekursif(self, zona: str, sudah: set, hasil: list):
        sudah.add(zona)
        hasil.append(zona)
        for tetangga, _ in self.adjacency[zona]:
            if tetangga not in sudah:
                self._dfs_rekursif(tetangga, sudah, hasil)

    # ── Tampilkan hasil jalur ─────────────────────────────────────────
    def tampilkan_jalur(self, asal: str, tujuan: str):
        print(f"\n  🦅 JALUR MIGRASI: {asal} → {tujuan}")
        print(f"  {'─'*50}")

        # BFS (hop minimum)
        jalur_bfs = self.bfs_jalur_terpendek(asal, tujuan)
        if jalur_bfs:
            jarak_bfs = self._hitung_jarak_jalur(jalur_bfs)
            print(f"  [BFS] Jalur singgah minimum:")
            print(f"  {' → '.join(jalur_bfs)}")
            print(f"  Jumlah singgah: {len(jalur_bfs)-1} | Jarak: ±{jarak_bfs} km")
        else:
            print(f"  [BFS] Tidak ada jalur yang ditemukan.")

        print()

        # Dijkstra (jarak minimum)
        jalur_dijk, total = self.dijkstra_jarak_terpendek(asal, tujuan)
        if jalur_dijk:
            print(f"  [Dijkstra] Jalur jarak terpendek:")
            print(f"  {' → '.join(jalur_dijk)}")
            print(f"  Jumlah singgah: {len(jalur_dijk)-1} | Jarak: {total} km")
        else:
            print(f"  [Dijkstra] Tidak ada jalur yang ditemukan.")
        print(f"  {'─'*50}")

    def _hitung_jarak_jalur(self, jalur: list) -> float:
        total = 0.0
        for i in range(len(jalur) - 1):
            for tetangga, jarak in self.adjacency[jalur[i]]:
                if tetangga == jalur[i + 1]:
                    total += jarak
                    break
        return round(total, 1)

    # ── Tampilkan semua zona yang terhubung ───────────────────────────
    def tampilkan_dfs(self, awal: str):
        hasil = self.dfs_terhubung(awal)
        print(f"\n  🔗 Zona terhubung dari {awal} (DFS):")
        print(f"  {'─'*35}")
        for i, zona in enumerate(hasil, 1):
            print(f"  {i}. {zona}")
        print(f"  {'─'*35}")
        print(f"  Total: {len(hasil)} zona terhubung")


# ════════════════════════════════════════
#  MENU
# ════════════════════════════════════════

def menu_graph(graph: GraphMigrasi):
    while True:
        print(f"\n  ╔══ PETA HABITAT & MIGRASI (Graph) {'═'*6}")
        print(f"  ║  1. Tampilkan peta habitat")
        print(f"  ║  2. Cari jalur migrasi (BFS + Dijkstra)")
        print(f"  ║  3. Zona terhubung dari suatu zona (DFS)")
        print(f"  ║  0. Kembali")
        print(f"  ╚{'═'*40}")
        pilih = input("  Pilih: ").strip()

        if pilih == "1":
            graph.tampilkan_peta()
            input("\n  Tekan Enter untuk lanjut...")
        elif pilih == "2":
            print("  Zona tersedia: Zona A, Zona B, Zona C, Zona D,")
            print("                 Zona E, Zona F, Zona G, Zona H, Zona I, Zona J")
            asal   = input("  Asal   : ").strip()
            tujuan = input("  Tujuan : ").strip()
            graph.tampilkan_jalur(asal, tujuan)
            input("\n  Tekan Enter untuk lanjut...")
        elif pilih == "3":
            awal = input("  Mulai dari zona: ").strip()
            graph.tampilkan_dfs(awal)
            input("\n  Tekan Enter untuk lanjut...")
        elif pilih == "0":
            break
        else:
            print("  [!] Pilihan tidak valid.")