import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Matrikulasi Super Detail & Simulasi 3D", page_icon="🌐", layout="wide")

st.markdown("""
<style>
div[data-testid="stMarkdownContainer"] p {
    text-align: justify;
}
</style>
""", unsafe_allow_html=True)

st.title("MODUL MATRIKULASI KOMPREHENSIF & SPASIAL ASTRONOMI")
st.header("Fondasi Matematika, Trigonometri, dan Tiga Sistem Koordinat Bola Langit")
st.divider()

# ==========================================
# 1. DASAR TRIGONOMETRI SEGITIGA DATAR & RUANG
# ==========================================
st.markdown("""
### 1. Landasan Matematika: Trigonometri Segitiga Datar (*Plane Trigonometry*)
Sebelum melangkah ke geometri bola, mahasiswa wajib menguasai manipulasi aljabar dan identitas trigonometri bidang datar (*Euclidean plane*). Buku-buku klasik seperti W.M. Smart sering kali melewati langkah-langkah aljabar dasar karena menganggap pembaca telah mahir.

#### A. Aturan Dasar Segitiga Datar
1. **Aturan Sinus (Sine Rule):** Digunakan untuk relasi sudut dan sisi berhadapan.
   $$
   \\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C}
   $$
2. **Aturan Kosinus (Cosine Rule):** Digunakan saat dua sisi dan satu sudut apit diketahui ($b, c, A$) untuk mencari sisi ketiga ($a$):
   $$
   a^2 = b^2 + c^2 - 2bc \\cos A
   $$

#### B. Fungsi Kebalikannya (*Reciprocal Functions*)
Astronomi bola sangat sering menggunakan fungsi kebalikan yang jarang muncul di kalkulus modern:
* **Secan ($\\sec$):** $\\sec \\theta = \\frac{1}{\\cos \\theta}$
* **Cosecan ($\\text{cosec}$):** $\\text{cosec } \\theta = \\frac{1}{\\sin \\theta}$
* **Cotangen ($\\cot$):** $\\cot \\theta = \\frac{\\cos \\theta}{\\sin \\theta} = \\frac{1}{\\tan \\theta}$

#### C. Identitas Sudut Paruh (*Half-Angle Identities*)
Sangat krusial dalam penurunan rumus logaritma astronomi:
$$
\\sin^2 \\left(\\frac{A}{2}\\right) = \\frac{(s-b)(s-c)}{bc}, \\quad \\text{di mana } s = \\frac{a+b+c}{2}
$$
""")
st.divider()

# ==========================================
# 2. PENGANTAR ASTRONOMI BOLA
# ==========================================
st.markdown("""
### 2. Pengantar Astronomi Bola & Konsep Bola Langit (*Celestial Sphere*)
* **Bola Langit:** Bola khayal berpusat di mata pengamat ($O$) dengan jari-jari tak berhingga ($R=1$ untuk kemudahan matematis). Semua benda langit dipetakan arah pandangnya ke permukaan bola ini.
* **Lingkaran Besar (*Great Circle*):** Perpotongan permukaan bola dengan bidang yang melewati titik pusat bola ($O$). Ini adalah jarak terdekat antara dua titik di permukaan bola (analog dengan garis lurus di bidang datar).
* **Kelebihan Bola (*Spherical Excess*):** Berbeda dengan segitiga bidang datar yang jumlah sudutnya selalu $180^\\circ$ ($\\pi$ radian), jumlah ketiga sudut segitiga bola ($\\alpha + \\beta + \\gamma$) **selalu lebih besar dari $180^\\circ$**.
""")
st.divider()

# ==========================================
# 3. TIGA SISTEM KOORDINAT UTAMA & SIMULASI 3D
# ==========================================
st.subheader("3. Anatomi Tiga Sistem Koordinat Utama & Simulasi Interaktif 3D")
st.info("💡 **Petunjuk:** Pilih sistem koordinat di bawah ini untuk mempelajari definisi matematisnya sekaligus mengamati peraga visualisasi 3D interaktifnya.")

pilihan_sistem = st.selectbox(
    "Pilih Sistem Koordinat Astronomi:",
    [
        "A. Sistem Koordinat Horizon (Lokal)", 
        "B. Sistem Koordinat Ekuator (Global / Langit)", 
        "C. Sistem Koordinat Ekliptika (Tata Surya)"
    ]
)

fig_coord = go.Figure()

# Bola Transparan Umum sebagai latar belakang
u = np.linspace(0, 2 * np.pi, 40)
v = np.linspace(0, np.pi, 40)
xs = np.outer(np.cos(u), np.sin(v))
ys = np.outer(np.sin(u), np.sin(v))
zs = np.outer(np.ones(np.size(u)), np.cos(v))

fig_coord.add_trace(go.Surface(
    x=xs, y=ys, z=zs, colorscale='Blues', opacity=0.08, showscale=False, name='Bola Langit'
))

