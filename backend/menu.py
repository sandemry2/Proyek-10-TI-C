from data_dummy_ekosistem import data_satwa, animals_obj
from struktur.searching import menu_pencarian
from struktur.manajemen_data import ManajemenPopulasi, DatabaseSatwa, SpesiesUnik, KoordinatHabitat
from struktur.hash_table import HashTableMedis
from data_dummy_ekosistem import (
    queue_medis, stack_undo, log_penampakan,
    hash_medis, simulasi_rantai_makanan,
    bubble_sort_usia, selection_sort_berat,
    data_sorting, data_kepunahan, status_habitat
)


def _build_daftar_satwa():
    """Konversi data_satwa dict -> list objek Satwa untuk digunakan struktur data."""
    from struktur.satwa import Satwa
    return [
        Satwa(k, v["nama"], v["spesies"], v["usia"], v["berat_kg"],
              v["zona"], v["status_kepunahan"], v["jenis_kelamin"])
        for k, v in data_satwa.items()
    ]


def menu_utama():

    daftar_satwa = _build_daftar_satwa()

    while True:

        print("\n")
        print("=" * 50)
        print("   SISTEM SIMULASI EKOSISTEM - KELOMPOK 10")
        print("=" * 50)
        print("  1.  Lihat Data Satwa")
        print("  2.  Jumlah Satwa")
        print("  3.  Pencarian Satwa")
        print("  4.  Populasi per Zona")
        print("  5.  Spesies Unik (Set)")
        print("  6.  Antrean Medis (Queue)")
        print("  7.  Riwayat Undo (Stack)")
        print("  8.  Simulasi Rantai Makanan")
        print("  9.  Sorting Satwa")
        print(" 10.  Status Habitat")
        print("  0.  Keluar")
        print("=" * 50)

        pilih = input("  Pilih menu : ").strip()

        if pilih == "1":
            _menu_lihat_satwa(daftar_satwa)

        elif pilih == "2":
            print(f"\n  Total satwa terdaftar : {len(daftar_satwa)}")

        elif pilih == "3":
            menu_pencarian(daftar_satwa)

        elif pilih == "4":
            mp = ManajemenPopulasi()
            for s in daftar_satwa:
                mp.tambah_satwa(s)
            mp.tampilkan_per_zona()

        elif pilih == "5":
            su = SpesiesUnik()
            su.tambah_dari_daftar(daftar_satwa)
            su.tampilkan()

        elif pilih == "6":
            _tampilkan_queue()

        elif pilih == "7":
            _tampilkan_stack()

        elif pilih == "8":
            predator = input("  Masukkan nama predator (cth: Harimau Sumatera) : ").strip()
            print()
            simulasi_rantai_makanan(predator, maks=3)

        elif pilih == "9":
            _menu_sorting()

        elif pilih == "10":
            _tampilkan_status_habitat()

        elif pilih == "0":
            print("\n  Program selesai. Sampai jumpa!")
            break

        else:
            print("\n  [!] Menu tidak tersedia")


def _menu_lihat_satwa(daftar_satwa):
    db = DatabaseSatwa()
    db.muat_dari_list(daftar_satwa)
    db.tampilkan()


def _tampilkan_queue():
    print(f"\n  🏥 ANTREAN PEMERIKSAAN MEDIS — {len(queue_medis)} satwa")
    print(f"  {'─'*60}")
    print(f"  {'No':<4} {'Chip ID':<10} {'Nama':<10} {'Prioritas':<10} {'Keluhan':<30} Waktu")
    print(f"  {'─'*60}")
    for q in queue_medis:
        print(f"  {q['no']:<4} {q['chip_id']:<10} {q['nama']:<10} {q['prioritas']:<10} {q['keluhan']:<30} {q['waktu']}")
    print(f"  {'─'*60}")


def _tampilkan_stack():
    print(f"\n  📋 RIWAYAT AKSI (STACK — LIFO)")
    print(f"  {'─'*60}")
    print(f"  Urutan dari aksi terbaru (top of stack):")
    print(f"  {'─'*60}")
    for i, aksi in enumerate(reversed(stack_undo), 1):
        nilai_lama = aksi['nilai_lama'] if aksi['nilai_lama'] is not None else '-'
        nilai_baru = aksi['nilai_baru'] if aksi['nilai_baru'] is not None else '-'
        print(f"  [{i}] {aksi['aksi']:<6} | {aksi['chip_id']} | {aksi['field']}: {nilai_lama} → {nilai_baru}")
    print(f"  {'─'*60}")


def _menu_sorting():
    while True:
        print(f"\n  ╔══ SORTING SATWA {'═'*22}")
        print(f"  ║  1. Urutkan berdasarkan Usia (Bubble Sort)")
        print(f"  ║  2. Urutkan berdasarkan Berat (Selection Sort)")
        print(f"  ║  3. Urutkan berdasarkan Status Kepunahan")
        print(f"  ║  0. Kembali")
        print(f"  ╚{'═'*40}")
        pilih = input("  Pilih: ").strip()

        if pilih == "1":
            hasil = bubble_sort_usia(data_sorting)
            print(f"\n  Urutan Satwa (Termuda → Tertua):")
            print(f"  {'─'*50}")
            for s in hasil:
                print(f"  {s['chip_id']} | {s['nama']:<12} | Usia: {s['usia']} thn")
            print(f"  {'─'*50}")

        elif pilih == "2":
            hasil = selection_sort_berat(data_sorting)
            print(f"\n  Urutan Satwa (Terberat → Teringan):")
            print(f"  {'─'*50}")
            for s in hasil:
                print(f"  {s['chip_id']} | {s['nama']:<12} | Berat: {s['berat_kg']} kg")
            print(f"  {'─'*50}")

        elif pilih == "3":
            print(f"\n  Urutan Satwa berdasarkan Status Kepunahan:")
            print(f"  {'─'*55}")
            for s in data_kepunahan:
                print(f"  {s['status_kepunahan']:<12} | {s['nama']:<12} | {s['spesies']}")
            print(f"  {'─'*55}")

        elif pilih == "0":
            break
        else:
            print("  [!] Pilihan tidak valid.")


def _tampilkan_status_habitat():
    print(f"\n  🌿 STATUS HABITAT DAN LINGKUNGAN")
    print(f"  {'─'*70}")
    print(f"  {'Zona':<8} {'Nama':<25} {'Luas':>7} {'Kondisi':<12} {'Satwa':>6} {'Kapasitas':>10} {'Ancaman'}")
    print(f"  {'─'*70}")
    for zona, info in status_habitat.items():
        print(f"  {zona:<8} {info['nama']:<25} {info['luas_ha']:>5}ha "
              f"{info['kondisi']:<12} {info['satwa']:>6}/{info['kapasitas']:<10} {info['ancaman']}")
    print(f"  {'─'*70}")
