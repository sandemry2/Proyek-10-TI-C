# ============================================================
# DATA DUMMY - SIMULASI EKOSISTEM (Kelompok 10)
# 50 data satwa + semua kebutuhan struktur data
# ============================================================

from struktur.queue_medis import QueueMedis
from struktur.stack_undo import StackUndo
from struktur.sll_log import SLLLog
from struktur.dll_galeri import DLLGaleri
from struktur.cll_patroli import CLLPatroli, menu_patroli


# ─────────────────────────────────────────────────────────────
#  DICTIONARY — 50 Data Satwa berdasarkan Chip ID - menu.py
# ─────────────────────────────────────────────────────────────
data_satwa = {
    # ── Harimau Sumatera (5 ekor) ──
    "SWA-001": {"nama": "Rimba",   "spesies": "Harimau Sumatera",  "usia": 5,  "berat_kg": 120,  "zona": "Zona A", "status_kepunahan": "Kritis",   "jenis_kelamin": "Jantan"},
    "SWA-002": {"nama": "Luna",    "spesies": "Harimau Sumatera",  "usia": 3,  "berat_kg": 95,   "zona": "Zona F", "status_kepunahan": "Kritis",   "jenis_kelamin": "Betina"},
    "SWA-003": {"nama": "Tegar",   "spesies": "Harimau Sumatera",  "usia": 8,  "berat_kg": 130,  "zona": "Zona J", "status_kepunahan": "Kritis",   "jenis_kelamin": "Jantan"},
    "SWA-004": {"nama": "Senja",   "spesies": "Harimau Sumatera",  "usia": 2,  "berat_kg": 65,   "zona": "Zona A", "status_kepunahan": "Kritis",   "jenis_kelamin": "Betina"},
    "SWA-005": {"nama": "Gagah",   "spesies": "Harimau Sumatera",  "usia": 11, "berat_kg": 140,  "zona": "Zona F", "status_kepunahan": "Kritis",   "jenis_kelamin": "Jantan"},
    # ── Orangutan Borneo (5 ekor) ──
    "SWA-006": {"nama": "Borno",   "spesies": "Orangutan Borneo",  "usia": 12, "berat_kg": 78,   "zona": "Zona B", "status_kepunahan": "Terancam", "jenis_kelamin": "Jantan"},
    "SWA-007": {"nama": "Sari",    "spesies": "Orangutan Borneo",  "usia": 8,  "berat_kg": 52,   "zona": "Zona I", "status_kepunahan": "Terancam", "jenis_kelamin": "Betina"},
    "SWA-008": {"nama": "Obi",     "spesies": "Orangutan Borneo",  "usia": 3,  "berat_kg": 25,   "zona": "Zona B", "status_kepunahan": "Terancam", "jenis_kelamin": "Jantan"},
    "SWA-009": {"nama": "Nisa",    "spesies": "Orangutan Borneo",  "usia": 15, "berat_kg": 60,   "zona": "Zona I", "status_kepunahan": "Terancam", "jenis_kelamin": "Betina"},
    "SWA-010": {"nama": "Raka",    "spesies": "Orangutan Borneo",  "usia": 20, "berat_kg": 85,   "zona": "Zona B", "status_kepunahan": "Terancam", "jenis_kelamin": "Jantan"},
    # ── Gajah Sumatera (5 ekor) ──
    "SWA-011": {"nama": "Agung",   "spesies": "Gajah Sumatera",    "usia": 20, "berat_kg": 3500, "zona": "Zona D", "status_kepunahan": "Kritis",   "jenis_kelamin": "Jantan"},
    "SWA-012": {"nama": "Permata", "spesies": "Gajah Sumatera",    "usia": 15, "berat_kg": 2800, "zona": "Zona D", "status_kepunahan": "Kritis",   "jenis_kelamin": "Betina"},
    "SWA-013": {"nama": "Besar",   "spesies": "Gajah Sumatera",    "usia": 25, "berat_kg": 4100, "zona": "Zona D", "status_kepunahan": "Kritis",   "jenis_kelamin": "Jantan"},
    "SWA-014": {"nama": "Anggun",  "spesies": "Gajah Sumatera",    "usia": 10, "berat_kg": 2400, "zona": "Zona D", "status_kepunahan": "Kritis",   "jenis_kelamin": "Betina"},
    "SWA-015": {"nama": "Ksatria", "spesies": "Gajah Sumatera",    "usia": 8,  "berat_kg": 1800, "zona": "Zona D", "status_kepunahan": "Kritis",   "jenis_kelamin": "Jantan"},
    # ── Badak Sumatera (3 ekor) ──
    "SWA-016": {"nama": "Wira",    "spesies": "Badak Sumatera",    "usia": 7,  "berat_kg": 650,  "zona": "Zona F", "status_kepunahan": "Kritis",   "jenis_kelamin": "Jantan"},
    "SWA-017": {"nama": "Melati",  "spesies": "Badak Sumatera",    "usia": 12, "berat_kg": 720,  "zona": "Zona J", "status_kepunahan": "Kritis",   "jenis_kelamin": "Betina"},
    "SWA-018": {"nama": "Kuat",    "spesies": "Badak Sumatera",    "usia": 4,  "berat_kg": 480,  "zona": "Zona F", "status_kepunahan": "Kritis",   "jenis_kelamin": "Jantan"},
    # ── Beruang Madu (3 ekor) ──
    "SWA-019": {"nama": "Madu",    "spesies": "Beruang Madu",      "usia": 4,  "berat_kg": 55,   "zona": "Zona A", "status_kepunahan": "Rentan",   "jenis_kelamin": "Betina"},
    "SWA-020": {"nama": "Nara",    "spesies": "Beruang Madu",      "usia": 6,  "berat_kg": 60,   "zona": "Zona F", "status_kepunahan": "Rentan",   "jenis_kelamin": "Jantan"},
    "SWA-021": {"nama": "Manis",   "spesies": "Beruang Madu",      "usia": 2,  "berat_kg": 30,   "zona": "Zona E", "status_kepunahan": "Rentan",   "jenis_kelamin": "Betina"},
    # ── Macan Tutul Jawa (3 ekor) ──
    "SWA-022": {"nama": "Jago",    "spesies": "Macan Tutul Jawa",  "usia": 6,  "berat_kg": 48,   "zona": "Zona E", "status_kepunahan": "Kritis",   "jenis_kelamin": "Jantan"},
    "SWA-023": {"nama": "Lincah",  "spesies": "Macan Tutul Jawa",  "usia": 4,  "berat_kg": 38,   "zona": "Zona J", "status_kepunahan": "Kritis",   "jenis_kelamin": "Betina"},
    "SWA-024": {"nama": "Bintik",  "spesies": "Macan Tutul Jawa",  "usia": 9,  "berat_kg": 55,   "zona": "Zona E", "status_kepunahan": "Kritis",   "jenis_kelamin": "Jantan"},
    # ── Rusa Sambar (3 ekor) ──
    "SWA-025": {"nama": "Dara",    "spesies": "Rusa Sambar",       "usia": 3,  "berat_kg": 180,  "zona": "Zona D", "status_kepunahan": "Rentan",   "jenis_kelamin": "Betina"},
    "SWA-026": {"nama": "Riko",    "spesies": "Rusa Sambar",       "usia": 5,  "berat_kg": 200,  "zona": "Zona E", "status_kepunahan": "Rentan",   "jenis_kelamin": "Jantan"},
    "SWA-027": {"nama": "Cepat",   "spesies": "Rusa Sambar",       "usia": 4,  "berat_kg": 190,  "zona": "Zona A", "status_kepunahan": "Rentan",   "jenis_kelamin": "Jantan"},
    # ── Tapir Asia (3 ekor) ──
    "SWA-028": {"nama": "Tapa",    "spesies": "Tapir Asia",        "usia": 9,  "berat_kg": 310,  "zona": "Zona A", "status_kepunahan": "Terancam", "jenis_kelamin": "Jantan"},
    "SWA-029": {"nama": "Belang",  "spesies": "Tapir Asia",        "usia": 5,  "berat_kg": 270,  "zona": "Zona F", "status_kepunahan": "Terancam", "jenis_kelamin": "Betina"},
    "SWA-030": {"nama": "Hitam",   "spesies": "Tapir Asia",        "usia": 2,  "berat_kg": 190,  "zona": "Zona D", "status_kepunahan": "Terancam", "jenis_kelamin": "Jantan"},
    # ── Binturong (2 ekor) ──
    "SWA-031": {"nama": "Bintang", "spesies": "Binturong",         "usia": 5,  "berat_kg": 18,   "zona": "Zona B", "status_kepunahan": "Rentan",   "jenis_kelamin": "Jantan"},
    "SWA-032": {"nama": "Koko",    "spesies": "Binturong",         "usia": 7,  "berat_kg": 22,   "zona": "Zona I", "status_kepunahan": "Rentan",   "jenis_kelamin": "Jantan"},
    # ── Trenggiling Sunda (3 ekor) ──
    "SWA-033": {"nama": "Sisik",   "spesies": "Trenggiling Sunda", "usia": 2,  "berat_kg": 5,    "zona": "Zona C", "status_kepunahan": "Kritis",   "jenis_kelamin": "Betina"},
    "SWA-034": {"nama": "Kanci",   "spesies": "Trenggiling Sunda", "usia": 3,  "berat_kg": 6,    "zona": "Zona I", "status_kepunahan": "Kritis",   "jenis_kelamin": "Jantan"},
    "SWA-035": {"nama": "Gulung",  "spesies": "Trenggiling Sunda", "usia": 4,  "berat_kg": 7,    "zona": "Zona A", "status_kepunahan": "Kritis",   "jenis_kelamin": "Betina"},
    # ── Elang Jawa (3 ekor) ──
    "SWA-036": {"nama": "Garuda",  "spesies": "Elang Jawa",        "usia": 10, "berat_kg": 3.0,  "zona": "Zona E", "status_kepunahan": "Terancam", "jenis_kelamin": "Jantan"},
    "SWA-037": {"nama": "Elok",    "spesies": "Elang Jawa",        "usia": 6,  "berat_kg": 2.8,  "zona": "Zona G", "status_kepunahan": "Terancam", "jenis_kelamin": "Betina"},
    "SWA-038": {"nama": "Sayap",   "spesies": "Elang Jawa",        "usia": 3,  "berat_kg": 2.2,  "zona": "Zona J", "status_kepunahan": "Terancam", "jenis_kelamin": "Jantan"},
    # ── Rangkong Gading (2 ekor) ──
    "SWA-039": {"nama": "Rangka",  "spesies": "Rangkong Gading",   "usia": 14, "berat_kg": 2.5,  "zona": "Zona B", "status_kepunahan": "Kritis",   "jenis_kelamin": "Jantan"},
    "SWA-040": {"nama": "Tanduk",  "spesies": "Rangkong Gading",   "usia": 10, "berat_kg": 2.1,  "zona": "Zona G", "status_kepunahan": "Kritis",   "jenis_kelamin": "Betina"},
    # ── Kucing Batu (2 ekor) ──
    "SWA-041": {"nama": "Lincah",  "spesies": "Kucing Batu",       "usia": 3,  "berat_kg": 8,    "zona": "Zona F", "status_kepunahan": "Rentan",   "jenis_kelamin": "Betina"},
    "SWA-042": {"nama": "Batu",    "spesies": "Kucing Batu",       "usia": 5,  "berat_kg": 10,   "zona": "Zona B", "status_kepunahan": "Rentan",   "jenis_kelamin": "Jantan"},
    # ── Bekantan (2 ekor) ──
    "SWA-043": {"nama": "Bekan",   "spesies": "Bekantan",          "usia": 7,  "berat_kg": 20,   "zona": "Zona C", "status_kepunahan": "Terancam", "jenis_kelamin": "Jantan"},
    "SWA-044": {"nama": "Hidung",  "spesies": "Bekantan",          "usia": 4,  "berat_kg": 10,   "zona": "Zona H", "status_kepunahan": "Terancam", "jenis_kelamin": "Betina"},
    # ── Siamang (2 ekor) ──
    "SWA-045": {"nama": "Siama",   "spesies": "Siamang",           "usia": 11, "berat_kg": 12,   "zona": "Zona B", "status_kepunahan": "Terancam", "jenis_kelamin": "Betina"},
    "SWA-046": {"nama": "Nyaring", "spesies": "Siamang",           "usia": 8,  "berat_kg": 14,   "zona": "Zona I", "status_kepunahan": "Terancam", "jenis_kelamin": "Jantan"},
    # ── Landak, Musang, Buaya, Ular, Kura-kura (masing-masing 1) ──
    "SWA-047": {"nama": "Duri",    "spesies": "Landak Sumatera",   "usia": 2,  "berat_kg": 4,    "zona": "Zona D", "status_kepunahan": "Rentan",   "jenis_kelamin": "Jantan"},
    "SWA-048": {"nama": "Luwak",   "spesies": "Musang Luwak",      "usia": 4,  "berat_kg": 6,    "zona": "Zona E", "status_kepunahan": "Rentan",   "jenis_kelamin": "Betina"},
    "SWA-049": {"nama": "Croco",   "spesies": "Buaya Senyulong",   "usia": 25, "berat_kg": 200,  "zona": "Zona C", "status_kepunahan": "Rentan",   "jenis_kelamin": "Jantan"},
    "SWA-050": {"nama": "Kura",    "spesies": "Kura-kura Hutan",   "usia": 30, "berat_kg": 12,   "zona": "Zona H", "status_kepunahan": "Rentan",   "jenis_kelamin": "Jantan"},
}

