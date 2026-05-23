"""
structures/stack_undo.py — Anggota 3
═════════════════════════════════════
Stack untuk undo input data pengamatan satwa.
Implementasi: Linked List (bukan list Python biasa)

Konsep Stack: LIFO — Last In, First Out
  Push → masuk ke atas
  Pop  → keluar dari atas (undo)
"""

from tabulate import tabulate
from datetime import datetime


# ════════════════════════════════════════
#  NODE
# ════════════════════════════════════════

class NodeStack:
    def __init__(self, data: dict):
        """
        data: dict berisi satu catatan pengamatan
          {
            'chip_id'   : str,
            'nama'      : str,
            'aksi'      : str   — "Tambah" / "Update Zona" / dll
            'detail'    : str   — detail perubahan
            'waktu'     : str
          }
        """
        self.data = data
        self.next = None


# ════════════════════════════════════════
#  STACK
# ════════════════════════════════════════

class StackUndo:
    """
    Stack riwayat aksi pengamatan satwa.
    Setiap input data baru di-push ke stack.
    Undo = pop dari stack dan kembalikan ke kondisi sebelumnya.
    """

    def __init__(self, kapasitas: int = 20):
        self.top = None
        self.ukuran = 0
        self.kapasitas = kapasitas  # batas riwayat yang disimpan

    # ── Push ─────────────────────────────────────────────────────────
    def push(self, chip_id: str, nama: str, aksi: str, detail: str):
        """Simpan aksi ke dalam stack."""
        if self.ukuran >= self.kapasitas:
            print(f"  [!] Stack penuh ({self.kapasitas} riwayat). Aksi terlama dihapus otomatis.")
            self._hapus_bawah()

        data = {
            "chip_id": chip_id,
            "nama"   : nama,
            "aksi"   : aksi,
            "detail" : detail,
            "waktu"  : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        node = NodeStack(data)
        node.next = self.top
        self.top = node
        self.ukuran += 1
        print(f"  [📝] Aksi '{aksi}' untuk {nama} disimpan ke stack.")

    # ── Pop (Undo) ────────────────────────────────────────────────────
    def pop(self) -> dict:
        """Undo aksi terakhir — keluarkan dari top stack."""
        if self.kosong():
            print("  [!] Tidak ada aksi yang bisa di-undo.")
            return None

        data = self.top.data
        self.top = self.top.next
        self.ukuran -= 1
        print(f"\n  [↩️ ] Undo: '{data['aksi']}' untuk {data['nama']} ({data['chip_id']}) dibatalkan.")
        return data

    # ── Peek ──────────────────────────────────────────────────────────
    def peek(self) -> dict:
        """Lihat aksi terakhir tanpa menghapus."""
        if self.kosong():
            print("  [!] Stack kosong.")
            return None
        return self.top.data

    def kosong(self) -> bool:
        return self.top is None

    def panjang(self) -> int:
        return self.ukuran

    # ── Hapus node paling bawah (saat overflow) ───────────────────────
    def _hapus_bawah(self):
        if self.top is None:
            return
        if self.top.next is None:
            self.top = None
            self.ukuran -= 1
            return
        node = self.top
        while node.next and node.next.next:
            node = node.next
        node.next = None
        self.ukuran -= 1

    # ── Tampilkan riwayat ──────────────────────────────────────────────
    def tampilkan(self):
        print(f"\n  📋 RIWAYAT AKSI (Stack) — {self.ukuran} entri")
        print(f"  {'─'*58}")
        if self.kosong():
            print("  (Belum ada riwayat)")
            print(f"  {'─'*58}")
            return

        print(f"  {'No':<4} {'Chip ID':<9} {'Nama':<14} {'Aksi':<16} {'Waktu'}")
        print(f"  {'─'*58}")
        node = self.top
        nomor = 1
        while node:
            d = node.data
            label = "← TERBARU" if nomor == 1 else ""
            print(f"  {nomor:<4} {d['chip_id']:<9} {d['nama']:<14} {d['aksi']:<16} {d['waktu']} {label}")
            node = node.next
            nomor += 1
        print(f"  {'─'*58}")
        print(f"  Kapasitas stack: {self.kapasitas} aksi")


# ════════════════════════════════════════
#  MENU
# ════════════════════════════════════════

def menu_undo(stack: StackUndo, daftar_satwa: list):
    while True:
        print(f"\n  ╔══ INPUT & UNDO DATA PENGAMATAN {'═'*9}")
        print(f"  ║  1. Catat pengamatan baru (Push)")
        print(f"  ║  2. Undo aksi terakhir (Pop)")
        print(f"  ║  3. Lihat aksi terakhir (Peek)")
        print(f"  ║  4. Tampilkan semua riwayat")
        print(f"  ║  0. Kembali")
        print(f"  ╚{'═'*40}")
        pilihan = input("  Pilih: ").strip()

        if pilihan == "1":
            chip = input("  Chip ID satwa : ").strip()
            satwa = next((s for s in daftar_satwa if s.chip_id == chip), None)
            if not satwa:
                print(f"  [!] Chip ID '{chip}' tidak ditemukan.")
            else:
                print("  Jenis aksi: 1. Tambah Data  2. Update Zona  3. Update Berat  4. Lainnya")
                jenis = input("  Pilih       : ").strip()
                aksi_map = {"1": "Tambah Data", "2": "Update Zona", "3": "Update Berat", "4": "Lainnya"}
                aksi = aksi_map.get(jenis, "Lainnya")
                detail = input("  Detail aksi : ").strip()
                stack.push(chip, satwa.nama, aksi, detail)

        elif pilihan == "2":
            hasil = stack.pop()
            if hasil:
                print(f"  Detail yang dibatalkan: {hasil['detail']}")
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "3":
            aksi = stack.peek()
            if aksi:
                print(f"\n  Aksi terakhir: [{aksi['chip_id']}] {aksi['nama']} — {aksi['aksi']}")
                print(f"  Detail       : {aksi['detail']}")
                print(f"  Waktu        : {aksi['waktu']}")
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "4":
            stack.tampilkan()
            input("\n  Tekan Enter untuk lanjut...")

        elif pilihan == "0":
            break
        else:
            print("  [!] Pilihan tidak valid.")
