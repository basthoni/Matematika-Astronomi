import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Pengantar Trigonometri & Simulasi 3D Koordinat Bola Langit", page_icon="🌐", layout="wide")

st.markdown("""
<style>
div[data-testid="stMarkdownContainer"] p {
    text-align: justify;
}
</style>
""", unsafe_allow_html=True)

st.title("PENGANTAR SINGKAT TRIGONOMETRI & ASTRONOMI BOLA")
st.header("Dasar Matematika, Trigonometri Bola, dan Sistem Koordinat Bola Langit")
st.divider()

# ==========================================
# 1. DASAR TRIGONOMETRI SEGITIGA DATAR & RUANG
# ==========================================
st.markdown("""
### 1. Landasan Matematika: Trigonometri Dasar & Identitas Trigonometri
Sebelum mahasiswa memasuki penurunan rumus analitis W.M. Smart dalam geometri bola, penguasaan terhadap konsep dasar segitiga datar (*Euclidean plane*) wajib dikuasai secara mendalam. Mari kita mulai dari fondasi yang paling mendasar.

#### A. Segitiga Siku-Siku & Teorema Pythagoras
Bayangkan sebuah segitiga siku-siku dengan salah satu sudutnya adalah $\\theta$. Segitiga ini memiliki tiga sisi yang kita namai berdasarkan posisinya terhadap sudut $\\theta$:
""")

# --- Visualisasi Segitiga Siku-Siku dengan Plotly ---
fig1 = go.Figure()
# Gambar sisi segitiga (0,0) -> (4,0) -> (4,3) -> (0,0)
fig1.add_trace(go.Scatter(x=[0, 4, 4, 0], y=[0, 0, 3, 0], mode='lines', line=dict(color='royalblue', width=3), showlegend=False))
# Simbol Siku-siku
fig1.add_trace(go.Scatter(x=[3.7, 3.7, 4], y=[0, 0.3, 0.3], mode='lines', line=dict(color='black', width=1.5), showlegend=False))
# Simbol Sudut Theta
theta_arc = np.linspace(0, np.arctan(3/4), 20)
fig1.add_trace(go.Scatter(x=0.6*np.cos(theta_arc), y=0.6*np.sin(theta_arc), mode='lines', line=dict(color='crimson', width=2), showlegend=False))

# Label
fig1.add_annotation(x=0.8, y=0.25, text="<b>θ</b>", showarrow=False, font=dict(size=18, color='crimson'))
fig1.add_annotation(x=2, y=-0.25, text="<b>b</b> (Sisi Samping / Adjacent)", showarrow=False, font=dict(size=14))
fig1.add_annotation(x=4.1, y=1.5, text="<b>a</b><br>(Sisi Depan / Opposite)", showarrow=False, font=dict(size=14), xanchor='left')
fig1.add_annotation(x=1.7, y=1.8, text="<b>c</b> (Sisi Miring / Hipotenusa)", showarrow=False, font=dict(size=14), textangle=-37)

fig1.update_layout(xaxis=dict(visible=False), yaxis=dict(visible=False), plot_bgcolor='rgba(0,0,0,0)', width=600, height=400, margin=dict(l=0,r=120,b=20,t=0))
st.plotly_chart(fig1, use_container_width=False)
# --------------------------------------------------