# ─────────────────────────────────────────────────────────────
# STACK — Riwayat Undo Input Data Pengamatan (10 aksi)
#    push = append()  |  pop = pop()
# ─────────────────────────────────────────────────────────────
stack_undo = StackUndo()

# ─────────────────────────────────────────────────────────────
# QUEUE — Antrean Pemeriksaan Medis (15 satwa, FIFO)
# ─────────────────────────────────────────────────────────────

queue_medis = QueueMedis()

# ─────────────────────────────────────────────────────────────
# SINGLE LINKED LIST — Log Penampakan Satwa (20 node)
# ─────────────────────────────────────────────────────────────
log_penampakan = SLLLog()

# ─────────────────────────────────────────────────────────────
# DOUBLE LINKED LIST — Galeri Foto Satwa (10 node)
# ─────────────────────────────────────────────────────────────

data_galeri = [
    {
        "chip_id": "SWA-001",
        "nama": "Rimba",
        "spesies": "Harimau Sumatera",
        "nama_file": "rimba_berburu_0103.jpg",
        "deskripsi": "Rimba mengintai mangsa di semak",
        "tanggal": "2025-01-03",
        "zona": "Zona A"
    },
    {
        "chip_id": "SWA-006",
        "nama": "Borno",
        "spesies": "Orangutan Kalimantan",
        "nama_file": "borno_makan_0105.jpg",
        "deskripsi": "Borno makan buah ara di pohon",
        "tanggal": "2025-01-05",
        "zona": "Zona B"
    },
    {
        "chip_id": "SWA-011",
        "nama": "Agung",
        "spesies": "Gajah Sumatera",
        "nama_file": "agung_sungai_0107.jpg",
        "deskripsi": "Agung menyeberang sungai besar",
        "tanggal": "2025-01-07",
        "zona": "Zona D"
    },
    {
        "chip_id": "SWA-036",
        "nama": "Garuda",
        "spesies": "Elang Jawa",
        "nama_file": "garuda_terbang_0110.jpg",
        "deskripsi": "Garuda melayang di atas kanopi hutan",
        "tanggal": "2025-01-10",
        "zona": "Zona E"
    },
    {
        "chip_id": "SWA-022",
        "nama": "Jago",
        "spesies": "Macan Tutul Jawa",
        "nama_file": "jago_pohon_0112.jpg",
        "deskripsi": "Jago beristirahat di cabang pohon",
        "tanggal": "2025-01-12",
        "zona": "Zona E"
    },
    {
        "chip_id": "SWA-049",
        "nama": "Croco",
        "spesies": "Buaya Muara",
        "nama_file": "croco_berjemur_0115.jpg",
        "deskripsi": "Croco berjemur di tepi rawa gambut",
        "tanggal": "2025-01-15",
        "zona": "Zona C"
    },
    {
        "chip_id": "SWA-045",
        "nama": "Siama",
        "spesies": "Siamang",
        "nama_file": "siama_gelantung_0116.jpg",
        "deskripsi": "Siama bergelantungan bersama pasangan",
        "tanggal": "2025-01-16",
        "zona": "Zona B"
    },
    {
        "chip_id": "SWA-002",
        "nama": "Luna",
        "spesies": "Harimau Sumatera",
        "nama_file": "luna_anak_0118.jpg",
        "deskripsi": "Luna mengasuh dua anaknya di sarang",
        "tanggal": "2025-01-18",
        "zona": "Zona F"
    },
    {
        "chip_id": "SWA-039",
        "nama": "Rangka",
        "spesies": "Rangkong Gading",
        "nama_file": "rangka_sarang_0122.jpg",
        "deskripsi": "Rangka sedang membangun sarang",
        "tanggal": "2025-01-22",
        "zona": "Zona B"
    },
    {
        "chip_id": "SWA-003",
        "nama": "Tegar",
        "spesies": "Harimau Sumatera",
        "nama_file": "tegar_teritori_0125.jpg",
        "deskripsi": "Tegar menandai teritori dengan cakar",
        "tanggal": "2025-01-25",
        "zona": "Zona J"
    }
]

