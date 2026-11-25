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

def render_blok_substitusi_cos_t(label_waktu, h_deg, L_deg, d_deg):
    """Menampilkan alur penurunan & substitusi angka rumus cos(t) untuk satu nilai h tertentu."""
    sin_h = math.sin(math.radians(h_deg))
    sin_L = math.sin(math.radians(L_deg))
    sin_d = math.sin(math.radians(d_deg))
    cos_L = math.cos(math.radians(L_deg))
    cos_d = math.cos(math.radians(d_deg))
    penyebut = cos_L * cos_d
    pembilang = sin_h - (sin_L * sin_d)
    cos_t_raw = pembilang / penyebut if abs(penyebut) > 1e-12 else float("nan")

    st.markdown(
        f"**1. Hubungan Segitiga Bola P–Z–M untuk {label_waktu} ($h = {h_deg:.4f}^\\circ$):**\n"
        f"- Jarak *zenith* sisi $ZM = 90^\\circ - h = {90.0 - h_deg:.4f}^\\circ$ $\\Rightarrow$ $\\cos(ZM) = \\sin(h)$.\n"
        f"- *(Penurunan penuh Aturan Kosinus segitiga bola P–Z–M dari awal dapat dilihat di **Tab 0: Kulminasi & Zuhur**.)*"
    )
    st.latex(r"\cos(t) = \frac{\sin(h) - \sin(L)\sin(d)}{\cos(L)\cos(d)}")

    st.markdown("**2. Substitusi Nilai Aktif ($L$, $d$, dan $h$):**")
    st.latex(
        f"\\cos(t) = \\frac{{\\sin({h_deg:.4f}^\\circ) - \\sin({L_deg:.2f}^\\circ)\\sin({d_deg:.4f}^\\circ)}}"
        f"{{\\cos({L_deg:.2f}^\\circ)\\cos({d_deg:.4f}^\\circ)}} "
        f"= \\frac{{{sin_h:+.5f} - ({sin_L:+.5f} \\times {sin_d:+.5f})}}"
        f"{{{cos_L:.5f} \\times {cos_d:.5f}}}"
    )

    if abs(cos_t_raw) <= 1.0:
        t_val = math.degrees(math.acos(cos_t_raw))
        st.latex(
            f"\\cos(t) = {cos_t_raw:+.6f} \\implies t = \\arccos({cos_t_raw:+.6f}) = \\mathbf{{{t_val:.4f}^\\circ}} "
            f"\\;(\\text{{durasi }} {format_durasi(t_val)})"
        )
    else:
        st.warning(f"Nilai $\\cos(t) = {cos_t_raw:+.6f}$ berada di luar rentang $[-1, 1]$, sehingga sudut jam riil tidak tercapai pada parameter ini.")

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

