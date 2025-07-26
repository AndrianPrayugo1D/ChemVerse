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
        background-repeat: no-repeat;
        background-position: center center;
        min-height: 100vh;
        color: white;
    }

    h1, h2, h3, h4 {
        color: #00ccff;
    }

    html, body, p, label, .stMarkdown, .stRadio, .stCheckbox, .stSelectbox, 
    .stTextInput, .stNumberInput, .stDateInput, .stTextArea, .stFileUploader, 
    .stSlider, .stMultiSelect {
        color: white !important;
    }

    .custom-output {
        background-color: rgba(255, 255, 255, 0.9);
        color: black;
        font-weight: bold;
        padding: 10px 20px;
        border: 3px solid #00ccff;
        border-radius: 10px;
        text-align: center;
        margin-top: 20px;
        font-size: 1.1rem;
        box-shadow: 0 0 10px rgba(0, 204, 255, 0.4);
    }

    .stButton>button {
        background-color: #00ccff;
        color: white;
        border-radius: 12px;
        padding: 0.5em 1em;
        font-weight: bold;
        border: none;
        transition: 0.3s ease;
        box-shadow: 0px 4px 10px rgba(0, 204, 255, 0.4);
    }

    .stButton>button:hover {
        background-color: #0099cc;
        transform: scale(1.05);
        box-shadow: 0px 6px 15px rgba(0, 204, 255, 0.6);
    }

    .stTextInput>div>div>input {
        background-color: rgba(255, 255, 255, 0.9);
        color: black;
        border-radius: 8px;
        padding: 0.5em;
        border: 1px solid #00ccff;
    }

    .stTextInput>div>div>input:focus {
        border: 2px solid #00ccff;
        outline: none;
        box-shadow: 0 0 8px rgba(0, 204, 255, 0.5);
    }

    button[aria-label="Open sidebar"],
    button[aria-label="Close sidebar"] {
        background-color: #00ccff !important;
        color: white !important;
        border: 2px solid white !important;
        border-radius: 12px !important;
        padding: 6px 10px !important;
        font-weight: bold !important;
        box-shadow: 0 0 12px rgba(0, 255, 255, 0.8) !important;
        z-index: 9999 !important;
        transition: 0.3s ease-in-out;
    }

    button[aria-label="Open sidebar"]:hover,
    button[aria-label="Close sidebar"]:hover {
        background-color: white !important;
        color: #00ccff !important;
        transform: scale(1.1);
        box-shadow: 0 0 16px rgba(255, 255, 255, 0.9) !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #b3d9ff !important;
        color: black !important;
        font-weight: bold;
        border-right: 2px solid #00ccff;
    }

    section[data-testid="stSidebar"] .css-1v0mbdj,
    section[data-testid="stSidebar"] .css-1d391kg {
        color: black !important;
    }

    section[data-testid="stSidebar"] .css-1v0mbdj:hover {
        background-color: #99ccff !important;
        border-radius: 8px;
    }
    </style>
    <div style="position: fixed; top: 70px; left: 10px; color: white; background: rgba(0,0,0,0.6); padding: 6px 10px; border-radius: 8px; z-index:9999; font-size: 14px;">
        Klik tombol >> untuk buka menu
    </div>
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
    st.markdown("*Masukkan massa zat (gram) dan Mr (massa molar relatif)*")

    # 🔍 Petunjuk Edukatif
    st.markdown("""
    <div style='color: #cccccc; font-size: 16px;'>
    💡 <b>Petunjuk:</b><br>
    • Masukkan <b>massa zat (dalam gram)</b> dan <b>Mr</b> (massa molar relatif) dari zat tersebut.<br>
    • Rumus yang digunakan: <code>mol = massa (g) / Mr</code><br>
    • Nilai mol menunjukkan jumlah partikel zat dalam satuan mol (1 mol = 6.022×10²³ partikel).
    </small>
    """, unsafe_allow_html=True)

    massa = st.number_input("Massa (gram)", min_value=0.0, format="%.4f", key="mol_massa")
    mr = st.number_input("Mr (Massa Molar Relatif)", min_value=0.0, format="%.4f", key="mol_mr")

    col1, col2 = st.columns(2)

    if col1.button("Hitung", key="mol_hitung"):
        if mr <= 0:
            st.warning("⚠️ Masukkan nilai Mr yang lebih besar dari 0.")
        else:
            mol = massa / mr
            st.markdown(f"<div class='custom-output'>Mol = {mol:.4f} mol</div>", unsafe_allow_html=True)
            st.markdown("""
            <div style='color: #cccccc; font-size: 14px; margin-top: 10px;'>
            🔎 <b>Penjelasan:</b><br>
            • Menggunakan rumus: <code>mol = massa / Mr</code><br>
            • mol = {:.4f} / {:.4f} = {:.4f} mol
            </div>
            """.format(massa, mr, mol), unsafe_allow_html=True)

    if col2.button("Reset", key="mol_reset"):
        for key in ["mol_massa", "mol_mr"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# ------------------ Hitung pH ------------------
elif menu == "🧫 Hitung pH":
    st.header("🔹 Hitung pH")

    # 🔍 Petunjuk di atas input
    st.markdown("""
    <div style='color: #cccccc; font-size: 16px;'>
    💡 <b>Petunjuk:</b><br>
    • Masukkan nilai konsentrasi ion H⁺ (untuk larutan asam) atau OH⁻ (untuk larutan basa) dalam satuan mol/L.<br>
    • Nilai <b>harus lebih besar dari 0</b>, karena logaritma dari 0 tidak terdefinisi.<br>
    • Contoh masukan yang benar: <code>0.01</code>, <code>1e-3</code> (setara dengan 0.001), atau <code>0.0000001</code><br>
    • Nilai pH dihitung dari rumus:  
    &emsp;- Untuk <b>asam</b>: <code>pH = -log[H⁺]</code><br>
    &emsp;- Untuk <b>basa</b>: <code>pOH = -log[OH⁻]</code>, lalu <code>pH = 14 - pOH</code><br>
    • Rentang pH yang valid biasanya antara <b>0 hingga 14</b> (pH &lt; 7 asam, pH = 7 netral, pH &gt; 7 basa)
    </div>
    """, unsafe_allow_html=True)

    st.markdown("*Pilih jenis larutan dan masukkan konsentrasi ion (mol/L)*")

    jenis = st.radio("Jenis Larutan", ["Asam", "Basa"], key="ph_jenis")
    konsentrasi = st.number_input("Konsentrasi ion (mol/L)", min_value=0.0, format="%.10f", key="ph_kons")

    col1, col2 = st.columns(2)

    if col1.button("Hitung"):
        if konsentrasi <= 0:
            st.warning("⚠️ Masukkan konsentrasi ion yang lebih besar dari 0.")
        else:
            if jenis == "Asam":
                ph = -math.log10(konsentrasi)
            else:  # Basa
                poh = -math.log10(konsentrasi)
                ph = 14 - poh

            if ph < 0:
                st.markdown("<div class='custom-output'>❌ Hasil pH tidak valid (negatif).</div>", unsafe_allow_html=True)
            elif ph > 14:
                st.markdown(f"<div class='custom-output'>⚠️ Hasil pH = {ph:.2f}, melebihi batas skala pH normal.</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='custom-output'>pH = {ph:.2f}</div>", unsafe_allow_html=True)

    if col2.button("Reset"):
        for key in ["ph_jenis", "ph_kons"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# ------------------ Pengenceran Larutan ------------------
elif menu == "💧 Pengenceran Larutan":
    st.header("🔹 Pengenceran Larutan")
    st.markdown("*Hitung volume akhir berdasarkan rumus pengenceran: M₁ × V₁ = M₂ × V₂*")

    # 🔍 Petunjuk Edukatif
    st.markdown("""
    <div style='color: #cccccc; font-size: 16px;'>
    💡 <b>Petunjuk:</b><br>
    • Masukkan konsentrasi awal (M₁), volume awal (V₁), dan konsentrasi akhir (M₂).<br>
    • Satuan yang digunakan harus konsisten (contoh: mL untuk volume, Molar untuk konsentrasi).<br>
    • Rumus yang digunakan: <code>M₁ × V₁ = M₂ × V₂</code><br>
    • Aplikasi akan menghitung volume akhir (V₂) yang diperlukan agar larutan menjadi lebih encer.
    </small>
    """, unsafe_allow_html=True)

    m1 = st.number_input("Konsentrasi awal (M₁)", min_value=0.0, format="%.4f", key="peng_m1")
    v1 = st.number_input("Volume awal (V₁) dalam mL", min_value=0.0, format="%.4f", key="peng_v1")
    m2 = st.number_input("Konsentrasi akhir (M₂)", min_value=0.0, format="%.4f", key="peng_m2")

    col1, col2 = st.columns(2)

    if col1.button("Hitung", key="pengenceran_hitung"):
        if m2 <= 0:
            st.warning("⚠️ Masukkan nilai M₂ yang lebih besar dari 0.")
        else:
            v2 = (m1 * v1) / m2
            st.markdown(f"<div class='custom-output'>Volume akhir (V₂) = {v2:.2f} mL</div>", unsafe_allow_html=True)
            st.markdown("""
            <div style='color: #cccccc; font-size: 14px; margin-top: 10px;'>
            🔎 <b>Penjelasan:</b><br>
            • Menggunakan rumus: <code>M₁ × V₁ = M₂ × V₂</code><br>
            • ({:.4f}) × ({:.2f}) = ({:.4f}) × V₂<br>
            • V₂ = {:.4f} mL
            </div>
            """.format(m1, v1, m2, v2), unsafe_allow_html=True)

    if col2.button("Reset", key="pengenceran_reset"):
        for key in ["peng_m1", "peng_v1", "peng_m2"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()

# ------------------ Persentase Konsentrasi ------------------
elif menu == "📊 Persentase Konsentrasi":
    st.header("🔹 Persentase Konsentrasi (% b/b)")
    st.markdown("*Hitung persentase konsentrasi larutan berdasarkan massa zat dan massa total larutan*")

    # 🔍 Petunjuk Edukatif
    st.markdown("""
    <div style='color: #cccccc; font-size: 16px;'>
    💡 <b>Petunjuk:</b><br>
    • Masukkan <b>massa zat terlarut</b> dan <b>massa total larutan</b> (zat + pelarut) dalam gram.<br>
    • Pastikan massa zat ≤ massa larutan.<br>
    • Rumus: <code>(massa zat / massa larutan) × 100%</code><br>
    • Hasil akan menunjukkan konsentrasi dalam persen (% b/b).
    </small>
    """, unsafe_allow_html=True)

    massa_zat = st.number_input("Massa zat terlarut (gram)", min_value=0.0, format="%.4f", key="persen_zat")
    massa_larutan = st.number_input("Massa total larutan (gram)", min_value=0.0, format="%.4f", key="persen_larutan")

    col1, col2 = st.columns(2)

    if col1.button("Hitung", key="persen_hitung"):
        if massa_larutan <= 0:
            st.warning("⚠️ Masukkan massa larutan yang lebih besar dari 0.")
        elif massa_zat > massa_larutan:
            st.warning("⚠️ Massa zat tidak boleh lebih besar dari massa larutan.")
        else:
            persen = (massa_zat / massa_larutan) * 100
            st.markdown(f"<div class='custom-output'>Konsentrasi = {persen:.2f}%</div>", unsafe_allow_html=True)
            st.markdown("""
            <div style='color: #cccccc; font-size: 14px; margin-top: 10px;'>
            🔎 <b>Penjelasan:</b><br>
            • Menggunakan rumus: <code>(massa zat / massa larutan) × 100%</code><br>
            • ({:.4f} / {:.4f}) × 100% = {:.2f}%
            </div>
            """.format(massa_zat, massa_larutan, persen), unsafe_allow_html=True)

    if col2.button("Reset", key="persen_reset"):
        for key in ["persen_zat", "persen_larutan"]:
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