galeri_foto = DLLGaleri()
galeri_foto.load_data(data_galeri)

# ─────────────────────────────────────────────────────────────
# CIRCULAR LINKED LIST — Rotasi Patroli Keamanan
# ─────────────────────────────────────────────────────────────
def patroli_cll():
    cll = CLLPatroli()

    cll.tambah_patroli("Zona A", "Nur Cahyani", "Pagi", 2)
    cll.tambah_patroli("Zona B", "Nurul Atiqa", "Pagi", 2)
    cll.tambah_patroli("Zona C", "Hadi Fauzan", "Siang", 3)
    cll.tambah_patroli("Zona D", "Sande Marya", "Siang", 3)

    return cll


# ─────────────────────────────────────────────────────────────
# TREE — Taksonomi Biologis Satwa
# ─────────────────────────────────────────────────────────────
taksonomi_tree = {
    "Animalia": {
        "Chordata": {
            "Mammalia": {
                "Carnivora": {
                    "Felidae":    ["Harimau Sumatera", "Macan Tutul Jawa", "Kucing Batu"],
                    "Ursidae":    ["Beruang Madu"],
                    "Viverridae": ["Binturong", "Musang Luwak"],
                },
                "Primates": {
                    "Hominidae":       ["Orangutan Borneo"],
                    "Hylobatidae":     ["Siamang"],
                    "Cercopithecidae": ["Bekantan"],
                },
                "Proboscidea":    {"Elephantidae":   ["Gajah Sumatera"]},
                "Perissodactyla": {"Rhinocerotidae": ["Badak Sumatera"], "Tapiridae": ["Tapir Asia"]},
                "Artiodactyla":   {"Cervidae":       ["Rusa Sambar"]},
                "Pholidota":      {"Manidae":        ["Trenggiling Sunda"]},
                "Rodentia":       {"Hystricidae":    ["Landak Sumatera"]},
            },
            "Reptilia": {
                "Crocodilia": {"Gavialidae":  ["Buaya Senyulong"]},
                "Squamata":   {"Pythonidae":  ["Ular Sanca Batik"]},
                "Testudines": {"Geoemydidae": ["Kura-kura Hutan"]},
            },
            "Aves": {
                "Accipitriformes": {"Accipitridae": ["Elang Jawa"]},
                "Bucerotiformes":  {"Bucerotidae":  ["Rangkong Gading"]},
            },
        }
    }
}