st.markdown("""
Hubungan fundamental dari ketiga sisi ini diikat oleh **Teorema Pythagoras**:

$$ a^2 + b^2 = c^2 $$

#### B. Definisi Fungsi Trigonometri Dasar
Dari segitiga siku-siku di atas, nilai perbandingan antar sisinya melahirkan tiga fungsi dasar trigonometri. Untuk memudahkan ingatan, kita biasa menggunakan akronim (De-Mi, Sa-Mi, De-Sa):
1. **Sinus ($\\sin$):** Perbandingan sisi **De**pan dengan sisi **Mi**ring. $\\implies \\sin \\theta = \\frac{a}{c}$
2. **Kosinus ($\\cos$):** Perbandingan sisi **Sa**mping dengan sisi **Mi**ring. $\\implies \\cos \\theta = \\frac{b}{c}$
3. **Tangen ($\\tan$):** Perbandingan sisi **De**pan dengan sisi **Sa**mping. $\\implies \\tan \\theta = \\frac{\\sin \\theta}{\\cos \\theta} = \\frac{a}{b}$

#### C. Fungsi Kebalikan (*Reciprocal Functions*)
Astronomi bola sangat sering menggunakan fungsi kebalikan dari fungsi dasar (jarang muncul di kalkulus modern namun krusial di falak):
1. **Cosecan ($\\text{cosec}$):** Kebalikan Sinus. $\\implies \\text{cosec } \\theta = \\frac{1}{\\sin \\theta} = \\frac{c}{a}$
2. **Secan ($\\sec$):** Kebalikan Kosinus. $\\implies \\sec \\theta = \\frac{1}{\\cos \\theta} = \\frac{c}{b}$
3. **Cotangen ($\\cot$):** Kebalikan Tangen. $\\implies \\cot \\theta = \\frac{1}{\\tan \\theta} = \\frac{b}{a}$

---

#### D. Aturan Sinus dan Kosinus pada Segitiga Sembarang
Bagaimana jika segitiganya tidak memiliki sudut $90^\\circ$ (segitiga sembarang)? Kita bisa menyelesaikannya dengan "meminjam" sifat segitiga siku-siku. 

Bayangkan segitiga sembarang $ABC$ dengan panjang sisi $a, b, c$. Kita tarik sebuah **garis tinggi ($h$)** dari sudut $C$ yang memotong tegak lurus sisi $c$ di titik $D$.
""")

# --- Visualisasi Segitiga Sembarang dengan Garis Tinggi ---
fig2 = go.Figure()
# Segitiga utama (0,0) -> (5,0) -> (3,4) -> (0,0)
fig2.add_trace(go.Scatter(x=[0, 7, 3, 0], y=[0, 0, 4, 0], mode='lines', line=dict(color='royalblue', width=3), showlegend=False))
# Garis Tinggi (h)
fig2.add_trace(go.Scatter(x=[3, 3], y=[0, 4], mode='lines', line=dict(color='crimson', width=2, dash='dash'), showlegend=False))
# Simbol Siku-siku di D
fig2.add_trace(go.Scatter(x=[2.8, 2.8, 3], y=[0, 0.2, 0.2], mode='lines', line=dict(color='black', width=1.5), showlegend=False))
fig2.add_trace(go.Scatter(x=[3.2, 3.2, 3], y=[0, 0.2, 0.2], mode='lines', line=dict(color='black', width=1.5), showlegend=False))

# Label Titik dan Sisi
fig2.add_annotation(x=-0.2, y=-0.2, text="<b>A</b>", showarrow=False, font=dict(size=18))
fig2.add_annotation(x=7.2, y=-0.2, text="<b>B</b>", showarrow=False, font=dict(size=18))
fig2.add_annotation(x=3, y=4.3, text="<b>C</b>", showarrow=False, font=dict(size=18))
fig2.add_annotation(x=3, y=-0.3, text="<b>D</b>", showarrow=False, font=dict(size=16))

fig2.add_annotation(x=1.3, y=2.2, text="<b>b</b>", showarrow=False, font=dict(size=16))
fig2.add_annotation(x=5.2, y=2.2, text="<b>a</b>", showarrow=False, font=dict(size=16))
fig2.add_annotation(x=2.8, y=2, text="<b>h</b>", showarrow=False, font=dict(size=16, color='crimson'))

fig2.add_annotation(x=1.5, y=-0.3, text="<b>x</b>", showarrow=False, font=dict(size=16))
fig2.add_annotation(x=5, y=-0.3, text="<b>c - x</b>", showarrow=False, font=dict(size=16))
fig2.add_annotation(x=3.5, y=-0.75, text="<───────────── <b>c</b> ─────────────>", showarrow=False, font=dict(size=14))

