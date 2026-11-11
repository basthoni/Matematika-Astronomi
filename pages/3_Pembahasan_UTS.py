import streamlit as st
import math
import numpy as np

st.set_page_config(page_title="Pembahasan UTS", page_icon="📝", layout="wide")

st.title("📝 Pembahasan UTS Matematika Astronomi")
st.markdown("Masukkan Nomor Presensi Anda untuk melihat langkah penyelesaian dan kunci jawaban spesifik sesuai variabel soal Anda.")
st.divider()

# ==========================================
# INPUT NOMOR PRESENSI
# ==========================================
col_input, _ = st.columns([1, 2])
with col_input:
    x = st.number_input("Masukkan Nomor Presensi [ X ]", min_value=1, max_value=100, value=5, step=1)

st.info(f"Kunci Jawaban di bawah ini dikalkulasi secara otomatis menggunakan variabel **[ X ] = {x}**.")

# ==========================================
# TABS UNTUK MASING-MASING SOAL
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
    
    st.markdown(f"""
    **Data Diketahui:**
    * Lintang ($L$) = -7° 00'
    * Deklinasi ($d$) = -(10 + {x})° = {d_deg}°
    
    **Penjabaran Rumus Napier:**
    Karena bintang berada di ufuk, Jarak Zenith ($z$) = 90°. Berdasarkan aturan Napier Kuadran:
    """)
    
    st.latex(r"\cos(t) = -\tan(L) \times \tan(d)")
    
    st.markdown(f"""
    **Langkah Perhitungan:**
    * $\\tan(-7^\circ) = {tan_L:.5f}$
    * $\\tan({d_deg}^\circ) = {tan_d:.5f}$
    * $\\cos(t) = - ({tan_L:.5f} \\times {tan_d:.5f})$
    * $\\cos(t) = {cos_t:.5f}$
    
    **Hasil Akhir Sudut Jam ($t$):**
    """)
    st.success(f"**t = {t_deg:.5f}°** (atau {t_jam:.5f} Jam)")

with tab2:
    st.header("Soal 2: Segitiga P-Z-K (Jarak & Azimuth)")
    
    L_z = -7.25 # -7° 15'
    B_z = 109 + x
    L_k = 21.41667 # 21° 25' LU
    B_k = 39.81667 # 39° 49' BT
    
    delta_B = B_z - B_k
    
    L_z_rad = math.radians(L_z)
    L_k_rad = math.radians(L_k)
    delta_B_rad = math.radians(delta_B)
    
    # Hitung Jarak
    sin_Lz = math.sin(L_z_rad)
    sin_Lk = math.sin(L_k_rad)
    cos_Lz = math.cos(L_z_rad)
    cos_Lk = math.cos(L_k_rad)
    cos_dB = math.cos(delta_B_rad)
    
    cos_c = (sin_Lz * sin_Lk) + (cos_Lz * cos_Lk * cos_dB)
    c_deg = math.degrees(math.acos(cos_c))
    jarak_km = c_deg * 111.11 # konversi derajat ke km
    
    # Hitung Azimuth
    sin_dB = math.sin(delta_B_rad)
    tan_Lk = math.tan(L_k_rad)
    
    pembilang = sin_dB
    penyebut = (cos_Lz * tan_Lk) - (sin_Lz * cos_dB)
    tan_Q = pembilang / penyebut
    Q_deg = math.degrees(math.atan(tan_Q))
    
    # Konversi ke UTS (Utara Sejati)
    if Q_deg < 0:
        Q_deg += 180
    UTS = 360 - Q_deg
    
    st.markdown(f"""
    **Data Diketahui:**
    * Masjid (Z): $L_Z$ = -7° 15', $B_Z$ = {B_z}° BT
    * Makkah (K): $L_K$ = 21° 25' LU, $B_K$ = 39° 49' BT
    * Selisih Bujur ($\Delta B$) = {delta_B:.5f}°
    
    **1. Menghitung Jarak (c)**
    """)
    st.latex(r"\cos(c) = \sin(L_Z)\sin(L_K) + \cos(L_Z)\cos(L_K)\cos(\Delta B)")
    st.markdown(f"""
    * $\\cos(c) = ({sin_Lz:.5f} \\times {sin_Lk:.5f}) + ({cos_Lz:.5f} \\times {cos_Lk:.5f} \\times {cos_dB:.5f})$
    * $\\cos(c) = {cos_c:.5f}$
    * $c = {c_deg:.5f}^\circ$
    """)
    st.success(f"**Jarak ke Makkah** = {c_deg:.5f} × 111.11 = **{jarak_km:.2f} km**")
    
    st.markdown("**2. Menghitung Azimuth (Q)**")
    st.latex(r"\tan(Q) = \frac{\sin(\Delta B)}{\cos(L_Z)\tan(L_K) - \sin(L_Z)\cos(\Delta B)}")
    st.markdown(f"""
    * Pembilang = ${sin_dB:.5f}$
    * Penyebut = $({cos_Lz:.5f} \\times {tan_Lk:.5f}) - ({sin_Lz:.5f} \\times {cos_dB:.5f}) = {penyebut:.5f}$
    * $\\tan(Q) = {tan_Q:.5f}$
    * $Q = {Q_deg:.5f}^\circ$ (U-B)
    """)
    st.success(f"**Azimuth Utara Sejati (UTS)** = 360° - {Q_deg:.5f}° = **{UTS:.5f}°**")

with tab3:
    st.header("Soal 3: Segitiga P-Z-M (Waktu Maghrib)")
    
    d_deg = -(15 + (x / 60.0))
    L_deg = -6.5 # -6° 30'
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
    
    # Konversi desimal jam ke H:M:S
    jam = int(t_jam)
    sisa_menit = (t_jam - jam) * 60
    menit = int(sisa_menit)
    detik = int(round((sisa_menit - menit) * 60))
    
    # Tambah ke Waktu Zuhur (11:45:00)
    total_detik_maghrib = (11 * 3600 + 45 * 60) + (jam * 3600 + menit * 60 + detik)
    m_jam = (total_detik_maghrib // 3600) % 24
    m_menit = (total_detik_maghrib % 3600) // 60
    m_detik = total_detik_maghrib % 60
    
    st.markdown(f"""
    **Data Diketahui:**
    * Deklinasi ($d$) = -15° {x}' = {d_deg:.5f}°
    * Lintang ($L$) = -6° 30'
    * Tinggi Matahari ($h$) = -1°
    * Waktu Zuhur = 11:45:00 WIB
    
    **Penjabaran Rumus Aturan Kosinus:**
    """)
    st.latex(r"\cos(t) = \frac{\sin(h) - \sin(L)\sin(d)}{\cos(L)\cos(d)}")
    
    st.markdown(f"""
    **Langkah Perhitungan:**
    * $\\cos(t) = \frac{{{sin_h:.5f} - ({sin_L:.5f} \\times {sin_d:.5f})}}{{{cos_L:.5f} \\times {cos_d:.5f}}}$
    * $\\cos(t) = {cos_t:.5f}$
    * $t = {t_deg:.5f}^\circ$
    
    Konversi $t$ ke satuan Jam:
    $t = {t_deg:.5f} \\div 15 = {t_jam:.5f}$ Jam (**{jam} Jam {menit} Menit {detik} Detik**)
    """)
    
    st.success(f"**Waktu Maghrib** = 11:45:00 + {jam:02d}:{menit:02d}:{detik:02d} = **{m_jam:02d}:{m_menit:02d}:{m_detik:02d} WIB**")