# ─────────────────────────────────────────────────────────────
# GRAPH — Peta Habitat & Jalur Migrasi (adjacency list + bobot km)
# ─────────────────────────────────────────────────────────────
peta_migrasi = {
    "Zona A": [("Zona B", 12.5), ("Zona D", 8.3),  ("Zona F", 15.1)],
    "Zona B": [("Zona A", 12.5), ("Zona C", 10.2), ("Zona I", 9.7)],
    "Zona C": [("Zona B", 10.2), ("Zona D", 7.8),  ("Zona H", 11.3)],
    "Zona D": [("Zona A", 8.3),  ("Zona C", 7.8),  ("Zona E", 6.5)],
    "Zona E": [("Zona D", 6.5),  ("Zona F", 9.1),  ("Zona J", 13.4)],
    "Zona F": [("Zona A", 15.1), ("Zona E", 9.1),  ("Zona J", 5.6)],
    "Zona G": [("Zona H", 4.2),  ("Zona J", 16.0)],
    "Zona H": [("Zona C", 11.3), ("Zona G", 4.2)],
    "Zona I": [("Zona B", 9.7),  ("Zona J", 12.8)],
    "Zona J": [("Zona E", 13.4), ("Zona F", 5.6),  ("Zona G", 16.0), ("Zona I", 12.8)],
}

