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

st.title("MODUL MATRIKULASI KOMPREHENSIF & LABORATORIUM SPASIAL ASTRONOMI")
st.header("Fondasi Matematika, Trigonometri Bola, dan Bedah Detail Tiga Sistem Koordinat Bola Langit")
st.divider()

# ==========================================
# 1. DASAR TRIGONOMETRI SEGITIGA DATAR & RUANG
# ==========================================
st.markdown("""
### 1. Landasan Matematika: Trigonometri Segitiga Datar & Identitas Lanjut
Sebelum mahasiswa memasuki penurunan rumus analitis W.M. Smart, penguasaan terhadap manipulasi aljabar dan identitas trigonometri bidang datar (*Euclidean plane*) wajib dikuasai secara mendalam:

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
# 3. LABORATORIUM SIMULASI 3D SUPER DETAIL
# ==========================================
st.subheader("3. Laboratorium Spasial 3D: Bedah Detail Tiga Sistem Koordinat Utama")
st.info("💡 **Petunjuk:** Pilih sistem koordinat di bawah ini. Pusat bola kini dilengkapi dengan representasi Bumi geosentrik untuk memperjelas posisi pengamat.")

pilihan_sistem = st.selectbox(
    "Pilih Sistem Koordinat Astronomi:",
    [
        "A. Sistem Koordinat Horizon (Lokal)", 
        "B. Sistem Koordinat Ekuator (Global / Langit)", 
        "C. Sistem Koordinat Ekliptika (Tata Surya)"
    ]
)

# Kerangka dasar bola langit transparan (Radius = 1)
u = np.linspace(0, 2 * np.pi, 40)
v = np.linspace(0, np.pi, 40)
xs = np.outer(np.cos(u), np.sin(v))
ys = np.outer(np.sin(u), np.sin(v))
zs = np.outer(np.ones(np.size(u)), np.cos(v))

fig_coord = go.Figure()
fig_coord.add_trace(go.Surface(
    x=xs, y=ys, z=zs, colorscale='Blues', opacity=0.05, showscale=False, name='Bola Langit'
))

# Fungsi pembantu untuk membuat bola Bumi kecil di pusat (0,0,0) dengan radius 0.07
def add_mini_earth(fig):
    ue = np.linspace(0, 2 * np.pi, 20)
    ve = np.linspace(0, np.pi, 20)
    r_earth = 0.07
    xe = r_earth * np.outer(np.cos(ue), np.sin(ve))
    ye = r_earth * np.outer(np.sin(ue), np.sin(ve))
    ze = r_earth * np.outer(np.ones(np.size(ue)), np.cos(ve))
    fig.add_trace(go.Surface(
        x=xe, y=ye, z=ze, colorscale='Viridis', opacity=0.9, showscale=False, name='Bumi (Pusat / Pengamat)'
    ))

if pilihan_sistem == "A. Sistem Koordinat Horizon (Lokal)":
    st.markdown("""
    #### A. Sistem Koordinat Horizon (Lokal / Alt-Azimuth)
    * **Bidang Referensi:** Bidang horizon pengamat (cakrawala). Titik Zenith ($Z$) berada tepat di atas kepala, Nadir ($N'$) di bawah kaki.
    * **Posisi Pengamat:** Berada di pusat bola $(0,0,0)$, berdiri di atas bidang horizon lokal.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        azimuth_deg = st.slider("Atur Azimuth (A) [Derajat]", 0, 360, 45, step=1)
    with col2:
        alt_deg = st.slider("Atur Tinggi / Altitude (h) [Derajat]", 0, 90, 30, step=1)
        
    az = np.radians(azimuth_deg)
    alt = np.radians(alt_deg)
    
    x_star = np.cos(alt) * np.cos(az)
    y_star = np.cos(alt) * np.sin(az)
    z_star = np.sin(alt)
    
    theta = np.linspace(0, 2 * np.pi, 100)
    fig_coord.add_trace(go.Scatter3d(x=np.cos(theta), y=np.sin(theta), z=np.zeros_like(theta), mode='lines', line=dict(color='green', width=4), name='Bidang Horizon'))
    fig_coord.add_trace(go.Scatter3d(x=[x_star, x_star], y=[y_star, y_star], z=[0, z_star], mode='lines', line=dict(color='orange', width=3, dash='dash'), name='Garis Tinggi (Altitude)'))
    fig_coord.add_trace(go.Scatter3d(x=[0, x_star], y=[0, y_star], z=[0, z_star], mode='lines', line=dict(color='red', width=5), name='Vektor Pengamatan'))
    
    add_mini_earth(fig_coord)
    
    hx = [0,  0,  1,  0, -1,  0, x_star]
    hy = [0,  0,  0,  1,  0, -1, y_star]
    hz = [1, -1,  0,  0,  0,  0, z_star]
    htext = ['Zenith (Z)', 'Nadir (N\')', 'Utara (N, 0°)', 'Timur (E, 90°)', 'Selatan (S, 180°)', 'Barat (W, 270°)', f'Bintang (h={alt_deg}°, A={azimuth_deg}°)']
    hcolor = ['green', 'gray', 'blue', 'blue', 'blue', 'blue', 'red']
    
    fig_coord.add_trace(go.Scatter3d(x=hx, y=hy, z=hz, mode='text+markers', text=htext, marker=dict(size=[6, 6, 6, 6, 6, 6, 8], color=hcolor), textfont=dict(size=11)))
    fig_coord.update_layout(title=f"Simulasi 3D: Koordinat Horizon (Alt: {alt_deg}°, Az: {azimuth_deg}°)")

elif pilihan_sistem == "B. Sistem Koordinat Ekuator (Global / Langit)":
    st.markdown("""
    #### B. Sistem Koordinat Ekuator (Celestial Equatorial Coordinates)
    * **Bidang Referensi:** Ekuator langit (Merah) dan Lingkaran Ekliptika (Oranye).
    * **Pusat Geosentrik:** Miniatur Bumi di tengah menunjukkan bahwa sistem koordinat ini diturunkan dari pusat bola bumi. Perpotongan kedua bidang di sumbu $X$ positif membentuk **Titik Aries ($\\gamma$)**.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        ra_deg = st.slider("Atur Asensio Rekta (α) [Derajat]", 0, 360, 60, step=1)
    with col2:
        dec_deg = st.slider("Atur Deklinasi (δ) [Derajat]", -90, 90, 20, step=1)
        
    ra = np.radians(ra_deg)
    dec = np.radians(dec_deg)
    eps = np.radians(23.5)
    
    x_star = np.cos(dec) * np.cos(ra)
    y_star = np.cos(dec) * np.sin(ra)
    z_star = np.sin(dec)
    
    t = np.linspace(0, 2 * np.pi, 100)
    # Ekuator Langit
    fig_coord.add_trace(go.Scatter3d(x=np.cos(t), y=np.sin(t), z=np.zeros_like(t), mode='lines', line=dict(color='crimson', width=4), name='Ekuator Langit'))
    # Lingkaran Ekliptika
    xe_circ = np.cos(t)
    ye_circ = np.sin(t) * np.cos(eps)
    ze_circ = np.sin(t) * np.sin(eps)
    fig_coord.add_trace(go.Scatter3d(x=xe_circ, y=ye_circ, z=ze_circ, mode='lines', line=dict(color='darkorange', width=3, dash='dash'), name='Lingkaran Ekliptika'))
    
    # Titik Aries (Perpotongan)
    fig_coord.add_trace(go.Scatter3d(x=[1], y=[0], z=[0], mode='text+markers', text=['Titik Aries (γ): Perpotongan Ekuator & Ekliptika'], marker=dict(size=8, color='purple'), textfont=dict(color='purple', size=12)))
    
    # Vektor Bintang
    fig_coord.add_trace(go.Scatter3d(x=[0, x_star], y=[0, y_star], z=[0, z_star], mode='lines', line=dict(color='red', width=5), name='Vektor Bintang'))
    
    add_mini_earth(fig_coord)
    
    fig_coord.add_trace(go.Scatter3d(
        x=[0, 0, x_star], y=[0, 0, y_star], z=[1, -1, z_star],
        mode='text+markers',
        text=['Kutub Utara (NCP)', 'Kutub Selatan (SCP)', f'Bintang (α={ra_deg}°, δ={dec_deg}°)'],
        marker=dict(size=[6, 6, 8], color=['crimson', 'crimson', 'red']),
        textfont=dict(size=11)
    ))
    fig_coord.update_layout(title=f"Simulasi 3D: Koordinat Ekuator & Titik Aries (RA: {ra_deg}°, Dec: {dec_deg}°)")

else:
    st.markdown("""
    #### C. Sistem Koordinat Ekliptika (Ecliptic Coordinates)
    * **Bidang Referensi:** Bidang ekliptika (jalur edar semu matahari).
    * **Pusat Geosentrik:** Miniatur Bumi di pusat $(0,0,0)$ menegaskan posisi pengamat bumi melihat benda tata surya relatif terhadap bidang ekliptika.
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        lam_deg = st.slider("Atur Bujur Ekliptika (λ) [Derajat]", 0, 360, 90, step=1)
    with col2:
        bet_deg = st.slider("Atur Lintang Ekliptika (β) [Derajat]", -90, 90, 10, step=1)
        
    lam = np.radians(lam_deg)
    bet = np.radians(bet_deg)
    eps = np.radians(23.5)
    
    xe = np.cos(bet) * np.cos(lam)
    ye = np.cos(bet) * np.sin(lam) * np.cos(eps) - np.sin(bet) * np.sin(eps)
    ze = np.cos(bet) * np.sin(lam) * np.sin(eps) + np.sin(bet) * np.cos(eps)
    
    t = np.linspace(0, 2 * np.pi, 100)
    fig_coord.add_trace(go.Scatter3d(x=np.cos(t), y=np.sin(t), z=np.zeros_like(t), mode='lines', line=dict(color='gray', width=2, dash='dot'), name='Ekuator Langit'))
    
    x_ecl = np.cos(t)
    y_ecl = np.sin(t) * np.cos(eps)
    z_ecl = np.sin(t) * np.sin(eps)
    fig_coord.add_trace(go.Scatter3d(x=x_ecl, y=y_ecl, z=z_ecl, mode='lines', line=dict(color='darkorange', width=5), name='Bidang Ekliptika'))
    
    fig_coord.add_trace(go.Scatter3d(x=[0, xe], y=[0, ye], z=[0, ze], mode='lines', line=dict(color='red', width=5), name='Vektor Objek'))
    
    add_mini_earth(fig_coord)
    
    fig_coord.add_trace(go.Scatter3d(
        x=[1, xe], y=[0, ye], z=[0, ze],
        mode='text+markers',
        text=['Titik Aries (γ)', f'Objek (λ={lam_deg}°, β={bet_deg}°)'],
        marker=dict(size=[8, 8], color=['purple', 'red']),
        textfont=dict(size=11)
    ))
    fig_coord.update_layout(title=f"Simulasi 3D Interaktif: Koordinat Ekliptika (λ: {lam_deg}°, β: {bet_deg}°)")

fig_coord.update_layout(
    scene=dict(xaxis_title='Sumbu X', yaxis_title='Sumbu Y', zaxis_title='Sumbu Z'),
    width=850, height=550,
    margin=dict(l=0, r=0, b=0, t=40)
)

st.plotly_chart(fig_coord, use_container_width=True)
