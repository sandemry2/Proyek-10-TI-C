"""
structures/cll_patroli.py — Anggota 3
══════════════════════════════════════
Rotasi patroli keamanan zona konservasi menggunakan Circular Linked List (CLL).
Node terakhir selalu menunjuk kembali ke node pertama (circular).

Struktur CLL: Head → Node1 → Node2 → ... → NodeN → (kembali ke Head)
"""

from tabulate import tabulate
from datetime import datetime


# ════════════════════════════════════════
#  NODE
# ════════════════════════════════════════

class NodePatroli:
    def __init__(self, data: dict):
        """
        data: dict berisi info satu tugas patroli
          {
            'id_patroli': int,
            'zona'      : str   — zona yang dipatroli
            'ranger'    : str   — nama petugas
            'shift'     : str   — "Pagi" / "Siang" / "Malam"
            'durasi_jam': int   — durasi patroli
            'status'    : str   — "Menunggu" / "Berlangsung" / "Selesai"
          }
        """
        self.data = data
        self.next = None    # pada CLL, node terakhir → node pertama


# ════════════════════════════════════════
#  CIRCULAR LINKED LIST
# ════════════════════════════════════════

class CLLPatroli:
    """
    Jadwal rotasi patroli menggunakan Circular Linked List.
    Setelah patroli terakhir selesai, otomatis kembali ke patroli pertama.
    """

    def __init__(self):
        self.head    = None
        self.tail    = None
        self.aktif   = None     # node patroli yang sedang/akan berjalan
        self.jumlah  = 0
        self._id_counter = 1

    # ── Tambah zona patroli ──────────────────────────────────────────
    def tambah_patroli(self, zona: str, ranger: str, shift: str, durasi_jam: int):
        data = {
            "id_patroli": self._id_counter,
            "zona"      : zona,
            "ranger"    : ranger,
            "shift"     : shift,
            "durasi_jam": durasi_jam,
            "status"    : "Menunggu"
        }
        node = NodePatroli(data)

        if self.head is None:
            self.head = node
            self.tail = node
            node.next = node    # menunjuk ke diri sendiri (circular)
            self.aktif = node
        else:
            node.next = self.head       # node baru menunjuk ke head
            self.tail.next = node       # tail lama menunjuk ke node baru
            self.tail = node            # tail diperbarui

        self.jumlah += 1
        self._id_counter += 1
        print(f"  [✓] Patroli #{data['id_patroli']} ditambahkan: {ranger} di {zona} ({shift}).")

    # ── Hapus zona patroli berdasarkan ID ────────────────────────────
    def hapus_patroli(self, id_patroli: int) -> bool:
        if self.head is None:
            print("  [!] Daftar patroli kosong.")
            return False

        # Kasus: hanya satu node
        if self.jumlah == 1:
            if self.head.data["id_patroli"] == id_patroli:
                self.head = self.tail = self.aktif = None
                self.jumlah -= 1
                print(f"  [✓] Patroli #{id_patroli} dihapus.")
                return True
            print(f"  [!] Patroli #{id_patroli} tidak ditemukan.")
            return False

        node = self.head
        prev = self.tail
        for _ in range(self.jumlah):
            if node.data["id_patroli"] == id_patroli:
                if node == self.head:
                    self.head = node.next
                if node == self.tail:
                    self.tail = prev
                if node == self.aktif:
                    self.aktif = node.next
                prev.next = node.next
                self.jumlah -= 1
                print(f"  [✓] Patroli #{id_patroli} dihapus.")
                return True
            prev = node
            node = node.next

        print(f"  [!] Patroli #{id_patroli} tidak ditemukan.")
        return False

    # ── Rotasi: jalankan patroli berikutnya ──────────────────────────
    def rotasi(self) -> dict:
        """
        Tandai patroli aktif sebagai 'Selesai', lalu pindah ke berikutnya.
        Karena circular, setelah terakhir otomatis kembali ke pertama.
        """
        if self.aktif is None:
            print("  [!] Daftar patroli kosong.")
            return None

        # Tandai yang aktif sebagai selesai
        self.aktif.data["status"] = "Selesai"
        nama_selesai = self.aktif.data["ranger"]
        zona_selesai = self.aktif.data["zona"]

        # Pindah ke node berikutnya
        self.aktif = self.aktif.next
        self.aktif.data["status"] = "Berlangsung"

        print(f"\n  [🔄] Rotasi patroli:")
        print(f"  Selesai   : {nama_selesai} ({zona_selesai})")
        print(f"  Berlangsung: {self.aktif.data['ranger']} ({self.aktif.data['zona']})")
        return self.aktif.data

    def mulai_patroli_pertama(self):
        """Tandai patroli pertama sebagai aktif."""
        if self.aktif:
            self.aktif.data["status"] = "Berlangsung"
            print(f"  [▶] Patroli dimulai: {self.aktif.data['ranger']} di {self.aktif.data['zona']}")

    # ── Tampilkan jadwal rotasi lengkap ──────────────────────────────
    def tampilkan_jadwal(self):
        print(f"\n  🛡️  JADWAL ROTASI PATROLI (Circular Linked List)")
        print(f"  {'─'*60}")
        if self.head is None:
            print("  (Belum ada jadwal patroli)")
            print(f"  {'─'*60}")
            return

        print(f"  {'ID':<5} {'Zona':<18} {'Ranger':<16} {'Shift':<8} {'Durasi':>7} {'Status'}")
        print(f"  {'─'*60}")

        node = self.head
        for _ in range(self.jumlah):
            d = node.data
            aktif_label = " ◄ AKTIF" if node == self.aktif else ""
            status_icon = {"Berlangsung": "🟢", "Selesai": "✅", "Menunggu": "⏳"}.get(d['status'], "")
            print(f"  {d['id_patroli']:<5} {d['zona']:<18} {d['ranger']:<16} "
                  f"{d['shift']:<8} {d['durasi_jam']:>5} jam "
                  f"{status_icon} {d['status']}{aktif_label}")
            node = node.next

        print(f"  {'─'*60}")
        print(f"  Total zona patroli : {self.jumlah}")
        print(f"  Sifat              : Circular (setelah #{self.tail.data['id_patroli']} → kembali ke #{self.head.data['id_patroli']})")

    # ── Simulasi satu siklus penuh ────────────────────────────────────
    def simulasi_siklus(self):
        if self.head is None:
            print("  [!] Daftar patroli kosong.")
            return
        print(f"\n  🔁 SIMULASI SATU SIKLUS PENUH ({self.jumlah} zona)")
        print(f"  {'─'*40}")
        self.mulai_patroli_pertama()
        for i in range(self.jumlah - 1):
            input(f"  Tekan Enter untuk rotasi ke zona berikutnya...")
            self.rotasi()
        print(f"\n  [✓] Satu siklus selesai. Memulai kembali dari awal...")
        self.rotasi()