# ─────────────────────────────────────────────────────────────
# HASH TABLE — Data Rekam Medis (10 record)
# ─────────────────────────────────────────────────────────────
hash_medis = {
    "MED-001": {"chip_id": "SWA-016", "tanggal": "2025-01-02", "diagnosa": "Luka infeksi kaki", "obat": "Amoksisilin 500mg",  "dokter": "drh. Rina"},
    "MED-002": {"chip_id": "SWA-033", "tanggal": "2025-01-05", "diagnosa": "Malnutrisi ringan", "obat": "Suplemen vitamin",   "dokter": "drh. Hendra"},
    "MED-003": {"chip_id": "SWA-001", "tanggal": "2025-01-08", "diagnosa": "Demam",             "obat": "Parasetamol drh",    "dokter": "drh. Rina"},
    "MED-004": {"chip_id": "SWA-050", "tanggal": "2025-01-15", "diagnosa": "Cangkang retak",    "obat": "Kalsium + plester",  "dokter": "drh. Hendra"},
    "MED-005": {"chip_id": "SWA-012", "tanggal": "2024-12-15", "diagnosa": "Abses gigi",        "obat": "Metronidazol",       "dokter": "drh. Hendra"},
    "MED-006": {"chip_id": "SWA-034", "tanggal": "2025-01-08", "diagnosa": "Stres akut",        "obat": "Diazepam 5mg",       "dokter": "drh. Rina"},
    "MED-007": {"chip_id": "SWA-031", "tanggal": "2025-01-12", "diagnosa": "Konjungtivitis",    "obat": "Tetes mata kloram",  "dokter": "drh. Rina"},
    "MED-008": {"chip_id": "SWA-007", "tanggal": "2025-01-01", "diagnosa": "Hamil 3 bulan",     "obat": "Vitamin prenatal",   "dokter": "drh. Rina"},
    "MED-009": {"chip_id": "SWA-022", "tanggal": "2025-01-20", "diagnosa": "Luka cakaran",      "obat": "Antiseptik + perban","dokter": "drh. Hendra"},
    "MED-010": {"chip_id": "SWA-049", "tanggal": "2024-11-30", "diagnosa": "Sehat",             "obat": "-",                  "dokter": "drh. Rina"},
}


