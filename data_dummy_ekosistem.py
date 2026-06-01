# ============================================================
# DATA DUMMY - SIMULASI EKOSISTEM (Kelompok 10)
# 50 data satwa + semua kebutuhan struktur data
# ============================================================

# ─────────────────────────────────────────────────────────────
# 1. LIST — Daftar Spesies Satwa (20 spesies)
# ─────────────────────────────────────────────────────────────
from struktur.queue_medis import QueueMedis
from struktur.stack_undo import StackUndo

daftar_spesies = [
    "Harimau Sumatera",     # 1
    "Orangutan Borneo",     # 2
    "Gajah Sumatera",       # 3
    "Badak Sumatera",       # 4
    "Beruang Madu",         # 5
    "Macan Tutul Jawa",     # 6
    "Rusa Sambar",          # 7
    "Tapir Asia",           # 8
    "Binturong",            # 9
    "Trenggiling Sunda",    # 10
    "Elang Jawa",           # 11
    "Rangkong Gading",      # 12
    "Kucing Batu",          # 13
    "Bekantan",             # 14
    "Siamang",              # 15
    "Landak Sumatera",      # 16
    "Musang Luwak",         # 17
    "Buaya Senyulong",      # 18
    "Ular Sanca Batik",     # 19
    "Kura-kura Hutan",      # 20
]

# ─────────────────────────────────────────────────────────────
# 2. TUPLE — Koordinat Geografis Habitat (10 zona)
# ─────────────────────────────────────────────────────────────
koordinat_habitat = [
    ("Zona A - Hutan Primer Utara",     (2.3456,  101.7823)),
    ("Zona B - Hutan Sekunder Timur",   (2.1234,  102.1045)),
    ("Zona C - Rawa Gambut Barat",      (1.9876,  101.4567)),
    ("Zona D - Tepi Sungai Selatan",    (1.7654,  101.9321)),
    ("Zona E - Savana Tengah",          (2.0011,  101.6789)),
    ("Zona F - Pegunungan Barat Laut",  (2.5678,  101.3456)),
    ("Zona G - Pantai Timur",           (1.8900,  102.3456)),
    ("Zona H - Hutan Mangrove",         (1.6543,  102.0987)),
    ("Zona I - Lembah Terlindung",      (2.4321,  101.8654)),
    ("Zona J - Dataran Tinggi",         (2.6789,  101.5432)),
]

# ─────────────────────────────────────────────────────────────
# 3. SET — Spesies Unik per Zona (tanpa duplikasi)
# ─────────────────────────────────────────────────────────────
spesies_zona = {
    "Zona A": {"Harimau Sumatera", "Tapir Asia", "Rusa Sambar", "Beruang Madu", "Trenggiling Sunda"},
    "Zona B": {"Orangutan Borneo", "Siamang", "Rangkong Gading", "Binturong", "Kucing Batu"},
    "Zona C": {"Buaya Senyulong", "Ular Sanca Batik", "Trenggiling Sunda", "Bekantan", "Kura-kura Hutan"},
    "Zona D": {"Gajah Sumatera", "Rusa Sambar", "Tapir Asia", "Musang Luwak", "Landak Sumatera"},
    "Zona E": {"Macan Tutul Jawa", "Rusa Sambar", "Elang Jawa", "Musang Luwak", "Beruang Madu"},
    "Zona F": {"Badak Sumatera", "Harimau Sumatera", "Tapir Asia", "Beruang Madu", "Kucing Batu"},
    "Zona G": {"Buaya Senyulong", "Kura-kura Hutan", "Bekantan", "Rangkong Gading", "Elang Jawa"},
    "Zona H": {"Bekantan", "Buaya Senyulong", "Ular Sanca Batik", "Kura-kura Hutan", "Musang Luwak"},
    "Zona I": {"Orangutan Borneo", "Siamang", "Binturong", "Landak Sumatera", "Trenggiling Sunda"},
    "Zona J": {"Elang Jawa", "Rangkong Gading", "Macan Tutul Jawa", "Harimau Sumatera", "Badak Sumatera"},
}

