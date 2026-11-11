import streamlit as st
import math
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="Pembahasan UTS", page_icon="📝", layout="wide")

st.title("📝 Pembahasan UTS Matematika Astronomi")
st.markdown("Masukkan Nomor Presensi Anda untuk melihat simulasi 3D bola langit, bola bumi di pusat, langkah penyelesaian, dan proses penurunan rumus lengkap.")
st.divider()

# ==========================================
# FUNGSI HELPER UNTUK GRAFIK 3D BOLA LANGIT & BUMI
# ==========================================
def slerp(p0, p1, num=50):
    """Fungsi interpolasi slerp agar garis menempel melengkung di permukaan bola"""
    p0 = np.array(p0)
    p1 = np.array(p1)
    norm_p0 = np.linalg.norm(p0)
    norm_p1 = np.linalg.norm(p1)
    if norm_p0 == 0 or norm_p1 == 0:
        return np.linspace(p0, p1, num)
    dot = np.dot(p0, p1) / (norm_p0 * norm_p1)
    dot = np.clip(dot, -1.0, 1.0)
    omega = np.arccos(dot)
    if abs(omega) < 1e-3:
        return np.linspace(p0, p1, num)
    t = np.linspace(0, 1, num)
    p = np.sin((1 - t) * omega) / np.sin(omega) * p0[:, None] + np.sin(t * omega) / np.sin(omega) * p1[:, None]
    return p.T

def plot_horizon_sphere(L_deg, alt_deg, A_deg, obj_name):
    fig = go.Figure()
    
    # 1. Base Sphere (Bola Langit Transparan R = 1.0)
    u = np.linspace(0, 2 * np.pi, 40)
    v = np.linspace(0, np.pi, 40)
    x_sph = np.outer(np.cos(u), np.sin(v))
    y_sph = np.outer(np.sin(u), np.sin(v))
    z_sph = np.outer(np.ones(np.size(u)), np.cos(v))
    fig.add_surface(x=x_sph, y=y_sph, z=z_sph, opacity=0.08, showscale=False, colorscale='Blues', name='Bola Langit')
    
    # 2. Bola Bumi Kecil di Pusat (R = 0.25)
    r_earth = 0.25
    x_earth = r_earth * x_sph
    y_earth = r_earth * y_sph
    z_earth = r_earth * z_sph
    fig.add_surface(x=x_earth, y=y_earth, z=z_earth, opacity=0.7, showscale=False, colorscale='YlGnBu', name='Bumi (Pusat)')
    
    # 3. Horizon (Hz / Ufuk)
    theta = np.linspace(0, 2*np.pi, 100)
    fig.add_trace(go.Scatter3d(x=np.cos(theta), y=np.sin(theta), z=np.zeros_like(theta),
                               mode='lines', line=dict(color='lime', width=4), name='Horizon (Hz)'))
                               
    # 4. Ekuator Langit (Eq)
    L_rad = np.radians(L_deg)
    alpha = np.linspace(0, 2*np.pi, 100)
    x_eq = -np.sin(L_rad) * np.sin(alpha)
    y_eq = np.cos(alpha)
    z_eq = np.cos(L_rad) * np.sin(alpha)
    fig.add_trace(go.Scatter3d(x=x_eq, y=y_eq, z=z_eq,
                               mode='lines', line=dict(color='blue', width=4, dash='dash'), name='Ekuator Langit (Eq)'))

    # 5. Zenith & Arah Mata Angin
    Z = np.array([0, 0, 1])
    fig.add_trace(go.Scatter3d(x=[Z[0]], y=[Z[1]], z=[Z[2]], mode='markers+text', marker=dict(color='lime', size=5), text=['Zenith (Z)'], textposition='top center', name='Zenith (Z)'))
    fig.add_trace(go.Scatter3d(x=[1, 0, -1, 0], y=[0, 1, 0, -1], z=[0, 0, 0, 0], mode='text', text=['Utara', 'Timur', 'Selatan', 'Barat'], textposition='bottom center', name='Mata Angin'))
    
    # 6. Penyesuaian Kutub (P) berdasarkan Lintang
    if L_deg >= 0:
        P = np.array([np.cos(L_rad), 0, np.sin(L_rad)])
        pole_name = "NCP (P)"
    else:
        P = np.array([-np.cos(L_rad), 0, -np.sin(L_rad)])
        pole_name = "SCP (P)"
        
    fig.add_trace(go.Scatter3d(x=[P[0]], y=[P[1]], z=[P[2]], mode='markers+text', marker=dict(color='red', size=6), text=[pole_name], textposition='top left', name='Kutub (P)'))
    
    # 7. Posisi Objek (Bintang/Matahari)
    alt_rad = np.radians(alt_deg)
    A_rad = np.radians(A_deg)
    M = np.array([np.cos(alt_rad) * np.cos(A_rad), np.cos(alt_rad) * np.sin(A_rad), np.sin(alt_rad)])
    fig.add_trace(go.Scatter3d(x=[M[0]], y=[M[1]], z=[M[2]], mode='markers+text', marker=dict(color='orange', size=8), text=[obj_name], textposition='middle left', name=obj_name))
    
    # 8. Sisi Segitiga Bola Melengkung (Slerp) P-Z-M
    s_pz = slerp(P, Z)
    s_pm = slerp(P, M)
    s_zm = slerp(Z, M)
    
    fig.add_trace(go.Scatter3d(x=s_pz[:,0], y=s_pz[:,1], z=s_pz[:,2], mode='lines', line=dict(color='yellow', width=4), name='Sisi P-Z (90-L)'))
    fig.add_trace(go.Scatter3d(x=s_pm[:,0], y=s_pm[:,1], z=s_pm[:,2], mode='lines', line=dict(color='magenta', width=4), name='Sisi P-M (90-d)'))
    fig.add_trace(go.Scatter3d(x=s_zm[:,0], y=s_zm[:,1], z=s_zm[:,2], mode='lines', line=dict(color='cyan', width=4), name='Sisi Z-M (Jarak Zenith)'))
    
    # Pengaturan Sudut Pandang Kamera 3D menyerupai Buku Teks
    fig.update_layout(
        scene=dict(
            xaxis_visible=False, yaxis_visible=False, zaxis_visible=False,
            camera=dict(
                eye=dict(x=1.5, y=-1.5, z=1.2)
            )
        ), 
        margin=dict(l=0, r=0, b=0, t=0), 
        height=450
    )
    return fig

