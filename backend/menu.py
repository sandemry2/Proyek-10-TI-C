from tabulate import tabulate
from data_dummy_ekosistem import data_satwa, animals_obj

from struktur.searching import menu_pencarian

from struktur.manajemen_data import (
    ManajemenPopulasi,
    DatabaseSatwa,
    SpesiesUnik,
    KoordinatHabitat
)

from struktur.hash_table import HashTableMedis

# ==============================
# IMPORT DATA DUMMY EKOSISTEM
# ==============================

from data_dummy_ekosistem import (
    queue_medis,
    stack_undo,
    log_penampakan,
    galeri_foto,
    jadwal_patroli,
    hash_medis,
    simulasi_rantai_makanan,
    bubble_sort_usia,
    selection_sort_berat,
    data_sorting,
    data_kepunahan,
    status_habitat
)

# ==============================
# IMPORT MENU STRUKTUR DATA
# ==============================

from struktur.queue_medis import menu_antrean
from struktur.stack_undo import menu_undo
from struktur.sll_log import menu_log
from struktur.dll_galeri import menu_galeri
from struktur.cll_patroli import menu_patroli


# ==============================
# KONVERSI DATA SATWA
# ==============================

def _build_daftar_satwa():
    """Konversi data_satwa dict -> list objek Satwa"""

    from struktur.satwa import Satwa

    return [
        Satwa(
            k,
            v["nama"],
            v["spesies"],
            v["usia"],
            v["berat_kg"],
            v["zona"],
            v["status_kepunahan"],
            v["jenis_kelamin"]
        )
        for k, v in data_satwa.items()
    ]


# ==============================
# DATA UTAMA
# ==============================

DAFTAR_SATWA = _build_daftar_satwa()

pengguna_aktif = "Admin Konservasi"


# ==============================
# MENU UTAMA
# ==============================

def menu_utama():

    while True:

        print("\n")
        print("=" * 55)
        print("     SISTEM SIMULASI EKOSISTEM - KELOMPOK 10")
        print("=" * 55)

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
        print(" 11.  Log Aktivitas Satwa (SLL)")
        print(" 12.  Galeri Foto Satwa (DLL)")
        print(" 13.  Rotasi Patroli (CLL)")
        print("  0.  Keluar")

        print("=" * 55)

        pilih = input("  Pilih menu : ").strip()

        # ==============================
        # MENU 1
        # ==============================

        if pilih == "1":
            _menu_lihat_satwa()

        # ==============================
        # MENU 2
        # ==============================

        elif pilih == "2":

            print(
                f"\n  Total satwa terdaftar : "
                f"{len(DAFTAR_SATWA)}"
            )

        # ==============================
        # MENU 3
        # ==============================

        elif pilih == "3":

            menu_pencarian(DAFTAR_SATWA)

        # ==============================
        # MENU 4
        # ==============================

        elif pilih == "4":

            mp = ManajemenPopulasi()

            for s in DAFTAR_SATWA:
                mp.tambah_satwa(s)

            mp.tampilkan_per_zona()

        # ==============================
        # MENU 5
        # ==============================

        elif pilih == "5":

            su = SpesiesUnik()

            su.tambah_dari_daftar(DAFTAR_SATWA)

            su.tampilkan()

        # ==============================
        # MENU 6 - QUEUE
        # ==============================

        elif pilih == "6":

            menu_antrean(queue_medis, DAFTAR_SATWA)

        # ==============================
        # MENU 7 - STACK
        # ==============================

        elif pilih == "7":

            menu_undo(stack_undo, DAFTAR_SATWA)

        # ==============================
        # MENU 8 - REKURSI
        # ==============================

        elif pilih == "8":

            predator = input(
                "  Masukkan nama predator "
                "(cth: Harimau Sumatera): "
            ).strip()

            print()

            simulasi_rantai_makanan(
                predator,
                maks=3
            )

        # ==============================
        # MENU 9 - SORTING
        # ==============================

        elif pilih == "9":

            _menu_sorting()

        # ==============================
        # MENU 10
        # ==============================

        elif pilih == "10":

            _tampilkan_status_habitat()

        # ==============================
        # MENU 11 - SINGLE LINKED LIST
        # ==============================

        elif pilih == "11":

            menu_log(
                log_penampakan,
                DAFTAR_SATWA,
                pengguna_aktif
            )

        # ==============================
        # MENU 12 - DOUBLE LINKED LIST
        # ==============================

        elif pilih == "12":

            menu_galeri(
                galeri_foto,
                DAFTAR_SATWA
            )

        # ==============================
        # MENU 13 - CIRCULAR LINKED LIST
        # ==============================

        elif pilih == "13":

            menu_patroli(jadwal_patroli)

        # ==============================
        # MENU 0
        # ==============================

        elif pilih == "0":

            print("\n  Program selesai. Sampai jumpa!")

            break

        else:

            print("\n  [!] Menu tidak tersedia")