def plot_geometri_bayangan_ashar(S, z0_deg, b0, b_jumhur, b_hanafi, h_jumhur_deg, h_hanafi_deg):
    """Diagram teknis 2D perbandingan panjang bayangan (B0, Jumhur, Hanafi) & tinggi matahari (h_ashar)."""
    fig = go.Figure()

    max_x = max(b_hanafi * 1.15, S * 2.2)
    max_y = max(S * 1.42, b_hanafi * 0.42)

    # Bidang tanah
    fig.add_trace(go.Scatter(
        x=[-0.35 * S, max_x], y=[0, 0],
        mode="lines", line=dict(color="#94a3b8", width=3),
        name="Bidang Datar (Tanah)"
    ))

    # Tongkat / Gnomon vertikal (tinggi S) di x = 0
    fig.add_trace(go.Scatter(
        x=[0, 0], y=[0, S],
        mode="lines+markers", line=dict(color="#f8fafc", width=5),
        marker=dict(size=7, color="#f8fafc"),
        name=f"Gnomon (S = {S:.2f} m)"
    ))

    # Garis vertikal zenith ke atas dari puncak gnomon (0, S)
    y_zenith_top = min(S * 1.32, max_y * 0.94)
    fig.add_trace(go.Scatter(
        x=[0, 0], y=[S, y_zenith_top],
        mode="lines", line=dict(color="#cbd5e1", width=1.5, dash="dot"),
        name="Arah Vertikal / Zenith"
    ))

    # 1. Bayangan Kulminasi B0 & sinar kulminasi
    fig.add_trace(go.Scatter(
        x=[0, b0], y=[0, 0],
        mode="lines+markers", line=dict(color="#38bdf8", width=6),
        marker=dict(size=6, color="#38bdf8"),
        name=f"Bayangan Kulminasi B0 ({b0:.3f} m)"
    ))
    fig.add_trace(go.Scatter(
        x=[b0, 0], y=[0, S],
        mode="lines", line=dict(color="#38bdf8", width=1.8, dash="dash"),
        name=f"Sinar Kulminasi (z0 = {z0_deg:.2f}°)"
    ))

    if z0_deg > 0.5:
        r_z0 = min(0.26 * S, max(0.12 * S, b0 * 0.55))
        ang_z0 = np.linspace(0, math.radians(min(z0_deg, 75.0)), 30)
        vx = r_z0 * np.sin(ang_z0)
        vy = S - r_z0 * np.cos(ang_z0)
        fig.add_trace(go.Scatter(
            x=vx, y=vy, mode="lines",
            line=dict(color="#38bdf8", width=2),
            showlegend=False
        ))
        fig.add_annotation(
            x=vx[-1], y=vy[-1],
            ax=max(0.45 * S, b0 * 1.1 + 0.25 * S), ay=S + 0.18 * S,
            text=f"z0={z0_deg:.1f}°",
            showarrow=True, arrowhead=2, arrowsize=0.8, arrowwidth=1.2, arrowcolor="#38bdf8",
            font=dict(color="#38bdf8", size=11),
            bgcolor="rgba(15,23,42,0.85)", borderpad=2
        )

    # 2. Bayangan Jumhur (total b_jumhur) & sinar dari (b_jumhur, 0) ke (0, S)
    fig.add_trace(go.Scatter(
        x=[b0, b_jumhur], y=[0, 0],
        mode="lines+markers", line=dict(color="#fb923c", width=5),
        marker=dict(size=6, color="#fb923c"),
        name=f"Bayangan Jumhur B_J ({b_jumhur:.3f} m)"
    ))
    fig.add_trace(go.Scatter(
        x=[b_jumhur, 0], y=[0, S],
        mode="lines", line=dict(color="#fb923c", width=2.2),
        showlegend=False
    ))

    r_hj = min(0.28 * S, 0.35 * max(b_jumhur - b0, 0.25 * S))
    ang_hj = np.linspace(0, math.radians(h_jumhur_deg), 30)
    fig.add_trace(go.Scatter(
        x=b_jumhur - r_hj * np.cos(ang_hj),
        y=r_hj * np.sin(ang_hj),
        mode="lines", line=dict(color="#fb923c", width=2),
        showlegend=False
    ))
    fig.add_annotation(
        x=b_jumhur - r_hj * 0.85, y=r_hj * 0.45,
        ax=b_jumhur - 0.12 * S, ay=0.22 * S,
        text=f"h_J={h_jumhur_deg:.1f}°",
        showarrow=True, arrowhead=2, arrowsize=0.8, arrowwidth=1.2, arrowcolor="#fb923c",
        font=dict(color="#fb923c", size=11),
        bgcolor="rgba(15,23,42,0.85)", borderpad=2
    )

    # 3. Bayangan Hanafi (total b_hanafi) & sinar dari (b_hanafi, 0) ke (0, S)
    fig.add_trace(go.Scatter(
        x=[b_jumhur, b_hanafi], y=[0, 0],
        mode="lines+markers", line=dict(color="#f87171", width=5),
        marker=dict(size=6, color="#f87171"),
        name=f"Bayangan Hanafi B_H ({b_hanafi:.3f} m)"
    ))
    fig.add_trace(go.Scatter(
        x=[b_hanafi, 0], y=[0, S],
        mode="lines", line=dict(color="#f87171", width=2.2, dash="dot"),
        showlegend=False
    ))

    r_hh = min(0.28 * S, 0.35 * max(b_hanafi - b_jumhur, 0.25 * S))
    ang_hh = np.linspace(0, math.radians(h_hanafi_deg), 30)
    fig.add_trace(go.Scatter(
        x=b_hanafi - r_hh * np.cos(ang_hh),
        y=r_hh * np.sin(ang_hh),
        mode="lines", line=dict(color="#f87171", width=2),
        showlegend=False
    ))
    fig.add_annotation(
        x=b_hanafi - r_hh * 0.85, y=r_hh * 0.45,
        ax=b_hanafi - 0.05 * S, ay=0.16 * S,
        text=f"h_H={h_hanafi_deg:.1f}°",
        showarrow=True, arrowhead=2, arrowsize=0.8, arrowwidth=1.2, arrowcolor="#f87171",
        font=dict(color="#f87171", size=11),
        bgcolor="rgba(15,23,42,0.85)", borderpad=2
    )

    # Label tinggi tongkat S di sisi kiri luar tongkat
    fig.add_annotation(
        x=-0.04 * S, y=0.5 * S,
        text=f"S={S:.1f}m", showarrow=False, xanchor="right",
        font=dict(color="#f8fafc", size=11),
        bgcolor="rgba(15,23,42,0.75)", borderpad=2
    )

    fig.update_layout(
        xaxis=dict(
            title=dict(text="Panjang Bayangan di Tanah [m]", standoff=10),
            range=[-0.35 * S, max_x],
            zeroline=False
        ),
        yaxis=dict(
            title="Ketinggian [m]",
            range=[-0.12 * S, max_y],
            scaleanchor="x",
            scaleratio=1,
            zeroline=False
        ),
        height=450,
        margin=dict(l=10, r=10, t=15, b=115),
        legend=dict(
            orientation="h",
            yanchor="top",
            y=-0.22,
            xanchor="center",
            x=0.5,
            font=dict(size=11)
        )
    )
    return fig

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

    Z = np.array([0.0, 0.0, 1.0])
    fig.add_trace(go.Scatter3d(x=[Z[0]], y=[Z[1]], z=[Z[2]], mode='markers+text', marker=dict(color='lime', size=5), text=['Zenith (Z)'], textposition='top center', name='Zenith (Z)'))
    fig.add_trace(go.Scatter3d(x=[1, 0, -1, 0], y=[0, 1, 0, -1], z=[0, 0, 0, 0], mode='text', text=['Utara', 'Timur', 'Selatan', 'Barat'], textposition='bottom center', name='Mata Angin'))

    if L_deg >= 0:
        P = np.array([np.cos(L_rad), 0, np.sin(L_rad)])
        pole_name = "NCP (P)"
    else:
        P = np.array([-np.cos(L_rad), 0, -np.sin(L_rad)])
        pole_name = "SCP (P)"
    fig.add_trace(go.Scatter3d(x=[P[0]], y=[P[1]], z=[P[2]], mode='markers+text', marker=dict(color='red', size=6), text=[pole_name], textposition='top left', name='Kutub (P)'))

    # Sisi dasar segitiga bola: busur P - Z (komplemen lintang 90° - L)
    s_pz = slerp(P, Z)
    fig.add_trace(go.Scatter3d(
        x=s_pz[:, 0], y=s_pz[:, 1], z=s_pz[:, 2],
        mode='lines',
        line=dict(color='hotpink', width=4),
        name='Busur PZ (90° - L)'
    ))

    for idx_t, item in enumerate(titik_list):
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

        # Beri sedikit offset radial saat kulminasi agar busur PM & ZM tidak sepenuhnya tertelan busur PZ
        is_kulminasi_line = abs(math.sin(A_rad)) < 1e-3 and abs(item["h"] - (90.0 - abs(L_deg - math.degrees(math.asin(np.clip(math.sin(math.radians(item["h"])) , -1, 1)))))) < 1e-6
        offset_pm = 1.015 if is_kulminasi_line else 1.003
        offset_zm = 0.985 if is_kulminasi_line else 1.001

        # Sisi PM (jarak kutub 90° - d)
        s_pm = slerp(P, M) * offset_pm
        fig.add_trace(go.Scatter3d(
            x=s_pm[:,0], y=s_pm[:,1], z=s_pm[:,2],
            mode='lines',
            line=dict(color=item["color"], width=3.5, dash='dot'),
            name=f"Busur PM ({item['label']})" if idx_t == 0 else None,
            showlegend=(idx_t == 0)
        ))
        # Sisi ZM (jarak zenith z = 90° - h) untuk melengkapi segitiga bola P-Z-M
        s_zm = slerp(Z, M) * offset_zm
        fig.add_trace(go.Scatter3d(
            x=s_zm[:, 0], y=s_zm[:, 1], z=s_zm[:, 2],
            mode='lines',
            line=dict(color=item["color"], width=3.0, dash='dash'),
            name=f"Busur ZM ({item['label']})" if idx_t == 0 else None,
            showlegend=(idx_t == 0)
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
        st.latex(r"T_{\text{kulminasi}} = 12^{\text{j}} + \Delta t_{\text{EoT}} + \Delta t_{\text{bujur}}")
        st.latex(
            f"T_{{\\text{{kulminasi}}}} = 12:00:00 + ({format_selisih_menit_detik(koreksi_eot_jam)}) "
            f"+ ({format_selisih_menit_detik(koreksi_bujur_jam)}) = \\mathbf{{{format_jam_wib(meridian_pass_jam)}}}"
        )
        st.markdown(
            f"- Waktu matahari hakiki di meridian: `12:00:00`\n"
            f"- Koreksi EoT ($\\Delta t_{{\\text{{EoT}}}}$): `{format_selisih_menit_detik(koreksi_eot_jam)}`\n"
            f"- Koreksi bujur ($\\Delta t_{{\\text{{bujur}}}}$): `{format_selisih_menit_detik(koreksi_bujur_jam)}`\n"
            f"- **Hasil Kulminasi:** **`{format_jam_wib(meridian_pass_jam)}`**"
        )

        st.markdown(f"**4. Waktu Zuhur (+ *Ikhtiyath* `{ikhtiyath_menit}` menit)**")
        st.latex(r"T_{\text{zuhur}} = T_{\text{kulminasi}} + \frac{\text{Ikhtiyath}}{60}")
        st.latex(
            f"T_{{\\text{{zuhur}}}} = {format_jam_wib(meridian_pass_jam)} + (+{ikhtiyath_menit}\\text{{m}}\\ 00\\text{{d}}) "
            f"= \\mathbf{{{format_jam_wib(zuhur_wib)}}}"
        )
        st.markdown(
            f"- Kulminasi ($T_{{\\text{{kulminasi}}}}$): `{format_jam_wib(meridian_pass_jam)}`\n"
            f"- Tambahan *ikhtiyath*: `+{ikhtiyath_menit}m 00d`\n"
            f"- **Hasil Zuhur:** **`{format_jam_wib(zuhur_wib)}`**"
        )

        st.info(
            f"**Geometri Saat Kulminasi:**\n"
            f"- Jarak zenith: $z_0 = |L - d| = {jarak_zenith_kulminasi:.4f}^\\circ$\n"
            f"- Tinggi maksimum matahari: $h_{{\\text{{maks}}}} = 90^\\circ - z_0 = {h_kulminasi:.4f}^\\circ$"
        )

        with st.expander("📐 Penurunan Lengkap Rumus Sudut Jam cos(t) (Segitiga Bola P–Z–M)"):
            sin_h_k = math.sin(math.radians(h_kulminasi))
            sin_L = math.sin(math.radians(L_deg))
            sin_d = math.sin(math.radians(d_deg))
            cos_L = math.cos(math.radians(L_deg))
            cos_d = math.cos(math.radians(d_deg))
            cos_t_k = (sin_h_k - sin_L * sin_d) / (cos_L * cos_d)
            cos_t_k_clip = float(np.clip(cos_t_k, -1.0, 1.0))
            t_k_deg = math.degrees(math.acos(cos_t_k_clip))

            st.markdown(
                "**Rujukan Fondasi Utama:** Rumus $\\cos(t)$ yang dipakai pada perhitungan **Subuh**, **Ashar**, dan **Isya** adalah rumus tunggal yang berasal dari **Aturan Kosinus Sisi pada Segitiga Bola P–Z–M** (Kutub langit $P$, *Zenith* $Z$, dan posisi Matahari $M$)."
            )

            st.markdown("**Langkah 1: Identifikasi Tiga Titik & Tiga Sisi Segitiga Bola P–Z–M**")
            st.markdown(
                "- **$P$ (Kutub Langit):** Kutub Utara Langit (*NCP*, $L > 0^\\circ$) atau Kutub Selatan Langit (*SCP*, $L < 0^\\circ$).\n"
                "- **$Z$ (*Zenith*):** Titik puncak tepat di atas kepala pengamat.\n"
                "- **$M$ (Matahari):** Posisi pusat Matahari pada saat ketinggian $h$.\n"
                "- **Sudut di Kutub ($\\angle ZPM$):** Sudut jam matahari (**$t$**), diukur dari meridian pengamat ke lingkaran jam Matahari.\n"
                "- **Panjang ketiga sisi busur segitiga bola:**\n"
                "  - Sisi $PZ = 90^\\circ - L$ (komplemen lintang tempat $L$)\n"
                "  - Sisi $PM = 90^\\circ - d$ (komplemen deklinasi $d$)\n"
                "  - Sisi $ZM = z = 90^\\circ - h$ (jarak *zenith*, komplemen tinggi matahari $h$)"
            )

            st.markdown("**Langkah 2: Aturan Kosinus Sisi Terhadap Sisi $ZM$**")
            st.latex(r"\cos(ZM) = \cos(PZ)\cos(PM) + \sin(PZ)\sin(PM)\cos(t)")

            st.markdown("**Langkah 3: Substitusi Sisi $ZM$, $PZ$, dan $PM$ dengan $h$, $L$, dan $d$**")
            st.markdown(
                "Menggunakan identitas sudut berpenyiku ($\\cos(90^\\circ - \\theta) = \\sin\\theta$ dan $\\sin(90^\\circ - \\theta) = \\cos\\theta$):"
            )
            st.latex(r"""
            \begin{aligned}
            \cos(90^\circ - h) &= \cos(90^\circ - L)\cos(90^\circ - d) + \sin(90^\circ - L)\sin(90^\circ - d)\cos(t) \\
            \sin(h) &= \sin(L)\sin(d) + \cos(L)\cos(d)\cos(t)
            \end{aligned}
            """)

            st.markdown("**Langkah 4: Isolasi $\\cos(t)$ dan Sudut Jam $t$**")
            st.latex(r"""
            \begin{aligned}
            \sin(h) - \sin(L)\sin(d) &= \cos(L)\cos(d)\cos(t) \\
            \cos(t) &= \frac{\sin(h) - \sin(L)\sin(d)}{\cos(L)\cos(d)} \\
            t &= \arccos\left(\frac{\sin(h) - \sin(L)\sin(d)}{\cos(L)\cos(d)}\right)
            \end{aligned}
            """)

            st.markdown(
                f"**Contoh Substitusi Nilai Aktif (saat kulminasi $h = {h_kulminasi:.4f}^\\circ$, $L = {L_deg:.2f}^\\circ$, $d = {d_deg:.4f}^\\circ$):**"
            )
            st.latex(
                f"\\cos(t) = \\frac{{\\sin({h_kulminasi:.2f}^\\circ) - \\sin({L_deg:.2f}^\\circ)\\sin({d_deg:.2f}^\\circ)}}"
                f"{{\\cos({L_deg:.2f}^\\circ)\\cos({d_deg:.2f}^\\circ)}} "
                f"= \\frac{{{sin_h_k:+.5f} - ({sin_L:+.5f} \\times {sin_d:+.5f})}}"
                f"{{{cos_L:.5f} \\times {cos_d:.5f}}} = {cos_t_k:+.6f} \\Rightarrow t = {t_k_deg:.4f}^\\circ"
            )
            st.markdown(
                "**Cara memakai di waktu shalat lain:** Cukup ganti nilai **$h$** sesuai kriteria masing-masing (misal $h = h_{\\text{ashar}}$ untuk Ashar, $h = -20^\\circ / -18^\\circ / -15^\\circ$ untuk Subuh, atau $h = -18^\\circ / -17^\\circ / -15^\\circ$ untuk Isya), lalu ubah $t$ menjadi jam dengan membagi $15^\\circ$ per jam ($\\Delta T = t / 15^\\circ$)."
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
        st.caption("Visualisasi 3D: Segitiga bola P–Z–M saat Matahari melintasi meridian lokal (kulminasi atas) terhadap Horizon dan Ekuator Langit.")

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

        S_contoh = 1.0
        b0_contoh = S_contoh * tan_z0
        b_jumhur_contoh = S_contoh + b0_contoh
        b_hanafi_contoh = 2.0 * S_contoh + b0_contoh

        st.markdown("**Geometri Bayangan Gnomon & Sudut Tinggi Matahari ($h_{\\text{ashar}}$)**")
        st.plotly_chart(
            plot_geometri_bayangan_ashar(
                S_contoh, jarak_zenith_kulminasi, b0_contoh,
                b_jumhur_contoh, b_hanafi_contoh, h_ashar_jumhur, h_ashar_hanafi
            ),
            use_container_width=True
        )
        st.caption("Ilustrasi Geometri Bayangan (S = 1.00 m): Menghubungkan jarak zenith kulminasi (z0), panjang bayangan (B0, B_J, B_H), dan sudut elevasi matahari (h_ashar).")

        with st.expander("🔍 Proses Penurunan Rumus Tinggi Matahari Ashar (Langkah 1–3)"):
            st.markdown(
                f"**Acuan Parameter & Nilai Awal:**\n"
                f"- Lintang $L = {L_deg:.2f}^\\circ$ dan deklinasi $d = {d_deg:.4f}^\\circ$, sehingga jarak zenith kulminasi $z_0 = |L - d| = {jarak_zenith_kulminasi:.4f}^\\circ$\n"
                f"- Tinggi tongkat / gnomon tegak $S = {S_contoh:.2f}\\text{{ m}}$\n"
                f"- Kulminasi: `{format_jam_wib(meridian_pass_jam)}`, *Ikhtiyath*: `{ikhtiyath_menit}` menit"
            )

            st.markdown("**Langkah 1: Panjang Bayangan Saat Kulminasi ($B_0$)**")
            st.markdown(
                "- **Posisi sudut:** Sudut $z_0 = |L - d|$ diukur di **puncak tongkat** (antara garis vertikal/zenith dan sinar matahari saat kulminasi atas).\n"
                "- **Hubungan trigonometri:** Sisi di depan sudut $z_0$ adalah bayangan kulminasi ($B_0$) dan sisi di sampingnya adalah tinggi tongkat ($S$), sehingga $\\tan(z_0) = \\frac{B_0}{S}$."
            )
            st.latex(r"B_0 = S \cdot \tan|L - d|")
            st.latex(f"B_0 = {S_contoh:.2f} \\times \\tan({jarak_zenith_kulminasi:.4f}^\\circ) = {b0_contoh:.5f}\\text{{ m}}")

            st.markdown("**Langkah 2: Panjang Bayangan Total Saat Awal Ashar ($B$)**")
            st.markdown(
                "- **Makna syarat bayangan:** Setelah kulminasi, matahari bergerak ke arah barat sehingga bayangan memanjang menjadi bayangan kulminasi ($B_0$) ditambah kelipatan tinggi tongkat ($n \\cdot S$). Dengan mensubstitusikan $B_0 = S \\cdot \\tan|L - d|$ lalu memfaktorkan $S$:"
            )
            st.latex(r"""
            \begin{aligned}
            B &= n \cdot S + B_0 \\
              &= n \cdot S + S \cdot \tan|L - d| \\
              &= S\bigl(n + \tan|L - d|\bigr)
            \end{aligned}
            """)
            st.markdown(
                f"- **Jumhur ($n = 1$):** $B_{{\\text{{jumhur}}}} = 1 \\times {S_contoh:.2f} + {b0_contoh:.5f} = \\mathbf{{{b_jumhur_contoh:.5f}\\text{{ m}}}}$\n"
                f"- **Hanafi ($n = 2$):** $B_{{\\text{{hanafi}}}} = 2 \\times {S_contoh:.2f} + {b0_contoh:.5f} = \\mathbf{{{b_hanafi_contoh:.5f}\\text{{ m}}}}$"
            )

            st.markdown("**Langkah 3: Konversi Bayangan ke Tinggi Matahari ($h_{\\text{ashar}}$), Sudut Jam ($t$) & Jam**")
            st.markdown(
                "- **Mengapa muncul $\\cot(h_{\\text{ashar}})$?** Sudut tinggi matahari $h_{\\text{ashar}}$ diukur di **ujung bayangan di tanah** (antara bidang datar dan sinar matahari), sehingga $\\tan(h_{\\text{ashar}}) = \\frac{S}{B}$ dan kebalikannya adalah $\\cot(h_{\\text{ashar}}) = \\frac{B}{S} = n + \\tan|L - d|$."
            )
            st.latex(r"h_{\text{ashar}} = \arctan\left(\frac{1}{n + \tan|L - d|}\right)")
            st.markdown(
                f"- **Jumhur ($n = 1$):** $h_{{\\text{{ashar}}}} = \\mathbf{{{h_ashar_jumhur:.4f}^\\circ}}$ $\\rightarrow$ $t = {t_jumhur:.4f}^\\circ$ (`{format_durasi(t_jumhur)}` setelah kulminasi) $\\rightarrow$ **Jam Ashar = `{format_jam_wib(wib_jumhur)}`**\n"
                f"- **Hanafi ($n = 2$):** $h_{{\\text{{ashar}}}} = \\mathbf{{{h_ashar_hanafi:.4f}^\\circ}}$ $\\rightarrow$ $t = {t_hanafi:.4f}^\\circ$ (`{format_durasi(t_hanafi)}` setelah kulminasi) $\\rightarrow$ **Jam Ashar = `{format_jam_wib(wib_hanafi)}`**"
            )
            st.markdown("Nilai $h_{\\text{ashar}}$ kemudian disubstitusikan ke rumus sudut jam bola langit:")
            st.latex(r"\cos(t) = \frac{\sin(h) - \sin(L)\sin(d)}{\cos(L)\cos(d)}")

        with st.expander("📐 Penurunan Rumus Sudut Jam cos(t) untuk Waktu Ashar"):
            render_blok_substitusi_cos_t("Ashar Jumhur", h_ashar_jumhur, L_deg, d_deg)
            st.markdown("---")
            render_blok_substitusi_cos_t("Ashar Hanafi", h_ashar_hanafi, L_deg, d_deg)

    with col_a2:
        titik_ashar = [
            {"label": f"Ashar Jumhur ({h_ashar_jumhur:.1f}°)", "h": h_ashar_jumhur, "A": hitung_azimuth_matahari(L_deg, d_deg, h_ashar_jumhur, True), "color": "orange"},
            {"label": f"Ashar Hanafi ({h_ashar_hanafi:.1f}°)", "h": h_ashar_hanafi, "A": hitung_azimuth_matahari(L_deg, d_deg, h_ashar_hanafi, True), "color": "red"},
            {"label": "Maghrib (Ufuk)", "h": h_maghrib_syuruq, "A": hitung_azimuth_matahari(L_deg, d_deg, h_maghrib_syuruq, True), "color": "purple"}
        ]
        st.plotly_chart(plot_perbandingan_3d(L_deg, titik_ashar), use_container_width=True)
        st.caption("Visualisasi 3D Bola Langit: Segitiga bola P–Z–M untuk posisi matahari di langit barat antara Ashar Jumhur (oranye) dan Ashar Hanafi (merah).")

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

        with st.expander("📐 Penurunan Rumus Sudut Jam cos(t) untuk Waktu Subuh (-20°, -18°, -15°)"):
            render_blok_substitusi_cos_t("Subuh Kemenag / MABIMS", -20.0, L_deg, d_deg)
            st.markdown("---")
            render_blok_substitusi_cos_t("Subuh Muhammadiyah", -18.0, L_deg, d_deg)
            st.markdown("---")
            render_blok_substitusi_cos_t("Subuh ISNA", -15.0, L_deg, d_deg)

    with col_s2:
        st.plotly_chart(plot_perbandingan_3d(L_deg, titik_subuh), use_container_width=True)
        st.caption("Visualisasi 3D: Segitiga bola P–Z–M untuk posisi matahari di bawah ufuk Timur pada kedalaman -20°, -18°, -15°, hingga saat terbit (Syuruq).")

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

        with st.expander("📐 Penurunan Rumus Sudut Jam cos(t) untuk Waktu Isya (-18°, -17°, -15°)"):
            render_blok_substitusi_cos_t("Isya Kemenag / MABIMS & Muhammadiyah", -18.0, L_deg, d_deg)
            st.markdown("---")
            render_blok_substitusi_cos_t("Isya Moderat", -17.0, L_deg, d_deg)
            st.markdown("---")
            render_blok_substitusi_cos_t("Isya ISNA", -15.0, L_deg, d_deg)

    with col_i2:
        st.plotly_chart(plot_perbandingan_3d(L_deg, titik_isya), use_container_width=True)
        st.caption("Visualisasi 3D: Segitiga bola P–Z–M untuk pergerakan matahari turun di bawah ufuk Barat mulai dari Maghrib hingga kedalaman Isya -15°, -17°, dan -18°.")

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