# ==========================================
# INPUT NOMOR PRESENSI
# ==========================================
col_input, _ = st.columns([1, 2])
with col_input:
    x = st.number_input("Masukkan Nomor Presensi [ X ]", min_value=1, max_value=100, value=5, step=1)

st.info(f"Semua perhitungan, rumus, dan simulasi 3D dikalkulasi otomatis menggunakan variabel **[ X ] = {x}**.")

# ==========================================
# TABS SOAL
# ==========================================
tab1, tab2, tab3 = st.tabs(["Soal 1: Napier Kuadran", "Soal 2: Arah Kiblat", "Soal 3: Waktu Maghrib"])

with tab1:
    st.header("Soal 1: Bintang di Ufuk Barat")
    
    L_deg = -7.0
    d_deg = -(10 + x)
    
    L_rad = math.radians(L_deg)
    d_rad = math.radians(d_deg)
    tan_L = math.tan(L_rad)
    tan_d = math.tan(d_rad)
    cos_t = -(tan_L * tan_d)
    t_deg = math.degrees(math.acos(cos_t)) if abs(cos_t) <= 1 else 0
    t_jam = t_deg / 15.0
    
    cos_A = math.sin(d_rad) / math.cos(L_rad)
    A_deg = 360 - math.degrees(math.acos(cos_A))
    
    col1a, col1b = st.columns([1, 1])
    with col1a:
        st.markdown(f"**Data Presensi [ X ] = {x}**")
        st.markdown(f"* Lintang ($L$) = -7° 00'\n* Deklinasi ($d$) = {d_deg}°")
        st.markdown("**Rumus Napier Kuadran (z = 90°):**")
        st.latex(r"\cos(t) = -\tan(L) \times \tan(d)")
        
        st.markdown("**Langkah Perhitungan:**")
        st.markdown(f"* $\\tan(-7^\circ) = {tan_L:.5f}$")
        st.markdown(f"* $\\tan({d_deg}^\circ) = {tan_d:.5f}$")
        st.latex(r"\cos(t) = - (" + f"{tan_L:.5f}" + r" \times " + f"{tan_d:.5f}" + r")")
        st.markdown(f"* $\\cos(t) = {cos_t:.5f}$")
        
        st.success(f"**Hasil Akhir Sudut Jam (t): {t_deg:.5f}°** (atau {t_jam:.5f} Jam)")
    
    with col1b:
        st.plotly_chart(plot_horizon_sphere(L_deg, 0.0, A_deg, "Bintang"), use_container_width=True)
        st.caption("Visualisasi 3D: Bola langit dengan replika Bumi kecil di pusatnya, menampilkan Horizon (Hz), Ekuator (Eq), dan Segitiga P-Z-M.")

    with st.expander("🔍 Proses Penurunan Rumus & Development (Soal 1)"):
        st.markdown(r"""
        **1. Konsep Dasar Segitiga Bola ($P-Z-M$):**
        * $P$ = Kutub Langit, $Z$ = Zenith pengamat, $M$ = Posisi Bintang.
        * Sisi $PZ = 90^\circ - L$ (Ko-lintang)
        * Sisi $PM = 90^\circ - d$ (Ko-deklinasi)
        * Sisi $ZM = z$ (Jarak Zenith)
        * Sudut di $P$ adalah Sudut Jam ($t$).

        **2. Penerapan Aturan Kosinus untuk Sisi:**
        Berdasarkan aturan kosinus umum pada segitiga bola:
        $$\cos(z) = \cos(90^\circ - L)\cos(90^\circ - d) + \sin(90^\circ - L)\sin(90^\circ - d)\cos(t)$$

        **3. Kondisi Khusus di Ufuk Barat ($z = 90^\circ$):**
        Karena bintang berada tepat di ufuk, maka jarak zenitnya $z = 90^\circ$, sehingga $\cos(90^\circ) = 0$:
        $$0 = \sin(L)\sin(d) + \cos(L)\cos(d)\cos(t)$$
        Pindahkan suku ke ruas kiri dan bagi dengan $\cos(L)\cos(d)$:
        $$\cos(t) = -\frac{\sin(L)\sin(d)}{\cos(L)\cos(d)} = -\tan(L)\tan(d)$$
        Rumus inilah yang digunakan untuk menghitung sudut jam $t$ saat bintang terbenam.
        """)

    st.divider()
    st.subheader("💡 Soal Pendalaman (Latihan Mandiri)")
    st.info("Coba hitung ulang secara manual: Bagaimana jika bintang ini diamati dari kota dengan lintang Utara (misal L = +7°)? Apakah bintang ini masih bisa terlihat terbenam, atau menjadi bintang Sirkumpolar?")