if pilihan_sistem == "A. Sistem Koordinat Horizon (Lokal)":
    st.markdown("""
    #### A. Sistem Koordinat Horizon (Lokal / Alt-Azimuth)
    * **Bidang Referensi:** Bidang horizon pengamat (cakrawala). Titik Zenith ($Z$) berada tepat di atas kepala, Nadir ($N'$) di bawah kaki.
    * **Parameter Koordinat:**
      1. **Tinggi (*Altitude* / $h$):** Jangkauan sudut benda langit diukur vertikal dari horizon ke arah bintang ($0^\\circ$ s.d. $+90^\\circ$).
      2. **Azimuth ($A$):** Sudut horizontal yang diukur dari titik Utara (atau Selatan) ke arah timur sepanjang horizon ($0^\\circ$ s.d. $360^\\circ$).
    * **Karakteristik:** Bersifat lokal dan terikat waktu tempatan (berubah terus akibat rotasi bumi).
    """)
    
    # Simulasi 3D Horizon
    theta = np.linspace(0, 2 * np.pi, 100)
    fig_coord.add_trace(go.Scatter3d(x=np.cos(theta), y=np.sin(theta), z=np.zeros_like(theta), mode='lines', line=dict(color='green', width=5), name='Bidang Horizon'))
    fig_coord.add_trace(go.Scatter3d(x=[0, 0, 0, 1, -1], y=[0, 0, -1, 0, 0], z=[1, -1, 0, 0, 0], mode='text+markers', text=['Zenith (Z)', 'Nadir (N\')', 'Selatan (S)', 'Utara (N)', 'Timur/Barat'], marker=dict(size=7, color='green'), textfont=dict(color='darkgreen', size=12)))
    fig_coord.update_layout(title="Simulasi 3D: Sistem Koordinat Horizon")

elif pilihan_sistem == "B. Sistem Koordinat Ekuator (Global / Langit)":
    st.markdown("""
    #### B. Sistem Koordinat Ekuator (Celestial Equatorial Coordinates)
    * **Bidang Referensi:** Ekuator langit (*celestial equator*), yaitu proyeksi ekuator bumi ke bola langit.
    * **Titik Acuan Utama:** Titik Aries ($\\gamma$ / *Vernal Equinox*), titik potong semu pergerakan matahari melintasi ekuator dari belahan selatan ke utara.
    * **Parameter Koordinat:**
      1. **Deklinasi ($\\delta$):** Analog dengan lintang bumi, diukur utara/selatan dari ekuator langit ($0^\\circ$ s.d. $\\pm 90^\\circ$).
      2. **Asensio Rekta (*Right Ascension* / $\\alpha$):** Analog dengan bujur bumi, diukur ke arah timur dari Titik Aries ($0^\\text{h}$ s.d. $24^\\text{h}$).
    """)
    
    # Simulasi 3D Ekuator
    theta = np.linspace(0, 2 * np.pi, 100)
    fig_coord.add_trace(go.Scatter3d(x=np.cos(theta), y=np.sin(theta), z=np.zeros_like(theta), mode='lines', line=dict(color='crimson', width=5), name='Ekuator Langit'))
    fig_coord.add_trace(go.Scatter3d(x=[0, 0, 1], y=[0, 0, 0], z=[1, -1, 0], mode='text+markers', text=['Kutub Langit Utara (NCP)', 'Kutub Langit Selatan (SCP)', 'Titik Aries (γ)'], marker=dict(size=7, color='crimson'), textfont=dict(color='darkred', size=12)))
    fig_coord.update_layout(title="Simulasi 3D: Sistem Koordinat Ekuator")

else:
    st.markdown("""
    #### C. Sistem Koordinat Ekliptika (Ecliptic Coordinates)
    * **Bidang Referensi:** Bidang ekliptika, yaitu bidang orbit semu tahunan pergerakan matahari mengelilingi bumi (atau bidang orbit bumi mengelilingi matahari).
    * **Titik Acuan Utama:** Titik Aries ($\\gamma$).
    * **Parameter Koordinat:**
      1. **Lintang Ekliptika ($\\beta$):** Jarak sudut utara/selatan dari bidang ekliptika ($0^\\circ$ s.d. $\\pm 90^\\circ$).
      2. **Bujur Ekliptika ($\\lambda$):** Sudut yang diukur dari Titik Aries ke arah timur sepanjang jalur ekliptika ($0^\\circ$ s.d. $360^\\circ$).
    * **Catatan Astronomis:** Bidang ekliptika miring sebesar $\\varepsilon \\approx 23.5^\\circ$ terhadap bidang ekuator langit (kemiringan sumbu bumi / *obliquity of the ecliptic*).
    """)
    
    # Simulasi 3D Ekliptika (Dimiringkan 23.5 derajat)
    eps = np.radians(23.5)
    t = np.linspace(0, 2 * np.pi, 100)
    xe = np.cos(t)
    ye = np.sin(t) * np.cos(eps)
    ze = np.sin(t) * np.sin(eps)
    
    # Ekuator pembanding (garis tipis biru)
    fig_coord.add_trace(go.Scatter3d(x=np.cos(t), y=np.sin(t), z=np.zeros_like(t), mode='lines', line=dict(color='gray', width=2, dash='dot'), name='Ekuator Langit (Referensi)'))
    # Ekliptika (garis tebal oranye)
    fig_coord.add_trace(go.Scatter3d(x=xe, y=ye, z=ze, mode='lines', line=dict(color='darkorange', width=6), name='Bidang Ekliptika (Miring 23.5°)'))
    fig_coord.add_trace(go.Scatter3d(x=[0], y=[0], z=[0], mode='text+markers', text=['Pusat Pengamat (O)'], marker=dict(size=6, color='orange'), textfont=dict(color='chocolate', size=12)))
    fig_coord.update_layout(title="Simulasi 3D: Sistem Koordinat Ekliptika Terhadap Ekuator")

fig_coord.update_layout(
    scene=dict(xaxis_title='Sumbu X', yaxis_title='Sumbu Y', zaxis_title='Sumbu Z'),
    width=850, height=520,
    margin=dict(l=0, r=0, b=0, t=40)
)

st.plotly_chart(fig_coord, use_container_width=True)