def info(self):
        return (f"[{self.kode_zona}] {self.nama_zona} | {self.luas_ha} ha | "
                f"Kondisi: {self.kondisi} | Ancaman: {self.ancaman}")

def __repr__(self):
        return f"Habitat({self.kode_zona}, {self.nama_zona})"


# ─────────────────────────────────────────────────────────────
# SORTING — Bubble Sort (usia) & Selection Sort (berat)
# ─────────────────────────────────────────────────────────────
data_sorting = [{"chip_id": k, "nama": v["nama"], "usia": v["usia"], "berat_kg": v["berat_kg"]}
                for k, v in data_satwa.items()]

def bubble_sort_usia(data):
    arr = data[:]
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j]["usia"] > arr[j+1]["usia"]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def selection_sort_berat(data):
    arr = data[:]
    n = len(arr)
    for i in range(n):
        max_idx = i
        for j in range(i+1, n):
            if arr[j]["berat_kg"] > arr[max_idx]["berat_kg"]:
                max_idx = j
        arr[i], arr[max_idx] = arr[max_idx], arr[i]
    return arr

urutan_level = {"Kritis": 0, "Terancam": 1, "Rentan": 2, "Aman": 3}
data_kepunahan = sorted(
    [{"chip_id": k, **v} for k, v in data_satwa.items()],
    key=lambda x: urutan_level[x["status_kepunahan"]]
)