with tab2:
    st.header("Soal 2: Segitiga P-Z-K (Arah Kiblat)")
    
    L_z = -7.25 
    B_z = 109 + x
    L_k = 21.41667 
    B_k = 39.81667 
    delta_B = B_z - B_k
    
    L_z_rad = math.radians(L_z)
    L_k_rad = math.radians(L_k)
    delta_B_rad = math.radians(delta_B)
    
    sin_Lz = math.sin(L_z_rad)
    sin_Lk = math.sin(L_k_rad)
    cos_Lz = math.cos(L_z_rad)
    cos_Lk = math.cos(L_k_rad)
    cos_dB = math.cos(delta_B_rad)
    
    cos_c = (sin_Lz * sin_Lk) + (cos_Lz * cos_Lk * cos_dB)
    c_deg = math.degrees(math.acos(cos_c))
    jarak_km = c_deg * 111.11 
    
    sin_dB = math.sin(delta_B_rad)
    tan_Lk = math.tan(L_k_rad)
    pembilang = sin_dB
    penyebut = (cos_Lz * tan_Lk) - (sin_Lz * cos_dB)
    tan_Q = pembilang / penyebut
    Q_deg = abs(math.degrees(math.atan(tan_Q)))
    UTS = 360 - Q_deg
    
    col2a, col2b = st.columns([1, 1])
    with col2a:
        st.markdown(f"**Data Presensi [ X ] = {x}**")
        st.markdown(f"* Masjid (Z): $L_Z = -7^\circ 15', B_Z = {B_z}^\circ$ BT")
        st.markdown(f"* Makkah (K): $L_K = 21^\circ 25'$ LU, $B_K = 39^\circ 49'$ BT")
        st.markdown(f"* Selisih Bujur ($\\Delta B$) = {delta_B:.5f}°")
        
        st.markdown("**1. Hitung Jarak**")
        st.latex(r"\cos(c) = \sin(L_Z)\sin(L_K) + \cos(L_Z)\cos(L_K)\cos(\Delta B)")
        st.latex(r"\cos(c) = (" + f"{sin_Lz:.5f}" + r")(" + f"{sin_Lk:.5f}" + r") + (" + f"{cos_Lz:.5f}" + r")(" + f"{cos_Lk:.5f}" + r")(" + f"{cos_dB:.5f}" + r")")
        st.success(f"**Jarak ke Makkah = {jarak_km:.2f} km**")
        
        st.markdown("**2. Hitung Azimuth**")
        st.latex(r"\tan(Q) = \frac{\sin(\Delta B)}{\cos(L_Z)\tan(L_K) - \sin(L_Z)\cos(\Delta B)}")
        st.latex(r"\tan(Q) = \frac{ " + f"{sin_dB:.5f}" + r" }{ " + f"{penyebut:.5f}" + r" } = " + f"{tan_Q:.5f}")
        st.success(f"**Azimuth (UTS) = 360° - {Q_deg:.5f}° = {UTS:.5f}°**")
    
    with col2b:
        fig_globe = go.Figure(go.Scattergeo(
            lat=[L_z, L_k], lon=[B_z, B_k], mode='markers+lines',
            line=dict(width=3, color='red'), marker=dict(size=8, color='blue'),
            text=['Lokasi Masjid', "Ka'bah (Makkah)"], textposition='top center'
        ))
        fig_globe.update_geos(projection_type="orthographic", showcountries=True, center=dict(lat=10, lon=70))
        fig_globe.update_layout(margin=dict(l=0, r=0, t=0, b=0), height=400)
        st.plotly_chart(fig_globe, use_container_width=True)
        st.caption("Proyeksi Globe 3D: Garis merah menunjukkan Jarak Terpendek (Great Circle) Arah Kiblat.")

    with st.expander("🔍 Proses Penurunan Rumus & Development (Soal 2)"):
        st.markdown(r"""
        **1. Konsep Segitiga Bola Terestrial ($P-Z-K$):**
        * $P$ = Kutub Utara Bumi, $Z$ = Posisi Masjid, $K$ = Kota Makkah (Ka'bah).
        * Sisi $PZ = 90^\circ - L_Z$ (Co-lintang Masjid)
        * Sisi $PK = 90^\circ - L_K$ (Co-lintang Makkah)
        * Sudut antara kedua sisi di kutub $P$ adalah Selisih Bujur ($\Delta B = B_Z - B_K$).

        **2. Penurunan Rumus Jarak ($c$):**
        Menggunakan Aturan Kosinus Sisi pada segitiga $PZK$:
        $$\cos(c) = \cos(PZ)\cos(PK) + \sin(PZ)\sin(PK)\cos(\Delta B)$$
        Karena $\cos(90^\circ - L) = \sin(L)$ dan $\sin(90^\circ - L) = \cos(L)$, persamaannya menjadi:
        $$\cos(c) = \sin(L_Z)\sin(L_K) + \cos(L_Z)\cos(L_K)\cos(\Delta B)$$

        **3. Penurunan Rumus Azimuth Kiblat ($Q$):**
        Menggunakan rumus kotangen/aturan empat bagian unsur segitiga bola untuk mencari sudut arah kiblat terhadap utara:
        $$\tan(Q) = \frac{\sin(\Delta B)}{\cos(L_Z)\tan(L_K) - \sin(L_Z)\cos(\Delta B)}$$
        Hasil sudut $Q$ dikonversi menjadi Azimuth Utara Sejati ($\text{UTS} = 360^\circ - Q$).
        """)

    st.divider()
    st.subheader("💡 Soal Pendalaman (Latihan Mandiri)")
    st.info("Coba hitung Arah Kiblat untuk masjid di Jayapura (Papua) yang berada di Bujur 140° BT. Bandingkan nilai Azimuth-nya dengan Semarang. Apakah bergeser semakin ke Utara atau semakin ke Barat?")