# ==============================
# MENU LIHAT SATWA
# ==============================

def _menu_lihat_satwa():

    table = []

    for s in DAFTAR_SATWA:

        table.append([
            s.chip_id,
            s.nama,
            s.spesies,
            f"{s.usia} th",
            f"{s.berat_kg} kg",
            s.zona,
            s.status_kepunahan
        ])

    headers = [
        "Chip ID",
        "Nama",
        "Spesies",
        "Usia",
        "Berat",
        "Zona",
        "Status"
    ]

    print("\n🌿 DATA SATWA EKOSISTEM\n")

    print(
        tabulate(
            table,
            headers=headers,
            tablefmt="fancy_grid"
        )
    )


# ==============================
# MENU SORTING
# ==============================

def _menu_sorting():

    while True:

        print(f"\n  ╔══ SORTING SATWA {'═'*22}")
        print(f"  ║  1. Urutkan berdasarkan Usia (Bubble Sort)")
        print(f"  ║  2. Urutkan berdasarkan Berat (Selection Sort)")
        print(f"  ║  3. Urutkan berdasarkan Status Kepunahan")
        print(f"  ║  0. Kembali")
        print(f"  ╚{'═'*40}")

        pilih = input("  Pilih: ").strip()

        # ==============================
        # BUBBLE SORT
        # ==============================

        if pilih == "1":

            hasil = bubble_sort_usia(data_sorting)

            print(f"\n  Urutan Satwa (Termuda → Tertua):")
            print(f"  {'─'*50}")

            for s in hasil:

                print(
                    f"  {s['chip_id']} | "
                    f"{s['nama']:<12} | "
                    f"Usia: {s['usia']} thn"
                )

            print(f"  {'─'*50}")

        # ==============================
        # SELECTION SORT
        # ==============================

        elif pilih == "2":

            hasil = selection_sort_berat(data_sorting)

            print(f"\n  Urutan Satwa (Terberat → Teringan):")
            print(f"  {'─'*50}")

            for s in hasil:

                print(
                    f"  {s['chip_id']} | "
                    f"{s['nama']:<12} | "
                    f"Berat: {s['berat_kg']} kg"
                )

            print(f"  {'─'*50}")

        # ==============================
        # STATUS KEPUNAHAN
        # ==============================

        elif pilih == "3":

            print(
                f"\n  Urutan Satwa "
                f"berdasarkan Status Kepunahan:"
            )

            print(f"  {'─'*55}")

            for s in data_kepunahan:

                print(
                    f"  {s['status_kepunahan']:<12} | "
                    f"{s['nama']:<12} | "
                    f"{s['spesies']}"
                )

            print(f"  {'─'*55}")

        elif pilih == "0":

            break

        else:

            print("  [!] Pilihan tidak valid.")


# ==============================
# STATUS HABITAT
# ==============================

def _tampilkan_status_habitat():

    print(f"\n  🌿 STATUS HABITAT DAN LINGKUNGAN")

    print(f"  {'─'*70}")

    print(
        f"  {'Zona':<8} "
        f"{'Nama':<25} "
        f"{'Luas':>7} "
        f"{'Kondisi':<12} "
        f"{'Satwa':>6} "
        f"{'Kapasitas':>10} "
        f"{'Ancaman'}"
    )

    print(f"  {'─'*70}")

    for zona, info in status_habitat.items():

        print(
            f"  {zona:<8} "
            f"{info['nama']:<25} "
            f"{info['luas_ha']:>5}ha "
            f"{info['kondisi']:<12} "
            f"{info['satwa']:>6}/"
            f"{info['kapasitas']:<10} "
            f"{info['ancaman']}"
        )

    print(f"  {'─'*70}")