# ─────────────────────────────────────────────────────────────
# 4. DICTIONARY — 50 Data Satwa berdasarkan Chip ID
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
# 5. STACK — Riwayat Undo Input Data Pengamatan (10 aksi)
#    push = append()  |  pop = pop()
# ─────────────────────────────────────────────────────────────
stack_undo = StackUndo()

# ─────────────────────────────────────────────────────────────
# 6. QUEUE — Antrean Pemeriksaan Medis (15 satwa, FIFO)
# ─────────────────────────────────────────────────────────────

queue_medis = QueueMedis()

# ─────────────────────────────────────────────────────────────
# 7. SINGLE LINKED LIST — Log Penampakan Satwa (20 node)
# ─────────────────────────────────────────────────────────────
log_penampakan = [
    {"id": 1,  "tanggal": "2025-01-03", "waktu": "06:12", "chip_id": "SWA-001", "nama": "Rimba",   "zona": "Zona A", "aktivitas": "Berburu",           "next": 2},
    {"id": 2,  "tanggal": "2025-01-05", "waktu": "08:34", "chip_id": "SWA-006", "nama": "Borno",   "zona": "Zona B", "aktivitas": "Makan buah",        "next": 3},
    {"id": 3,  "tanggal": "2025-01-07", "waktu": "14:20", "chip_id": "SWA-011", "nama": "Agung",   "zona": "Zona D", "aktivitas": "Minum di sungai",   "next": 4},
    {"id": 4,  "tanggal": "2025-01-09", "waktu": "07:00", "chip_id": "SWA-022", "nama": "Jago",    "zona": "Zona E", "aktivitas": "Mengintai mangsa",  "next": 5},
    {"id": 5,  "tanggal": "2025-01-10", "waktu": "17:45", "chip_id": "SWA-036", "nama": "Garuda",  "zona": "Zona E", "aktivitas": "Terbang melayang",  "next": 6},
    {"id": 6,  "tanggal": "2025-01-12", "waktu": "09:15", "chip_id": "SWA-019", "nama": "Madu",    "zona": "Zona A", "aktivitas": "Mencari madu",      "next": 7},
    {"id": 7,  "tanggal": "2025-01-13", "waktu": "06:50", "chip_id": "SWA-028", "nama": "Tapa",    "zona": "Zona A", "aktivitas": "Berendam",          "next": 8},
    {"id": 8,  "tanggal": "2025-01-15", "waktu": "11:30", "chip_id": "SWA-049", "nama": "Croco",   "zona": "Zona C", "aktivitas": "Berjemur",          "next": 9},
    {"id": 9,  "tanggal": "2025-01-16", "waktu": "16:00", "chip_id": "SWA-045", "nama": "Siama",   "zona": "Zona B", "aktivitas": "Bergelantungan",    "next": 10},
    {"id": 10, "tanggal": "2025-01-18", "waktu": "07:20", "chip_id": "SWA-002", "nama": "Luna",    "zona": "Zona F", "aktivitas": "Mengasuh anak",     "next": 11},
    {"id": 11, "tanggal": "2025-01-19", "waktu": "13:10", "chip_id": "SWA-043", "nama": "Bekan",   "zona": "Zona C", "aktivitas": "Makan daun",        "next": 12},
    {"id": 12, "tanggal": "2025-01-20", "waktu": "08:05", "chip_id": "SWA-026", "nama": "Riko",    "zona": "Zona E", "aktivitas": "Berlari",           "next": 13},
    {"id": 13, "tanggal": "2025-01-22", "waktu": "15:40", "chip_id": "SWA-039", "nama": "Rangka",  "zona": "Zona B", "aktivitas": "Membuat sarang",    "next": 14},
    {"id": 14, "tanggal": "2025-01-23", "waktu": "10:00", "chip_id": "SWA-050", "nama": "Kura",    "zona": "Zona H", "aktivitas": "Berjemur",          "next": 15},
    {"id": 15, "tanggal": "2025-01-25", "waktu": "06:30", "chip_id": "SWA-003", "nama": "Tegar",   "zona": "Zona J", "aktivitas": "Menandai teritori", "next": 16},
    {"id": 16, "tanggal": "2025-01-26", "waktu": "09:45", "chip_id": "SWA-032", "nama": "Koko",    "zona": "Zona I", "aktivitas": "Bermain",           "next": 17},
    {"id": 17, "tanggal": "2025-01-27", "waktu": "12:15", "chip_id": "SWA-014", "nama": "Anggun",  "zona": "Zona D", "aktivitas": "Mandi lumpur",      "next": 18},
    {"id": 18, "tanggal": "2025-01-28", "waktu": "07:55", "chip_id": "SWA-033", "nama": "Sisik",   "zona": "Zona C", "aktivitas": "Menggali tanah",    "next": 19},
    {"id": 19, "tanggal": "2025-01-29", "waktu": "16:30", "chip_id": "SWA-037", "nama": "Elok",    "zona": "Zona G", "aktivitas": "Berburu ikan",      "next": 20},
    {"id": 20, "tanggal": "2025-01-30", "waktu": "08:00", "chip_id": "SWA-009", "nama": "Nisa",    "zona": "Zona I", "aktivitas": "Menyusui anak",     "next": None},
]

