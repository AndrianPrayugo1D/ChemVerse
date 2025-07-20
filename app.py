import streamlit as st
import math

# ------------------ Styling CSS ------------------
st.markdown("""
    <style>
    .stApp {
        background-image: linear-gradient(rgba(0,0,0,0.75), rgba(0,0,0,0.75)),
                          url("https://i.imgur.com/BSBUvyu.jpeg");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
        color: white;
    }
    header[data-testid="stHeader"] { background: transparent !important; }
    .block-container { padding-top: 1rem !important; }
    h1, h2, h3, h4, h5 { color: white !important; }
    label, .stMarkdown { color: white !important; }
    input[type="number"], input[type="text"] {
        color: black !important;
        background-color: rgba(255,255,255,0.9) !important;
        border-radius: 5px !important;
    }
    .custom-output {
        background-color: rgba(255, 255, 255, 0.9);
        color: black;
        font-weight: bold;
        padding: 10px;
        border-radius: 10px;
        border: 2px solid #00ccff;
        text-align: center;
        margin-top: 10px;
    }
    [data-testid="stSidebar"] {
        background-image: linear-gradient(135deg, #cceeff 0%, #99ccff 100%);
        color: black;
        padding-top: 0 !important;
        margin-top: 0 !important;
    }
    [data-testid="stSidebar"] .block-container {
        padding-top: 0px !important;
        margin-top: 0px !important;
    }
    [data-testid="stSidebar"] .stMarkdown {
        color: black !important;
        font-weight: bold;
        font-size: 1.1rem;
        margin-bottom: 0px !important;
        padding-bottom: 0px !important;
    }
    .stButton button {
        background-color: #00ccff;
        color: black;
        border-radius: 8px;
        padding: 0.5em 1em;
        font-weight: bold;
    }
    .stButton button:hover {
        background-color: #0099cc;
        color: white;
    }
   div[role="radiogroup"] > label, 
div[role="radiogroup"] span, 
div[role="radiogroup"] div {
    color: white !important;
    font-weight: bold !important;
}

    </style>
""", unsafe_allow_html=True)

# ------------------ Judul ------------------
st.title("🧪 ChemVerse (Kalkulator Kimia Digital)")

# ------------------ Navigasi Sidebar ------------------
st.sidebar.markdown("<p style='color: black; font-weight: bold;'>📘 Menu Navigasi</p>", unsafe_allow_html=True)
menu = st.sidebar.selectbox("", [
    "🏠 Beranda",
    "👥 Tentang Kami",
    "ℹ️ Tentang Aplikasi",
    "🧪 Hitung Mol",
    "🧫 Hitung pH",
    "💧 Pengenceran Larutan",
    "📊 Persentase Konsentrasi",
    "🧠 Kuis Kimia"
])

# ------------------ Halaman Beranda ------------------
if menu == "🏠 Beranda":
    st.header("Selamat datang di ChemVerse - Aplikasi Kimia Pintar 🎉")
    st.markdown("""
    Bersama aplikasi ini, mari wujudkan perhitungan kimia yang cepat, cerdas, dan praktis.  
    Aplikasi ini dirancang untuk mendukung aktivitas perkuliahan, praktikum, dan penelitian kimiamu.  
    Yuk, manfaatkan ChemVerse sebagai sahabat belajar dan praktikum.
    """)

# ------------------ Tentang Kami ------------------
elif menu == "👥 Tentang Kami":
    st.subheader("👥 Tentang Kami")
    st.markdown("""
    **Kelompok 3 - 1D**  
    1. Andrian Prayugo (2460324)  
    2. Dhisa Nur Azizah (2460358)  
    3. Marcelino David Mangatur (2460411)  
    4. Nabil Syafiq Suhendar (2460446)  
    5. Sefina Zahra Pangestika (2460515)
    """)

