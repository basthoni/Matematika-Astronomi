import streamlit as st

# Konfigurasi Halaman Utama
st.set_page_config(
    page_title="Matematika Astronomi - UIN Walisongo",
    page_icon="🌌",
    layout="wide"
)

# Judul dan Header Utama
st.title("🌌 Modul Digital Matematika Astronomi")
st.subheader("Program Studi Ilmu Falak | UIN Walisongo Semarang")
st.divider()

st.markdown("""
Selamat datang di Modul Pembelajaran Interaktif Matematika Astronomi (PIF-6048). 
Silakan gunakan menu navigasi di sebelah kiri untuk mengakses materi per bab, mulai dari Trigonometri Bola hingga aplikasi perhitungan falak.
""")

st.write("---")

# Bagian Deskripsi Singkat Mata Kuliah
st.header("Deskripsi Singkat Mata Kuliah")
st.info("""
Mata kuliah ini berisi topik dan materi yang mengintegrasikan nilai-nilai keislaman dan pengetahuan terkait: dasar-dasar matematika berkenaan dengan kajian ilmu falak, konsep pengertian titik, garis, sudut, dan sistem koordinat; aplikasi titik, garis, sudut, dan sistem koordinat dalam Bumi; konsep arah; segitiga datar, konsep lingkaran dalam matematika dan astronomi, trigonometri; dasar-dasar trigonometri dalam kajian ilmu falak; konsep aturan sinus dan cosinus dalam segitiga bidang datar; geometri bola, segi tiga bola, aturan sinus dan cosinus dalam segi tiga bola.
""")

# Bagian Capaian Pembelajaran (CPMK)
st.header("Capaian Pembelajaran Mata Kuliah (CPMK)")
st.success("""
* **CPMK-01:** Mahasiswa mampu memahami dan menjelaskan konsep dan perhitungan dalam matematika astronomi.
* **CPMK-02:** Mahasiswa mampu mendindetifikasi pemanfaatan konsep dan perhitungan matematika astronomi untuk dimanfaatkan dalam ilmu falak.
""")

# Footer tambahan opsional
st.divider()
st.caption("© 2026 Dosen Pengampu: M. Basthoni | Fakultas Syariah dan Hukum")