# ─────────────────────────────────────────────────────────────
# 8. DOUBLE LINKED LIST — Galeri Foto Satwa (10 node)
# ─────────────────────────────────────────────────────────────
galeri_foto = [
    {"id": 1,  "chip_id": "SWA-001", "file": "rimba_berburu_0103.jpg",   "deskripsi": "Rimba mengintai mangsa di semak",      "fotografer": "Ranger Budi",  "prev": None, "next": 2},
    {"id": 2,  "chip_id": "SWA-006", "file": "borno_makan_0105.jpg",     "deskripsi": "Borno makan buah ara di pohon",        "fotografer": "Ranger Andi",  "prev": 1,    "next": 3},
    {"id": 3,  "chip_id": "SWA-011", "file": "agung_sungai_0107.jpg",    "deskripsi": "Agung menyeberang sungai besar",       "fotografer": "Ranger Citra", "prev": 2,    "next": 4},
    {"id": 4,  "chip_id": "SWA-036", "file": "garuda_terbang_0110.jpg",  "deskripsi": "Garuda melayang di atas kanopi hutan", "fotografer": "Ranger Dewi",  "prev": 3,    "next": 5},
    {"id": 5,  "chip_id": "SWA-022", "file": "jago_pohon_0112.jpg",      "deskripsi": "Jago beristirahat di cabang pohon",    "fotografer": "Ranger Eko",   "prev": 4,    "next": 6},
    {"id": 6,  "chip_id": "SWA-049", "file": "croco_berjemur_0115.jpg",  "deskripsi": "Croco berjemur di tepi rawa gambut",   "fotografer": "Ranger Fajar", "prev": 5,    "next": 7},
    {"id": 7,  "chip_id": "SWA-045", "file": "siama_gelantung_0116.jpg", "deskripsi": "Siama bergelantungan bersama pasangan","fotografer": "Ranger Budi",  "prev": 6,    "next": 8},
    {"id": 8,  "chip_id": "SWA-002", "file": "luna_anak_0118.jpg",       "deskripsi": "Luna mengasuh dua anaknya di sarang",  "fotografer": "Ranger Andi",  "prev": 7,    "next": 9},
    {"id": 9,  "chip_id": "SWA-039", "file": "rangka_sarang_0122.jpg",   "deskripsi": "Rangka sedang membangun sarang",       "fotografer": "Ranger Citra", "prev": 8,    "next": 10},
    {"id": 10, "chip_id": "SWA-003", "file": "tegar_teritori_0125.jpg",  "deskripsi": "Tegar menandai teritori dengan cakar", "fotografer": "Ranger Dewi",  "prev": 9,    "next": None},
]