# ════════════════════════════════════════
#  MENU
# ════════════════════════════════════════

def menu_patroli(cll: CLLPatroli):
    while True:
        print(f"\n  ╔══ ROTASI PATROLI KEAMANAN (CLL) {'═'*7}")
        print(f"  ║  1. Tampilkan jadwal patroli")
        print(f"  ║  2. Tambah zona patroli")
        print(f"  ║  3. Mulai patroli pertama")
        print(f"  ║  4. Rotasi ke petugas berikutnya")
        print(f"  ║  5. Simulasi satu siklus penuh")
        print(f"  ║  6. Hapus zona patroli")
        print(f"  ║  0. Kembali")
        print(f"  ╚{'═'*40}")
        pilihan = input("  Pilih: ").strip()

        if pilihan == "1":
            cll.tampilkan_jadwal()
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "2":
            zona     = input("  Nama zona          : ").strip()
            ranger   = input("  Nama ranger        : ").strip()
            print("  Shift: 1. Pagi  2. Siang  3. Malam")
            s = input("  Pilih shift        : ").strip()
            shift_map = {"1": "Pagi", "2": "Siang", "3": "Malam"}
            shift = shift_map.get(s, "Pagi")
            try:
                durasi = int(input("  Durasi (jam)       : ").strip())
            except ValueError:
                durasi = 2
            cll.tambah_patroli(zona, ranger, shift, durasi)

        elif pilihan == "3":
            cll.mulai_patroli_pertama()
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "4":
            cll.rotasi()
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "5":
            cll.simulasi_siklus()
            input("\n  Selesai. Tekan Enter untuk lanjut...")

        elif pilihan == "6":
            try:
                id_p = int(input("  ID patroli yang akan dihapus: ").strip())
                cll.hapus_patroli(id_p)
            except ValueError:
                print("  [!] Masukkan angka yang valid.")

        elif pilihan == "0":
            break
        else:
            print("  [!] Pilihan tidak valid.")