fig2.update_layout(xaxis=dict(visible=False, range=[-1, 8]), yaxis=dict(visible=False, range=[-1, 5]), plot_bgcolor='rgba(0,0,0,0)', width=650, height=450, margin=dict(l=0,r=0,b=0,t=0))
st.plotly_chart(fig2, use_container_width=False)
# ----------------------------------------------------------

st.markdown("""
Garis $CD = h$ membelah segitiga $ABC$ menjadi **dua buah segitiga siku-siku**: $\\Delta ADC$ di sebelah kiri dan $\\Delta BDC$ di sebelah kanan. Jika panjang $AD = x$, maka panjang $DB = c - x$.

##### 1. Pembuktian Aturan Sinus (*Sine Rule*)
Mari kita tinjau nilai Sinus pada kedua segitiga siku-siku tersebut:
*   Pada $\\Delta ADC$ (kiri): $\\sin A = \\frac{h}{b} \\implies \\mathbf{h = b \\sin A}$
*   Pada $\\Delta BDC$ (kanan): $\\sin B = \\frac{h}{a} \\implies \\mathbf{h = a \\sin B}$

Karena kedua persamaan sama-sama mendefinisikan tinggi $h$, kita dapat menyamakannya:

$$ b \\sin A = a \\sin B $$

Jika kedua ruas kita bagi dengan $(\\sin A \\cdot \\sin B)$, kita akan mendapatkan **Aturan Sinus**:

$$ \\frac{a}{\\sin A} = \\frac{b}{\\sin B} = \\frac{c}{\\sin C} $$

##### 2. Pembuktian Aturan Kosinus (*Cosine Rule*)
Sekarang kita gunakan **Teorema Pythagoras** pada kedua segitiga siku-siku tersebut:
*   Pada $\\Delta ADC$ (kiri): Nilai $\\cos A = \\frac{x}{b}$, sehingga $\\mathbf{x = b \\cos A}$.
    Melalui Pythagoras: 
    
    $$ h^2 + x^2 = b^2 \\implies \\mathbf{h^2 = b^2 - x^2} $$
    
*   Pada $\\Delta BDC$ (kanan), melalui Pythagoras juga:
    
    $$ a^2 = h^2 + (c - x)^2 $$
    
    $$ a^2 = h^2 + (c^2 - 2cx + x^2) $$

Sekarang, substitusikan nilai $\\mathbf{h^2}$ dari segitiga kiri ke dalam persamaan segitiga kanan:

$$ a^2 = (b^2 - x^2) + c^2 - 2cx + x^2 $$

Karena nilai $-x^2$ dan $+x^2$ saling menghilangkan, persamaannya tersisa menjadi:

$$ a^2 = b^2 + c^2 - 2cx $$

Langkah terakhir, substitusikan nilai $\\mathbf{x = b \\cos A}$ (yang kita dapat dari segitiga kiri) ke dalam persamaan di atas:

$$ a^2 = b^2 + c^2 - 2c(b \\cos A) $$

$$ \\mathbf{a^2 = b^2 + c^2 - 2bc \\cos A} $$

Inilah pondasi utama yang kelak akan dibuktikan ulang oleh W.M. Smart namun dalam bentuk ruang bidang lengkung (Trigonometri Bola).

#### E. Identitas Sudut Paruh (*Half-Angle Identities*)
Sangat krusial dalam penurunan rumus logaritma astronomi:

$$
\\sin^2 \\left(\\frac{A}{2}\\right) = \\frac{(s-b)(s-c)}{bc}, \\quad \\text{di mana } s = \\frac{a+b+c}{2}
$$
""")