# ─────────────────────────────────────────────────────────────
# 9. CIRCULAR LINKED LIST — Rotasi Patroli Keamanan
# ─────────────────────────────────────────────────────────────
jadwal_patroli = [
    {"id_ranger": "RNG-01", "nama": "Budi Santoso",   "zona": "Zona A", "zona_next": "Zona B", "shift": "Pagi  (06:00-12:00)"},
    {"id_ranger": "RNG-02", "nama": "Andi Pratama",   "zona": "Zona B", "zona_next": "Zona C", "shift": "Pagi  (06:00-12:00)"},
    {"id_ranger": "RNG-03", "nama": "Citra Lestari",  "zona": "Zona C", "zona_next": "Zona D", "shift": "Siang (12:00-18:00)"},
    {"id_ranger": "RNG-04", "nama": "Dewi Anggraini", "zona": "Zona D", "zona_next": "Zona E", "shift": "Siang (12:00-18:00)"},
    {"id_ranger": "RNG-05", "nama": "Eko Prasetyo",   "zona": "Zona E", "zona_next": "Zona A", "shift": "Malam (18:00-00:00)"},
    # Rotasi ke-2
    {"id_ranger": "RNG-01", "nama": "Budi Santoso",   "zona": "Zona B", "zona_next": "Zona C", "shift": "Pagi  (06:00-12:00)"},
    {"id_ranger": "RNG-02", "nama": "Andi Pratama",   "zona": "Zona C", "zona_next": "Zona D", "shift": "Pagi  (06:00-12:00)"},
    {"id_ranger": "RNG-03", "nama": "Citra Lestari",  "zona": "Zona D", "zona_next": "Zona E", "shift": "Siang (12:00-18:00)"},
    {"id_ranger": "RNG-04", "nama": "Dewi Anggraini", "zona": "Zona E", "zona_next": "Zona A", "shift": "Siang (12:00-18:00)"},
    {"id_ranger": "RNG-05", "nama": "Eko Prasetyo",   "zona": "Zona A", "zona_next": "Zona B", "shift": "Malam (18:00-00:00)"},
]

# ─────────────────────────────────────────────────────────────
# 10. TREE — Taksonomi Biologis Satwa
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
# 11. GRAPH — Peta Habitat & Jalur Migrasi (adjacency list + bobot km)
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
# 12. HASH TABLE — Data Rekam Medis (10 record)
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

# ─────────────────────────────────────────────────────────────
# 13. OOP — Class Animal, Habitat, Ranger
# ─────────────────────────────────────────────────────────────
class Animal:
    def __init__(self, chip_id, nama, spesies, usia, berat_kg, zona, status_kepunahan, jenis_kelamin):
        self.chip_id          = chip_id
        self.nama             = nama
        self.spesies          = spesies
        self.usia             = usia
        self.berat_kg         = berat_kg
        self.zona             = zona
        self.status_kepunahan = status_kepunahan
        self.jenis_kelamin    = jenis_kelamin

    def info(self):
        return (f"[{self.chip_id}] {self.nama} ({self.spesies}) | "
                f"{self.usia} thn | {self.berat_kg} kg | {self.zona} | {self.status_kepunahan}")

    def __repr__(self):
        return f"Animal({self.chip_id}, {self.nama})"


class Habitat:
    def __init__(self, kode_zona, nama_zona, koordinat, luas_ha, kapasitas, kondisi, ancaman):
        self.kode_zona = kode_zona
        self.nama_zona = nama_zona
        self.koordinat = koordinat
        self.luas_ha   = luas_ha
        self.kapasitas = kapasitas
        self.kondisi   = kondisi
        self.ancaman   = ancaman

    def info(self):
        return (f"[{self.kode_zona}] {self.nama_zona} | {self.luas_ha} ha | "
                f"Kondisi: {self.kondisi} | Ancaman: {self.ancaman}")

    def __repr__(self):
        return f"Habitat({self.kode_zona}, {self.nama_zona})"


class Ranger:
    def __init__(self, id_ranger, nama, zona_tugas, shift, no_hp):
        self.id_ranger  = id_ranger
        self.nama       = nama
        self.zona_tugas = zona_tugas
        self.shift      = shift
        self.no_hp      = no_hp

    def info(self):
        return (f"[{self.id_ranger}] {self.nama} | Zona: {self.zona_tugas} | "
                f"Shift: {self.shift} | HP: {self.no_hp}")

    def __repr__(self):
        return f"Ranger({self.id_ranger}, {self.nama})"


animals_obj = [Animal(k, v["nama"], v["spesies"], v["usia"], v["berat_kg"],
                      v["zona"], v["status_kepunahan"], v["jenis_kelamin"])
               for k, v in list(data_satwa.items())[:5]]

