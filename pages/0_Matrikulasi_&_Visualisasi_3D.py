import streamlit as st
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Matrikulasi & Simulasi 3D", page_icon="🌐", layout="wide")

st.markdown("""
<style>
div[data-testid="stMarkdownContainer"] p {
    text-align: justify;
}
</style>
""", unsafe_allow_html=True)

st.title("MODUL MATRIKULASI & VISUALISASI SPASIAL")
st.header("Prasyarat Matematika & Geometri Bola untuk Astronomi")
st.divider()

matrikulasi_mendalam = r"""
### A. Pengantar Filosofis: Geometri Bidang (Euclidean) vs Geometri Bola (Spherical)
Sebelum mahasiswa mendalami penurunan analitis dari W.M. Smart, penguasaan terhadap fondasi geometri ruang dan trigonometri lanjut mutlak diperlukan untuk mencegah disorientasi konseptual:
1. **Garis Lurus vs Lingkaran Besar:** Dalam geometri datar, jarak terdekat antara dua titik adalah garis lurus. Dalam astronomi bola (permukaan bola), karena pengamat berada di pusat dan mengamati objek di cangkang bola langit, jarak terdekat antara dua titik di permukaan bola adalah busur dari **lingkaran besar** (*great circle*), yaitu irisan bidang yang melewati pusat bola ($O$).
2. **Jumlah Sudut Segitiga:** 
   - Pada bidang datar, total sudut segitiga selalu tepat $180^\circ$ ($\pi$ radian).
   - Pada segitiga bola, total sudut $\alpha + \beta + \gamma$ **selalu lebih besar dari $180^\circ$** (dikenal sebagai kelebihan bola / *spherical excess*).

### B. Review Identitas Trigonometri & Fungsi Sekawan
Buku-buku klasik astronomi bola sangat sering menggunakan fungsi kebalikan (*reciprocal trigonometric functions*) yang jarang dipakai di kalkulus modern:
* **Secan & Cosecan:** $\sec \theta = \frac{1}{\cos \theta}$, $\text{cosec } \theta = \frac{1}{\sin \theta}$
* **Cotangen:** $\cot \theta = \frac{\cos \theta}{\sin \theta} = \frac{1}{\tan \theta}$
* **Identitas Selisih Kosinus:**
  $$
  \cos(b - c) = \cos b \cos c + \sin b \sin c
  $$
* **Hubungan Sudut Paruh:**
  $$
  \cos A = 1 - 2 \sin^2 \left(\frac{A}{2}\right)
  $$

### C. Sistem Koordinat Sudut & Waktu dalam Falak
Dalam perhitungan astronomi, satuan sudut tidak hanya dinyatakan dalam derajat desimal, tetapi juga dikonversi ke dalam sistem sexagesimal (derajat, menit, detik arcus) serta sistem waktu (Jam, Menit, Detik waktu):
$$
24^\text{h} = 360^\circ \implies 1^\text{h} = 15^\circ, \quad 1^\text{m} = 15', \quad 1^\text{s} = 15''
$$
"""
st.markdown(matrikulasi_mendalam, unsafe_allow_html=True)
st.divider()

st.subheader("🌐 Simulasi Interaktif 3D: Bola Langit & Lingkaran Besar")
st.info("💡 **Petunjuk:** Putar bola 3D di bawah ini menggunakan tetikus (klik & geser di laptop) atau usap layar (di HP) untuk mengamati struktur bola langit, sumbu kutub vertikal, serta bidang lingkaran besar yang memotong pusat bola.")

# Membuat plot 3D menggunakan Plotly (Responsif untuk HP & Laptop)
fig = go.Figure()

# 1. Permukaan Bola Transparan
u = np.linspace(0, 2 * np.pi, 40)
v = np.linspace(0, np.pi, 40)
x_sphere = np.outer(np.cos(u), np.sin(v))
y_sphere = np.outer(np.sin(u), np.sin(v))
z_sphere = np.outer(np.ones(np.size(u)), np.cos(v))

fig.add_trace(go.Surface(
    x=x_sphere, y=y_sphere, z=z_sphere, 
    colorscale='Teal', 
    opacity=0.12, 
    showscale=False,
    name='Bola Langit'
))

# 2. Lingkaran Besar (Great Circle di bidang XY / Ekuator)
theta = np.linspace(0, 2 * np.pi, 100)
fig.add_trace(go.Scatter3d(
    x=np.cos(theta), y=np.sin(theta), z=np.zeros_like(theta),
    mode='lines',
    line=dict(color='crimson', width=6),
    name='Lingkaran Besar (Great Circle)'
))

# 3. Titik Pusat O, Kutub P dan Q
fig.add_trace(go.Scatter3d(
    x=[0, 0, 0], y=[0, 0, 0], z=[0, 1, -1],
    mode='text+markers',
    text=['Pusat (O)', 'Kutub Utara (P)', 'Kutub Selatan (Q)'],
    marker=dict(size=7, color='navy'),
    textfont=dict(color='navy', size=13),
    name='Sumbu Bola'
))

fig.update_layout(
    title="Visualisasi Interaktif Ruang Bola Langit 3D",
    scene=dict(
        xaxis_title='Sumbu X',
        yaxis_title='Sumbu Y',
        zaxis_title='Sumbu Z',
    ),
    height=450,
    margin=dict(l=0, r=0, b=0, t=40)
)

st.plotly_chart(fig, use_container_width=True)
