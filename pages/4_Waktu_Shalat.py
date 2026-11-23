import streamlit as st
import datetime
import json
import math
import urllib.request
import urllib.error
import numpy as np
import pandas as pd
import plotly.graph_objects as go

st.set_page_config(page_title="Perhitungan Waktu Shalat", page_icon="🕌", layout="wide")

st.title("🕌 Perhitungan & Komparasi Waktu Shalat")
st.markdown("Simulasi astronomi bola untuk memahami pengaruh perbedaan kriteria **Ashar, Subuh, dan Isya** terhadap sudut jam ($t$) dan jadwal waktu shalat standar.")
st.divider()

# ==========================================
# FUNGSI HELPER MATEMATIKA ASTRONOMI, 3D & GSHEET
# ==========================================
def slerp(p0, p1, num=50):
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

def estimasi_solar_params(tanggal_obj):
    """Menghitung estimasi Deklinasi (d) [derajat] dan Equation of Time (e) [menit] dari tanggal."""
    hari_ke = tanggal_obj.timetuple().tm_yday
    gamma = 2.0 * math.pi * (hari_ke - 1) / 365.0

    d_rad = (
        0.006918
        - 0.399912 * math.cos(gamma)
        + 0.070257 * math.sin(gamma)
        - 0.006758 * math.cos(2 * gamma)
        + 0.000907 * math.sin(2 * gamma)
        - 0.002697 * math.cos(3 * gamma)
        + 0.001480 * math.sin(3 * gamma)
    )
    d_deg = math.degrees(d_rad)

    eot_menit = 229.18 * (
        0.000075
        + 0.001868 * math.cos(gamma)
        - 0.032077 * math.sin(gamma)
        - 0.014615 * math.cos(2 * gamma)
        - 0.040849 * math.sin(2 * gamma)
    )
    return d_deg, eot_menit, hari_ke

def hitung_sudut_jam(L_deg, d_deg, h_deg):
    L_rad = math.radians(L_deg)
    d_rad = math.radians(d_deg)
    h_rad = math.radians(h_deg)
    cos_t = (math.sin(h_rad) - math.sin(L_rad) * math.sin(d_rad)) / (math.cos(L_rad) * math.cos(d_rad))
    if abs(cos_t) > 1.0:
        return None, cos_t
    t_deg = math.degrees(math.acos(cos_t))
    return t_deg, cos_t

def hitung_azimuth_matahari(L_deg, d_deg, h_deg, sisi_barat=True):
    L_rad = math.radians(L_deg)
    d_rad = math.radians(d_deg)
    h_rad = math.radians(h_deg)
    cos_A = (math.sin(d_rad) - math.sin(L_rad) * math.sin(h_rad)) / (math.cos(L_rad) * math.cos(h_rad))
    cos_A = np.clip(cos_A, -1.0, 1.0)
    A_raw = math.degrees(math.acos(cos_A))
    return 360.0 - A_raw if sisi_barat else A_raw