habitats_obj = [
    Habitat("Zona A", "Hutan Primer Utara",    (2.3456, 101.7823), 1200, 50, "Baik",     "Perambahan rendah"),
    Habitat("Zona B", "Hutan Sekunder Timur",  (2.1234, 102.1045), 800,  35, "Cukup",    "Perambahan sedang"),
    Habitat("Zona C", "Rawa Gambut Barat",     (1.9876, 101.4567), 600,  25, "Terancam", "Kebakaran & drainase"),
    Habitat("Zona D", "Tepi Sungai Selatan",   (1.7654, 101.9321), 950,  40, "Baik",     "Pendangkalan sungai"),
    Habitat("Zona E", "Savana Tengah",         (2.0011, 101.6789), 1100, 45, "Cukup",    "Kekeringan musiman"),
]

rangers_obj = [
    Ranger("RNG-01", "Budi Santoso",   "Zona A", "Pagi",  "0812-3456-7890"),
    Ranger("RNG-02", "Andi Pratama",   "Zona B", "Pagi",  "0813-2345-6789"),
    Ranger("RNG-03", "Citra Lestari",  "Zona C", "Siang", "0814-3456-7891"),
    Ranger("RNG-04", "Dewi Anggraini", "Zona D", "Siang", "0815-4567-8901"),
    Ranger("RNG-05", "Eko Prasetyo",   "Zona E", "Malam", "0816-5678-9012"),
]

# ─────────────────────────────────────────────────────────────
# 14. SORTING — Bubble Sort (usia) & Selection Sort (berat)
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
# 15. SEARCHING — Linear Search (zona) & Binary Search (chip_id)
# ─────────────────────────────────────────────────────────────
def linear_search_zona(target_zona):
    return [{"chip_id": k, **v} for k, v in data_satwa.items() if v["zona"] == target_zona]

sorted_satwa = sorted([{"chip_id": k, **v} for k, v in data_satwa.items()], key=lambda x: x["chip_id"])

def binary_search_chip(target_id):
    low, high = 0, len(sorted_satwa) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_satwa[mid]["chip_id"] == target_id:
            return sorted_satwa[mid]
        elif sorted_satwa[mid]["chip_id"] < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return None

# ─────────────────────────────────────────────────────────────
# 16. REKURSIF — Simulasi Rantai Makanan
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
# 17. DATA SENSOR HABITAT
# ─────────────────────────────────────────────────────────────
data_sensor = [
    {"zona": "Zona A", "timestamp": "2025-01-30 06:00", "suhu_C": 26.5, "kelembaban_pct": 82, "curah_hujan_mm": 0.0, "kualitas_udara": "Baik"},
    {"zona": "Zona A", "timestamp": "2025-01-30 12:00", "suhu_C": 31.2, "kelembaban_pct": 71, "curah_hujan_mm": 0.0, "kualitas_udara": "Baik"},
    {"zona": "Zona B", "timestamp": "2025-01-30 06:00", "suhu_C": 25.8, "kelembaban_pct": 85, "curah_hujan_mm": 2.5, "kualitas_udara": "Baik"},
    {"zona": "Zona B", "timestamp": "2025-01-30 12:00", "suhu_C": 29.4, "kelembaban_pct": 78, "curah_hujan_mm": 0.0, "kualitas_udara": "Baik"},
    {"zona": "Zona C", "timestamp": "2025-01-30 06:00", "suhu_C": 27.1, "kelembaban_pct": 91, "curah_hujan_mm": 5.0, "kualitas_udara": "Cukup"},
    {"zona": "Zona C", "timestamp": "2025-01-30 12:00", "suhu_C": 30.0, "kelembaban_pct": 88, "curah_hujan_mm": 1.2, "kualitas_udara": "Cukup"},
    {"zona": "Zona D", "timestamp": "2025-01-30 06:00", "suhu_C": 25.3, "kelembaban_pct": 80, "curah_hujan_mm": 0.0, "kualitas_udara": "Baik"},
    {"zona": "Zona D", "timestamp": "2025-01-30 12:00", "suhu_C": 32.1, "kelembaban_pct": 68, "curah_hujan_mm": 0.0, "kualitas_udara": "Baik"},
    {"zona": "Zona E", "timestamp": "2025-01-30 06:00", "suhu_C": 24.9, "kelembaban_pct": 75, "curah_hujan_mm": 0.0, "kualitas_udara": "Baik"},
    {"zona": "Zona E", "timestamp": "2025-01-30 12:00", "suhu_C": 34.5, "kelembaban_pct": 60, "curah_hujan_mm": 0.0, "kualitas_udara": "Cukup"},
]

