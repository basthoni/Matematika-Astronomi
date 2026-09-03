elif pilihan_sistem == "A. Sistem Koordinat Horizon (Lokal)":
    st.markdown("""
    #### A. Sistem Koordinat Horizon (Lokal / Alt-Azimuth)
    * **Bidang Referensi:** Bidang horizon pengamat (cakrawala). Titik Zenith ($Z$) berada tepat di atas kepala, Nadir ($N'$) di bawah kaki, dan **Pengamat ($O$)** berada di pusat bola $(0,0,0)$.
    * **Parameter Koordinat:**
      1. **Tinggi (*Altitude* / $h$):** Jangkauan sudut benda langit diukur vertikal dari horizon ke arah bintang ($0^\circ$ s.d. $+90^\circ$).
      2. **Azimuth ($A$):** Sudut horizontal yang diukur dari titik Utara ($0^\circ$) berputar ke arah Timur ($90^\circ$), Selatan ($180^\circ$), dan Barat ($270^\circ$) sepanjang horizon.
    """)
    
    # Slider Interaktif untuk Horizon
    col1, col2 = st.columns(2)
    with col1:
        azimuth_deg = st.slider("Atur Azimuth (A) [Derajat]", 0, 360, 45, step=1)
    with col2:
        alt_deg = st.slider("Atur Tinggi / Altitude (h) [Derajat]", 0, 90, 30, step=1)
        
    az = np.radians(azimuth_deg)
    alt = np.radians(alt_deg)
    
    # Konversi koordinat bola ke Kartesius 3D (Z = tinggi, X = Utara/Selatan, Y = Timur/Barat)
    x_star = np.cos(alt) * np.cos(az)
    y_star = np.cos(alt) * np.sin(az)
    z_star = np.sin(alt)
    
    # Gambar Bidang Horizon
    theta = np.linspace(0, 2 * np.pi, 100)
    fig_coord.add_trace(go.Scatter3d(x=np.cos(theta), y=np.sin(theta), z=np.zeros_like(theta), mode='lines', line=dict(color='green', width=4), name='Bidang Horizon'))
    
    # Garis Proyeksi dari Bintang ke Bidang Horizon
    fig_coord.add_trace(go.Scatter3d(x=[x_star, x_star], y=[y_star, y_star], z=[0, z_star], mode='lines', line=dict(color='orange', width=3, dash='dash'), name='Garis Tinggi (Altitude)'))
    
    # Vektor Bintang dari Pusat Pengamat (0,0,0)
    fig_coord.add_trace(go.Scatter3d(x=[0, x_star], y=[0, y_star], z=[0, z_star], mode='lines', line=dict(color='red', width=5), name='Vektor Pengamatan Bintang'))
    
    # Titik Istimewa Horizon (Pusat, Zenith, Nadir, dan 4 Mata Angin Utama)
    hx = [0,  0,  0,  1,  0, -1,  0, x_star]
    hy = [0,  0,  0,  0,  1,  0, -1, y_star]
    hz = [1, -1,  0,  0,  0,  0,  0, z_star]
    htext = [
        'Zenith (Z)', 
        'Nadir (N\')', 
        'Pusat / Pengamat (O)', 
        'Utara (N, 0°)', 
        'Timur (E, 90°)', 
        'Selatan (S, 180°)', 
        'Barat (W, 270°)', 
        f'Bintang (h={alt_deg}°, A={azimuth_deg}°)'
    ]
    hcolor = ['green', 'gray', 'purple', 'blue', 'blue', 'blue', 'blue', 'red']
    
    fig_coord.add_trace(go.Scatter3d(
        x=hx, y=hy, z=hz,
        mode='text+markers',
        text=htext,
        marker=dict(size=[6, 6, 7, 6, 6, 6, 6, 8], color=hcolor),
        textfont=dict(size=11)
    ))
    fig_coord.update_layout(title=f"Simulasi 3D Interaktif: Koordinat Horizon (Alt: {alt_deg}°, Az: {azimuth_deg}°)")