with st.expander("📚 Syarah: Mengapa Sudut Paruh Sangat Penting di Ilmu Falak?"):
    st.markdown("""
Dalam astronomi modern (menggunakan Python/komputer), mesin bisa menghitung rumus apapun dalam hitungan milidetik. Namun, dalam literatur **Ilmu Falak klasik** dan sejarah astronomi bola, **Identitas Sudut Paruh (*Half-Angle Identities*) adalah "senjata rahasia" yang sangat berharga**.

Berikut adalah 4 alasan utama mengapa rumus sudut paruh sangat krusial dalam Ilmu Falak:

**1. Kunci Utama Perhitungan Logaritma (Zaman Pra-Kalkulator)**

Sebelum adanya kalkulator elektronik, para ulama falak dan astronom menghitung menggunakan **Tabel Logaritma**. Sifat dasar logaritma adalah: **Logaritma tidak bisa memproses operasi penjumlahan/pengurangan**, ia hanya bisa memecah perkalian/pembagian.
*   **Masalah pada Rumus Kosinus Fundamental:**
    
    $$ \\cos a = \\cos b \\cos c + \\sin b \\sin c \\cos A $$
    
    *(Terdapat tanda tambah (+), sehingga sangat sulit dan panjang jika dihitung menggunakan tabel logaritma manual).*
*   **Solusi dengan Sudut Paruh:**
    
    $$ \\sin^2 \\left(\\frac{A}{2}\\right) = \\frac{\\sin(s-b)\\sin(s-c)}{\\sin b \\sin c} $$
    
    *(Semua operasi adalah perkalian dan pembagian!).* Dengan ini, ahli falak masa lalu cukup menggunakan rumus:
    
    $$ \\log \\sin \\left(\\frac{A}{2}\\right) = \\frac{1}{2} [ \\log \\sin(s-b) + \\log \\sin(s-c) - \\log \\sin b - \\log \\sin c ] $$
    
    Hitungan yang tadinya rumit berubah menjadi sekadar tambah-kurang angka logaritma dari tabel.

**2. Cikal Bakal Rumus Haversine (Menghitung Jarak & Arah Kiblat)**

Dalam navigasi dan falak, ada fungsi bernama **Haversine**. Haversine sebenarnya adalah bentuk lain dari sudut paruh:

$$ \\text{hav}(\\theta) = \\sin^2 \\left(\\frac{\\theta}{2}\\right) = \\frac{1 - \\cos \\theta}{2} $$

Fungsi Haversine sangat populer untuk menghitung **Jarak Lingkaran Besar (Great Circle Distance)** dan **Arah Kiblat**. Keunggulannya adalah nilainya selalu positif (karena dikuadratkan) sehingga ahli falak tidak perlu pusing memikirkan apakah suatu sudut berada di kuadran negatif atau positif.

**3. Akurasi Tinggi untuk Jarak/Sudut yang Sangat Kecil**

Ketika kita menghitung arah kiblat atau jarak antara dua kota yang berdekatan, sudut jarak di pusat bumi sangatlah kecil (mendekati $0^\\circ$).
*   Jika menggunakan fungsi **Kosinus**, nilai $\\cos(0^\\circ) = 1$. Untuk sudut yang sangat kecil (misal $0.001^\\circ$), nilainya adalah $0.999999...$ Pada kalkulator biasa atau tabel klasik, angka ini akan dibulatkan menjadi $1$, sehingga **terjadi error/hilang akurasi (*loss of significance*)**.
*   Jika menggunakan **Sudut Paruh (Sinus)**, nilai $\\sin(0^\\circ) = 0$. Perubahan kecil pada sudut dekat $0$ sangat sensitif pada fungsi sinus. Oleh karena itu, rumus sudut paruh memberikan akurasi yang jauh lebih presisi untuk jarak pandang yang berdekatan. Menariknya, sistem GPS modern di dalam *smartphone* kita pun masih beroperasi menggunakan landasan rumus ini!

**4. Menghilangkan Ambiguitas Kuadran (Kasus Waktu Salat)**

Dalam menghitung **Sudut Waktu Matahari (*Hour Angle*)** untuk jadwal salat (terutama waktu Ashar dan Isya/Subuh), kita sering mencari nilai sudut $H$ ketika ketinggian matahari ($h$) diketahui.
Jika kita memecahkannya dengan Aturan Sinus biasa, kita akan bertemu ambiguitas (karena $\\sin 30^\\circ = \\sin 150^\\circ$, kita bingung mana hasil yang benar). Dengan menggunakan rumus **Kosinus Sudut Paruh** atau **Tangen Sudut Paruh**, rentang jawabannya menjadi terukur secara absolut dan membuang jawaban ganda yang salah secara astronomis.
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
st.subheader("3. Laboratorium Spasial 3D: Bedah Detail Sistem Koordinat & Glosarium Istilah")
st.info("💡 **Petunjuk:** Pahami penjelasan istilah di bawah, lalu pilih sistem koordinat untuk melihat simulasinya secara spasial.")

# Penjelasan/Glosarium Istilah Koordinat
with st.expander("📖 Glosarium & Penjelasan Istilah Penting dalam Sistem Koordinat"):
    st.markdown("""
    Sebelum mengoperasikan simulasi 3D, berikut adalah definisi dan **kegunaan praktis** dari istilah-istilah utama yang digunakan dalam berbagai sistem koordinat astronomi dan ilmu falak:
    
    1. **Zenith ($Z$) & Nadir ($N'$)**
       * *Definisi:* Zenith adalah titik di bola langit yang tepat berada di atas kepala pengamat; sebaliknya, Nadir adalah titik yang tepat berada di bawah kaki pengamat.
       * *Kegunaan:* Sebagai sumbu vertikal utama dalam pengamatan astronomi lokal.
    
    2. **Azimuth ($A$)**
       * *Definisi:* Sudut arah horisontal yang diukur dari titik Utara (atau Selatan) ke arah timur sepanjang lingkaran horizon (0° hingga 360°).
       * *Kegunaan:* Menentukan arah kompas suatu objek di langit dari posisi pengamat. Dalam **Ilmu Falak**, nilai Azimuth kiblat sangat krusial untuk menentukan arah hadap bangunan masjid/surau menghadap Ka'bah.
    
    3. **Altitude / Tinggi Bintang ($h$)**
       * *Definisi:* Sudut vertikal ketinggian benda langit diukur dari bidang horizon ke arah atas (0° hingga 90°).
       * *Kegunaan:* Mengetahui seberapa tinggi posisi matahari atau bintang di atas cakrawala (misalnya untuk menentukan waktu salat seperti tergelincirnya matahari untuk zuhur).
    
    4. **Deklinasi ($\\delta$)**
       * *Definisi:* Lintang benda langit pada bola langit, diukur utara (+) atau selatan (-) dari ekuator langit (analog dengan garis lintang di bumi).
       * *Kegunaan:* Mengetahui posisi lintang objek tata surya/bintang di bola langit secara global tanpa terikat lokasi pengamat di bumi.
    
    5. **Asensio Rekta / Right Ascension ($\\alpha$)**
       * *Definisi:* Bujur langit yang diukur dari **Titik Aries ($\\gamma$)** ke arah timur sepanjang ekuator langit.
       * *Kegunaan:* Menentukan koordinat horizontal-waktu bintang secara universal di bola langit.
    
    6. **Lintang ($\\phi$) & Bujur ($\\lambda$) Geografis**
       * *Definisi:* Koordinat posisi absolut suatu kota atau titik di permukaan bumi relatif terhadap garis Ekuator (Lintang 0°) dan Meridian Utama Greenwich (Bujur 0°).
       * *Kegunaan:* **Fondasi mutlak** dalam perhitungan ilmu falak (seperti penentuan arah kiblat dan waktu salat) karena menghubungkan posisi pengamat di permukaan bumi dengan posisi astronomis benda langit.
    """)

pilihan_sistem = st.selectbox(
    "Pilih Sistem Koordinat Astronomi & Geografis:",
    [
        "A. Sistem Koordinat Horizon (Lokal)", 
        "B. Sistem Koordinat Ekuator (Global / Langit)", 
        "C. Sistem Koordinat Ekliptika (Tata Surya)",
        "D. Sistem Koordinat Geografis (Terestrial / Kota & Kiblat)"
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

elif pilihan_sistem == "C. Sistem Koordinat Ekliptika (Tata Surya)":
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

else:
    st.markdown("""
    #### D. Sistem Koordinat Geografis (Terestrial / Kota & Kiblat)
    * **Bidang Referensi:** Ekuator Bumi (Lintang 0°) dan Meridian Utama Greenwich (Bujur 0°).
    * **Kegunaan Falak:** Menentukan posisi absolut suatu kota di permukaan bumi. Ini adalah fondasi utama dalam menghitung **Arah Kiblat** dan jarak antar kota menggunakan segitiga bola (misal: segitiga antara Kota Pengamat, Ka'bah di Mekkah, dan Kutub Utara Bumi).
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        lat_kota = st.slider("Lintang Kota (Latitude, φ) [Derajat]", -90, 90, -7, step=1, help="Posisi utara (+) atau selatan (-) dari ekuator")
    with col2:
        lon_kota = st.slider("Bujur Kota (Longitude, λ) [Derajat]", -180, 180, 110, step=1, help="Posisi timur (+) atau barat (-) dari Greenwich")
        
    # Koordinat Mekkah (Ka'bah) sebagai referensi kiblat utama
    lat_mecca = 21.4225
    lon_mecca = 39.8262
    
    # Konversi ke radian untuk pemetaan vektor 3D
    lat_r = np.radians(lat_kota)
    lon_r = np.radians(lon_kota)
    
    x_kota = np.cos(lat_r) * np.cos(lon_r)
    y_kota = np.cos(lat_r) * np.sin(lon_r)
    z_kota = np.sin(lat_r)
    
    lat_m_r = np.radians(lat_mecca)
    lon_m_r = np.radians(lon_mecca)
    x_m = np.cos(lat_m_r) * np.cos(lon_m_r)
    y_m = np.cos(lat_m_r) * np.sin(lon_m_r)
    z_m = np.sin(lat_m_r)
    
    t = np.linspace(0, 2 * np.pi, 100)
    fig_coord.add_trace(go.Scatter3d(x=np.cos(t), y=np.sin(t), z=np.zeros_like(t), mode='lines', line=dict(color='blue', width=3), name='Ekuator Bumi (0°)'))
    
    fig_coord.add_trace(go.Scatter3d(x=[0, x_kota], y=[0, y_kota], z=[0, z_kota], mode='lines', line=dict(color='orange', width=4), name='Vektor Lokasi Kota'))
    fig_coord.add_trace(go.Scatter3d(x=[0, x_m], y=[0, y_m], z=[0, z_m], mode='lines', line=dict(color='purple', width=4, dash='dash'), name='Vektor Ka\'bah (Mekkah)'))
    
    add_mini_earth(fig_coord)
    
    fig_coord.add_trace(go.Scatter3d(
        x=[x_kota, x_m], y=[y_kota, y_m], z=[z_kota, z_m],
        mode='text+markers',
        text=[f'Kota Anda (Lat: {lat_kota}°, Lon: {lon_kota}°)', 'Ka\'bah / Mekkah (21.4°N, 39.8°E)'],
        marker=dict(size=[8, 8], color=['orange', 'purple']),
        textfont=dict(size=11)
    ))
    fig_coord.update_layout(title=f"Simulasi 3D: Koordinat Geografis & Referensi Arah Kiblat")

fig_coord.update_layout(
    scene=dict(xaxis_title='Sumbu X', yaxis_title='Sumbu Y', zaxis_title='Sumbu Z'),
    width=850, height=550,
    margin=dict(l=0, r=0, b=0, t=40)
)

st.plotly_chart(fig_coord, use_container_width=True)