# ─────────────────────────────────────────────────────────────
# 18. STATUS HABITAT DAN LINGKUNGAN
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

# ─────────────────────────────────────────────────────────────
# MAIN — Demo semua fitur
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    SEP = "=" * 62

    print(SEP)
    print("   SIMULASI EKOSISTEM - DATA DUMMY (Kelompok 10)")
    print(SEP)
    print(f"\n Total satwa terdaftar : {len(data_satwa)}")
    print(f" Total spesies         : {len(daftar_spesies)}")
    print(f" Total zona habitat    : {len(koordinat_habitat)}")
    print(f" Antrean medis         : {len(queue_medis)}")
    print(f" Log penampakan        : {len(log_penampakan)}")
    print(f" Foto galeri           : {len(galeri_foto)}")
    print(f" Record medis          : {len(hash_medis)}")

    print(f"\n{'-'*62}")
    print(" [OOP] Info Animal (5 pertama):")
    for a in animals_obj:
        print(" ", a.info())

    print(f"\n{'-'*62}")
    print(" [OOP] Info Habitat:")
    for h in habitats_obj:
        print(" ", h.info())

    print(f"\n{'-'*62}")
    print(" [OOP] Info Ranger:")
    for r in rangers_obj:
        print(" ", r.info())

    print(f"\n{'-'*62}")
    print(" [REKURSIF] Rantai Makanan: Harimau Sumatera (kedalaman 2)")
    simulasi_rantai_makanan("Harimau Sumatera", maks=2)

    print(f"\n{'-'*62}")
    print(" [LINEAR SEARCH] Satwa di Zona D:")
    for s in linear_search_zona("Zona D"):
        print(f"  {s['chip_id']} - {s['nama']} ({s['spesies']})")

    print(f"\n{'-'*62}")
    print(" [BINARY SEARCH] Cari SWA-039:")
    hasil = binary_search_chip("SWA-039")
    print(f"  Ditemukan -> {hasil['nama']} ({hasil['spesies']}) | {hasil['zona']}")

    print(f"\n{'-'*62}")
    print(" [BUBBLE SORT] 5 Satwa Termuda:")
    for s in bubble_sort_usia(data_sorting)[:5]:
        print(f"  {s['chip_id']} {s['nama']:10s} usia={s['usia']} thn")

    print(f"\n{'-'*62}")
    print(" [SELECTION SORT] 5 Satwa Terberat:")
    for s in selection_sort_berat(data_sorting)[:5]:
        print(f"  {s['chip_id']} {s['nama']:10s} berat={s['berat_kg']} kg")

    print(f"\n{'-'*62}")
    print(" [SORTING KEPUNAHAN] 10 Teratas (Kritis -> Rentan):")
    for s in data_kepunahan[:10]:
        print(f"  {s['status_kepunahan']:10s} | {s['nama']:10s} | {s['spesies']}")

    print(f"\n{'-'*62}")
    print(" [QUEUE] Antrean Medis (3 terdepan):")

    current = queue_medis.head
    count = 0

    while current and count < 3:
        data = current.data
        print(
            f"  [{data['chip_id']}] "
            f"{data['nama']:8s} | "
            f"{data['prioritas']:8s} | "
            f"{data['keluhan']}"
    )

    current = current.next
    count += 1

    print(f"\n{'-'*62}")
    print(" [STACK] 3 Aksi Undo Terakhir:")
    for u in stack_undo.stack[-3:]:
        print(
            f"  {u['aksi']:6s} | "
            f"{u['chip_id']} | "
            f"{u['field']} : "
            f"{u['nilai_lama']} -> {u['nilai_baru']}"
        )

    print(f"\n{SEP}")
    print(" Selesai. 50 satwa (SWA-001 s/d SWA-050) + semua struktur data.")
    print(SEP)