# ─────────────────────────────────────────────────────────────
#  REKURSIF — Simulasi Rantai Makanan
# ─────────────────────────────────────────────────────────────
rantai_makanan = {
    "Harimau Sumatera":  ["Rusa Sambar", "Tapir Asia", "Beruang Madu"],
    "Macan Tutul Jawa":  ["Rusa Sambar", "Musang Luwak", "Landak Sumatera"],
    "Elang Jawa":        ["Musang Luwak", "Landak Sumatera", "Ular Sanca Batik"],
    "Buaya Senyulong":   ["Rusa Sambar", "Ular Sanca Batik", "Kura-kura Hutan"],
    "Ular Sanca Batik":  ["Musang Luwak", "Landak Sumatera"],
    "Beruang Madu":      ["Madu Lebah", "Buah-buahan", "Serangga"],
    "Orangutan Borneo":  ["Buah-buahan", "Daun Muda", "Serangga"],
    "Rusa Sambar":       ["Rumput", "Daun", "Tunas"],
    "Tapir Asia":        ["Rumput", "Daun", "Buah Jatuh"],
    "Musang Luwak":      ["Buah Kopi", "Serangga", "Tikus"],
    "Landak Sumatera":   ["Akar", "Umbi", "Kulit Pohon"],
    "Trenggiling Sunda": ["Semut", "Rayap"],
}

def simulasi_rantai_makanan(predator, kedalaman=0, maks=3):
    print("  " * kedalaman + f"-> {predator}")
    if kedalaman >= maks or predator not in rantai_makanan:
        return
    for mangsa in rantai_makanan[predator]:
        simulasi_rantai_makanan(mangsa, kedalaman + 1, maks)

# ─────────────────────────────────────────────────────────────
# STATUS HABITAT DAN LINGKUNGAN
# ─────────────────────────────────────────────────────────────
status_habitat = {
    "Zona A": {"nama": "Hutan Primer Utara",    "luas_ha": 1200, "kondisi": "Baik",     "ancaman": "Perambahan rendah",    "satwa": 8,  "kapasitas": 50, "tutupan_pohon_pct": 92},
    "Zona B": {"nama": "Hutan Sekunder Timur",  "luas_ha": 800,  "kondisi": "Cukup",    "ancaman": "Perambahan sedang",    "satwa": 7,  "kapasitas": 35, "tutupan_pohon_pct": 75},
    "Zona C": {"nama": "Rawa Gambut Barat",     "luas_ha": 600,  "kondisi": "Terancam", "ancaman": "Kebakaran & drainase", "satwa": 6,  "kapasitas": 25, "tutupan_pohon_pct": 60},
    "Zona D": {"nama": "Tepi Sungai Selatan",   "luas_ha": 950,  "kondisi": "Baik",     "ancaman": "Pendangkalan sungai",  "satwa": 7,  "kapasitas": 40, "tutupan_pohon_pct": 88},
    "Zona E": {"nama": "Savana Tengah",         "luas_ha": 1100, "kondisi": "Cukup",    "ancaman": "Kekeringan musiman",   "satwa": 6,  "kapasitas": 45, "tutupan_pohon_pct": 45},
    "Zona F": {"nama": "Pegunungan Barat Laut", "luas_ha": 1400, "kondisi": "Baik",     "ancaman": "Perburuan liar",       "satwa": 5,  "kapasitas": 30, "tutupan_pohon_pct": 89},
    "Zona G": {"nama": "Pantai Timur",          "luas_ha": 300,  "kondisi": "Cukup",    "ancaman": "Abrasi pantai",        "satwa": 3,  "kapasitas": 15, "tutupan_pohon_pct": 50},
    "Zona H": {"nama": "Hutan Mangrove",        "luas_ha": 450,  "kondisi": "Terancam", "ancaman": "Konversi lahan",       "satwa": 4,  "kapasitas": 20, "tutupan_pohon_pct": 65},
    "Zona I": {"nama": "Lembah Terlindung",     "luas_ha": 700,  "kondisi": "Baik",     "ancaman": "Minimal",              "satwa": 5,  "kapasitas": 38, "tutupan_pohon_pct": 94},
    "Zona J": {"nama": "Dataran Tinggi",        "luas_ha": 900,  "kondisi": "Cukup",    "ancaman": "Perburuan ilegal",     "satwa": 4,  "kapasitas": 28, "tutupan_pohon_pct": 78},
}