def format_jam_wib(jam_desimal):
    jam_desimal = jam_desimal % 24.0
    total_detik = int(round(jam_desimal * 3600))
    j = (total_detik // 3600) % 24
    m = (total_detik % 3600) // 60
    d = total_detik % 60
    return f"{j:02d}:{m:02d}:{d:02d}"

def format_durasi(t_deg):
    t_jam = t_deg / 15.0
    total_detik = int(round(t_jam * 3600))
    j = total_detik // 3600
    m = (total_detik % 3600) // 60
    d = total_detik % 60
    return f"{j:02d}j {m:02d}m {d:02d}d"

def format_selisih_menit_detik(jam_desimal):
    tanda = "-" if jam_desimal < 0 else "+"
    total_detik = int(round(abs(jam_desimal) * 3600))
    menit = total_detik // 60
    detik = total_detik % 60
    return f"{tanda}{menit}m {detik:02d}d"

def kirim_ke_gsheet(payload_dict):
    """Mengirim data percobaan mahasiswa ke Google Apps Script Web App jika dikonfigurasi di st.secrets."""
    webhook_url = st.secrets.get("gsheet_webhook_url", "").strip()
    if not webhook_url:
        return False, "URL Google Sheet belum dikonfigurasi pada st.secrets['gsheet_webhook_url']."
    try:
        data_bytes = json.dumps(payload_dict).encode("utf-8")
        req = urllib.request.Request(
            webhook_url,
            data=data_bytes,
            headers={"Content-Type": "application/json"},
            method="POST"
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            status_code = resp.getcode()
        if 200 <= status_code < 300:
            return True, "Data percobaan berhasil dicatat ke Google Sheets."
        return False, f"Respons server tidak terduga (HTTP {status_code})."
    except (urllib.error.URLError, TimeoutError, Exception) as exc:
        return False, f"Gagal mengirim ke Google Sheets: {exc}"

def plot_perbandingan_3d(L_deg, titik_list):
    fig = go.Figure()

    u = np.linspace(0, 2 * np.pi, 40)
    v = np.linspace(0, np.pi, 40)
    x_sph = np.outer(np.cos(u), np.sin(v))
    y_sph = np.outer(np.sin(u), np.sin(v))
    z_sph = np.outer(np.ones(np.size(u)), np.cos(v))
    fig.add_surface(x=x_sph, y=y_sph, z=z_sph, opacity=0.07, showscale=False, colorscale='Blues', name='Bola Langit')

    r_earth = 0.25
    fig.add_surface(x=r_earth * x_sph, y=r_earth * y_sph, z=r_earth * z_sph, opacity=0.75, showscale=False, colorscale='YlGnBu', name='Bumi (Pusat)')

    theta = np.linspace(0, 2*np.pi, 100)
    fig.add_trace(go.Scatter3d(x=np.cos(theta), y=np.sin(theta), z=np.zeros_like(theta),
                               mode='lines', line=dict(color='lime', width=4), name='Horizon (Hz)'))
    L_rad = np.radians(L_deg)
    fig.add_trace(go.Scatter3d(x=-np.sin(L_rad)*np.sin(theta), y=np.cos(theta), z=np.cos(L_rad)*np.sin(theta),
                               mode='lines', line=dict(color='blue', width=3, dash='dash'), name='Ekuator Langit (Eq)'))

    fig.add_trace(go.Scatter3d(x=[0], y=[0], z=[1], mode='markers+text', marker=dict(color='lime', size=5), text=['Zenith (Z)'], textposition='top center', name='Zenith'))
    fig.add_trace(go.Scatter3d(x=[1, 0, -1, 0], y=[0, 1, 0, -1], z=[0, 0, 0, 0], mode='text', text=['Utara', 'Timur', 'Selatan', 'Barat'], textposition='bottom center', name='Mata Angin'))

    if L_deg >= 0:
        P = np.array([np.cos(L_rad), 0, np.sin(L_rad)])
        pole_name = "NCP (P)"
    else:
        P = np.array([-np.cos(L_rad), 0, -np.sin(L_rad)])
        pole_name = "SCP (P)"
    fig.add_trace(go.Scatter3d(x=[P[0]], y=[P[1]], z=[P[2]], mode='markers+text', marker=dict(color='red', size=6), text=[pole_name], textposition='top left', name='Kutub (P)'))

    for item in titik_list:
        if item["h"] is None or item["A"] is None:
            continue
        alt_rad = math.radians(item["h"])
        A_rad = math.radians(item["A"])
        M = np.array([math.cos(alt_rad)*math.cos(A_rad), math.cos(alt_rad)*math.sin(A_rad), math.sin(alt_rad)])
        fig.add_trace(go.Scatter3d(
            x=[M[0]], y=[M[1]], z=[M[2]],
            mode='markers+text',
            marker=dict(color=item["color"], size=7),
            text=[item["label"]],
            textposition='middle left',
            name=item["label"]
        ))
        s_pm = slerp(P, M)
        fig.add_trace(go.Scatter3d(
            x=s_pm[:,0], y=s_pm[:,1], z=s_pm[:,2],
            mode='lines',
            line=dict(color=item["color"], width=3, dash='dot'),
            showlegend=False
        ))

    fig.update_layout(
        scene=dict(
            xaxis_visible=False, yaxis_visible=False, zaxis_visible=False,
            camera=dict(eye=dict(x=1.55, y=-1.55, z=1.15))
        ),
        margin=dict(l=0, r=0, b=0, t=0),
        height=440
    )
    return fig

# ==========================================
# PANEL INPUT PARAMETER PENGAMAT & MATAHARI
# ==========================================
st.subheader("1️⃣ Parameter Lokasi & Data Matahari")
c1, c2, c3 = st.columns(3)
with c1:
    L_deg = st.number_input("Lintang Tempat (L) [°]", value=-6.98, step=0.1, format="%.2f", help="Negatif untuk Lintang Selatan (misal Semarang -6.98°)")
with c2:
    B_deg = st.number_input("Bujur Tempat (B) [° BT]", value=110.42, step=0.1, format="%.2f", help="Semarang ~ 110.42° BT")
with c3:
    mode_solar = st.radio("Mode Data Matahari (d & e)", options=["Otomatis dari Tanggal", "Input Manual"], horizontal=True)

if mode_solar == "Otomatis dari Tanggal":
    col_tgl1, col_tgl2, col_tgl3 = st.columns([1.2, 1, 1])
    with col_tgl1:
        tgl_pilih = st.date_input("Pilih Tanggal Pengamatan", value=datetime.date.today())
    d_deg, eot_menit, hari_ke = estimasi_solar_params(tgl_pilih)
    with col_tgl2:
        st.metric("Deklinasi Otomatis (d)", f"{d_deg:+.4f}°", help=f"Hari ke-{hari_ke} dalam tahun")
    with col_tgl3:
        st.metric("Equation of Time Otomatis (e)", f"{eot_menit:+.2f} menit")
else:
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        d_deg = st.number_input("Deklinasi Matahari (d) [°]", value=-15.0, step=0.5, format="%.4f")
    with col_m2:
        eot_menit = st.number_input("Equation of Time (e) [menit]", value=14.0, step=0.5, format="%.2f", help="Perata waktu dalam menit (+ atau -)")

c5, c6, c7 = st.columns(3)
with c5:
    bujur_daerah = st.selectbox("Zona Waktu Standar", options=[105.0, 120.0, 135.0], format_func=lambda x: f"WIB ({x:.0f}° BT)" if x==105 else (f"WITA ({x:.0f}° BT)" if x==120 else f"WIT ({x:.0f}° BT)"))
with c6:
    elevasi_m = st.number_input("Ketinggian Tempat [meter dpl]", min_value=0, max_value=3000, value=10, step=10)
with c7:
    ikhtiyath_menit = st.number_input("Ikhtiyath / Pengaman [menit]", min_value=0, max_value=5, value=2, step=1)

koreksi_eot_jam = -(eot_menit / 60.0)
koreksi_bujur_jam = (bujur_daerah - B_deg) / 15.0
meridian_pass_jam = 12.0 + koreksi_eot_jam + koreksi_bujur_jam
zuhur_wib = meridian_pass_jam + (ikhtiyath_menit / 60.0)

dip_deg = 0.0347 * math.sqrt(elevasi_m)
h_maghrib_syuruq = -(0.8333 + dip_deg)

st.info(
    f"**Kulminasi (Meridian Pass):** `{format_jam_wib(meridian_pass_jam)}` | "
    f"**Zuhur (+Ikhtiyath {ikhtiyath_menit}m):** `{format_jam_wib(zuhur_wib)}` | "
    f"**Koreksi Dip Ufuk:** `{dip_deg:.4f}°`"
)

# ==========================================
# TABS KOMPARASI KRITERIA
# ==========================================
tab_kulminasi, tab_ashar, tab_subuh, tab_isya, tab_rekap = st.tabs([
    "🕛 0. Kulminasi & Zuhur",
    "☀️ 1. Ashar (2 Versi)",
    "🌅 2. Subuh (3 Versi)",
    "🌃 3. Isya (3 Versi)",
    "📋 4. Rekap & Eksperimen Mandiri"
])

# ------------------------------------------
# TAB 0: KULMINASI & ZUHUR
# ------------------------------------------
with tab_kulminasi:
    st.header("Asal-Usul & Perhitungan Waktu Kulminasi dan Zuhur")

    jarak_zenith_kulminasi = abs(L_deg - d_deg)
    h_kulminasi = 90.0 - jarak_zenith_kulminasi
    selisih_bujur_deg = bujur_daerah - B_deg
    az_kulminasi = 180.0 if (L_deg - d_deg) >= 0 else 0.0

    col_k1, col_k2 = st.columns([1.2, 1])
    with col_k1:
        st.markdown("**1. Koreksi *Equation of Time* ($e$)**")
        st.markdown("Menyesuaikan waktu matahari hakiki (pukul `12:00:00` saat sudut jam $t = 0^\\circ$) menjadi waktu matahari menengah:")
        st.latex(r"\Delta t_{\text{EoT}} = -\frac{e}{60}")
        st.latex(f"\\Delta t_{{\\text{{EoT}}}} = -\\frac{{{eot_menit:+.2f}}}{{60}} = {koreksi_eot_jam:+.6f}\\text{{ jam}}")
        st.markdown(f"Setara dengan: **`{format_selisih_menit_detik(koreksi_eot_jam)}`**")

        st.markdown(f"**2. Koreksi Selisih Bujur Terhadap Acuan (`{bujur_daerah:.0f}° BT`)**")
        st.markdown("Rotasi Bumi menempuh $15^\\circ$ per jam ($1^\\circ = 4$ menit):")
        st.latex(r"\Delta t_{\text{bujur}} = \frac{B_{\text{standar}} - B_{\text{lokasi}}}{15^\circ}")
        st.latex(f"\\Delta t_{{\\text{{bujur}}}} = \\frac{{{bujur_daerah:.2f}^\\circ - {B_deg:.2f}^\\circ}}{{15^\\circ}} = {koreksi_bujur_jam:+.6f}\\text{{ jam}}")
        st.markdown(f"Setara dengan: **`{format_selisih_menit_detik(koreksi_bujur_jam)}`** (selisih bujur `{selisih_bujur_deg:+.2f}°`)")

        st.markdown("**3. Waktu Kulminasi Atas (*Meridian Pass*)**")
        st.markdown(
            f"- Waktu matahari hakiki di meridian: `12:00:00`\n"
            f"- Koreksi EoT: `{format_selisih_menit_detik(koreksi_eot_jam)}`\n"
            f"- Koreksi bujur: `{format_selisih_menit_detik(koreksi_bujur_jam)}`\n"
            f"- **Hasil Kulminasi:** **`{format_jam_wib(meridian_pass_jam)}`**"
        )

        st.markdown(f"**4. Waktu Zuhur (+ *Ikhtiyath* `{ikhtiyath_menit}` menit)**")
        st.markdown(
            f"- Kulminasi: `{format_jam_wib(meridian_pass_jam)}`\n"
            f"- Tambahan *ikhtiyath*: `+{ikhtiyath_menit}m 00d`\n"
            f"- **Hasil Zuhur:** **`{format_jam_wib(zuhur_wib)}`**"
        )

        st.info(
            f"**Geometri Saat Kulminasi:**\n"
            f"- Jarak zenith: $z_0 = |L - d| = {jarak_zenith_kulminasi:.4f}^\\circ$\n"
            f"- Tinggi maksimum matahari: $h_{{\\text{{maks}}}} = 90^\\circ - z_0 = {h_kulminasi:.4f}^\\circ$"
        )

    with col_k2:
        titik_kulminasi = [
            {
                "label": f"Kulminasi ({h_kulminasi:.1f}°)",
                "h": h_kulminasi,
                "A": az_kulminasi,
                "color": "gold"
            }
        ]
        st.plotly_chart(plot_perbandingan_3d(L_deg, titik_kulminasi), use_container_width=True)
        st.caption("Visualisasi 3D: Posisi Matahari saat melintasi meridian lokal (kulminasi atas) terhadap Horizon dan Ekuator Langit.")

# ------------------------------------------
# TAB 1: ASHAR (2 VERSI)
# ------------------------------------------
with tab_ashar:
    st.header("Komparasi Waktu Ashar: Mazhab Jumhur vs. Mazhab Hanafi")
    
    jarak_zenith_kulminasi = abs(L_deg - d_deg)
    tan_z0 = math.tan(math.radians(jarak_zenith_kulminasi))
    
    h_ashar_jumhur = math.degrees(math.atan(1.0 / (1.0 + tan_z0)))
    h_ashar_hanafi = math.degrees(math.atan(1.0 / (2.0 + tan_z0)))
    
    t_jumhur, _ = hitung_sudut_jam(L_deg, d_deg, h_ashar_jumhur)
    t_hanafi, _ = hitung_sudut_jam(L_deg, d_deg, h_ashar_hanafi)
    
    wib_jumhur = meridian_pass_jam + (t_jumhur / 15.0) + (ikhtiyath_menit / 60.0)
    wib_hanafi = meridian_pass_jam + (t_hanafi / 15.0) + (ikhtiyath_menit / 60.0)
    selisih_ashar_menit = (wib_hanafi - wib_jumhur) * 60.0

    col_a1, col_a2 = st.columns([1.15, 1])
    with col_a1:
        df_ashar = pd.DataFrame([
            {
                "Kriteria / Mazhab": "1. Jumhur (Syafi'i, Maliki, Hanbali)",
                "Syarat Bayangan": "1 × tinggi benda + bayangan Zuhur",
                "Tinggi Matahari (h)": f"{h_ashar_jumhur:.4f}°",
                "Sudut Jam (t)": f"{t_jumhur:.4f}° ({format_durasi(t_jumhur)})",
                "Waktu Ashar": format_jam_wib(wib_jumhur)
            },
            {
                "Kriteria / Mazhab": "2. Hanafi",
                "Syarat Bayangan": "2 × tinggi benda + bayangan Zuhur",
                "Tinggi Matahari (h)": f"{h_ashar_hanafi:.4f}°",
                "Sudut Jam (t)": f"{t_hanafi:.4f}° ({format_durasi(t_hanafi)})",
                "Waktu Ashar": format_jam_wib(wib_hanafi)
            }
        ])
        st.dataframe(df_ashar, use_container_width=True, hide_index=True)
        
        st.warning(f"**Implikasi Perbedaan:** Waktu Ashar versi Hanafi masuk **{selisih_ashar_menit:.1f} menit lebih lambat** dibandingkan versi Jumhur karena menunggu bayangan gnomon memanjang dua kali lipat tinggi benda (posisi matahari turun dari `{h_ashar_jumhur:.2f}°` ke `{h_ashar_hanafi:.2f}°`).")

        b0_contoh = 1.0 * tan_z0
        b_jumhur_contoh = 1.0 + b0_contoh
        b_hanafi_contoh = 2.0 + b0_contoh

        with st.expander("🔍 Proses Penurunan Rumus Tinggi Matahari Ashar (Lengkap & Contoh Angka)"):
            st.markdown(
                f"**Acuan Parameter Aktif:**\n"
                f"- Lintang $L = {L_deg:.2f}^\\circ$, Deklinasi $d = {d_deg:.4f}^\\circ$, tinggi tongkat $S = 1.00\\text{{ m}}$\n"
                f"- Kulminasi: `{format_jam_wib(meridian_pass_jam)}`, *Ikhtiyath*: `{ikhtiyath_menit}` menit"
            )

            st.markdown("**1. Panjang Bayangan Saat Kulminasi ($B_0$)**")
            st.latex(f"z_0 = |L - d| = |{L_deg:.2f}^\\circ - ({d_deg:.4f}^\\circ)| = {jarak_zenith_kulminasi:.4f}^\\circ")
            st.latex(r"B_0 = S \cdot \tan|L - d|")
            st.latex(f"B_0 = 1.00 \\times \\tan({jarak_zenith_kulminasi:.4f}^\\circ) = {b0_contoh:.5f}\\text{{ m}}")

            st.markdown("**2. Panjang Bayangan Total Saat Awal Ashar ($B$)**")
            st.latex(r"B = n \cdot S + B_0 = S(n + \tan|L - d|)")
            st.markdown(
                f"- **Jumhur ($n = 1$):** $B = 1.00 + {b0_contoh:.5f} = \\mathbf{{{b_jumhur_contoh:.5f}\\text{{ m}}}}$\n"
                f"- **Hanafi ($n = 2$):** $B = 2.00 + {b0_contoh:.5f} = \\mathbf{{{b_hanafi_contoh:.5f}\\text{{ m}}}}$"
            )

            st.markdown("**3. Tinggi Matahari ($h_{\\text{ashar}}$), Sudut Jam ($t$) & Jam**")
            st.latex(r"h_{\text{ashar}} = \arctan\left(\frac{1}{n + \tan|L - d|}\right)")
            st.markdown(
                f"- **Jumhur ($n = 1$):** $h_{{\\text{{ashar}}}} = \\mathbf{{{h_ashar_jumhur:.4f}^\\circ}}$ $\\rightarrow$ $t = {t_jumhur:.4f}^\\circ$ (`{format_durasi(t_jumhur)}` setelah kulminasi) $\\rightarrow$ **Jam Ashar = `{format_jam_wib(wib_jumhur)}`**\n"
                f"- **Hanafi ($n = 2$):** $h_{{\\text{{ashar}}}} = \\mathbf{{{h_ashar_hanafi:.4f}^\\circ}}$ $\\rightarrow$ $t = {t_hanafi:.4f}^\\circ$ (`{format_durasi(t_hanafi)}` setelah kulminasi) $\\rightarrow$ **Jam Ashar = `{format_jam_wib(wib_hanafi)}`**"
            )
            st.markdown("Nilai $h_{\\text{ashar}}$ kemudian disubstitusikan ke rumus sudut jam:")
            st.latex(r"\cos(t) = \frac{\sin(h) - \sin(L)\sin(d)}{\cos(L)\cos(d)}")

    with col_a2:
        titik_ashar = [
            {"label": f"Ashar Jumhur ({h_ashar_jumhur:.1f}°)", "h": h_ashar_jumhur, "A": hitung_azimuth_matahari(L_deg, d_deg, h_ashar_jumhur, True), "color": "orange"},
            {"label": f"Ashar Hanafi ({h_ashar_hanafi:.1f}°)", "h": h_ashar_hanafi, "A": hitung_azimuth_matahari(L_deg, d_deg, h_ashar_hanafi, True), "color": "red"},
            {"label": "Maghrib (Ufuk)", "h": h_maghrib_syuruq, "A": hitung_azimuth_matahari(L_deg, d_deg, h_maghrib_syuruq, True), "color": "purple"}
        ]
        st.plotly_chart(plot_perbandingan_3d(L_deg, titik_ashar), use_container_width=True)
        st.caption("Visualisasi 3D: Perbandingan posisi matahari di langit barat antara Ashar Jumhur (oranye) dan Ashar Hanafi (merah).")

# ------------------------------------------
# TAB 2: SUBUH (3 VERSI)
# ------------------------------------------
with tab_subuh:
    st.header("Komparasi Waktu Subuh: Kemenag RI (-20°) vs. Muhammadiyah (-18°) vs. ISNA (-15°)")
    
    kriteria_subuh = [
        ("Kemenag RI / MABIMS", -20.0, "Kriteria resmi pemerintah Indonesia & negara anggota MABIMS"),
        ("Muhammadiyah (Munas Tarjih)", -18.0, "Koreksi ketinggian fajar shadiq akibat hamburan atmosfer & observasi SQM"),
        ("ISNA (Amerika Utara)", -15.0, "Standar Islamic Society of North America")
    ]
    
    rows_subuh = []
    titik_subuh = []
    warna_subuh = ["cyan", "orange", "yellow"]
    
    for idx, (nama, h_val, ket) in enumerate(kriteria_subuh):
        t_val, _ = hitung_sudut_jam(L_deg, d_deg, h_val)
        if t_val is not None:
            wib_val = meridian_pass_jam - (t_val / 15.0) + (ikhtiyath_menit / 60.0)
            t_str = f"{t_val:.4f}° ({format_durasi(t_val)})"
            jam_str = format_jam_wib(wib_val)
            az_val = hitung_azimuth_matahari(L_deg, d_deg, h_val, sisi_barat=False)
        else:
            t_str = "Tidak tercapai (|cos t| > 1)"
            jam_str = "-"
            az_val = None
        rows_subuh.append({
            "Lembaga / Kriteria": nama,
            "Tinggi Matahari (h)": f"{h_val:.1f}°",
            "Sudut Jam (t)": t_str,
            "Waktu Subuh": jam_str,
            "Keterangan": ket
        })
        titik_subuh.append({
            "label": f"Subuh {h_val:.0f}°",
            "h": h_val if t_val is not None else None,
            "A": az_val,
            "color": warna_subuh[idx]
        })

    t_syuruq, _ = hitung_sudut_jam(L_deg, d_deg, h_maghrib_syuruq)
    wib_syuruq = meridian_pass_jam - (t_syuruq / 15.0) - (ikhtiyath_menit / 60.0)
    titik_subuh.append({
        "label": f"Syuruq ({h_maghrib_syuruq:.2f}°)",
        "h": h_maghrib_syuruq,
        "A": hitung_azimuth_matahari(L_deg, d_deg, h_maghrib_syuruq, sisi_barat=False),
        "color": "lime"
    })

    col_s1, col_s2 = st.columns([1.15, 1])
    with col_s1:
        st.dataframe(pd.DataFrame(rows_subuh), use_container_width=True, hide_index=True)
        
        t_20, _ = hitung_sudut_jam(L_deg, d_deg, -20.0)
        t_18, _ = hitung_sudut_jam(L_deg, d_deg, -18.0)
        if t_20 is not None and t_18 is not None:
            selisih_20_18 = ((t_20 - t_18) / 15.0) * 60.0
            st.warning(f"**Implikasi Perbedaan:** Pergeseran sudut depresi matahari dari `-20°` ke `-18°` membuat waktu Subuh bergeser sekitar **{selisih_20_18:.1f} menit lebih siang** (lebih dekat ke waktu Syuruq `{format_jam_wib(wib_syuruq)}`). Di wilayah tropis dengan polusi cahaya perkotaan, cahaya fajar astronomis pada `-20°` sering kali masih tertutup *sky glow* sehingga fajar shadiq baru terdeteksi secara fotometris mendekati `-18°`.")
        else:
            st.warning("Pada lintang/deklinasi ekstrem ini, salah satu sudut depresi Subuh tidak tercapai secara geometris (`|cos t| > 1`).")

        with st.expander("🔍 Proses Penurunan Rumus Subuh & Makna Tanda Negatif"):
            st.markdown("**1. Posisi Matahari Sebelum Terbit**")
            st.markdown("Pada waktu Subuh, matahari masih berada di bawah horizon timur sehingga ketinggiannya bernilai negatif ($h < 0^\\circ$):")
            st.latex(r"z = 90^\circ - h")

            st.markdown("**2. Rumus Sudut Jam Subuh**")
            st.latex(r"\cos(t_{\text{subuh}}) = \frac{\sin(h_{\text{subuh}}) - \sin(L)\sin(d)}{\cos(L)\cos(d)}")

            st.markdown("**3. Pengurangan terhadap Waktu Kulminasi**")
            st.markdown("Karena terjadi sebelum matahari melintasi meridian (sisi timur), sudut jam $t$ **dikurangkan** dari waktu kulminasi:")
            st.latex(r"\text{Waktu Subuh} = \text{Meridian Pass} - \frac{t_{\text{subuh}}}{15^\circ} + \text{Ikhtiyath}")

    with col_s2:
        st.plotly_chart(plot_perbandingan_3d(L_deg, titik_subuh), use_container_width=True)
        st.caption("Visualisasi 3D: Posisi matahari di bawah ufuk Timur pada kedalaman -20°, -18°, -15°, hingga saat terbit (Syuruq).")

# ------------------------------------------
# TAB 3: ISYA (3 VERSI)
# ------------------------------------------
with tab_isya:
    st.header("Komparasi Waktu Isya: -18° (Kemenag/Muhammadiyah) vs. -17° vs. -15° (ISNA)")
    
    kriteria_isya = [
        ("Kemenag RI / MABIMS & Muhammadiyah", -18.0, "Hilangnya mega merah (syafaq ahmar) secara astronomis"),
        ("Kriteria Moderat (-17°)", -17.0, "Digunakan pada beberapa kalender regional Timur Tengah"),
        ("ISNA (Amerika Utara)", -15.0, "Standar lintang menengah/tinggi di Amerika Utara")
    ]
    
    rows_isya = []
    titik_isya = []
    warna_isya = ["magenta", "orange", "yellow"]
    
    t_maghrib, _ = hitung_sudut_jam(L_deg, d_deg, h_maghrib_syuruq)
    wib_maghrib = meridian_pass_jam + (t_maghrib / 15.0) + (ikhtiyath_menit / 60.0)
    titik_isya.append({
        "label": f"Maghrib ({h_maghrib_syuruq:.2f}°)",
        "h": h_maghrib_syuruq,
        "A": hitung_azimuth_matahari(L_deg, d_deg, h_maghrib_syuruq, sisi_barat=True),
        "color": "red"
    })

    for idx, (nama, h_val, ket) in enumerate(kriteria_isya):
        t_val, _ = hitung_sudut_jam(L_deg, d_deg, h_val)
        if t_val is not None:
            wib_val = meridian_pass_jam + (t_val / 15.0) + (ikhtiyath_menit / 60.0)
            jeda_dari_maghrib = (wib_val - wib_maghrib) * 60.0
            t_str = f"{t_val:.4f}° ({format_durasi(t_val)})"
            jam_str = format_jam_wib(wib_val)
            jeda_str = f"+{jeda_dari_maghrib:.1f} menit"
            az_val = hitung_azimuth_matahari(L_deg, d_deg, h_val, sisi_barat=True)
        else:
            t_str = "Tidak tercapai (|cos t| > 1)"
            jam_str = "-"
            jeda_str = "-"
            az_val = None
        rows_isya.append({
            "Lembaga / Kriteria": nama,
            "Tinggi Matahari (h)": f"{h_val:.1f}°",
            "Sudut Jam (t)": t_str,
            "Waktu Isya": jam_str,
            "Jeda dari Maghrib": jeda_str
        })
        titik_isya.append({
            "label": f"Isya {h_val:.0f}°",
            "h": h_val if t_val is not None else None,
            "A": az_val,
            "color": warna_isya[idx]
        })

    col_i1, col_i2 = st.columns([1.15, 1])
    with col_i1:
        st.dataframe(pd.DataFrame(rows_isya), use_container_width=True, hide_index=True)
        st.warning(f"**Implikasi Perbedaan:** Dari waktu Maghrib (`{format_jam_wib(wib_maghrib)}`), jeda menuju waktu Isya pada kriteria `-18°` membutuhkan sekitar **{rows_isya[0]['Jeda dari Maghrib']}**, sedangkan pada kriteria `-15°` lebih singkat. Pada bulan-bulan dengan deklinasi ekstrem, durasi senja (*twilight*) memanjang sehingga selisih antar-kriteria ikut melebar.")

        with st.expander("🔍 Proses Penurunan Rumus Waktu Isya"):
            st.markdown("**1. Simetri Senja Astronomis di Ufuk Barat**")
            st.latex(r"\cos(t_{\text{isya}}) = \frac{\sin(h_{\text{isya}}) - \sin(L)\sin(d)}{\cos(L)\cos(d)}")

            st.markdown("**2. Penambahan terhadap Waktu Kulminasi**")
            st.markdown("Karena terjadi setelah kulminasi atas (sisi barat), sudut jam $t$ **ditambahkan** ke waktu kulminasi:")
            st.latex(r"\text{Waktu Isya} = \text{Meridian Pass} + \frac{t_{\text{isya}}}{15^\circ} + \text{Ikhtiyath}")

    with col_i2:
        st.plotly_chart(plot_perbandingan_3d(L_deg, titik_isya), use_container_width=True)
        st.caption("Visualisasi 3D: Pergerakan matahari turun di bawah ufuk Barat mulai dari Maghrib hingga kedalaman Isya -15°, -17°, dan -18°.")

# ------------------------------------------
# TAB 4: REKAP JADWAL, EKSPERIMEN & KUNCI TERKUNCI
# ------------------------------------------
with tab_rekap:
    st.header("📋 Rekapitulasi Jadwal Lengkap & Eksperimen Mahasiswa")
    
    t_subuh_kemenag, _ = hitung_sudut_jam(L_deg, d_deg, -20.0)
    t_subuh_muh, _ = hitung_sudut_jam(L_deg, d_deg, -18.0)
    t_isya_15, _ = hitung_sudut_jam(L_deg, d_deg, -15.0)
    
    jadwal_lengkap = pd.DataFrame([
        {"Waktu Shalat": "Subuh (Kemenag -20°)", "h [°]": "-20.00°", "Jam Standar": format_jam_wib(meridian_pass_jam - t_subuh_kemenag/15.0 + ikhtiyath_menit/60.0) if t_subuh_kemenag is not None else "-"},
        {"Waktu Shalat": "Subuh (Muhammadiyah -18°)", "h [°]": "-18.00°", "Jam Standar": format_jam_wib(meridian_pass_jam - t_subuh_muh/15.0 + ikhtiyath_menit/60.0) if t_subuh_muh is not None else "-"},
        {"Waktu Shalat": "Syuruq / Terbit", "h [°]": f"{h_maghrib_syuruq:.2f}°", "Jam Standar": format_jam_wib(wib_syuruq)},
        {"Waktu Shalat": "Zuhur", "h [°]": "Kulminasi", "Jam Standar": format_jam_wib(zuhur_wib)},
        {"Waktu Shalat": "Ashar (Jumhur)", "h [°]": f"{h_ashar_jumhur:.2f}°", "Jam Standar": format_jam_wib(wib_jumhur)},
        {"Waktu Shalat": "Ashar (Hanafi)", "h [°]": f"{h_ashar_hanafi:.2f}°", "Jam Standar": format_jam_wib(wib_hanafi)},
        {"Waktu Shalat": "Maghrib", "h [°]": f"{h_maghrib_syuruq:.2f}°", "Jam Standar": format_jam_wib(wib_maghrib)},
        {"Waktu Shalat": "Isya (-18°)", "h [°]": "-18.00°", "Jam Standar": format_jam_wib(meridian_pass_jam + t_subuh_muh/15.0 + ikhtiyath_menit/60.0) if t_subuh_muh is not None else "-"},
        {"Waktu Shalat": "Isya (-15°)", "h [°]": "-15.00°", "Jam Standar": format_jam_wib(meridian_pass_jam + t_isya_15/15.0 + ikhtiyath_menit/60.0) if t_isya_15 is not None else "-"},
    ])
    st.table(jadwal_lengkap)

    st.subheader("🧪 Tugas Eksperimen Mandiri Mahasiswa")
    st.info(
        "1. **Pengaruh Bujur dalam Satu Zona Waktu:** Ubah input Bujur Tempat dari `110.42° BT` (Semarang) menjadi `95.32° BT` (Banda Aceh) dengan tetap mempertahankan zona waktu `WIB (105° BT)`. Berapa menit seluruh jadwal shalat bergeser? Mengapa demikian?\n"
        "2. **Pengaruh Ketinggian Tempat (Dip):** Naikkan Ketinggian Tempat dari `10 m` menjadi `2.000 m` (misal kawasan dataran tinggi Dieng). Amati perubahan nilai `Koreksi Dip Ufuk` dan pergeseran waktu **Syuruq** serta **Maghrib**.\n"
        "3. **Eksperimen Lintang Tinggi:** Ubah Lintang Tempat menjadi `+55° LU` (misal Moskow/Kopenhagen) dan Deklinasi `+23.4°` (Juni). Apa yang terjadi pada perhitungan Subuh `-20°` dan Isya `-18°`? Mengapa nilai `cos(t)` bisa keluar dari rentang `[-1, 1]`?"
    )

    st.divider()
    st.subheader("✍️ Form Catatan Percobaan & Pembukaan Kunci Jawaban")

    if "eksperimen_dicoba" not in st.session_state:
        st.session_state["eksperimen_dicoba"] = False

    col_id1, col_id2 = st.columns([1, 1])
    with col_id1:
        nama_mhs = st.text_input("Nama Mahasiswa", placeholder="Contoh: Ahmad Fauzi")
    with col_id2:
        presensi_mhs = st.text_input("No. Presensi / NIM", placeholder="Contoh: 12")

    jawaban_eksperimen = st.text_area(
        "Ringkasan Hasil Eksperimen Anda (1–3 poin):",
        placeholder="Tuliskan temuan Anda mengenai selisih bujur, efek ketinggian dip, dan kondisi lintang tinggi..."
    )

    if st.button("📤 Kirim Percobaan & Buka Kunci Jawaban"):
        if not nama_mhs.strip() or not presensi_mhs.strip() or not jawaban_eksperimen.strip():
            st.warning("Mohon lengkapi **Nama Mahasiswa**, **No. Presensi/NIM**, dan **Ringkasan Hasil Eksperimen** terlebih dahulu.")
        else:
            payload = {
                "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "nama": nama_mhs.strip(),
                "presensi_nim": presensi_mhs.strip(),
                "lintang": L_deg,
                "bujur": B_deg,
                "deklinasi": round(d_deg, 4),
                "eot_menit": round(eot_menit, 2),
                "elevasi_m": elevasi_m,
                "jawaban_eksperimen": jawaban_eksperimen.strip()
            }
            terkirim, pesan_gsheet = kirim_ke_gsheet(payload)
            st.session_state["eksperimen_dicoba"] = True
            if terkirim:
                st.success(pesan_gsheet)
            else:
                st.info(f"Kunci jawaban dibuka untuk sesi Anda. *(Catatan rekap: {pesan_gsheet})*")

    if st.session_state["eksperimen_dicoba"]:
        with st.expander("🔑 Kunci Jawaban & Pembahasan Tugas Eksperimen", expanded=True):
            st.markdown(
                "**1. Pengaruh Bujur (`110.42° BT` ke `95.32° BT`, Zona WIB `105° BT`):**\n"
                "- Selisih bujur `ΔB = 110.42° - 95.32° = 15.10°`.\n"
                "- Karena `15° = 1 jam = 60 menit`, pergeserannya adalah `(15.10° / 15°) × 60 menit = 60.4 menit` (**sekitar 60 menit 24 detik lebih lambat** pada jam WIB).\n"
                "- Bujur yang lebih ke barat mengalami kulminasi/meridian lokal lebih lambat terhadap bujur standar `105° BT`.\n\n"
                "**2. Pengaruh Ketinggian Tempat (`10 m` ke `2.000 m`):**\n"
                "- Nilai koreksi *dip* ufuk meningkat dari sekitar `0.11°` menjadi sekitar `1.55°`.\n"
                "- Ufuk tampak lebih rendah sehingga **Syuruq** bergeser lebih awal (maju) dan **Maghrib** bergeser lebih lambat (mundur).\n\n"
                "**3. Eksperimen Lintang Tinggi (`L = +55° LU`, `d = +23.4°`):**\n"
                "- Nilai `|cos(t)|` dapat melebihi `1` (`cos(t) < -1`) sehingga `arccos(cos(t))` tidak memiliki solusi sudut jam riil untuk depresi `-18°` atau `-20°`.\n"
                "- Secara fisis, matahari pada malam musim panas di lintang tinggi tersebut tidak turun sedalam `-18°` atau `-20°` di bawah ufuk (*midnight twilight* / malam putih), sehingga diperlukan pendekatan alternatif penentuan waktu Subuh dan Isya."
            )