# ------------------ Tentang Aplikasi ------------------
elif menu == "ℹ️ Tentang Aplikasi":
    st.subheader("📘 Tentang Aplikasi - ChemVerse")
    tab = st.selectbox("Pilih Penjelasan", [
        "🧪 Deskripsi",
        "🔍 Latar Belakang",
        "🎯 Tujuan",
        "⚙️ Fitur",
        "🌟 Manfaat"
    ])

    if tab == "🧪 Deskripsi":
        st.markdown("""
ChemVerse adalah aplikasi kalkulator kimia digital yang interaktif, inovatif, dan cerdas. Dirancang untuk mempermudah perhitungan kimia sekaligus menjadi ruang eksplorasi konsep kimia dalam satu ekosistem terintegrasi.
        """)

        elif tab == "🔍 Latar Belakang":
        st.markdown("""
        Perkembangan teknologi digital dalam era Revolusi Industri 4.0 telah mendorong transformasi di berbagai bidang, termasuk dalam dunia pendidikan dan laboratorium sains. Salah satu bidang yang turut merasakan dampaknya adalah ilmu kimia, yang dalam praktiknya memerlukan perhitungan kompleks seperti perhitungan mol, konsentrasi, pH, dan pengenceran larutan.

        Perhitungan tersebut sering kali memakan waktu dan rawan terjadi kesalahan apabila dilakukan secara manual, terutama oleh mahasiswa atau praktikan di laboratorium pendidikan. Oleh karena itu, diperlukan suatu inovasi berbasis teknologi yang dapat membantu mempermudah dan mempercepat proses perhitungan kimia secara akurat dan efisien.

        Salah satu solusi yang dapat diimplementasikan adalah pembuatan aplikasi kalkulator kimia berbasis web yang bersifat interaktif dan mudah diakses. Python merupakan bahasa pemrograman yang populer dan fleksibel, serta memiliki berbagai pustaka yang mendukung pengembangan aplikasi berbasis sains.

        Di sisi lain, Streamlit merupakan sebuah framework Python yang memungkinkan pembuatan antarmuka web secara cepat dan sederhana, tanpa memerlukan pengetahuan mendalam tentang pengembangan front-end. Dengan menggabungkan Python dan Streamlit, aplikasi kalkulator kimia ini dirancang untuk membantu pengguna — khususnya mahasiswa dan tenaga pendidik — dalam melakukan perhitungan kimia dasar secara otomatis, interaktif, dan user-friendly.

        Ilmu kimia merupakan salah satu cabang sains yang berperan penting dalam berbagai bidang kehidupan, mulai dari industri, kesehatan, pertanian, hingga pendidikan. Dalam proses pembelajaran dan praktik di laboratorium, mahasiswa dan praktikan sering kali dihadapkan pada kebutuhan untuk melakukan berbagai perhitungan kimia yang kompleks dan berulang, seperti perhitungan mol, konsentrasi larutan, pH, pengenceran, serta massa molar suatu senyawa.

        Sayangnya, proses perhitungan ini tidak jarang menimbulkan kesulitan tersendiri, terutama bagi mahasiswa yang masih dalam tahap pemahaman konsep dasar.

        **Permasalahan umum yang sering ditemui di lapangan antara lain:**
        - Kesalahan perhitungan manual akibat kurangnya ketelitian atau pemahaman konsep.
        - Keterbatasan waktu saat praktikum, sehingga praktikan sulit menyelesaikan perhitungan secara cepat.
        - Minimnya alat bantu digital yang praktis, interaktif, dan mudah diakses untuk mendukung kegiatan belajar maupun praktikum kimia.

        Melihat permasalahan tersebut, diperlukan sebuah solusi berbasis teknologi yang mampu mengotomatisasi proses perhitungan, memberikan hasil yang cepat dan akurat, serta dapat digunakan secara fleksibel kapan saja dan di mana saja. Maka dari itu, dibuatlah sebuah proyek web aplikasi kalkulator kimia yang bertujuan untuk menjawab kebutuhan tersebut.

        Pembuatan aplikasi ini menggunakan bahasa pemrograman **Python** karena kemampuannya yang kuat dalam pengolahan data numerik dan kemudahan integrasinya dengan berbagai pustaka sains. Untuk antarmuka dan aksesibilitas berbasis web, digunakan **Streamlit**, sebuah framework Python yang memungkinkan pembuatan aplikasi web secara cepat dan intuitif tanpa perlu keahlian desain web yang kompleks.

        **Aplikasi ini dirancang agar dapat digunakan oleh:**
        - Mahasiswa atau siswa yang sedang belajar kimia.  
        - Guru dan dosen sebagai alat bantu pembelajaran.  
        - Praktikan laboratorium untuk mempercepat perhitungan saat eksperimen.

        **Fitur utama yang direncanakan dalam aplikasi ini mencakup:**
        - Kalkulasi mol, massa molar, konsentrasi (% b/b, b/v, v/v), dan pengenceran larutan.  
        - Perhitungan pH untuk larutan asam dan basa kuat maupun lemah.  
        - Antarmuka sederhana dan ramah pengguna (user-friendly).  
        - Hasil perhitungan yang cepat dan akurat.

        Dengan memanfaatkan teknologi digital yang tersedia, proyek ini diharapkan dapat menjadi solusi praktis sekaligus mendukung integrasi pembelajaran kimia dengan inovasi teknologi. Hal ini sejalan dengan semangat **Revolusi Industri 4.0**, yang menekankan kolaborasi antara ilmu pengetahuan dan teknologi informasi.
        """)


    elif tab == "🎯 Tujuan":
        st.markdown("""
        1. Mempermudah perhitungan kimia dasar.  
        2. Meningkatkan pemahaman konsep mol, pH, pengenceran, dan konsentrasi.  
        3. Menghemat waktu dalam kegiatan laboratorium.
        4. Menyediakan alat bantu praktis dan responsif untuk pelajar dan mahasiswa.
        """)

    elif tab == "⚙️ Fitur":
        st.markdown("""
        1. Perhitungan Molaritas  
        2. Perhitungan pH  
        3. Pengenceran Larutan  
        4. Perhitungan Persentase Konsentrasi
        """)

    elif tab == "🌟 Manfaat":
        st.markdown("""
        1. Membantu proses belajar dan praktikum secara mandiri maupun kelompok.  
        2. Menurunkan tingkat kesalahan hitung manual, sehingga hasil perhitungan yang didapat akurat.  
        3. Menghemat waktu dalam analisis kimia.  
        """)