with tab3:
    st.header("Soal 3: Waktu Maghrib (Segitiga P-Z-M)")
    
    d_deg = -(15 + (x / 60.0))
    L_deg = -6.5 
    h_deg = -1.0
    
    d_rad = math.radians(d_deg)
    L_rad = math.radians(L_deg)
    h_rad = math.radians(h_deg)
    
    sin_h = math.sin(h_rad)
    sin_L = math.sin(L_rad)
    sin_d = math.sin(d_rad)
    cos_L = math.cos(L_rad)
    cos_d = math.cos(d_rad)
    
    cos_t = (sin_h - (sin_L * sin_d)) / (cos_L * cos_d)
    t_deg = math.degrees(math.acos(cos_t))
    t_jam = t_deg / 15.0
    
    jam = int(t_jam)
    sisa_menit = (t_jam - jam) * 60
    menit = int(sisa_menit)
    detik = int(round((sisa_menit - menit) * 60))
    
    total_detik_maghrib = (11 * 3600 + 45 * 60) + (jam * 3600 + menit * 60 + detik)
    m_jam = (total_detik_maghrib // 3600) % 24
    m_menit = (total_detik_maghrib % 3600) // 60
    m_detik = total_detik_maghrib % 60
    
    cos_A = (sin_d - (sin_L * sin_h)) / (cos_L * math.cos(h_rad))
    A_deg = 360 - math.degrees(math.acos(cos_A))

    col3a, col3b = st.columns([1, 1])
    with col3a:
        st.markdown(f"**Data Presensi [ X ] = {x}**")
        st.markdown(f"* Deklinasi ($d$) = {d_deg:.5f}°\n* Lintang ($L$) = -6° 30'\n* Tinggi Maghrib ($h$) = -1°")
        
        st.markdown("**Penjabaran Aturan Kosinus:**")
        st.latex(r"\cos(t) = \frac{\sin(h) - \sin(L)\sin(d)}{\cos(L)\cos(d)}")
        
        st.markdown("**Langkah Perhitungan:**")
        st.latex(r"\cos(t) = \frac{ " + f"{sin_h:.5f} - ({sin_L:.5f} \\times {sin_d:.5f})" + r" }{ " + f"{cos_L:.5f} \\times {cos_d:.5f}" + r" }")
        st.markdown(f"* $\\cos(t) = {cos_t:.5f}$  --> $t = {t_deg:.5f}^\circ$")
        st.markdown(f"Konversi Jam: {t_deg:.5f} ÷ 15 = **{jam} Jam {menit} Menit {detik} Detik**")
        
        st.success(f"**Waktu Maghrib** = 11:45:00 + {jam:02d}:{menit:02d}:{detik:02d} = **{m_jam:02d}:{m_menit:02d}:{m_detik:02d} WIB**")

    with col3b:
        st.plotly_chart(plot_horizon_sphere(L_deg, -1.0, A_deg, "Matahari"), use_container_width=True)
        st.caption("Visualisasi 3D: Bola langit dengan bola bumi kecil di pusat, menampilkan Horizon (Hz), Ekuator (Eq), dan posisi Matahari (oranye).")

    with st.expander("🔍 Proses Penurunan Rumus & Development (Soal 3)"):
        st.markdown(r"""
        **1. Konsep Segitiga Bola Astronomis ($P-Z-M$):**
        * $P$ = Kutub Langit, $Z$ = Zenith, $M$ = Matahari.
        * Sisi $PZ = 90^\circ - L$ (Co-lintang pengamat)
        * Sisi $PM = 90^\circ - d$ (Co-deklinasi matahari)
        * Sisi $ZM = 90^\circ - h$ (Jarak zenith matahari saat tinggi $h$)

        **2. Penurunan Rumus Sudut Jam ($t$):**
        Menggunakan Aturan Kosinus untuk Sisi pada segitiga $PZM$ dengan sisi $ZM = 90^\circ - h$:
        $$\cos(90^\circ - h) = \cos(90^\circ - L)\cos(90^\circ - d) + \sin(90^\circ - L)\sin(90^\circ - d)\cos(t)$$
        Karena $\cos(90^\circ - h) = \sin(h)$, maka persamaannya menjadi:
        $$\sin(h) = \sin(L)\sin(d) + \cos(L)\cos(d)\cos(t)$$

        **3. Isolasi Variabel Sudut Jam ($t$):**
        $$\cos(t) = \frac{\sin(h) - \sin(L)\sin(d)}{\cos(L)\cos(d)}$$
        * Nilai $t$ dikonversi ke jam ($t / 15$).
        * Waktu Maghrib diperoleh dengan menambahkan selisih waktu tersebut terhadap Waktu Zuhur referensi (11:45:00 WIB).
        """)

    st.divider()
    st.subheader("💡 Soal Pendalaman (Latihan Mandiri)")
    st.info("Berdasarkan logika yang sama, coba hitung Waktu Terbit Matahari (Fajar/Syuruq). Jika saat terbit tinggi matahari juga diasumsikan h = -1° di ufuk Timur, jam berapakah matahari terbit jika dikurangkan dari Waktu Zuhur?")