#=========================================
"""
═════════════════════════════════════════
Fungsi untuk mengisi data awal Queue, Stack, SLL, DLL, CLL
agar program langsung bisa didemonstrasikan.

"""

from struktur.queue_medis import QueueMedis
from struktur.stack_undo  import StackUndo
from struktur.sll_log     import SLLLog
from struktur.dll_galeri  import DLLGaleri
from struktur.cll_patroli import CLLPatroli


def isi_sll(sll: SLLLog, daftar_satwa: list):
    """Isi log penampakan dengan data awal."""
    catatan = [
        ("A001", "Raja",      "Panthera tigris",  "Zona A", "Dekat sungai utara",  "Berburu",     "Budi Santoso"),
        ("A008", "Rusa1",     "Cervus unicolor",  "Zona A", "Padang rumput timur", "Merumput",    "Budi Santoso"),
        ("A006", "Orangtan1", "Pongo pygmaeus",   "Zona D", "Pohon ara besar",     "Makan buah",  "Rina Wijaya"),
        ("A003", "Gajah1",    "Elephas maximus",  "Zona B", "Sumber air",          "Minum",       "Agus Pratama"),
        ("A010", "Tapir1",    "Tapirus indicus",  "Zona C", "Semak rimbun",        "Bersembunyi", "Budi Santoso"),
        ("A001", "Raja",      "Panthera tigris",  "Zona A", "Batas zona A-B",      "Menjelajah",  "Rina Wijaya"),
    ]
    for chip_id, nama, spesies, zona, lokasi, aktivitas, petugas in catatan:
        sll.tambah_log(chip_id, nama, spesies, zona, lokasi, aktivitas, petugas)


def isi_dll(dll: DLLGaleri, daftar_satwa: list):
    """Isi galeri foto dengan data awal."""
    foto = [
        ("A001", "Raja",      "Panthera tigris",           "raja_berburu_01.jpg",   "Raja sedang berburu rusa di tepi sungai",        "2025-01-10", "Zona A"),
        ("A003", "Gajah1",    "Elephas maximus",            "gajah1_minum_01.jpg",   "Gajah1 minum di sumber air bersama kawanan",     "2025-01-11", "Zona B"),
        ("A006", "Orangtan1", "Pongo pygmaeus",             "orangtan1_makan_01.jpg","Orangtan1 memakan buah ara di puncak pohon",     "2025-01-12", "Zona D"),
        ("A005", "Badak1",    "Dicerorhinus sumatrensis",   "badak1_istirahat.jpg",  "Badak1 beristirahat di bawah pohon rindang",     "2025-01-13", "Zona C"),
        ("A008", "Rusa1",     "Cervus unicolor",            "rusa1_merumput.jpg",    "Rusa1 merumput di padang terbuka",               "2025-01-14", "Zona A"),
        ("A010", "Tapir1",    "Tapirus indicus",            "tapir1_sembunyi.jpg",   "Tapir1 bersembunyi di antara semak tebal",       "2025-01-15", "Zona C"),
        ("A001", "Raja",      "Panthera tigris",            "raja_istirahat_01.jpg", "Raja beristirahat setelah berburu",              "2025-01-16", "Zona A"),
    ]
    for chip_id, nama, spesies, nama_file, deskripsi, tanggal, zona in foto:
        dll.tambah_foto(chip_id, nama, spesies, nama_file, deskripsi, tanggal, zona)


def isi_cll(cll: CLLPatroli):
    """Isi jadwal patroli dengan data awal."""
    jadwal = [
        ("Zona A — Hutan Rimba Utara", "Budi Santoso",  "Pagi",  6),
        ("Zona B — Padang Savana",     "Agus Pratama",  "Pagi",  6),
        ("Zona C — Lembah Kabut",      "Rina Wijaya",   "Siang", 6),
        ("Zona D — Hutan Gambut",      "Budi Santoso",  "Siang", 6),
        ("Zona E — Sungai Besar",      "Agus Pratama",  "Malam", 8),
    ]
    for zona, ranger, shift, durasi in jadwal:
        cll.tambah_patroli(zona, ranger, shift, durasi)
    cll.mulai_patroli_pertama()