# ------------------ Hitung Mol ------------------
elif menu == "🧪 Hitung Mol":
    st.header("🔹 Hitung Mol")
    st.markdown("*Rumus:* mol = massa / Mr")

    massa = st.number_input("Masukkan massa zat (gram)", min_value=0.0, step=0.1, key="mol_massa")
    mr = st.number_input("Masukkan massa molar (Mr)", min_value=0.01, step=0.1, key="mol_mr")
    col1, col2 = st.columns(2)

    if col1.button("Hitung"):
        if massa == 0 or mr == 0:
            st.warning("⚠️ Mohon masukkan nilai massa dan Mr yang valid.")
        else:
            mol = massa / mr
            st.markdown(f"<div class='custom-output'>Mol = {mol:.4f} mol</div>", unsafe_allow_html=True)

    if col2.button("Reset"):
        for key in ["mol_massa", "mol_mr"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# ------------------ Hitung pH ------------------
elif menu == "🧫 Hitung pH":
    st.header("🔹 Hitung pH")
    st.markdown("*Rumus:* pH = -log[H⁺]")

    h_conc = st.number_input("Konsentrasi ion H⁺ (mol/L)", min_value=0.0, format="%.10f", key="ph_hconc")
    col1, col2 = st.columns(2)

    if col1.button("Hitung"):
        if h_conc <= 0:
            st.warning("⚠️ Masukkan konsentrasi ion H⁺ yang lebih besar dari 0.")
        else:
            ph = -math.log10(h_conc)
            st.markdown(f"<div class='custom-output'>pH = {ph:.2f}</div>", unsafe_allow_html=True)

    if col2.button("Reset"):
        if "ph_hconc" in st.session_state:
            del st.session_state["ph_hconc"]
        st.rerun()

# ------------------ Pengenceran ------------------
elif menu == "💧 Pengenceran Larutan":
    st.header("🔹 Pengenceran Larutan")
    st.markdown("*Rumus:* M₁V₁ = M₂V₂")

    m1 = st.number_input("Konsentrasi awal (M₁)", min_value=0.0, key="peng_m1")
    v1 = st.number_input("Volume awal (V₁) [mL]", min_value=0.0, key="peng_v1")
    m2 = st.number_input("Konsentrasi akhir (M₂)", min_value=0.01, key="peng_m2")
    col1, col2 = st.columns(2)

    if col1.button("Hitung"):
        if m1 == 0 or v1 == 0 or m2 == 0:
            st.warning("⚠️ Semua nilai harus diisi dengan benar.")
        else:
            v2 = (m1 * v1) / m2
            st.markdown(f"<div class='custom-output'>Volume akhir (V₂) = {v2:.2f} mL</div>", unsafe_allow_html=True)

    if col2.button("Reset"):
        for key in ["peng_m1", "peng_v1", "peng_m2"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# ------------------ Persentase Konsentrasi ------------------
elif menu == "📊 Persentase Konsentrasi":
    st.header("🔹 Persentase Konsentrasi")
    st.markdown("*Rumus:* (massa zat / massa larutan) × 100%")

    massa_zat = st.number_input("Massa zat (gram)", min_value=0.0, key="persen_mz")
    massa_larutan = st.number_input("Massa larutan total (gram)", min_value=0.01, key="persen_ml")
    col1, col2 = st.columns(2)

    if col1.button("Hitung"):
        if massa_zat == 0 or massa_larutan == 0:
            st.warning("⚠️ Masukkan nilai massa zat dan massa larutan yang valid.")
        elif massa_zat > massa_larutan:
            st.warning("❌ Massa zat tidak boleh lebih besar dari massa larutan.")
        else:
            persen = (massa_zat / massa_larutan) * 100
            st.markdown(f"<div class='custom-output'>Persentase Konsentrasi = {persen:.2f}%</div>", unsafe_allow_html=True)

    if col2.button("Reset"):
        for key in ["persen_mz", "persen_ml"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# ------------------ SMART QUIZIZ ------------------
elif menu == "🧠 Kuis Kimia":
    st.header("🧪 SMART QUIZIZ")
    st.markdown("Uji pemahamanmu tentang konsep dasar kimia melalui kuis singkat berikut!")

    st.markdown("""
        <style>
        .feedback.benar {
            background-color: rgba(0, 255, 0, 0.2);
            color: #00ff88;
            font-weight: bold;
            padding: 10px;
            border-left: 5px solid #00ff88;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .feedback.salah {
            background-color: rgba(255, 0, 0, 0.2);
            color: #ff4444;
            font-weight: bold;
            padding: 10px;
            border-left: 5px solid #ff4444;
            border-radius: 5px;
            margin-bottom: 10px;
        }
        .ucapan.sukses {
            background-color: rgba(0, 255, 128, 0.3);
            color: #00ff88;
            font-weight: bold;
            padding: 12px;
            border-left: 5px solid #00ff88;
            border-radius: 8px;
            margin-top: 10px;
        }
        .ucapan.info {
            background-color: rgba(255, 255, 0, 0.2);
            color: #ffe600;
            font-weight: bold;
            padding: 12px;
            border-left: 5px solid #ffe600;
            border-radius: 8px;
            margin-top: 10px;
        }
        .ucapan.peringatan {
            background-color: rgba(255, 0, 0, 0.2);
            color: #ff4444;
            font-weight: bold;
            padding: 12px;
            border-left: 5px solid #ff4444;
            border-radius: 8px;
            margin-top: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    if "submitted" not in st.session_state:
        st.session_state["submitted"] = False

    q1 = st.radio("1. Apa satuan dari molaritas?", ["mol", "mol/L", "gram", "L/mol"], key="q1_submit")
    q2 = st.radio("2. 10 gram NaCl (Mr = 58,5 g/mol) dilarutkan. Berapa mol yang terlarut?",
                  ["0,15 mol", "0,17 mol", "0,18 mol", "0,20 mol"], key="q2_submit")
    q3 = st.radio("3. Rumus pengenceran larutan adalah?",
                  ["M1 + M2 = V", "M1V1 = M2V2", "M = mol × V", "M1V2 = M2V1"], key="q3_submit")
    q4 = st.radio("4. Jika H⁺ = 1 × 10⁻³ mol/L, maka pH-nya adalah?",
                  ["3", "4", "7", "10"], key="q4_submit")
    q5 = st.radio("5. Massa molar dari H₂O adalah?",
                  ["16 g/mol", "18 g/mol", "20 g/mol", "10 g/mol"], key="q5_submit")

    if st.button("Submit Jawaban"):
        st.session_state["submitted"] = True

    if st.session_state["submitted"]:
        score = 0
        st.markdown("---")
        st.subheader("📋 Hasil Kuis:")

        if q1 == "mol/L":
            st.markdown("<div class='feedback benar'>✅ 1. Benar! Molaritas satuannya mol/L.</div>", unsafe_allow_html=True)
            score += 1
        else:
            st.markdown("<div class='feedback salah'>❌ 1. Salah. Jawabannya adalah mol/L.</div>", unsafe_allow_html=True)

        if q2 == "0,17 mol":
            st.markdown("<div class='feedback benar'>✅ 2. Tepat! 10 / 58,5 = 0,17 mol.</div>", unsafe_allow_html=True)
            score += 1
        else:
            st.markdown("<div class='feedback salah'>❌ 2. Salah. Jawabannya adalah 0,17 mol.</div>", unsafe_allow_html=True)

        if q3 == "M1V1 = M2V2":
            st.markdown("<div class='feedback benar'>✅ 3. Betul! Itu rumus pengenceran larutan.</div>", unsafe_allow_html=True)
            score += 1
        else:
            st.markdown("<div class='feedback salah'>❌ 3. Salah. Yang benar adalah M1V1 = M2V2.</div>", unsafe_allow_html=True)

        if q4 == "3":
            st.markdown("<div class='feedback benar'>✅ 4. Tepat! pH = -log(10⁻³) = 3.</div>", unsafe_allow_html=True)
            score += 1
        else:
            st.markdown("<div class='feedback salah'>❌ 4. Salah. Jawabannya adalah 3.</div>", unsafe_allow_html=True)

        if q5 == "18 g/mol":
            st.markdown("<div class='feedback benar'>✅ 5. Benar! H₂ (2) + O (16) = 18 g/mol.</div>", unsafe_allow_html=True)
            score += 1
        else:
            st.markdown("<div class='feedback salah'>❌ 5. Salah. Jawabannya adalah 18 g/mol.</div>", unsafe_allow_html=True)

        st.markdown("---")
        st.markdown(f"<div class='custom-output'>Skor akhir kamu: {score} dari 5 soal</div>", unsafe_allow_html=True)

        if score == 5:
            st.balloons()
            st.markdown("<div class='ucapan sukses'>🎉 Hebat! Kamu benar semua.</div>", unsafe_allow_html=True)
        elif score >= 3:
            st.markdown("<div class='ucapan info'>👍 Bagus! Tinggal sedikit lagi jadi master kimia.</div>", unsafe_allow_html=True)
        else:
            st.markdown("<div class='ucapan peringatan'>📚 Yuk belajar lagi, kamu pasti bisa!</div>", unsafe_allow_html=True)

        if st.button("Ulangi Kuis"):
            for k in list(st.session_state.keys()):
                if k.startswith("q") or k == "submitted":
                    del st.session_state[k]
            st.rerun()

# ------------------ Footer ------------------
# ------------------ Footer ------------------
st.markdown("""
<div style='text-align: center; color: white; font-size: 0.9rem; margin-top: 50px;'>
    © 2025 ChemVerse | Dibuat oleh Kelompok 3
</div>
""", unsafe_allow_html=True)
