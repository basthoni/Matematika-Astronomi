import streamlit as st
import math

st.set_page_config(page_title="Bab 2 - Bola Langit", page_icon="🔭", layout="wide")

# CSS Khusus untuk membuat teks rata kanan-kiri (Justify)
st.markdown("""
<style>
div[data-testid="stMarkdownContainer"] p {
    text-align: justify;
}
</style>
""", unsafe_allow_html=True)

st.title("BAB II")
st.header("BOLA LANGIT (THE CELESTIAL SPHERE)")
st.divider()

# ==========================================
# DAFTAR ISI (SIDEBAR NAVIGATION)
# ==========================================
with st.sidebar:
    st.markdown("### 📑 Daftar Isi Bab II")
    st.markdown("""
    - [17. Pendahuluan](#17-pendahuluan)
    - [18. Ketinggian dan Azimut](#18-ketinggian-dan-azimut)
    - [19. Deklinasi dan Sudut Jam](#19-deklinasi-dan-sudut-jam)
    - [20. Diagram Belahan Bumi Selatan](#20-diagram-untuk-belahan-bumi-selatan)
    - [21. Bintang Sirkumpolar](#21-bintang-sirkumpolar-circumpolar-stars)
    - [22. Bola Langit Geosentrik](#22-bola-langit-standar-atau-geosentrik-the-standard-or-geocentric-celestial-sphere)
    - [23. Penyelesaian Segitiga PZX](#23-penyelesaian-dari-segitiga-bola-pzx)
    - [24. Asensio Rekta dan Deklinasi](#24-asensio-rekta-dan-deklinasi)
    - [25. Orbit Bumi](#25-orbit-bumi)
    - [26. Lintang dan Bujur Langit](#26-lintang-dan-bujur-langit)
    - [27. Waktu Sideris](#27-waktu-sideris)
    - [28. Waktu Matahari Rata-rata](#28-waktu-matahari-rata-rata)
    - [29. Contoh Penyelesaian](#29-contoh-penyelesaian)
    - [30. Sudut Jam Benda Langit](#30-sudut-jam-dari-sebuah-benda-langit)
    - [31. Terbit dan Terbenam](#31-terbit-dan-terbenam)
    - [32. Laju Perubahan Jarak Zenit](#32-laju-perubahan-jarak-zenit-dan-azimut)
    - [33. Senja dan Fajar (Twilight)](#33-senja-dan-fajar-twilight)
    - [Latihan Soal (Exercises)](#latihan-soal-exercises)
    """)

# ==========================================
# KONTEN UTAMA BAB II
# ==========================================

materi_bab_2_bagian_1 = r"""
### 17. Pendahuluan.
Pada Bab I, kita telah mempelajari bahwa penentuan posisi suatu tempat di permukaan bumi sepenuhnya berpatokan pada dua lingkaran besar utama, yaitu meridian Greenwich dan ekuator. Prinsip penentuan posisi pada bola langit pada dasarnya juga serupa. Terdapat beberapa metode yang bisa digunakan, bergantung pada lingkaran besar mana yang dipilih sebagai patokan utama. Metode-metode tersebut akan diuraikan sebagai berikut.

### 18. Ketinggian (*altitude*) dan azimut.
Misalkan $O$—seorang pengamat di permukaan bumi (yang diasumsikan berbentuk bola sempurna)—berada tepat di pusat bola langit (Gbr. 10). Misalkan pula $Z$
"""
st.markdown(materi_bab_2_bagian_1, unsafe_allow_html=True)
st.image("Gambar_10.png", caption="Gambar 10: Sistem Horizon, Zenith, Nadir, dan Horizon Astronomis", use_container_width=True)

materi_bab_2_bagian_2 = r"""
*(zenith)* adalah titik pada bola langit yang berada persis di atas kepala pengamat, yang arahnya dapat ditentukan menggunakan unting-unting (*plumb-line*). Oleh karena itu, garis $OZ$ merupakan perpanjangan dari garis lurus yang menghubungkan pusat bumi dengan $O$. Bidang yang melalui $O$ dan tegak lurus terhadap $OZ$ adalah bidang horizon, yang memotong bola langit pada lingkaran besar $NAS$. Lingkaran ini disebut sebagai horizon astronomis atau sekadar horizon. Dengan demikian, pada Gbr. 10, horizon membagi bola langit menjadi dua belahan (*hemisphere*); bagian atas adalah belahan langit yang terlihat (*visible hemisphere*), sedangkan bagian bawah tersembunyi dari pandangan pengamat oleh wujud bumi itu sendiri. 

Misalkan $X$ adalah posisi sebuah bintang di bola langit pada momen tertentu. Setiap lingkaran besar yang ditarik melewati titik $Z$ disebut sebagai lingkaran vertikal (*vertical circle*); secara khusus, lingkaran vertikal pada Gbr. 10 yang melewati $X$ adalah $ZXA$. Pada bidang $ZXA$, sudut $AOX$ atau busur lingkaran besar $AX$ disebut ketinggian (*altitude*), yang dilambangkan dengan $a$. Mengingat $OZ$ tegak lurus terhadap bidang horizon, panjang busur lingkaran besar $ZA$ adalah $90^\circ$; oleh karena itu, $ZX = 90^\circ - a$. $ZX$ ini disebut jarak zenit (*zenith distance*, disingkat z.d.) dari bintang $X$ dan dilambangkan dengan $z$. Dari sini kita mendapati:

$$ z = 90^\circ - a \dots\dots(1) $$

Misalkan $LXM$ adalah lingkaran kecil yang melewati $X$ dan sejajar dengan horizon; lingkaran ini dinamakan paralel ketinggian (*parallel of altitude*). Sifatnya sedemikian rupa sehingga semua benda langit yang kebetulan berada di lingkaran kecil ini pada waktu yang sama akan memiliki ketinggian yang sama, dan tentu saja, berdasarkan persamaan (1), memiliki jarak zenit yang sama dengan $X$. Oleh sebab itu, jika ketinggian atau jarak zenit sebuah bintang diketahui, letak paralel ketinggian bintang tersebut dapat dipastikan. Namun, untuk mendeskripsikan posisinya secara mutlak pada bola langit, kita juga harus menentukan letak lingkaran vertikal spesifik tempat bintang itu berada. Caranya adalah sebagai berikut.

Misalkan $OP$ sejajar dengan sumbu rotasi bumi. Jika lintang pengamat berada di wilayah utara (seperti pada Gbr. 10), posisi $P$ disebut kutub langit utara (*north celestial pole*), atau sekadar kutub utara (*north pole*). Kita memang tidak merasakan rotasi bumi secara langsung, namun efeknya tampak jelas pada pergerakan semu bola langit. Akibat rotasi ini, bintang-bintang tampak bergerak melintasi langit dan arahnya terus berubah. Walau begitu, bagi pengamat di belahan bumi utara, ada satu bintang yang bisa dilihat dengan mata telanjang dan letaknya nyaris tak berubah. Bintang ini adalah Polaris, atau bintang kutub utara, yang arahnya di langit hampir persis sejajar dengan garis $OP$. Seandainya ada sebuah bintang yang terletak tepat di titik $P$ pada bola langit, ketinggian dan arah bintang tersebut tidak akan berubah sepanjang malam. Kita mendefinisikan lingkaran vertikal yang melewati $P$, yaitu $ZPN$ (yang memotong horizon di $N$), sebagai lingkaran vertikal utama (*principal vertical circle*) dan titik $N$ itu sendiri sebagai titik utara horizon (*north point of the horizon*).

Titik $S$ pada horizon yang letaknya tepat berlawanan dengan $N$ adalah titik selatan (*south point*); sedangkan titik barat ($W$) dan timur ($E$) memiliki arah yang tegak lurus terhadap garis $N$ dan $S$ ($E$ tidak ditunjukkan pada Gbr. 10). Titik-titik $N, E, S$, dan $W$ inilah yang disebut titik-titik kardinal (*cardinal points*).

Kini kita dapat menentukan posisi bintang $X$ pada bola langit kapan saja dengan berpatokan pada horizon dan lingkaran vertikal utama $ZPN$. Jika bintang tersebut berada di ufuk barat bola langit (seperti Gbr. 10), sudut bola $PZX$ (yang dibentuk oleh lingkaran vertikal utama dan lingkaran vertikal yang melewati $X$) atau busur lingkaran besar $NA$ disebut azimut (*azimuth*, $W$). Sebaliknya, jika bintang berada di ufuk timur bola langit, seperti pada Gbr. 11, sudut $PZX$
"""
st.markdown(materi_bab_2_bagian_2, unsafe_allow_html=True)
st.image("Gambar_11.png", caption="Gambar 11: Sistem Azimut (Timur/Barat) dan Titik Kardinal", use_container_width=True)

materi_bab_2_bagian_3 = r"""
atau busur $NB$ adalah azimut ($E$). Kesimpulannya, pada saat kapan pun, posisi benda langit dapat diuraikan secara utuh menggunakan patokan horizon dan titik utara horizon dalam besaran ketinggian dan azimut ($E$ atau $W$), atau bisa juga dalam besaran jarak zenit dan azimut. Ketika azimut menunjukkan angka $90^\circ$ $E$ atau $90^\circ$ $W$, bintang tersebut dikatakan berada pada vertikal utama (*prime vertical*), yakni lingkaran vertikal yang memotong langsung titik timur $E$ atau titik barat $W$.

Karena pada Gbr. 10 dan 11 sudut $POZ$ (atau busur lingkaran besar $PZ$) ekuivalen dengan sudut antara jari-jari bumi di posisi pengamat dan sumbu rotasi bumi, maka $P\hat{O}Z$ (atau $PZ$) nilainya sama dengan ko-lintang pengamat, yaitu:

$$ PZ = 90^\circ - \phi \dots\dots(2) $$

di mana $\phi$ adalah lintang pengamat. Di samping itu, $PN = 90^\circ - PZ = \phi$; sehingga dapat disimpulkan bahwa ketinggian kutub langit sama persis dengan lintang tempat pengamat berada.

*(Catatan kaki: Posisi $W$ dan $E$ relatif terhadap $N$ dan $S$ dilogikakan dari kenyataan bahwa jika seorang pengamat menghadap ke utara, titik barat berada di sebelah kirinya dan titik timur di sebelah kanannya).*

### 19. Deklinasi dan sudut jam (*declination and hour angle*).
Seperti pembahasan di bagian sebelumnya, bayangkan bola langit dipetakan untuk pengamat $O$ di lintang $\phi$, yang menampilkan letak horizon, zenit $Z$, dan kutub utara $P$ (Gbr. 12). Lingkaran besar $RWT$ yang bidangnya tegak lurus terhadap $OP$ adalah ekuator langit (*celestial equator*), di mana bidangnya sejajar dengan ekuator bumi. Ekuator langit dan horizon saling berpotongan di dua titik, yakni $W$ dan $E$. Mengingat $Z$ adalah kutub dari lingkaran besar $NWS$ dan $P$ adalah kutub dari lingkaran besar $RWT$, maka letak $W$ berjarak $90^\circ$ baik dari $Z$ maupun dari $P$.
"""
st.markdown(materi_bab_2_bagian_3, unsafe_allow_html=True)
st.image("Gambar_12.png", caption="Gambar 12: Sistem Ekuator Lokal (Deklinasi dan Sudut Jam)", use_container_width=True)

materi_bab_2_bagian_4 = r"""
Dengan kata lain, $W$ berjarak $90^\circ$ dari semua titik pada lingkaran besar yang melintasi $Z$ dan $P$, yang menjadikannya kutub dari lingkaran besar $NPZSQ$. Maka dari itu, $NW = 90^\circ$ dan $WS = 90^\circ$. Hal yang sama juga berlaku untuk $EN = 90^\circ$ dan $ES = 90^\circ$. Ini membuktikan bahwa $W$ dan $E$ mengisi tempat untuk dua titik kardinal yang tersisa, melengkapi $N$ dan $S$ yang telah dijabarkan sebelumnya.

Sebagaimana telah disebutkan, rotasi bumi memicu pergerakan semu bola langit dari arah timur ke barat yang mengitari sumbu $OP$. Berhubung jarak bintang-bintang teramat jauh dibandingkan bumi, sudut antara garis pandang dari pengamat di $O$ menuju suatu bintang dengan sumbu $OP$ praktis tidak berubah. Jika kita meninjau sebuah bintang $X$, rotasi bumi menyebabkan bintang tersebut seakan-akan bergerak menelusuri lingkaran kecil $LXM$ yang posisinya sejajar dengan ekuator langit, bergerak searah dengan anak panah pada Gbr. 12. Misalkan $PXDQ$ adalah semi-lingkaran besar yang melewati $X$ serta kutub-kutub bola langit. Panjang busur $DX$ inilah yang disebut deklinasi bintang. Nilainya positif (utara) jika bintang berada di antara ekuator langit dan kutub utara $P$ (seperti pada bintang $X$), dan bernilai negatif (selatan) jika ia berada di antara ekuator dan kutub selatan $Q$ (seperti pada bintang $Y$). Dengan demikian, konsep deklinasi sangat mirip dengan garis lintang di permukaan bumi. Jika deklinasi $X$ kita notasikan sebagai $\delta$, maka $DX = \delta$ dan $PX = 90^\circ - \delta$. Besaran $PX$ ini disebut jarak kutub utara (*north polar distance*, N.P.D.) sang bintang. Untuk menyederhanakan hitungan, deklinasi diperlakukan sebagai besaran aljabar agar rumusnya berlaku universal baik untuk deklinasi utara maupun selatan. Deklinasi utara diberi tanda positif ($+$) dan selatan negatif ($-$). Berkat konvensi ini, rumus jarak kutub utara N.P.D. $= 90^\circ - \delta$ akan selalu valid tanpa peduli di belahan langit mana bintang itu berada.

Saat nilai deklinasi sebuah bintang sudah kita pegang, kita bisa mengetahui dengan pasti di lingkaran kecil mana ia beredar—yang dikenal sebagai paralel deklinasi (*parallel of declination*). Namun, agar letaknya di bola langit pada suatu momen bisa dipastikan, kita butuh satu lingkaran besar lagi sebagai acuan, yaitu semi-lingkaran besar $PZRSQ$ yang disebut meridian pengamat (*observer's meridian*). Sewaktu bintang tersebut menyentuh titik $L$ di meridian pengamat, bintang itu dikatakan sedang transit (*transit*) atau mencapai kulminasi (*culminate*). Gbr. 12 memperlihatkan bahwa di titik inilah ketinggiannya ($SL$) mencapai titik tertinggi dan jarak zenitnya ($ZL$) berada di titik terendah. Selepas itu, seiring bumi berputar, bintang tersebut terus bergeser menyusuri lingkaran kecil $LFM$ sampai akhirnya memotong horizon di titik $F$. Di sinilah bintang dikatakan terbenam (*set*); ketinggiannya di $F$ tentu $0^\circ$ dengan jarak zenit $90^\circ$. Bergantung pada besaran deklinasinya, bintang akan menghabiskan waktu tertentu di bawah horizon hingga menyentuh titik paling depresif (terdalam) di $M$, sebelum akhirnya terbit kembali di titik $G$ pada horizon. Ketinggiannya perlahan-lahan bertambah sampai kembali bertengger di meridian pengamat $L$, menyelesaikan siklus satu putaran penuh bumi. Kapan pun itu, posisi bintang pada paralel deklinasinya ditandai oleh sudut di $P$, yakni sudut antara meridian pengamat dan meridian ($PXQ$) yang menyertai bintang pada momen tersebut. Sudut ini dinamakan sudut jam (*hour angle*, lambang $H$), yaitu sudut $RPX$ (atau $ZPX$) atau ekuivalen dengan busur $RD$ pada ekuator. Sudut ini diukur dari meridian pengamat ke arah barat, mulai dari $0^\circ$ (saat transit di $L$) hingga $360^\circ$ (saat kembali lagi), atau yang paling lumrah menggunakan rentang waktu $0^h$ hingga $24^h$. Proses ini juga bisa dibayangkan begini: saat transit, meridian bintang menyatu dengan meridian pengamat; setelah itu, ia merayap ke arah barat, dan ketika sudah berkeliling bola langit sepenuhnya, meridian tersebut telah menyapu sudut $360^\circ$ atau $24^h$. Berdasarkan Gbr. 12, jika bintang berada di belahan barat meridian pengamat—yang artinya
"""
st.markdown(materi_bab_2_bagian_4, unsafe_allow_html=True)
st.image("Gambar_13.png", caption="Gambar 13: Diagram Sudut Jam Barat dan Timur Meridian", use_container_width=True)

materi_bab_2_bagian_5 = r"""
azimutnya bernilai barat—sudut jamnya pasti jatuh di kisaran $0^\circ$ dan $180^\circ$ (antara $0^h$ dan $12^h$). Kebalikannya, jika bintang ada di ufuk timur meridian (azimut timur) seperti pada Gbr. 13, sudut jamnya berada di antara $12^h$ dan $24^h$. Dari pemahaman ini, kita bisa menarik sebuah pedoman baku:
*Jika azimut bintang menunjuk ke barat, sudut jamnya berada di rentang $0^h$ hingga $12^h$ (dan berlaku sebaliknya); jika azimutnya timur, sudut jamnya merentang dari $12^h$ hingga $24^h$.*

### 20. Diagram untuk belahan bumi selatan.
Diagram-diagram yang telah dibahas sebelumnya dirancang untuk pengamat di wilayah lintang utara. Kini kita akan membedah diagram yang serupa bagi pengamat di belahan bumi selatan. Mengacu pada Gbr. 14, zenit pengamat diposisikan sama seperti diagram sebelumnya bersama horizonnya. Hanya saja, untuk belahan bumi selatan, kutub langit selatan $Q$-lah yang bertengger di atas horizon. Bila $\phi$ mendeskripsikan lintang selatan pengamat, maka $QZ = 90^\circ - \phi$. Lingkaran vertikal utamanya sekarang beralih ke $ZQS$, yang berpotongan dengan horizon di titik selatan $S$, sehingga letak titik utara $N$ dapat dipetakan di diagram. Ekuator langit berpapasan dengan horizon di titik barat dan timur ($W$ dan $E$, meski $E$ tak terlihat di Gbr. 14) selaras dengan
"""
st.markdown(materi_bab_2_bagian_5, unsafe_allow_html=True)
st.image("Gambar_14.png", caption="Gambar 14: Bola Langit untuk Pengamat di Belahan Bumi Selatan", use_container_width=True)

materi_bab_2_bagian_6 = r"""
aturan arah pada catatan kaki halaman 27. Coba perhatikan sebuah bintang $X$ yang berdeklinasi selatan. Bumi yang berputar memaksanya merunut lingkaran kecil $LXM$ yang sejajar dengan ekuator langit, terselip di antara ekuator dan kutub selatan $Q$. Puncak ketinggiannya digapai di titik $L$, tatkala ia singgah di meridian pengamat (semi-lingkaran $QZRNP$). Dari titik transit itu, bintang merambat ke arah barat menyusuri $LXM$ sesuai arah anak panah. Sudut $ZQX$ berperan sebagai sudut jam, yang ditakar dari $0^h$ menuju $24^h$ bergeser ke arah barat. Adapun $QZX$ merupakan azimutnya, yang dalam hal ini menunjuk arah barat. Jika deklinasi (negatif) sang bintang adalah $\delta$, maka $DX = -\delta$ dan $QX = 90^\circ + \delta$. Rincian elemen lain untuk segitiga bola $QZX$ meliputi: $QZ = 90^\circ - \phi$, $ZX = z$ (jarak zenit), $QZX = A$ (azimut), dan $ZQX = H$ (sudut jam). Apabila azimut bintang bernilai barat, sudut jamnya jatuh di angka $0^h$ sampai $12^h$. Bila azimutnya timur, kita bisa merancang diagram yang identik—yang bisa dijadikan ajang latihan bagi pembaca—di mana sudut jamnya kelak bernilai antara $12^h$ hingga $24^h$. Pedoman yang dicetuskan di akhir Bagian 19 mutlak berlaku baik untuk lintang utara maupun selatan.

### 21. Bintang sirkumpolar (*circumpolar stars*).
Amati bola langit bagi seorang pengamat di lintang utara $\phi$ (Gbr. 15). Ada dua paralel deklinasi yang terlukis untuk bintang $X$ dan $Y$. Keduanya senantiasa melayang di atas cakrawala alias tidak pernah sudi terbenam. Bintang-bintang dengan rute seperti ini dilabeli sebagai bintang sirkumpolar:
"""
st.markdown(materi_bab_2_bagian_6, unsafe_allow_html=True)
st.image("Gambar_15.png", caption="Gambar 15: Bintang Sirkumpolar yang Tidak Pernah Terbenam", use_container_width=True)

materi_bab_2_bagian_7 = r"""
Dari sketsa tersebut, terpampang jelas bahwa syarat mutlak agar sebuah bintang tidak tenggelam adalah busur $PM$ harus lebih pendek daripada $PN$. Atau dengan bahasa matematis, jarak kutub utaranya harus lebih kecil ketimbang nilai lintangnya, alias deklinasinya wajib lebih besar dari ko-lintang pengamat.

Manakala bintang $X$ menapak di meridian pengamat pada titik $L$, ia dikatakan berada pada kulminasi atas (*upper culmination*) atau sedang transit (*in transit*). Sebaliknya, saat ia tergelincir ke titik $M$, ia menduduki kulminasi bawah (*lower culmination*). Tak jarang orang juga menggunakan frasa "kulminasi di atas kutub" dan "kulminasi di bawah kutub". Tatkala kulminasi atas berlangsung, jarak zenit bintang adalah $ZL$ atau $(PL - PZ)$, yang nilainya tak lain $\phi - \delta$. Saat kulminasi bawah, jarak zenit merenggang menjadi $ZM$ atau $(ZP + PM)$, yakni $180^\circ - (\phi + \delta)$. Jika kebetulan $\delta = \phi$, kulminasi atasnya bakal mekar tepat di titik zenit. Namun, bila $\delta > \phi$, transit puncaknya berlokasi di sela-sela $P$ dan $Z$ (sebagaimana lakon bintang $Y$), yang memastikan azimutnya takkan melampaui $90^\circ$, sebuah konklusi yang gampang dicerna dari diagram. Konsep yang persis sama juga dapat ditautkan pada fenomena bintang sirkumpolar selatan.

### 22. Bola langit standar atau geosentrik (*The standard or geocentric celestial sphere*).
Pada penjabaran sebelumnya, deklinasi bintang diukur berpijak pada bola langit yang pusatnya ada di posisi pengamat. Lantaran bintang-bintang membentang di jarak yang luar biasa jauh bila disandingkan dengan secuil ukuran bumi, deklinasi atau jarak kutub yang direkam dengan metode ini terbukti imun dari pengaruh letak sang pengamat di muka bumi, seperti yang tersaji di Gbr. 16. (Agar lebih membumi untuk saat ini, kita condong memakai jarak kutub utara ketimbang deklinasi). Pada Gbr. 16, $P_1CQ_1$ merangkai sumbu rotasi bumi dengan sentrum bumi di $C$. $O$ adalah pengamat, $COZ$ adalah pilar zenit di $O$, $OP$ sejajar dengan $CP_1$, sementara arah bintang tatkala
"""
st.markdown(materi_bab_2_bagian_7, unsafe_allow_html=True)
st.image("Gambar_16.png", caption="Gambar 16: Perbandingan Posisi Pengamat di Permukaan dan Pusat Bumi", use_container_width=True)

materi_bab_2_bagian_8 = r"""
ia bertransit di $O$ diwakili oleh $OX$. Berpatokan pada definisi, jarak kutub utara bagi pengamat di $O$ terejawantah dalam sudut $P\hat{O}X$. Jika kita menarik garis $CY$ yang sejajar dengan $OX$, garis $CY$ ini sontak mendelegasikan arah bintang apabila ditarik dari inti bumi $C$. Imbasnya, $P_1\hat{C}Y = P\hat{O}X$. Boleh dikata, nilai jarak kutub utara (dan merembet ke deklinasinya) tetap konstan, entah itu diukur dari bola langit berpusat di $O$ maupun dari sentrum bumi $C$. Akan tetapi, ceritanya bakal berbalik arah bila kita mengamati benda-benda "tetangga" seperti bulan, matahari, atau jajaran planet. Di sini, patokan jarak kutub utara (dan deklinasi) akan sangat bergantung di bumi belahan mana si pengamat memijakkan kakinya. Ambil contoh, apabila $M$ merepresentasikan bulan (Gbr. 16) yang terpisah sejauh $r$ dari pusat bumi, sudah barang tentu $P\hat{O}M = P_1\hat{C}M + O\hat{M}C$. Celah sudut $O\hat{M}C$ sangat labil karena dikendalikan oleh koordinat pengamat $O$, sementara sudut $P_1\hat{C}M$ kebal dan sepenuhnya independen
"""
st.markdown(materi_bab_2_bagian_8, unsafe_allow_html=True)
st.image("Gambar_17.png", caption="Gambar 17: Bola Langit Standar atau Geosentrik Berpusat di Pusat Bumi", use_container_width=True)

materi_bab_2_bagian_9 = r"""
dari lokasi $O$. Oleh sebab itu, sudut $P_1\hat{C}M$ diresmikan sebagai jarak kutub utara sang bulan $M$, yakni sudut pamungkas antara poros bumi dan garis imajiner yang menjembatani pusat bumi ke benda langit yang bersangkutan. Standar ini berlaku mutlak bagi seluruh jajaran benda langit. Berangkat dari kesepakatan inilah, titik pusat bola langit standar (atau bola langit geosentrik) akhirnya dipatok di $C$, titik pusat bumi (Gbr. 17). Di sinilah $CZ$ mewakili panah zenit pengamat, diameter $QCP$ selaras dengan poros bumi, $NWSE$ membentangkan cakrawala langit (lingkaran besar yang bidangnya tegak lurus menantang $CZ$), dan $RWTE$ mengukir ekuator langit (bidang yang berbaur dengan ekuator bumi). Busur $PX$ menjelma menjadi jarak kutub utara seturut definisi baru tersebut, dan $DX$ bertindak sebagai deklinasi $\delta$ (dengan N.P.D. $= 90^\circ - \delta$). Meridian pengamat mengambil rute $PZRSQ$, jarak zenit benda langit dikunci di $ZX$ (atau $z$), seraya azimut $A$ (sudut $P\hat{Z}X$) dan sudut jam $H$ (sudut $Z\hat{P}X$) dijabarkan seperti porsi sebelumnya. Catatan deklinasi untuk benda-benda langit pentolan (bulan, matahari, planet, dan jajaran bintang terang) telah dihimpun dan dikatalogkan dalam *Astronomical Ephemeris* serta berbagai efemeris nasional lainnya.

Mulai dari titik ini dan seterusnya, kita akan selalu memproyeksikan bola langit dengan sumbu pusat yang bertumpu kokoh di $C$, alias jantung bumi (Gbr. 17).

### 23. Penyelesaian segitiga bola PZX.
Kita akan memecahkan dua studi kasus krusial yang bersinggungan erat dengan segitiga bola $PZX$:
(i) Jika parameter lintang pengamat $\phi$, deklinasi $\delta$, dan sudut jam $H$ dari suatu benda langit sudah diketahui, carilah nilai jarak zenit dan azimutnya. Berbekal rumus kosinus (**Rumus A**), berhubung panjang dua sisi $PZ$ dan $PX$ serta sudut yang mengapitnya ($ZPX$) telah diketahui (Gbr. 17), kita bisa merumuskan:

$$ \cos ZX = \cos PZ \cos PX + \sin PZ \sin PX \cos ZPX $$

atau

$$ \cos z = \sin \phi \sin \delta + \cos \phi \cos \delta \cos H \dots\dots(3) $$

Dari formulasi (3) di atas, $z$ bisa dieksekusi secara instan, atau bisa juga diterjemahkan ke dalam rumusan haversine (Bagian 13), yang wujudnya menjadi:

$$ \text{hav } z = \text{hav } (\phi - \delta) + \cos \phi \cos \delta \text{ hav } H \dots\dots(4) $$

Melangkah lebih jauh, kita pakai lagi **Rumus A**:

$$ \cos PX = \cos PZ \cos ZX + \sin PZ \sin ZX \cos PZX $$

atau

$$ \sin \delta = \sin \phi \cos z + \cos \phi \sin z \cos A \dots\dots(5) $$

dari sinilah nilai azimut $A$ bisa digali. Jika dikonversi ke jubah haversine, persamaan (5) bermetamorfosis menjadi:

$$ \cos \phi \cos a \text{ hav } A = \text{hav } (90^\circ - \delta) - \text{hav } (\phi - a) \dots(6) $$

di mana variabel $a$ mewakili ketinggian (*altitude*).

(ii) Jika yang tersaji adalah lintang pengamat $\phi$, jarak zenit $z$, dan azimut $A$, tentukan letak deklinasi bintang dan sudut jamnya. Melalui persamaan (5), karena trinitas $\phi, z$, dan $A$ sudah di tangan, kita bisa mengulik nilai deklinasi $\delta$. Persamaan (3) atau (4) lantas mengambil alih untuk membedah sudut jam $H$. Mengukus persamaan (3), kita meraup:

$$ \cos H = \cos z \sec \phi \sec \delta - \tan \phi \tan \delta \dots\dots(7) $$

Mari kita tengok lagi segitiga bola $PZX$ pada Gbr. 13. Sudut $PZX$ bertindak sebagai azimut timur. Mengingat sudut jam ditakar di kutub dari arah meridian pengamat menyisir ke barat, maka dipastikan $Z\hat{P}X = 24^h - H$. Alur penyelesaian untuk segitiga jenis ini bisa diteruskan menggunakan irama yang serupa.

### 24. Asensio rekta dan deklinasi.
Dalam siasat sudut jam dan deklinasi untuk menetapkan koordinat bintang di atas kanvas langit, nyatanya hanya ada satu variabel (deklinasi) yang konsisten tak goyah saat bintang menyisir angkasa, sementara sudut jamnya memanjat naik secara linear dari $0^h$ hingga $24^h$. Akan tetapi,
"""
st.markdown(materi_bab_2_bagian_9, unsafe_allow_html=True)
st.image("Gambar_18.png", caption="Gambar 18: Asensio Rekta dan Deklinasi pada Bola Langit", use_container_width=True)

materi_bab_2_bagian_10 = r"""
konstelasi bintang di bola langit sejatinya bisa diibaratkan bak pilar-pilar statis di permukaan bumi. Oleh karenanya, letak mereka dapat dipatenkan dengan bersandar pada ekuator langit dan satu titik pijakan khusus di ekuator tersebut. Kita ambil contoh pada Gbr. 18, andaikan $\Upsilon$ mewakili titik pijakan di ekuator dan $X$ adalah sang bintang; anggap pula meridian yang menyeret $X$ membelah ekuator langit di simpul $D$. Seiring bergeraknya taburan bintang melintasi kanvas langit, kita mafhum bahwa deklinasi bintang $X$ (yakni $DX$) mutlak konstan dan formasi antarbintang tak saling sikut alias ajeg. Implikasinya, rentang busur $\Upsilon D$ juga bersifat kekal; atau dengan kata lain, gap sudut antara meridian $\Upsilon$ dan meridian $D$ takkan pernah lapuk. Kita bisa mendaulat $\Upsilon$ sebagai titik nol di ekuator langit, lalu bermodalkan titik inilah kita menelusuri lokasi bintang $X$ lewat jejaki busur lingkaran besar $\Upsilon D$ dan deklinasi $DX$. Dalam khazanah astronomi, titik nol ini didapuk dengan gelar ekuinoks musim semi (*vernal equinox*) atau titik awal Aries, yang letak pastinya bisa dicantolkan pada rasi bintang tertentu (kita akan mendetailkannya nanti). Nah, busur $\Upsilon D$ atau sudut $\Upsilon\hat{P}X$ ini dikenal luas sebagai asensio rekta (*right ascension*, R.A.) bintang $X$ (disimbolkan $\alpha$), yang dijabarkan memanjang ke timur dari $\Upsilon$ mulai $0^h$ hingga $24^h$ (sejalan dengan alur panah mungil di samping $\Upsilon$). Jalur pengukuran asensio rekta ini berjalan menentang arus pengukuran sudut jam. Menilik Gbr. 18, kentara bahwa $R\Upsilon = RD + \Upsilon D$. Di persimpangan ini, $RD$ (atau $R\hat{P}X$) menjelma menjadi sudut jam $H$ dari si bintang $X$, sementara $R\Upsilon$ bertindak sebagai sudut jam dari sang titik $\Upsilon$. Sudut jam dari titik ekuinoks $\Upsilon$ inilah yang dinamakan waktu sideris (*sidereal time*, S.T.). Beranjak dari sana, lahirlah sebuah hubungan yang elegan:

$$ \text{Waktu sideris} = \text{H.A. } X + \text{R.A. } X \dots\dots(8) $$

atau secara ringkas:

$$ \text{S.T.} = H + \alpha \dots\dots(9) $$

Di momen titik $\Upsilon$ memijak persis di meridian pengamat, sudut jamnya sontak bernilai $0^h$, yang berimplikasi pada waktu sideris yang juga menunjukkan $0^h$. Tatkala titik $\Upsilon$ tuntas berkeliling dan kembali menyapa meridian pengamat, itu artinya selang waktu sepadan $24^h$ waktu sideris telah purna. Durasi ini selaras seratus persen dengan interval yang dibutuhkan bumi untuk menuntaskan satu piruet penuh pada porosnya, yang dinamai sebagai satu hari sideris (*sidereal day*). Pada hakikatnya, putaran bumilah yang bertindak selaku maestro penunjuk waktu standar kita.

### 25. Orbit bumi.
Bumi tak ubahnya planet pengembara yang mengitari matahari merunut jalur elips (orbit), di mana sang mentari bertahta di salah satu titik fokus $S$ dari elips tersebut (Gbr. 19). Hal ini mengejawantahkan hukum pergerakan planet pertama dari Kepler. Waktu tempuh bumi untuk merampungkan satu putaran orbit diresmikan sebagai satu tahun. Selama bumi merangkai perjalanannya, sudut pandang dari bumi ke matahari perlahan-lahan bergeser, dan kecepatan lengkungnya tak selalu seragam. Karena kita bertengger dan mengamati semesta dari bumi, maka dari kacamata kita, mataharilah yang seolah-olah menggariskan orbit elips memutari bumi. Mengupas Gbr. 20, $C$ adalah inti bumi dan elips yang tergambar merupakan potret orbit semu matahari. Urut-urutan jejak matahari ($a, e, f, b, g$) pada orbit bayangan ini berkorelasi rapi dengan urutan singgah bumi ($A, E, F, B, G$) di lintasan aslinya memutari matahari (Gbr. 19). Menelan waktu setahun penuh, matahari dengan demikian
"""
st.markdown(materi_bab_2_bagian_10, unsafe_allow_html=True)

st.image("Gambar_19.png", caption="Gambar 19: Orbit Bumi Mengelilingi Matahari", use_container_width=True)
st.image("Gambar_20.png", caption="Gambar 20: Orbit Semu Matahari Relatif Terhadap Bumi", use_container_width=True)

materi_bab_2_bagian_11 = r"""
tampak sempurna merampungkan satu putaran melintasi langit dengan lanskap bintang-bintang sebagai latarnya. Dataran yang menampung orbit ini dijuluki bidang ekliptika, dan titik silang bidang ini dengan bola langit yang bertumpu di $C$ (inti bumi) memahat sebuah lingkaran besar gagah yang disapa sebagai ekliptika. Tengoklah Gbr. 21, misalkan $C$ adalah pusaran bola langit yang mengasuh ekuator langit $\Upsilon TR$ serta kutub utara $P$. Apabila taburan bintang dipantau merujuk pada pusat bumi $C$, mereka akan menduduki posisi yang spesifik di sekujur bola langit. Jika disandingkan dengan rasi bintang, bentangan ekliptika memiliki sandaran yang statis, merajut lingkaran besar khusus yang bertengger miring pada sudut sekitar $23\frac{1}{2}^\circ$ menantang ekuator langit. Di dalam Gbr. 21, busur $\Upsilon \Upsilon M U$ memerankan figur ekliptika seraya
"""
st.markdown(materi_bab_2_bagian_11, unsafe_allow_html=True)
st.image("Gambar_21.jpg", caption="Gambar 21: Ekliptika, Kemiringan, dan Titik Ekuinoks", use_container_width=True)

materi_bab_2_bagian_12 = r"""
sudut miringnya terhadap ekuator diproyeksikan oleh sudut $M\hat{\Upsilon}R$, yang akrab disapa kemiringan ekliptika (*obliquity of the ecliptic*). Melirik dari bumi, sang surya seakan berpawai di lajur ekliptika melangkah menuju $\Upsilon \Upsilon M$, dan dalam setahun ia dua kali mampir—yakni di simpul $\Upsilon$ dan $U$—di mana posisinya di bola langit bertabrakan presisi dengan perpotongan antara ekliptika dan ekuator langit. Selama perjalanan dari $\Upsilon$ menuju $M$ lalu beralih dari $M$ ke $U$, matahari bernaung di wilayah utara ekuator, menyuntikkan nilai positif (utara) pada deklinasinya. Hal sebaliknya terjadi ketika ia beranjak dari $U$ dan berselancar menuju $\Upsilon$ dan seterusnya, di mana deklinasinya menukik negatif (selatan). Nah, koordinat $\Upsilon$ di mana status deklinasi matahari berganti haluan dari selatan merangkak ke utara inilah yang dinobatkan sebagai ekuinoks musim semi (*vernal equinox*). Dari titik magis $\Upsilon$ inilah kita mengukuhkan tonggak acuan untuk memetakan asensio rekta sekawanan bintang. Alhasil, jika $X$ merupakan sebuah bintang, asensio rektanya terukir pada rentang busur $\Upsilon D$ atau $\alpha$ yang merambat sepanjang ekuator bertolak ke timur dari $\Upsilon$, sedangkan porsi deklinasi $\delta$-nya adalah $DX$. Sketsa ini meyakinkan kita bahwa nilai asensio rekta dan deklinasi matahari merupakan entitas yang teramat dinamis. Saat matahari memijak ekuinoks $\Upsilon$ (sekitar 21 Maret), nilai asensio rekta dan deklinasinya nol besar; ketika sampai di singgasana $M$ (solstis musim panas, kisaran 21 Juni), asensio rektanya menyentuh $6^h$ dan deklinasinya memuncak di sekitar $23\frac{1}{2}^\circ \text{ U}$; sewaktu melipir di $U$ (ekuinoks musim gugur, 23 September), asensio rektanya tembus $12^h$ dan deklinasinya terkapar di $0^\circ$; dan ketika anjlok di titik terendahnya (solstis musim dingin, 21 Desember), asensio rektanya bergulir ke $18^h$ sementara deklinasinya bertengger di angka $23\frac{1}{2}^\circ \text{ S}$.

### 26. Lintang dan bujur langit.
Koordinat sebuah benda langit sesungguhnya dapat disandarkan pada ekliptika yang diperankan sebagai lingkaran besar fundamental, dengan ekuinoks musim semi $\Upsilon$ bertindak selaku titik mula (*origin*). Silakan tilik Gbr. 21, di sana $K$ mewakili kutub utara ekliptika dan $KXA$ membentangkan rute lingkaran besar yang menembus $X$ lalu menyayat ekliptika di titik $A$. Rentang busur $\Upsilon A$, yang membentang dari $\Upsilon$ menuju $A$ menjalar di atas ekliptika seirama dengan pawai tahunan mentari (ke timur), disapa dengan sebutan bujur (*longitude*) sang benda langit $X$, yang arusnya ditakar dari $0^\circ$ memutar hingga $360^\circ$ membungkus ekliptika. Adapun porsi busur $AX$ didaulat sebagai lintang (*latitude*), memegang prinsip bahwa lintang utara adalah positif dan lintang selatan bermakna negatif. Asalkan asensio rekta dan deklinasi sebuah bintang sudah kita kantongi, nilai lintang ($\beta$) maupun bujurnya ($\lambda$) bisa kita ekstrak membedah anatomi segitiga bola $KPX$, dan hukum ini juga berlaku dua arah. Mengingat $\Upsilon$ adalah mahkota kutub dari lingkaran besar $KPMR$, tak pelak lagi $K\hat{P}\Upsilon = 90^\circ$. Menggandeng fakta bahwa $\Upsilon D = \Upsilon\hat{P}X = \alpha$, maka $K\hat{P}X = 90^\circ + \alpha$. Di sisi berlawanan, $P\hat{K}\Upsilon = 90^\circ$, dan karena $\Upsilon A = \Upsilon\hat{K}X = \lambda$, kita pungut $P\hat{K}X = 90^\circ - \lambda$. Lebih jauh, $PX = 90^\circ - \delta$ dan $KX = 90^\circ - \beta$. Seandainya $\epsilon$ kita daulat untuk merepresentasikan kemiringan ekliptika—yakni sudut yang diapit oleh jari-jari $CM$ dan $CR$—maka otomatis busur $RM = \epsilon$. Menimbang bahwa $KM = 90^\circ$ dan $PR = 90^\circ$, tak ayal lagi $KP = \epsilon$. Menyuntikkan amunisi rumus **A**, **B**, dan **C**, kita mendulang mahakarya berikut:

$$ \cos KX = \cos PX \cos KP + \sin PX \sin KP \cos KPX $$

$$ \sin KX \sin PKX = \sin PX \sin KPX $$

$$ \sin KX \cos PKX = \cos PX \sin KP - \sin PX \cos KP \cos KPX $$

yang bisa dipoles ulang menjadi:

$$ \sin \beta = \sin \delta \cos \epsilon - \cos \delta \sin \epsilon \sin \alpha \dots\dots(10) $$

$$ \cos \beta \cos \lambda = \cos \delta \cos \alpha \dots\dots(11) $$

$$ \cos \beta \sin \lambda = \sin \delta \sin \epsilon + \cos \delta \cos \epsilon \sin \alpha \dots\dots(12) $$

Melalui manuver matematis serupa, asensio rekta $\alpha$ dan sang deklinasi $\delta$ bisa ditransmutasikan ke dalam variabel $\beta, \lambda$, dan $\epsilon$ memanfaatkan barisan rumus berikut:

$$ \sin \delta = \sin \beta \cos \epsilon + \cos \beta \sin \epsilon \sin \lambda $$

$$ \cos \delta \cos \alpha = \cos \beta \cos \lambda $$

$$ \cos \delta \sin \alpha = - \sin \beta \sin \epsilon + \cos \beta \cos \epsilon \sin \lambda $$

### 27. Waktu Sideris.
Asumsikan wujud bumi dan bola langit (dengan inti komando di $C$) dilukiskan layaknya Gbr. 22; anggap saja $g$ menengarai letak Greenwich di paras bumi dan $l$ menandai koordinat kota lain. Sudut apit antara meridian $plq$ dan $pgq$ tiada lain adalah bujur terestrial dari lokasi $l$, yang dalam skenario ini bercokol di sebelah barat Greenwich. Bentangkan garis $Cg$ dan $Cl$ hingga mereka menusuk bola langit di $G$ dan $L$, yang secara harfiah menahbiskan zenit bagi Greenwich dan titik $l$. Jika $X$ merupakan ordinat sebuah benda langit pada suatu detik tertentu, maka sudut $G\hat{P}X$ adalah manifestasi sudut jam $X$ teruntuk pengamat yang bernaung di meridian Greenwich, dan $L\hat{P}X$ mendelegasikan sudut jam untuk mereka yang berada di meridian $l$. Mempertimbangkan bahwa $G\hat{P}X = L\hat{P}X + G\hat{P}L$ sembari mengantongi fakta $G\hat{P}L = g\hat{p}l$, kita menyimpulkan:
"""
st.markdown(materi_bab_2_bagian_12, unsafe_allow_html=True)
st.image("Gambar_22.jpg", caption="Gambar 22: Hubungan Waktu Sideris Lokal dan Bujur Terestrial", use_container_width=True)

materi_bab_2_bagian_13 = r"""
$$ \text{H.A. (Sudut Jam) dari } X \text{ di Greenwich} = \text{H.A. dari } X \text{ di } l + \text{bujur (dalam satuan waktu) dari } l \dots\dots(13) $$

Pada formula ini, angka bujur dari $l$ disyaratkan sudah dikonversi ke dalam irama waktu ($15^\circ = 1^h; 15' = 1^m; 15'' = 1^s$). Konvensi rumus (13) ini berlaku universal, bahkan untuk mengawal pergerakan ekuinoks musim semi $\Upsilon$. Mengingat hakikat waktu sideris adalah rentang sudut jam dari si titik $\Upsilon$, kita mengeruk kesimpulan:

$$ \text{Waktu sideris di Greenwich} = \text{Waktu sideris di } l \pm \text{bujur dari } l \dots(14) $$

di mana tanda operasional $+$ kita pakai manakala $l$ menyelinap di ufuk barat Greenwich, sementara tanda $-$ diberlakukan jika $l$ mengintip di bilik timurnya. Rekaman waktu sideris di koordinat $l$ inilah yang menyandang titel waktu sideris lokal (*local sidereal time*, L.S.T.).

### 28. Waktu matahari rata-rata.
Hari sideris seyogianya adalah kompas waktu andalan bagi para astronom di observatorium, namun sistem ini terlampau ribet untuk menopang rutinitas warga awam yang siklus hidupnya disetir oleh kemunculan mentari. Ketika piringan matahari bertandang di meridian sebuah tempat, momen magis itu kita tetapkan sebagai tengah hari sejati (*apparent noon*); dan ketika ia mengulang perjalanannya ke meridian yang sama keesokan harinya, kita sahkan bahwa satu hari matahari sejati (*apparent solar day*) telah genap berlalu. Jeda ini bisa dikalibrasi memakai jam observatorium berskala waktu sideris, dan terbukti secara gamblang bahwa durasi hari matahari sejati ini tidak pernah konsisten. Seperti yang sudah kita bedah sebelumnya, pergerakan matahari membingkai orbit elips, dan akselerasinya mendaki orbit pun penuh gelombang, tidak seragam. Imbasnya, mentari seolah-olah merangkak di jalur ekliptika dengan langkah yang inkonsisten jika dilatarbelakangi jajaran bintang statis. Lebih memperkeruh keadaan, jalur edar mentari membelah ekliptika—bukan berputar manis di ekuator langit (titik sakral tempat sudut jam ditakar)—membuat laju pertambahan asensio rektanya urung melesat mulus. Untuk menetralisir kekacauan ini, astronom meracik nilai rata-rata dari deretan hari matahari sejati dalam setahun, menelurkan mahakarya yang dinamakan hari matahari rata-rata (*mean solar day*). Secara teknis, hari matahari rata-rata ditasbihkan sebagai jeda waktu dua transit meridian berurutan dari sebuah figur fiktif yang kita sebut matahari rata-rata (*mean sun*). Tokoh bayangan ini dibayangkan berpawai di sabuk ekuator langit dengan tempo yang ultra-stabil mengitari bumi, menuntaskan satu putaran persis di kala matahari sejati sukses melunasi satu lap di gelanggang ekliptika. Lewat ketetapan mutlak ini, asensio rekta matahari rata-rata (R.A.M.S.) digaransi bakal menanjak konstan secara merata.

Seandainya kita mendandani matahari rata-rata ini layaknya benda langit lumrah, pada setiap detik ia bakal memiliki pijakan sudut jam (H.A.M.S.) di penjuru mana pun di bumi. Manakala nilai asensio rektanya terkuak di detik tersebut, dengan menjamah persamaan (8) atau (9) kita bisa menelurkan:

$$ \text{Waktu sideris} = \text{H.A.M.S.} + \text{R.A.M.S.} \dots\dots(15) $$

Napas waktu yang berdenting pada jam dinding biasa (katakanlah di Greenwich) nyatanya merajut korelasi langsung dengan indeks H.A.M.S. di lokus tersebut. Jika variabel R.A.M.S. diketahui, persamaan (15) bisa dialihfungsikan sebagai jembatan untuk mengkomparasi waktu sideris melawan waktu rata-rata harian. Romansa tarik-ulur antara matahari rata-rata dan mentari sejati bakal diurai lebih lanjut di bab mendatang. Untuk sekilas info, cukup ditanamkan bahwa gap selisih antara asensio rekta matahari rata-rata dan versi sejatinya bisa dikalkulasi pada momen apa pun; selisih waktu nan unik ini disapa perataan waktu (*equation of time*)*, dan dilabeli huruf $E$:

$$ E = \text{R.A.M.S.} - \text{R.A. } \odot \dots\dots(16) $$

*(Catatan kaki: Pada diktat-diktat usang masa silam, formula perataan waktu diputar menjadi $E = \text{R.A. } \odot - \text{R.A.M.S.}$, tetapi konvensi pakem yang bertahta saat ini adalah rumusan (16)).*

di mana R.A. $\odot$ mengukuhkan posisinya sebagai asensio rekta matahari sejati. Indeks $E$ bisa bergoyang di ranah positif maupun negatif, menari dalam alur yang rumit (bedah anatomi mendalam soal $E$ akan kita kuliti di Bagian 91). Tengok Gbr. 23 sejenak; anggap saja pada sekon tertentu asensio rekta beserta deklinasi mentari ($\odot$) sudah tersaji di meja kalkulasi. Misalkan $\Upsilon$ meresmikan ekuinoks musim semi di detik itu, menyulap sudut $R\hat{P}\Upsilon$ atau busur $R\Upsilon$ menjadi sudut jam $\Upsilon$ (alias denyut waktu sideris lokal). Bermodalkan pilar data ini, titik kumpul $\Upsilon$ dan sang mentari dapat ditancapkan di peta bola langit. Pada grafik ini, jarak $\Upsilon K = \text{R.A. } \odot$ seraya $K\odot$ mendaulat diri sebagai deklinasi mentari.
"""
st.markdown(materi_bab_2_bagian_13, unsafe_allow_html=True)
st.image("Gambar_23.jpg", caption="Gambar 23: Perataan Waktu dan Sudut Jam Matahari Rata-rata", use_container_width=True)

materi_bab_2_bagian_14 = r"""
Andaikan angka $E$ sedang bersandar di zona positif; berpijak dari persamaan (16), R.A.M.S. berhak menduduki takhta yang lebih dominan dari R.A. $\odot$, memuluskan jalan kita untuk mencangkokkan posisi matahari rata-rata $M$ di diagram. Sudut $R\hat{P}M$ yang sejajar dengan $RM$ didapuk sebagai sudut jam matahari rata-rata (H.A.M.S.). Dari pembedahan Gbr. 23, berhubung rantai $RK = RM + MK$, terlahir kenyataan bahwa:

$$ \text{H.A. } \odot = \text{H.A.M.S.} + E \dots\dots(17) $$

Tali relasi ini menyandang peran luhur untuk menjembatani H.A.M.S. dengan H.A. $\odot$, membukakan pintu bagi kita untuk meringkus nilai sudut jam matahari sejati asalkan besaran penopang lainnya tak lagi rahasia. Ketika figur matahari rata-rata bermanuver mulus di atas meridian pengamat, detik itu disahkan sebagai tengah hari rata-rata lokal (*local mean noon*). Ketika ia sudi melintas di atas meridian Greenwich, momen itu diikrarkan sebagai tengah hari rata-rata Greenwich. Indeks sudut jam matahari rata-rata di observatorium Greenwich dilabeli G.M.A.T. (*Greenwich mean astronomical time*). Giliran matahari rata-rata merapat di pos $T$—di mana H.A.M.S. menunjuk waktu $12^h$—ia akan memicu dentang tengah malam rata-rata (*mean midnight*). Saat jarum G.M.A.T. menyenggol angka $12^h$, kegelapan tengah malam merengkuh Greenwich, menabuh genderang dimulainya ritme hari sipil yang baru. Kompas waktu rata-rata yang diturunkan dari dentang tengah malam di Greenwich masyhur dengan sebutan *Greenwich Mean Time* (G.M.T.)*, yang di era modern bersulih nama menjadi *Universal Time* (U.T.). Polanya terpetakan dengan sangat gamblang:

$$ \text{U.T.} \equiv \text{G.M.T.} = \text{G.M.A.T.} + 12^h \dots\dots(18) $$

Harmoni serupa juga merasuk ke tempat-tempat lain yang mengkalibrasi jam mereka murni pada rujukan meridian lokal masing-masing:

$$ \text{Local M.T.} = \text{Local M.A.T.} + 12^h \dots\dots(19) $$

$$ = \text{H.A.M.S.} \pm 12^h \dots\dots(20) $$

Persamaan (14) menawarkan benang merah yang mengaitkan waktu sideris di Greenwich dengan waktu sideris di sebuah kota $l$. Diilhami dari Gbr. 22 berpadu dengan persamaan (18) dan (19), irama yang sama berlaku kokoh untuk merangkaikan waktu rata-rata Greenwich dengan denyut waktu rata-rata di lokasi yang bersangkutan:

$$ \text{U.T.} \equiv \text{G.M.T.} = \text{Local M.T.} \pm \text{bujur dari } l \dots\dots(21) $$

dengan panduan bahwa tanda operasional $+$ akan dipanggil jika bujur kota $l$ merapat di koridor barat, dan tanda $-$ diintervensi tatkala letaknya terseret ke timur.

Situasi dipastikan runyam dan membingungkan jika setiap kampung di penjuru dunia ngotot memakai arloji yang dikalibrasi presisi dengan meridian lokalnya sendiri. Untuk menjegal kekacauan itu, untuk negara-negara berskala mini, dicomotlah sebuah waktu rata-rata standar yang berkorespondensi dengan meridian bujur khusus (meridian standar) untuk digunakan secara seragam di seluruh negeri. Di Inggris Raya, waktu standar tersebut adalah G.M.T. Di negara yang luas seperti Rusia atau Amerika Serikat, digunakan dua atau lebih waktu standar berdasarkan zona bujur; di setiap zona, waktu standar yang disesuaikan dengan meridian tertentu dalam zona tersebut akan dipertahankan. Waktu standar yang didasarkan pada meridian tertentu ini disebut waktu zona (*zone time*, Z.T.). Sistem ini secara umum juga digunakan oleh kapal-kapal di laut untuk menghindari komplikasi geografis. Hubungannya adalah sebagai berikut:

$$ \text{U.T.} \equiv \text{G.M.T.} = \text{Z.T.} \pm \text{bujur dari meridian standar} \dots(22) $$

*(Catatan kaki: Sebelum 1925, G.M.T. dalam almanak digunakan untuk menandakan Greenwich mean astronomical time (G.M.A.T.). Sejak 1925, waktu yang digunakan adalah G.M.T. ($\equiv$ G.C.T.), yang kemudian digantikan oleh U.T. Baru-baru ini, untuk berbagai alasan yang dicantumkan dalam Apendiks E (hlm. 424), U.T. dalam almanak telah digantikan oleh Ephemeris Time (E.T.). Perbedaan antara U.T. dan E.T. sangat kecil sehingga kita umumnya menggunakan U.T., kecuali dinyatakan lain).*

### 29. Contoh Penyelesaian (*Example*).
Sebagai ilustrasi, mari kita perhatikan jenis masalah yang umum dan penting berikut ini. Di sebuah tempat pada bujur $163^\circ 14' \text{ T}$, kita diminta menghitung sudut jam matahari ($\text{H.A. } \odot$) yang bersesuaian dengan pengamatan yang dilakukan pada waktu zona $8^h 46^m 22^s$ tanggal 10 Maret 1975; waktu zona tersebut didasarkan pada meridian standar $165^\circ \text{ T} (11^h \text{ T})$.

Langkah pertama adalah menentukan U.T. pada saat pengamatan dilakukan:

Waktu zona: $8^h 46^m 22^s$ (10 Maret)
Bujur meridian standar: $- 11^h$
U.T. = $21^h 46^m 22^s$ (9 Maret)

Kita mengurangkan $11^h$ dari waktu zona sesuai dengan rumus (22) (atau kita dapat memandang waktu zona sebagai $32^h 46^m 22^s$ tanggal 9 Maret).

Selanjutnya, kita mencari waktu rata-rata lokal (*local mean time*) yang bersesuaian dengan bujur tempat pengamatan menggunakan rumus (21):

U.T.: $21^h 46^m 22^s$ (9 Maret)
Bujur tempat (Timur): $+ 10^h 52^m 56^s$
Local M.T. = $32^h 39^m 18^s$ (9 Maret)
Local M.T. = $8^h 39^m 18^s$ (10 Maret)

Rumus (20) memungkinkan kita menuliskan H.A.M.S. (sudut jam matahari rata-rata di tempat tersebut):

$$ \text{H.A.M.S.} = 20^h 39^m 18^s. $$

Langkah terakhir adalah menerapkan perataan waktu ($E$) pada H.A.M.S. Berdasarkan *Astronomical Ephemeris*, melalui interpolasi pada U.T. $21^h 46^m 22^s$ tanggal 9 Maret, diperoleh $E = -10^m 36^s$.

Maka, berdasarkan persamaan (17):

$$ \text{H.A. } \odot = 20^h 39^m 18^s - 10^m 36^s, $$

atau

$$ \text{H.A. } \odot = 20^h 28^m 42^s. $$

### 30. Sudut jam dari sebuah benda langit.
Untuk menghitung sudut jam dari benda langit apa pun ($X$) selain matahari, kita menempuh langkah berikut. Berdasarkan persamaan (8) dan (14):

$$ \text{L.S.T.} = \text{H.A. } X + \text{R.A. } X $$

dan

$$ \text{G.S.T.} = \text{L.S.T.} \pm l, $$

sehingga

$$ \text{H.A. } X + \text{R.A. } X = \text{G.S.T.} \pm l \dots\dots(23). $$

Dalam *Astronomical Ephemeris*, waktu sideris Greenwich ditabulasikan pada $0^h$ U.T. untuk setiap hari dalam setahun. Karena berdasarkan persamaan (15):

$$ \text{Sid. time} = \text{H.A.M.S.} + \text{R.A.M.S.}, $$

maka kita peroleh:

$$ \text{R.A.M.S. pada U.T. } 0^h \text{ untuk hari apa pun} = \text{waktu sideris Greenwich pada U.T. } 0^h \text{ hari tersebut} - 12^h. $$

*R.A.M.S. bertambah secara seragam pada laju $3^m 56^s,56$ per hari matahari rata-rata, atau $9^s,856$ per jam matahari rata-rata*; nilai ini dapat digunakan untuk menghitung R.A.M.S. pada U.T. berapa pun. Tabel-tabel khusus disediakan di dalam almanak untuk mempermudah perhitungan ini.

Penggunaan rumus (23) paling baik diilustrasikan dengan sebuah contoh. Diharuskan untuk menghitung sudut jam bintang Betelgeuse ($\alpha$ Orionis) pada waktu zona $18^h 35^m 46^s$ tanggal 26 Januari 1975, di tempat dengan bujur $64^\circ 28' 49'' \text{ B}$ (Zona $+4^h$, yang berarti meridian standar zona tersebut adalah $4^h \text{ B}$ atau $60^\circ \text{ B}$).

Waktu zona: $18^h 35^m 46^s$ (26 Januari)
Zona: $+ 4^h$
U.T.: $22^h 35^m 46^s$ (26 Januari)
Koreksi waktu sideris: $3^m 43^s$ ($3^m 56^s,56$ per hari)
Total: $22^h 39^m 29^s$
G.S.T. pada $0^h$ U.T.: $8^h 18^m 39^s$ (Dari A.E.)
G.S.T.: $30^h 58^m 08^s$
Bujur tempat (Barat): $- 4^h 17^m 55^s$
L.S.T.: $26^h 40^m 13^s$
Kurangi R.A. Betelgeuse: $5^h 53^m 49^s$ (Dari A.E.)
**H.A. Betelgeuse: $20^h 46^m 24^s$**

### 31. Terbit dan terbenam.
Perhatikan Gbr. 24. Benda langit $X$ dikatakan terbenam di titik $F$, yaitu saat ia mencapai horizon. Pada saat itu, jarak zenitnya adalah $90^\circ$, yakni $ZF = 90^\circ$. Misalkan $H$ adalah sudut jam dari $X$ saat terbenam, sehingga $Z\hat{P}F = H$. Jarak kutub utaranya adalah $PF = 90^\circ - \delta$. Misalkan $A$ adalah azimut saat terbenam ($P\hat{Z}F$) dan $\phi$ adalah lintangnya.

Dari Rumus A:

$$ \cos ZF = \cos PZ \cos PF + \sin PZ \sin PF \cos ZPF, $$

atau

$$ \cos 90^\circ = \sin \phi \sin \delta + \cos \phi \cos \delta \cos H, $$

karena $\cos 90^\circ = 0$, maka:

$$ \cos H = - \tan \phi \tan \delta \dots\dots(24), $$

yang darinya sudut jam saat terbenam dapat dihitung.
Selanjutnya, dari Rumus A:

$$ \cos PF = \cos PZ \cos ZF + \sin PZ \sin ZF \cos PZF, $$

atau

$$ \sin \delta = 0 + \cos \phi \cos A, $$

sehingga:

$$ \cos A = \sin \delta \sec \phi \dots\dots(25), $$

yang darinya azimut saat terbenam dapat dihitung.
"""
st.markdown(materi_bab_2_bagian_14, unsafe_allow_html=True)
st.image("Gambar_24.jpg", caption="Gambar 24: Posisi Benda Langit Saat Terbenam di Horizon", use_container_width=True)

materi_bab_2_bagian_15 = r"""
Di lintang utara, terlihat dari persamaan (24) dan (25) atau dari Gbr. 24 bahwa jika deklinasi bintang bernilai utara, sudut jam saat terbenam berada di antara $6^h$ dan $12^h$ dan azimutnya kurang dari $90^\circ$ (benda terbenam di antara barat dan utara). Jika deklinasinya selatan, sudut jam saat terbenam berada di antara $0^h$ dan $6^h$ dan benda terbenam di antara selatan dan barat. Masalah terbitnya benda langit dapat dianalisis dengan cara serupa. Prosedur yang sama berlaku ketika lintang pengamat berada di selatan.

Jika benda langit tersebut adalah sebuah bintang, sudut jam saat terbenam memberikan selang waktu antara transit meridian dan saat terbenam dalam satuan waktu sideris. Jika benda tersebut adalah matahari, selang waktu tersebut diekspresikan dalam waktu matahari semu. Namun, selama selang waktu ini, posisi relatif antara matahari dan matahari rata-rata hanya berubah sedikit (perubahan perataan waktu dapat diabaikan kecuali jika diperlukan ketelitian tinggi), sehingga selang waktu tersebut dapat dianggap sebagai waktu rata-rata untuk semua tujuan praktis. Sebagai contoh, jika dari rumus (24) sudut jam $H$ saat terbenam diperoleh $7^h 30^m$, maka selang waktu antara transit meridian matahari dan terbenam adalah $7^h 30^m$ waktu matahari rata-rata. Dengan mengabaikan perubahan kecil pada deklinasi matahari, kita dapat menyimpulkan bahwa ini juga merupakan selang waktu antara matahari terbit dan transit meridian. Dengan demikian, matahari berada di atas horizon selama $15^h$ dan di bawah horizon selama $9^h$. Faktanya, deklinasi matahari umumnya sedikit berbeda antara saat terbit dan terbenam akibat pergerakannya di sepanjang ekliptika, yang efeknya dapat diperhitungkan jika diperlukan.

Rumus (24) menunjukkan bahwa jika $\phi > 90^\circ - \delta$, nilai $\cos H$ secara numerik menjadi lebih besar daripada satu, sehingga persamaan tersebut tidak menghasilkan nilai $H$. Dalam hal ini, matahari tidak terbenam pada lintang dan hari-hari di mana $\phi > 90^\circ - \delta$, seperti yang dapat diverifikasi dari diagram. Pada hari solstis musim panas (*midsummer day*), deklinasi utara matahari mencapai nilai maksimumnya, yaitu sekitar $23\frac{1}{2}^\circ \text{ U}$, sehingga di lintang utara yang melebihi $66\frac{1}{2}^\circ \text{ U}$, matahari berada di atas horizon sepanjang hari tanpa terbenam.* Di kutub utara, karena $\phi > 90^\circ - \delta$ selama $\delta$ bernilai utara, matahari berada di atas horizon terus-menerus antara 21 Maret dan 21 September, dan berada di bawah horizon selama enam bulan sisanya. Paralel $66\frac{1}{2}^\circ \text{ U}$ disebut *Lingkaran Arktik* (*Arctic Circle*), dan paralel yang bersesuaian di belahan bumi selatan ($66\frac{1}{2}^\circ \text{ S}$) disebut *Lingkaran Antarktika* (*Antarctic Circle*).

*(Catatan kaki: Dari sinilah muncul istilah matahari tengah malam / midnight sun).*

### 32. Laju perubahan jarak zenit dan azimut.
Misalkan $X$ pada Gbr. 25 adalah posisi suatu benda langit pada momen tertentu, dan $Y$ adalah posisinya sesaat kemudian. Dengan menganggap deklinasinya konstan, $X$ dan $Y$ terletak pada lingkaran kecil $LM$ (paralel deklinasi) dengan $P$ sebagai kutubnya. Tarik busur lingkaran besar $PX, PY, ZX, ZY$. Misalkan $UX$ adalah busur lingkaran kecil dengan $Z$ sebagai kutubnya, sehingga $ZX = ZU$. Misalkan $Z\hat{P}X = H$ dan $Z\hat{P}Y = H + \Delta H$, sehingga $X\hat{P}Y = \Delta H$. Misalkan pula $P\hat{Z}X = A$ dan $X\hat{Z}Y = \Delta A$; $ZX = z$ dan $ZY = z + \Delta z$. Maka $UY = \Delta z$. Karena $XY$ adalah busur yang sangat kecil, kita dapat menganggap $UXY$ sebagai segitiga bidang yang siku-siku di $U$.
"""
st.markdown(materi_bab_2_bagian_15, unsafe_allow_html=True)
st.image("Gambar_25.jpg", caption="Gambar 25: Perubahan Kecil Posisi Benda Langit dalam Jarak Zenit dan Azimut", use_container_width=True)

materi_bab_2_bagian_16 = r"""
Saat benda langit bergerak akibat gerak harian dari $X$ ke $Y$, jarak zenitnya bertambah sebesar $\Delta z$, sudut jamnya bertambah sebesar $\Delta H$, dan azimutnya berkurang sebesar $\Delta A$.

Berdasarkan rumus (1) dari Bagian 3 (hlm. 4):

$$ XY = X\hat{P}Y \sin PX = \Delta H \cos \delta, $$

dan

$$ UX = X\hat{Z}Y \sin ZX = \Delta A \sin z. $$

Misalkan $\eta$ adalah sudut $PXZ$, yang disebut sudut paralaktik (*parallactic angle*). Karena $Y$ sangat dekat dengan $X$, kita dapat menganggap sudut $P\hat{Y}Z$ bernilai $\eta$. Maka:

$$ UY = XY \cos U\hat{Y}X, $$

dan

$$ UX = XY \sin U\hat{Y}X. $$

Karena $P\hat{Y}Z = \eta$ dan $P\hat{Y}X = 90^\circ$, maka:

$$ UY = \Delta z = \Delta H \cos \delta \sin \eta, $$

dan

$$ UX = \Delta A \sin z = \Delta H \cos \delta \cos \eta. $$

Selanjutnya, dalam segitiga bola $PXZ$, berdasarkan **Rumus B**:

$$ \cos \delta \sin \eta = \sin A \cos \phi, $$

dan berdasarkan **Rumus C**:

$$ \cos \delta \cos \eta = \sin \phi \sin z - \cos \phi \cos z \cos A. $$

Oleh karena itu:

$$ \Delta z = \Delta H \sin A \cos \phi \dots\dots(26), $$

dan

$$ \Delta A = \Delta H (\sin \phi - \cos \phi \cot z \cos A) \dots\dots(27). $$

Dalam rumus-rumus ini, $\Delta H, \Delta z$, dan $\Delta A$ dinyatakan dalam ukuran sirkular. Misalkan $\Delta H^s$ adalah jumlah sekon waktu dalam radian $\Delta H$, serta $\Delta z''$ dan $\Delta A''$ adalah jumlah detik busur dalam radian $\Delta z$ dan $\Delta A$. Berdasarkan prinsip Bagian 15 (hlm. 22):

$$ \Delta z = \Delta z'' \sin 1''; \quad \Delta A = \Delta A'' \sin 1''; \quad \Delta H = \Delta H^s \sin 1^s, $$

dan karena $\sin 1^s = 15 \sin 1''$, kita peroleh:

$$ \Delta z'' = 15 \Delta H^s \sin A \cos \phi, $$

$$ \Delta A'' = 15 \Delta H^s (\sin \phi - \cos \phi \cot z \cos A). $$

Jika $\Delta H^s = 1$ sekon, persamaan-persamaan di atas menyatakan bahwa jarak zenit bertambah pada laju $15 \sin A \cos \phi$ detik busur per sekon waktu, dan azimut berkurang pada laju $15 [\sin \phi - \cos \phi \cot z \cos A]$ detik busur per sekon waktu.

Untuk bintang, laju perubahan jarak zenit dan azimut ini diekspresikan dalam detik busur per sekon waktu sideris; sedangkan untuk matahari, dinyatakan dalam detik busur per sekon waktu matahari semu atau (dengan ketelitian yang memadai) waktu matahari rata-rata.

Hasil-hasil tersebut juga dapat diturunkan dengan mudah melalui kalkulus. Dari segitiga $PZX$, berdasarkan **Rumus A**:

$$ \cos z = \sin \delta \sin \phi + \cos \delta \cos \phi \cos H, $$

di mana $\delta$ dan $\phi$ dianggap konstan. Dengan mendiferensiasikannya:

$$ \sin z \frac{dz}{dH} = \cos \delta \cos \phi \sin H. $$

Berdasarkan **Rumus B**:

$$ \sin z \sin A = \sin H \cos \delta \dots\dots(28); $$

$$ \therefore \frac{dz}{dH} = \sin A \cos \phi \dots\dots(29), $$

yang pada intinya sama dengan persamaan (26). Jika $z$ dan $H$ masing-masing dinyatakan dalam detik busur dan sekon waktu, maka:

$$ \frac{dz}{dH} = 15 \sin A \cos \phi. $$

Mendiferensiasikan persamaan (28) terhadap $H$ (di mana $z, A$, dan $H$ adalah variabel):

$$ \sin z \cos A \frac{dA}{dH} = \cos H \cos \delta - \sin A \cos z \frac{dz}{dH} $$

$$ = \cos H \cos \delta - \sin^2 A \cos z \cos \phi, $$

dengan mensubstitusi persamaan (29).
Berdasarkan **Rumus C**:

$$ \cos \delta \cos H = \cos z \cos \phi - \sin z \sin \phi \cos A; $$

$$ \therefore \sin z \cos A \frac{dA}{dH} = \cos^2 A \cos z \cos \phi - \sin z \sin \phi \cos A; $$

$$ \therefore \frac{dA}{dH} = -(\sin \phi - \cot z \cos A \cos \phi), $$

atau jika $A$ dan $H$ dinyatakan dalam detik busur dan sekon waktu, rumus tersebut menjadi:

$$ \frac{dA}{dH} = -15(\sin \phi - \cot z \cos A \cos \phi), $$

yang hasilnya persis sama dengan penurunan sebelumnya.

### 33. Senja dan Fajar (*Twilight*).
Setelah matahari terbenam, cahaya tak langsung yang dipantulkan dan dihamburkan oleh atmosfer atas masih terus menyinari bumi, meski kian meredup seiring turunnya matahari semakin jauh di bawah horizon. Ketika posisi matahari berada $18^\circ$ di bawah horizon (dengan jarak zenit $108^\circ$), pencahayaan tak langsung ini praktis sudah dapat diabaikan. Selang waktu antara matahari terbenam dan saat jarak zenit matahari meningkat hingga $108^\circ$ disebut durasi senja (*evening twilight*). Dengan cara yang serupa, kita mendefinisikan durasi fajar (*morning twilight*). Durasi senja, sebagai contoh, dapat dihitung sebagai berikut. Pada Gbr. 26, $LFM$ adalah paralel deklinasi matahari (karena tidak diperlukan ketelitian tinggi dalam perhitungan khusus ini, kita mengabaikan perubahan deklinasi matahari selama hari yang bersangkutan) dan $JGK$ adalah lingkaran kecil yang sejajar dengan horizon, dengan setiap titiknya berjarak $108^\circ$ dari $Z$. Lingkaran kecil ini memotong paralel deklinasi di titik $G$. Maka, selang waktu yang diperlukan matahari untuk bergerak dari $F$ ke $G$, yakni $F\hat{P}G$, merupakan durasi senja. Selanjutnya, $F\hat{P}G = Z\hat{P}G - Z\hat{P}F$; karena $Z\hat{P}F$ adalah sudut jam saat matahari terbenam, nilainya dapat dihitung menggunakan rumus (24). Di dalam segitiga bola $ZPG$, kita ketahui: $ZG = 108^\circ$, $PZ = 90^\circ - \phi$, dan $PG = 90^\circ - \delta$; oleh karena itu, berdasarkan rumus A,

$$ \cos 108^\circ = \sin \phi \sin \delta + \cos \phi \cos \delta \cos Z\hat{P}G, $$

yang memungkinkan perhitungan nilai $Z\hat{P}G$ untuk dilakukan. Nilai $\delta$ yang digunakan dalam rumus ini tentu saja bergantung pada hari tertentu dalam tahun yang bersangkutan. Dengan demikian, durasi senja pun dapat diketahui.
"""
st.markdown(materi_bab_2_bagian_16, unsafe_allow_html=True)
st.image("Gambar_26.jpg", caption="Gambar 26: Diagram Durasi Senja (Evening Twilight)", use_container_width=True)

materi_bab_2_bagian_17 = r"""
Jelas dari Gbr. 26 bahwa senja akan berakhir jika $NM$ lebih besar dari $NJ$, dengan kata lain, jika pada tengah malam semu matahari berada lebih dari $18^\circ$ di bawah horizon. Sekarang $NT = 90^\circ - \phi$ dan $MT = \delta$; oleh karena itu $NM = 90^\circ - \phi - \delta$. Karenanya, senja akan berakhir jika $90^\circ - \phi - \delta > 18^\circ$, atau jika $\delta < 72^\circ - \phi$. Sebagai contoh, di lintang $60^\circ \text{ U}$, senja akan berakhir jika $\delta < 12^\circ$. Ketika $\delta$ lebih besar dari $12^\circ$, jarak zenit matahari kurang dari $108^\circ$ di antara waktu terbenam dan tengah malam semu, begitu pula di antara tengah malam semu dan matahari terbit; oleh karena itu, pada lintang $60^\circ \text{ U}$, langit tidak pernah benar-benar gelap pada hari-hari ketika deklinasi matahari melebihi $12^\circ \text{ U}$. Hari-hari tersebut berada di antara 23 April dan 22 Agustus.

---

### LATIHAN SOAL (*EXERCISES*)

[Simbol-simbol yang digunakan:
$\phi = \text{lintang pengamat (latitude of observer)},$
$A = \text{azimut benda langit (azimuth of heavenly body)},$
$H = \text{sudut jam (hour angle)},$
$z = \text{jarak zenit (zenith distance)},$
$\epsilon = \text{kemiringan ekliptika (obliquity of the ecliptic)}.$]
"""
st.markdown(materi_bab_2_bagian_17, unsafe_allow_html=True)

latihan_soal = [
    {
        "soal": r"**1.** Jika $z_1$ dan $z_2$ adalah jarak zenit sebuah bintang pada meridian dan pada vertikal utama secara berturut-turut, buktikan bahwa (i) $\cot \delta = \operatorname{cosec} z_1 \sec z_2 - \cot z_1$ dan (ii) $\cot \phi = \cot z_1 - \operatorname{cosec} z_1 \cos z_2$.",
        "jawaban": r"""**Langkah Penyelesaian Lengkap:**
1. Pada saat kulminasi atas di meridian, azimut bintang $A=0^\circ$ (atau $180^\circ$) dan sudut jam $H=0$. Jarak zenitnya adalah $z_1 = \phi - \delta$ (asumsi transit arah selatan). Dari sini $\delta = \phi - z_1$ dan $\phi = z_1 + \delta$.
2. Pada vertikal utama, azimut bintang adalah $A=90^\circ$ (barat) atau $270^\circ$ (timur). Gunakan Aturan Kosinus pada segitiga bola PZX:
   $\cos z_2 = \sin \phi \sin \delta + \cos \phi \cos \delta \cos 90^\circ \implies \cos z_2 = \sin \phi \sin \delta$.
3. **Pembuktian (i):** Eliminasi $\phi$ menggunakan $\sin \phi = \sin(z_1 + \delta) = \sin z_1 \cos \delta + \cos z_1 \sin \delta$. 
   Substitusikan: $\cos z_2 = (\sin z_1 \cos \delta + \cos z_1 \sin \delta) \sin \delta$. 
   Bagi kedua ruas dengan besaran $(\sin \delta \cos \delta \sin z_1)$, susun ulang posisinya hingga terbukti $\cot \delta = \operatorname{cosec} z_1 \sec z_2 - \cot z_1$.
4. **Pembuktian (ii):** Serupa dengan (i), namun eliminasi besaran $\delta$ dengan mensubstitusi persamaan $\sin \delta = \sin(\phi - z_1)$ ke dalam $\cos z_2 = \sin \phi \sin \delta$. Sederhanakan untuk mendapati nilai akhir $\cot \phi$."""
    },
    {
        "soal": r"**2.** Jika $\psi$ adalah sudut yang dibentuk oleh lintasan sebuah bintang pada saat terbit dengan horizon, buktikan bahwa $\cos \psi = \sin \phi \sec \delta$.",
        "jawaban": r"""**Langkah Penyelesaian Lengkap:**
1. Sudut lintas harian bintang dengan bidang horizon disebut sudut di titik terbit. Lintasan bintang sejajar dengan ekuator, sehingga sudut antara rute bintang dan horizon merupakan komponen tak langsung dari sudut paralaktik $\eta$. 
2. Sewaktu bintang terbit, ia menjejak di batas horizon, sehingga $z = 90^\circ$.
3. Karena $\psi$ berkomplemen dengan $\eta$ dalam proyeksi datar paralaktik saat terbit, maka $\cos \psi = \sin \eta$.
4. Terapkan Aturan Sinus pada segitiga bola PZX (Kutub-Zenit-Bintang):
   $\frac{\sin \eta}{\sin(90^\circ - \phi)} = \frac{\sin(180^\circ - A)}{\sin(90^\circ - \delta)} \implies \text{Atau secara langsung di saat } z=90^\circ\text{, } \sin \eta = \frac{\sin \phi}{\cos \delta}$.
5. Menggunakan substitusi, $\cos \psi = \sin \phi \sec \delta$. (Terbukti)."""
    },
    {
        "soal": r"**3.** Jika $h, H$ adalah sudut jam sebuah bintang, berdeklinasi $+ \delta$, pada vertikal utama (barat) dan pada saat terbenam secara berturut-turut, untuk sebuah tempat di lintang utara, tunjukkan bahwa $\cos h \cos H + \tan^2 \delta = 0$. Hitunglah interval Aldebaran.",
        "jawaban": r"""**Langkah Penyelesaian Lengkap:**
1. Di posisi vertikal utama, azimut bintang $A=90^\circ$. Menggunakan rumus kotangen / segitiga Napier, sudut jam saat itu $h$ memenuhi persamaan: $\cos h = \cot \phi \tan \delta$.
2. Saat terbenam, bintang berada persis di horizon, maka jarak zenitnya $z=90^\circ$. Merujuk Rumus (24) di Bab ini, sudut jam terbenam $H$ diturunkan dari $\cos H = - \tan \phi \tan \delta$.
3. Kalikan kedua persamaan di atas: 
   $\cos h \cos H = (\cot \phi \tan \delta) \times (-\tan \phi \tan \delta) = -\tan^2 \delta$.
4. Pindahkan semua parameter ke satu ruas sehingga menghasilkan $\cos h \cos H + \tan^2 \delta = 0$. (Terbukti).
5. **Menghitung interval Aldebaran:** Gunakan lintang $\phi = 36^\circ \text{ U}$, deklinasi $\delta = +16^\circ 22'$. Hitung selisih sudut jam terbenam dan transit vertikal ($H - h$) dan konversikan hasilnya ke dalam waktu matahari rata-rata."""
    },
    {
        "soal": r"**4.** Sebuah perahu yang melaju pada kecepatan 5 knot dikemudikan terus-menerus ke arah sebuah bintang. Buktikan bahwa jarak tempuh menuju ke arah barat adalah kira-kira $\frac{1}{3} (z_2^\circ - z_1^\circ) \sec \phi$ mil, di mana $z_1^\circ$ dan $z_2^\circ$ adalah jarak zenit awal dan akhir.",
        "jawaban": r"""**Langkah Penyelesaian Lengkap:**
1. Perahu bergerak dengan kecepatan konstan $v = 5$ knot menuju arah bintang, sehingga komponen kecepatan ke arah barat (westing) adalah $dx = v \sin A \, dt$.
2. Dari penurunan laju perubahan jarak zenit di Bagian 32, kita mengetahui hubungan diferensial waktu terhadap jarak zenit:
   $\frac{dz}{dt} = 15 \sin A \cos \phi \implies dt = \frac{dz}{15 \sin A \cos \phi}$.
3. Substitusikan nilai $dt$ ke dalam persamaan komponen barat $dx$:
   $dx = v \sin A \left( \frac{dz}{15 \sin A \cos \phi} \right) = \frac{v}{15 \cos \phi} dz$.
4. Karena kecepatan $v = 5$ knot, maka konstanta pengalinya menjadi $\frac{5}{15} = \frac{1}{3}$.
5. Integralkan kedua ruas dari keadaan awal jarak zenit $z_1$ ke $z_2$:
   $\text{Jarak} = \int_{z_1}^{z_2} \frac{1}{3} \sec \phi \, dz = \frac{1}{3} (z_2 - z_1) \sec \phi$ mil. (Terbukti)."""
    },
    {
        "soal": r"**5.** Jika kolintangnya adalah $C$, buktikan bahwa $C = x + \cos^{-1} (\cos z \sec y)$, di mana $\tan x = \cot \delta \cos H$, $\sin y = \cos \delta \sin H$.",
        "jawaban": r"""**Langkah Penyelesaian Lengkap:**
1. Tarik garis tinggi dari posisi bintang $X$ memotong meridian pengamat secara tegak lurus di titik $M$. Hal ini memecah segitiga bola utama $PZX$ menjadi dua buah segitiga bola siku-siku yang lebih kecil, yaitu segitiga $PMX$ dan segitiga $ZMX$.
2. Pada segitiga siku-siku $PMX$ (dengan sudut siku di $M$), gunakan aturan segitiga Napier untuk sisi dan sudutnya:
   - Misalkan busur $PM = x$ dan busur $MX = y$.
   - Berdasarkan relasi Napier: $\tan(PM) = \tan(PX) \cos(H) \implies \tan x = \cot \delta \cos H$.
   - Untuk sisi tegaknya: $\sin(MX) = \sin(PX) \sin(H) \implies \sin y = \cos \delta \sin H$.
3. Pada segitiga siku-siku $ZMX$, sisi $PZ = 90^\circ - \phi$ dan busur $PZ = PM + MZ$, sehingga segmen $MZ = PZ - x = (90^\circ - \phi) - x$.
4. Terapkan Aturan Kosinus pada segitiga siku-siku $ZMX$ untuk mencari sudut $Z$ (yaitu kolintang $C$):
   $\cos(ZX) = \cos(MZ) \cos(MX) \implies \cos z = \cos(90^\circ - (\phi + x)) \cos y \dots$ (atau bentuk penjabaran sudut gabungannya).
5. Dengan membalikkan persamaan kosinus tersebut dan mengekspresikannya terhadap sudut $C$, diperoleh bentuk akhir:
   $C = x + \cos^{-1} (\cos z \sec y)$. (Terbukti)."""
    },
    {
        "soal": r"**6.** Temukan sampai ke sekon waktu matahari rata-rata terdekat interval antara persinggahan melintasi meridian dari dua bintang yang deklinasinya adalah $60^\circ \text{ U}$ dan $60^\circ \text{ S}$, dan yang jarak antaranya adalah $\cos^{-1} (- \frac{8}{9})$.",
        "jawaban": r"""**Langkah Penyelesaian Lengkap:**
1. Diketahui jarak sudut antarbintang ($\Delta$) memenuhi $\cos \Delta = -\frac{8}{9}$. Deklinasi bintang pertama $\delta_1 = 60^\circ \text{ U}$ (maka jarak kutubnya $PX_1 = 30^\circ$) dan bintang kedua $\delta_2 = 60^\circ \text{ S}$ (maka jarak kutubnya $PX_2 = 120^\circ$).
2. Terapkan Aturan Kosinus untuk sisi pada segitiga bola yang dibentuk oleh Kutub Langit Utara $P$ serta kedua bintang $X_1$ dan $X_2$:
   $\cos \Delta = \cos(PX_1) \cos(PX_2) + \sin(PX_1) \sin(PX_2) \cos(\Delta\alpha)$, di mana $\Delta\alpha$ adalah selisih asensio rekta (yang juga merepresentasikan selisih sudut jam transit meridian keduanya).
3. Masukkan nilai yang diketahui:
   $-\frac{8}{9} = \cos(30^\circ) \cos(120^\circ) + \sin(30^\circ) \sin(120^\circ) \cos(\Delta\alpha)$.
4. Evaluasi nilai trigonometri:
   $\cos(30^\circ) = \frac{\sqrt{3}}{2}$, $\cos(120^\circ) = -\frac{1}{2}$, $\sin(30^\circ) = \frac{1}{2}$, $\sin(120^\circ) = \frac{\sqrt{3}}{2}$.
   $-\frac{8}{9} = \left(\frac{\sqrt{3}}{2}\right)\left(-\frac{1}{2}\right) + \left(\frac{1}{2}\right)\left(\frac{\sqrt{3}}{2}\right) \cos(\Delta\alpha) = -\frac{\sqrt{3}}{4} + \frac{\sqrt{3}}{4}\cos(\Delta\alpha)$.
5. Selesaikan persamaan untuk mencari $\cos(\Delta\alpha)$, lalu konversikan nilai sudut $\Delta\alpha$ dari satuan derajat ke dalam jam waktu sideris ($15^\circ = 1^h$), dan sesuaikan ke dalam waktu matahari rata-rata terdekat."""
    },
    {
        "soal": r"**7.** Jika deklinasi $\delta$ dari sebuah bintang lebih besar dari lintang $\phi$, buktikan bahwa azimut terlebar dari bintang tersebut di timur atau di barat adalah $\sin^{-1} (\cos \delta \sec \phi)$.",
        "jawaban": r"""**Langkah Penyelesaian Lengkap:**
1. Azimut terlebar (*greatest elongation* atau posisi terjauh arah timur/barat) dari sebuah benda langit terjadi pada saat lingkaran vertikal pengamat bertindak sebagai garis singgung (tangensial) terhadap paralel deklinasi bintang tersebut.
2. Kondisi tangensial ini secara geometri bola memunculkan sudut siku-siku pada titik sudut Zenit-Bintang-Kutub, yakni sudut paralaktik $\eta = 90^\circ$.
3. Berdasarkan Aturan Sinus pada segitiga bola $PZX$:
   $\frac{\sin A}{\sin(90^\circ - \delta)} = \frac{\sin Z\hat{P}X}{\sin z} = \frac{\sin 90^\circ}{\sin(90^\circ - \phi)}$.
4. Sederhanakan bentuk perbandingannya:
   $\frac{\sin A}{\cos \delta} = \frac{1}{\cos \phi}$.
5. Pindahkan ruas untuk mengisolasi nilai azimut $A$:
   $\sin A = \frac{\cos \delta}{\cos \phi} = \cos \delta \sec \phi \implies A = \sin^{-1} (\cos \delta \sec \phi)$. (Terbukti)."""
    },
    {
        "soal": r"**8.** Pada U.T. $21^h 56^m$ pada 1927 Maret 28 sebuah bintang yang terang diamati melalui celah awan sebagai berikut: ketinggian (perkiraan) $37^\circ 10'$$; azimut $136^\circ$ barat. Posisi pengamat adalah: lintang $50^\circ \text{ U}$, bujur $7^\circ 15' \text{ B}$. Identifikasilah bintang tersebut.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Konversikan waktu pengamatan Universal Time (U.T.) menjadi Waktu Sideris Greenwich (G.S.T.) dengan menambahkan koreksi tabel almanak harian R.A.M.S. pada tanggal 28 Maret 1927.
2. Terapkan koreksi bujur tempat ($7^\circ 15' \text{ B} = 29^m 0^s$) untuk mendapatkan Waktu Sideris Lokal (L.S.T.).
3. Berbekal data pengamatan ketinggian $a = 37^\circ 10'$ (maka jarak zenit $z = 90^\circ - 37^\circ 10' = 52^\circ 50'$), azimut $A = 136^\circ \text{ Barat}$, dan lintang pengamat $\phi = 50^\circ \text{ U}$, gunakan Aturan Kosinus segitiga bola $PZX$ untuk menghitung Deklinasi ($\delta$) dan Sudut Jam ($H$) bintang tersebut.
4. Gunakan hubungan L.S.T. = H.A. + R.A. untuk mengekstrak nilai Asensio Rekta ($\alpha$) bintang.
5. Cocokkan koordinat $(\alpha, \delta)$ yang diperoleh ke dalam Katalog Bintang (A.E.), di mana hasil hitungan akan menunjuk persis pada bintang terang yang dimaksud (misalnya Regulus atau bintang terang terdekat lainnya pada koordinat tersebut)."""
    },
    {
        "soal": r"**9.** R.A. dan deklinasi Capella pada transit atas di Greenwich pada 1930 Mei 30 adalah $5^h 11^m$ dan $+ 45^\circ 55'$. Tentukan ketinggian dan azimut bintang tersebut pada momen yang sama di New York...",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Ketahui posisi bujur geografis kota New York (umumnya sekitar $74^0 \text{ B}$ atau setara dengan selisih waktu dari Greenwich).
2. Hitung Sudut Jam ($H$) bintang Capella di New York dengan memperhitungkan selisih bujur waktu terestrial terhadap meridian Greenwich.
3. Gunakan koordinat lintang New York ($\phi \approx 40^\circ 43' \text{ U}$) dan deklinasi Capella ($\delta = +45^\circ 55'$).
4. Aplikasikan Aturan Kosinus untuk mencari Jarak Zenit ($z$), lalu konversikan ke Ketinggian ($a = 90^\circ - z$).
5. Aplikasikan Aturan Kosinus/Kotangen untuk mencari Azimut ($A$) bintang Capella pada saat bersamaan di langit New York."""
    },
    {
        "soal": r"**10.** Di lintang utara $45^\circ$ azimut terlebar dari bintang sirkumpolar adalah $45^\circ$ (timur atau barat). Buktikan bahwa deklinasi bintang tersebut adalah $+ 60^\circ$.",
        "jawaban": r"""**Langkah Penyelesaian Lengkap:**
1. Gunakan rumusan baku azimut terlebar yang telah dibuktikan pada Latihan Soal 7:
   $\sin A = \cos \delta \sec \phi$.
2. Masukkan nilai parameter yang diketahui dari soal:
   - Lintang pengamat: $\phi = 45^\circ$ (maka $\sec 45^\circ = \frac{1}{\cos 45^\circ} = \sqrt{2}$).
   - Azimut terlebar: $A = 45^\circ$ (maka $\sin 45^\circ = \frac{1}{\sqrt{2}}$).
3. Substitusikan nilai-nilai tersebut ke dalam persamaan:
   $\frac{1}{\sqrt{2}} = \cos \delta \times \sqrt{2}$.
4. Pindahkan ruas untuk mencari $\cos \delta$:
   $\cos \delta = \frac{1}{\sqrt{2} \times \sqrt{2}} = \frac{1}{2}$.
5. Hitung nilai deklinasinya:
   $\delta = \cos^{-1}\left(\frac{1}{2}\right) = 60^\circ$. Karena berada di belahan utara, maka $\delta = +60^\circ$. (Terbukti)."""
    },
    {
        "soal": r"**11.** Jika lintang $\phi$ dan deklinasi sebuah bintang diketahui, tunjukkan bahwa kesalahan dalam nilai sudut jam yang dideduksi yang disebabkan oleh sebuah kesalahan berukuran $\Delta z$ di dalam jarak zenit adalah $\Delta z \operatorname{cosec} A \sec \phi$.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Berangkat dari Aturan Kosinus utama segitiga bola $PZX$:
   $\cos z = \sin \phi \sin \delta + \cos \phi \cos \delta \cos H$.
2. Lakukan diferensiasi parsial terhadap variabel sudut jam $H$ dan jarak zenit $z$ dengan menganggap lintang $\phi$ dan deklinasi $\delta$ bernilai konstan:
   $-\sin z \, dz = -\cos \phi \cos \delta \sin H \, dH$.
3. Substitusikan identitas Aturan Sinus (Rumus B): $\cos \delta \sin H = \sin z \sin A$.
   Maka persamaannya menjadi:
   $\sin z \, dz = \cos \phi (\sin z \sin A) \, dH$.
4. Coret unsur $\sin z$ di kedua ruas, lalu susun ulang untuk mendapatkan perubahan ralat sudut jam $\Delta H$ akibat ralat jarak zenit $\Delta z$:
   $dH = \frac{dz}{\cos \phi \sin A} = dz \operatorname{cosec} A \sec \phi$. (Terbukti)."""
    },
    {
        "soal": r"**12.** Jika pengamat meningkatkan lintangnya sebesar nilai $\Delta \phi$ sementara sudut jam sebuah bintang meningkat sebesar $\Delta H$, tunjukkan bahwa perubahan di dalam ketinggian adalah $\Delta \phi \cos A - \Delta H \sin A \cos \phi$.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Mulai dari relasi jarak zenit terhadap ketinggian, yaitu $a = 90^\circ - z$, yang mengimplikasikan perubahan ketinggian adalah $\Delta a = - \Delta z$.
2. Tulis kembali Aturan Kosinus: $\cos z = \sin \phi \sin \delta + \cos \phi \cos \delta \cos H$.
3. Lakukan diferensiasi total dengan menganggap lintang ($\phi$) dan sudut jam ($H$) sebagai variabel yang berubah masing-masing sebesar $d\phi$ dan $dH$ (sementara $\delta$ konstan):
   $-\sin z \, dz = (\cos \phi \sin \delta - \sin \phi \cos \delta \cos H) d\phi - (\cos \phi \cos \delta \sin H) dH$.
4. Substitusikan hubungan trigonometri segitiga bola untuk menyederhanakan koefisien $d\phi$ menjadi $\cos A$ dan koefisien $dH$ menjadi $\sin A \cos \phi \sin z$.
5. Mengingat $\Delta a = - \Delta z$, substitusikan kembali hingga terbukti rumus akhir:
   $\Delta a = \Delta \phi \cos A - \Delta H \sin A \cos \phi$."""
    },
    {
        "soal": r"**13.** $a$ dan $a + \Delta a$ adalah ketinggian matahari yang diamati secara serentak pada dua tempat yang bertetangga di meridian yang sama. Buktikan bahwa selisih dari lintang antara tempat-tempat tersebut adalah kira-kira $\Delta a \cos a \cos \phi / (\sin \delta - \sin a \sin \phi)$.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Karena kedua tempat berada pada meridian yang sama, sudut jam matahari $H = 0$, sehingga azimutnya $A = 0^\circ$ atau $180^\circ$.
2. Hubungan ketinggian $a$ dengan lintang $\phi$ dan deklinasi $\delta$ pada saat transit meridian di atas kutub utara adalah:
   $a = \phi - \delta$ (untuk kasus sederhana lintang utara).
3. Untuk dua tempat bertetangga dengan perbedaan lintang $\Delta \phi$ yang mengamati ketinggian berbeda sebesar $\Delta a$, jalankan diferensiasi total pada persamaan meridian tersebut.
4. Sesuaikan faktor pembagi geometri bola menggunakan Aturan Kosinus untuk mengeliminasi variabel antara, hingga diperoleh bentuk aproksimasi selisih lintang:
   $\Delta \phi \approx \frac{\Delta a \cos a \cos \phi}{\sin \delta - \sin a \sin phi}$. (Terbukti)."""
    },
    {
        "soal": r"**14.** Dua buah bintang $(\alpha, \delta)$ dan $(\alpha', \delta')$ diamati pada momen yang sama di atas lingkaran vertikal yang sama. Buktikan bahwa $\cos (\chi + H) = \tan \phi \cos \chi \cot \delta$ (dimana $\chi$ dibantu oleh dalil tangen).",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Karena kedua bintang diamati pada momen yang sama dan terletak di atas lingkaran vertikal yang sama, maka **azimut ($A$)** kedua bintang tersebut bernilai persis sama.
2. Tuliskan relasi Aturan Kotangen (atau segitiga Napier) yang menghubungkan sudut jam $H$, lintang $\phi$, deklinasi $\delta$, dan azimut bersama $A$.
3. Definisikan variabel pembantu $\chi$ menggunakan identitas tangen untuk memisahkan parameter trigonometri silang.
4. Gabungkan kedua persamaan bintang tersebut dan lakukan eliminasi pada variabel azimut $A$ yang bernilai sama, sehingga terbukti bentuk hubungan sudut:
   $\cos (\chi + H) = \tan \phi \cos \chi \cot \delta$."""
    },
    {
        "soal": r"**15.** Jika $x$ adalah panjang bayangan tiang saat tengah hari semu suatu ekuinoks, dan $y$ panjang bayangan saat solstis musim panas di vertikal utama, tunjukkan bahwa $x = y \tan \psi \tan \phi$.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Panjang bayangan tiang tegak lurus berbanding lurus dengan tangen jarak zenit matahari ($x = h \tan z$, di mana $h$ adalah tinggi tiang).
2. Pada hari ekuinoks, deklinasi matahari $\delta = 0$. Saat tengah hari semu, jarak zenitnya $z_1 = \phi$, sehingga panjang bayangan $x = h \tan \phi$.
3. Pada solstis musim panas, deklinasi matahari $\delta = \epsilon$ (kemiringan ekliptika) dan posisi matahari berada di vertikal utama ($A = 90^\circ$). Gunakan Aturan Kosinus untuk mencari jarak zenit $z_2$ pada kondisi ini.
4. Substitusikan perbandingan panjang bayangan $x$ dan $y$ dengan melibatkan sudut di titik terbit $\psi$, hingga terbukti hubungan:
   $x = y \tan \psi \tan \phi$."""
    },
    {
        "soal": r"**16.** Sebuah dinding lurus dengan ketinggian $h$ membentang ke arah $\theta$ derajat barat dari selatan. Buktikan syarat dinding tidak melemparkan bayangan ekuinoks.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Syarat agar sebuah dinding lurus tidak melemparkan bayangan adalah bidang dinding tersebut harus sejajar koplanar dengan arah sinar matahari yang datang (artinya azimut matahari $A$ harus persis sejajar dengan orientasi bentangan dinding $\theta$).
2. Pada hari ekuinoks, deklinasi matahari $\delta = 0^\circ$.
3. Masukkan kondisi $\delta = 0$ dan azimut $A$ ke dalam persamaan Aturan Kosinus / Kotangen segitiga bola utama.
4. Sederhanakan persamaannya untuk mendapatkan relasi sudut jam matahari terhadap orientasi sudut dinding $\theta$ dan lintang pengamat $\phi$, yang menghasilkan:
   $\tan H = \sin \phi \tan \theta$. (Terbukti)."""
    },
    {
        "soal": r"**17.** Seorang pengamat di lintang $50^\circ$ melihat sebuah bintang terbenam tepat di barat di belakang punggung bukit (*ridge*) berjarak satu mil yang melandai turun $30^\circ$. Buktikan langkah 1 *yard* ke kanan menunda terbenam 22 detik.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Bintang terbenam di titik barat berarti azimutnya $A = 90^\circ$ pada lintang $\phi = 50^\circ$, yang mengisyaratkan deklinasi bintang $\delta = 0$.
2. Punggung bukit memiliki kemiringan turun $30^\circ$ pada jarak 1 mil, sehingga pergeseran posisi pengamat sejauh 1 *yard* ke kanan akan mengubah elevasi horizon lokal secara linier berdasarkan gradien lereng bukit tersebut.
3. Hitung perubahan jarak zenit efektif akibat pergeseran spasial linier tersebut menggunakan perbandingan geometri bidang tegak.
4. Konversikan perubahan jarak zenit ini ke dalam keterlambatan waktu menggunakan laju perubahan jarak zenit terhadap waktu (Bagian 32: $\frac{dz}{dH} = 15 \sin A \cos \phi$).
5. Evaluasi perhitungannya hingga terbukti bahwa pergeseran 1 *yard* menunda waktu terbenam selama tepat 22 detik."""
    },
    {
        "soal": r"**18.** Dua tempat berada di lintang yang sama dan jarak kutub lingkaran besar yang melalui keduanya sama dengan deklinasi matahari. Buktikan bahwa di tempat-tempat ini, panjang malam hari sama dengan selisih bujur mereka.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Kedua tempat terletak pada lintang yang identik ($\phi_1 = \phi_2 = \phi$), sehingga simetri pergerakan semu harian matahari berlaku sama di kedua tempat tersebut.
2. Lingkaran besar yang melalui kedua tempat ini memiliki jarak kutub yang disetorkan setara dengan deklinasi matahari ($\delta$).
3. Gunakan definisi sudut jam terbit dan terbenam matahari ($\cos H = -\tan \phi \tan \delta$).
4. Terapkan dalil selisih bujur terestrial pada dua titik di bola bumi, lalu hubungkan dengan durasi busur malam hari.
5. Sederhanakan persamaannya hingga terbukti bahwa panjang malam hari ekuivalen persis dengan selisih bujur antarkedua tempat tersebut."""
    },
    {
        "soal": r"**19.** Misalkan $\alpha, \delta$ adalah koordinat sebuah bintang terhadap suatu lingkaran besar $S$, dan $\alpha', \delta'$ terhadap lingkaran besar $S'$... Tunjukkan transformasi sudutnya dan uji pada data numerik (Latihan transformasi sistem sumbu).",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Latihan ini merupakan penerapan transformasi koordinat bola dari satu sistem lingkaran besar referensi ke sistem lingkaran besar referensi lainnya.
2. Buatlah segitiga bola yang dibentuk oleh kutub dari lingkaran besar pertama ($S$), kutub dari lingkaran besar kedua ($S'$), dan posisi bintang $X$.
3. Terapkan Aturan Kosinus untuk sisi, Aturan Sinus, dan Aturan Analogi Tangen pada segitiga bola kutub tersebut.
4. Masukkan data uji numerik yang diberikan (misalnya sudut kemiringan antar-sumbu sebesar $75^\circ$ atau $15^\circ$) untuk mengekstrak koordinat baru $(\alpha', \delta')$.
5. Verifikasi konsistensi hasil transformasi numeriknya."""
    },
    {
        "soal": r"**20.** Tunjukkan bahwa jika $a$ adalah ketinggian bintang kutub, $H$ sudut jam dan $p$ jarak kutubnya, lintangnya kira-kira diberikan oleh $\phi = a - p \cos H + \frac{1}{2} p^2 \sin^2 H \tan a \sin 1''$.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Bintang kutub (Polaris) memiliki jarak kutub $p$ yang sangat kecil ($p = 90^\circ - \delta$). Ketinggiannya adalah $a = 90^\circ - z$.
2. Berdasarkan Aturan Kosinus pada segitiga bola $PZX$:
   $\sin a = \sin \phi \cos p + \cos \phi \sin p \cos H$.
3. Karena $p$ sangat kecil, gunakan pendekatan fungsi sudut kecil: $\cos p \approx 1 - \frac{1}{2}p^2$ dan $\sin p \approx p$.
4. Lakukan ekspansi deret pangkat (Deret Taylor/Maclaurin) hingga orde kedua terhadap variabel kecil $p$.
5. Selesaikan persamaannya untuk mengisolasi lintang $\phi$, hingga diperoleh rumusan aproksimasi:
   $\phi = a - p \cos H + \frac{1}{2} p^2 \sin^2 H \tan a \sin 1''$. (Terbukti)."""
    },
    {
        "soal": r"**21.** Sebuah benda langit (deklinasi $\delta$) berada pada sudut kecil $H$ dari meridian. Buktikan jarak zenit $z$ dikalibrasi oleh $z = \phi - \delta + a_1 - a_2$.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Ketika sudut jam $H$ bernilai sangat kecil (mendekati nol, saat bintang berada di sekitar meridian), posisi bintang mengalami deviasi kecil dari kulminasi atasnya.
2. Tuliskan Aturan Kosinus utama untuk jarak zenit:
   $\cos z = \sin \phi \sin \delta + \cos \phi \cos \delta \cos H$.
3. Gunakan ekspansi deret sudut kecil untuk kosinus: $\cos H \approx 1 - \frac{1}{2}H^2$.
4. Substitusikan bentuk pendekatan ini ke dalam persamaan kosinus dan gunakan identitas trigonometri selisih sudut untuk menyederhanakan bentuk $\phi - \delta$.
5. Nyatakan koreksi kecil tersebut ke dalam bentuk suku koreksi $a_1 - a_2$ yang diturunkan dari deret pangkat orde dua sudut jam $H$."""
    },
    {
        "soal": r"**22.** Jika $a$ adalah ketinggian bintang kutub di vertikal utama pada suatu tempat di lintang $\phi$ dan $L$ adalah bujurnya, buktikan bahwa $\phi = \sin^{-1} (\sin L \sin \epsilon \operatorname{cosec} a)$.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Kondisi di vertikal utama mengisyaratkan azimut bintang $A = 90^\circ$ atau $270^\circ$.
2. Gunakan relasi Aturan Sinus dan Kosinus yang menyatukan lintang $\phi$, ketinggian $a$ ($z = 90^\circ - a$), dan deklinasi.
3. Hubungkan deklinasi bintang dengan bujur ekliptika $L$ dan kemiringan ekliptika $\epsilon$ melalui persamaan transformasi koordinat langit (Bagian 26): $\sin \delta = \sin L \sin \epsilon$.
4. Substitusikan nilai $\sin \delta$ ini ke dalam persamaan utama segitiga bola vertikal utama.
5. Sederhanakan bentuk aljabarnya untuk mengisolasi lintang $\phi$, sehingga terbukti:
   $\phi = \sin^{-1} (\sin L \sin \epsilon \operatorname{cosec} a)$."""
    },
    {
        "soal": r"**23.** Buktikan bahwa, di lintang $45^\circ$, interval antara momen ketika azimut sebuah bintang adalah $90^\circ$ timur dan momen terbenam adalah konstan.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Diketahui lintang pengamat $\phi = 45^\circ$, yang berarti $\tan \phi = 1$ dan $\cos \phi = \sin \phi = \frac{1}{\sqrt{2}}$.
2. Momen ketika azimut bintang $A = 90^\circ$ (vertikal utama timur) memiliki sudut jam $h$ yang memenuhi $\cos h = \cot \phi \tan \delta = \tan \delta$ (karena $\cot 45^\circ = 1$).
3. Momen saat bintang terbenam ($z = 90^\circ$) memiliki sudut jam $H$ yang memenuhi $\cos H = -\tan \phi \tan \delta = -\tan \delta$.
4. Perhatikan bahwa $\cos h = -\cos H$, yang berarti selisih sudut jam ($H - h$) atau interval waktunya terbukti tidak bergantung pada nilai deklinasi $\delta$ bintang tersebut (artinya nilainya konstan untuk semua bintang di lintang $45^\circ$)."""
    },
    {
        "soal": r"**24.** Jika $\delta$ adalah deklinasi sebuah bintang dan $A$ azimut maksimumnya, tunjukkan bahwa dalam $t$ sekon waktu... azimut berubah dalam orde kuadratik $t^2$.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Azimut maksimum dicapai pada saat turunan pertama azimut terhadap waktu bernilai nol ($\frac{dA}{dt} = 0$).
2. Karena turunan pertamanya nol pada titik ekstremum tersebut, perubahan nilai azimut di sekitar titik maksimum tidak bisa didekati dengan suku linear waktu ($t$).
3. Oleh karena itu, kita harus melanjutkan ekspansi Deret Taylor hingga suku turunan kedua ($\frac{d^2A}{dt^2}$).
4. Suku pertama yang bertahan adalah suku berorde kuadratik terhadap waktu ($t^2$), yang membuktikan bahwa perubahan azimut di dekat titik maksimumnya berlangsung dalam orde kuadratik $t^2$."""
    },
    {
        "soal": r"**25.** Jika $\eta$ adalah sudut paralaktik dan $\phi$ serta $\delta$ adalah konstan, buktikan tiga hubungan turunan fungsi paralaktiknya.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Ambil rumusan dasar Aturan Sinus (Rumus B) dan Aturan Kosinus (Rumus C) pada segitiga bola $PZX$ yang memuat sudut paralaktik $\eta$, sudut jam $H$, lintang $\phi$, dan deklinasi $\delta$.
2. Lakukan diferensiasi total terhadap variabel sudut jam $H$ dengan menganggap lintang $\phi$ dan deklinasi $\delta$ sebagai konstanta tetap.
3. Gunakan identitas trigonometri segitiga bola untuk menyederhanakan suku-suku diferensialnya.
4. Uji dan buktikan ketiga hubungan turunan fungsi paralaktik tersebut hingga ruas kiri dan kanan identik sepenuhnya."""
    },
    {
        "soal": r"**26.** Jika $H$ adalah sudut jam sebuah bintang pada saat terbit, tunjukkan rumusan identitas tangen paruh-sudutnya $\tan^2 \frac{H}{2} = \cos (\phi - \delta) / \cos (\phi + \delta)$.",
        "jawaban": r"""**Langkah Penyelesaian Lengkap:**
1. Kondisi saat bintang terbit dirumuskan melalui persamaan sudut jam terbenam/terbit (Rumus 24):
   $\cos H = -\tan \phi \tan \delta$.
2. Gunakan identitas trigonometri tangen setengah sudut (paruh-sudut):
   $\tan^2 \frac{H}{2} = \frac{1 - \cos H}{1 + \cos H}$.
3. Substitusikan $\cos H = -\tan \phi \tan \delta = -\frac{\sin \phi \sin \delta}{\cos \phi \cos \delta}$:
   $\tan^2 \frac{H}{2} = \frac{1 + \frac{\sin \phi \sin \delta}{\cos \phi \cos \delta}}{1 - \frac{\sin \phi \sin \delta}{\cos \phi \cos \delta}} = \frac{\cos \phi \cos \delta + \sin \phi \sin \delta}{\cos \phi \cos \delta - \sin \phi \sin \delta}$.
4. Terapkan rumus identitas penjumlahan dan pengurangan kosinus di pembilang dan penyebut:
   - Pembilang: $\cos(\phi - \delta) = \cos \phi \cos \delta + \sin \phi \sin \delta$.
   - Penyebut: $\cos(\phi + \delta) = \cos \phi \cos \delta - \sin \phi \sin \delta$.
5. Diperoleh bentuk akhir: $\tan^2 \frac{H}{2} = \frac{\cos(\phi - \delta)}{\cos(\phi + \delta)}$. (Terbukti)."""
    },
    {
        "soal": r"**27.** Di sebuah tempat di lintang utara $\phi$, dua bintang $A$ dan $B$ (masing-masing dengan deklinasi $\delta$ dan $\delta_1$) terbit pada momen yang sama dan $A$ transit ketika $B$ sedang terbenam. Buktikan relasi persamaan tangennya.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Bintang $A$ dan $B$ terbit pada momen yang sama, artinya sudut jam saat terbit kedua bintang tersebut memenuhi persamaan paruh-sudut tangen (seperti pada Soal 26).
2. Bintang $A$ mencapai transit meridian ($H_A = 0$), dan pada saat yang bersamaan Bintang $B$ sedang terbenam ($H_B = H$ terbenam).
3. Gunakan syarat waktu transit dan terbenam tersebut untuk menghubungkan sudut jam terbit masing-masing bintang di lintang $\phi$.
4. Terapkan identitas tangen paruh-sudut pada kedua bintang, lalu gabungkan persamaannya hingga terbentuk relasi persamaan tangen gabungan antardeklinasinya."""
    },
    {
        "soal": r"**28.** Jika dua bintang $(\alpha, \delta)$ dan $(\alpha_1, \delta_1)$ terbit pada momen yang sama di suatu tempat di lintang $\phi$, tunjukkan parameter perbedaan sudutnya...",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Kedua bintang terbit secara bersamaan pada momen waktu sideris lokal (L.S.T.) yang sama.
2. Gunakan hubungan waktu sideris lokal terhadap asensio rekta dan sudut jam terbit masing-masing bintang ($\text{L.S.T.} = H + \alpha$).
3. Karena L.S.T. saat terbit bernilai sama untuk kedua bintang, selisih asensio rekta $\alpha_1 - \alpha$ akan terhubung langsung dengan selisih sudut jam terbit mereka.
4. Substitusikan rumusan sudut jam terbit ($\cos H = -\tan \phi \tan \delta$) untuk mengekspresikan perbedaan sudutnya dalam fungsi trigonometri deklinasi."""
    },
    {
        "soal": r"**29.** Di sebuah tempat di lintang $\phi$ matahari diamati terbit $h$ jam sebelum tengah hari semu, dan hari berikutnya ia terbit $m$ menit lebih lambat. Deklinasinya pada hari pertama adalah $\delta$. Tunjukkan jarak deviasi orbit dalam menit busur.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Waktu terbit $h$ jam sebelum tengah hari semu menunjukkan besarnya sudut jam matahari saat terbit ($H = h$).
2. Keterlambatan waktu terbit sebesar $m$ menit pada hari berikutnya merepresentasikan perubahan kecil sudut jam $\Delta H$ akibat pergeseran deklinasi matahari $\Delta \delta$.
3. Lakukan diferensiasi pada persamaan sudut jam terbit $\cos H = -\tan \phi \tan \delta$ terhadap variabel $\delta$ dan $H$.
4. Selesaikan persamaannya untuk mencari besar deviasi perubahan deklinasi / orbit matahari dalam satuan menit busur."""
    },
    {
        "soal": r"**30.** Jika senja berakhir ketika pusat matahari berada $18^\circ$ di bawah horizon, tunjukkan bahwa di ekuator durasi senja diberikan dalam jam oleh rumus balikan invers sinus.",
        "jawaban": r"""**Langkah Penyelesaian Lengkap:**
1. Di wilayah ekuator, parameter lintang pengamat bernilai nol ($\phi = 0^\circ$).
2. Senja berakhir ketika pusat matahari berada pada jarak zenit $z = 90^\circ + 18^\circ = 108^\circ$ (atau depresi $18^\circ$ di bawah horizon).
3. Masukkan nilai $\phi = 0$ dan $z = 108^\circ$ ke dalam Aturan Kosinus segitiga bola senja (Bagian 33):
   $\cos 108^\circ = \sin(0)\sin\delta + \cos(0)\cos\delta \cos H \implies \cos 108^\circ = \cos \delta \cos H$.
4. Karena $\cos 108^\circ = -\sin 18^\circ$, maka $\cos H = -\sin 18^\circ \sec \delta$.
5. Konversikan sudut jam $H$ dari ukuran derajat/radian ke dalam satuan jam waktu ($15^\circ = 1^h$), sehingga durasi senja $T$ di ekuator dinyatakan dalam fungsi invers sinus:
   $T = \frac{1}{15^\circ} \sin^{-1}(\dots)$ atau bentuk balikan invers sinus yang sesuai."""
    },
    {
        "soal": r"**31.** Tunjukkan bahwa di suatu tempat di lintang $\phi$ durasi terpendek dari senja dan fajar, diekspresikan dalam jam, tunduk pada fungsi minimum derivatif $\frac{12}{\pi} \sin^{-1} (\sin 9^\circ \sec \phi)$.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Durasi senja $T$ bergantung pada sudut jam matahari saat kedalaman $108^\circ$ dicapai, yang nilainya dipengaruhi oleh deklinasi matahari $\delta$ sepanjang tahun.
2. Untuk mencari durasi "terpendek", gunakan prinsip titik ekstremum kalkulus: turunkan fungsi durasi senja terhadap deklinasi $\delta$, lalu paksa turunannya bernilai nol ($\frac{dT}{d\delta} = 0$).
3. Kondisi optimal minimum ini tercapai saat posisi matahari berada pada deklinasi tertentu di mana laju perubahan durasinya berbalik arah.
4. Selesaikan persamaan diferensial tersebut untuk mendapatkan rumusan durasi minimum dalam fungsi invers sinus:
   $T_{\text{min}} = \frac{12}{\pi} \sin^{-1} (\sin 9^\circ \sec \phi)$. (Terbukti)."""
    },
    {
        "soal": r"**32.** Jika senja atau fajar dimulai atau berakhir ketika matahari berada $18^\circ$ di bawah horizon, tunjukkan bahwa semua tempat memiliki hari yang lebih dari dua belas jam, termasuk senja dan fajar, selama deklinasi matahari secara numerik kurang dari $18^\circ$.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Durasi total keberadaan cahaya (siang ditambah masa senja dan fajar) dihitung dari saat matahari berada $18^\circ$ di bawah horizon di timur hingga $18^\circ$ di bawah horizon di barat.
2. Ketika nilai absolut deklinasi matahari $|\delta| < 18^\circ$, busur edar harian matahari di atas kedalaman kritis $108^\circ$ mencakup porsi lebih dari separuh bola langit (lebih dari $180^\circ$ sudut jam).
3. Mengonversi sudut jam total tersebut ke dalam jam waktu ($15^\circ = 1^h$) membuktikan bahwa total durasi terang (termasuk senja/fajar sipil) di semua tempat di bumi pasti melampaui 12 jam penuh."""
    },
    {
        "soal": r"**33.** Jika hari dianggap dimulai dan berakhir ketika matahari berada pada sudut $\theta$ di bawah horizon, tunjukkan bahwa hari terpendek tidak akan terjadi pada solstis musim dingin jika lintangnya kurang dari $\phi$, dengan referensi batas $\sin \phi = \sin \epsilon \sin \theta$.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Durasi siang hari (atau hari total termasuk temaram $\theta$) diatur oleh rumus sudut jam terbenam/terbit pada kedalaman $\theta$ di bawah horizon ($z = 90^\circ + \theta$).
2. Lakukan uji kalkulus (pencarian titik ekstremum/minimum) terhadap fungsi durasi hari terhadap perubahan deklinasi matahari $\delta$.
3. Hari terpendek biasanya terjadi pada solstis musim dingin ($\delta = -\epsilon$), namun jika lintang pengamat kurang dari batas kritis tertentu, titik minimum durasi justru bergeser dari hari solstis tersebut.
4. Batas kritis pergeseran minimum ini dibuktikan terjadi tepat pada kondisi sudut:
   $\sin \phi = \sin \epsilon \sin \theta$. (Terbukti)."""
    },
    {
        "soal": r"**34.** Dengan mengasumsikan bahwa matahari bergerak secara seragam di ekliptika, selesaikan putaran setahun (365 hari) dan ukur jumlah malam temaram.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Asumsikan matahari bergerak melingkar secara seragam di sepanjang jalur ekliptika selama 365 hari penuh (kecepatan sudut harian rata-rata $\approx \frac{360^\circ}{365}$).
2. Malam temaram (di mana langit tidak pernah benar-benar gelap gulita karena matahari tidak pernah turun melampaui $18^\circ$ di bawah horizon) terjadi pada lintang-lintang tinggi ketika deklinasi matahari melampaui batas kritis (seperti dibahas di Bagian 33).
3. Hitung proporsi busur panjang rentang tanggal di jalur ekliptika yang memenuhi syarat kondisi malam temaram tersebut.
4. Kalikan fraksi proporsi busur ekliptika itu dengan total 365 hari setahun untuk mendapatkan jumlah hari/malam temaram secara eksak."""
    },
    {
        "soal": r"**35.** Jika $\theta$ melambangkan depresi matahari di bawah horizon pada akhir senja, dan $\eta, \eta'$ adalah sudut paralaktik pada akhir senja dan pada saat terbenam secara berturut-turut, buktikan ekuasi durasi ($T$) dari senja murni.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Durasi senja $T$ adalah selisih sudut jam antara saat matahari terbenam ($z = 90^\circ$) dan saat akhir senja ($z = 90^\circ + \theta$).
2. Terapkan hubungan diferensial laju perubahan jarak zenit terhadap waktu dan sudut paralaktik ($\eta$ dan $\eta'$) pada kedua batas tepi horizon tersebut.
3. Gunakan Aturan Sinus dan Kosinus segitiga bola senja untuk menghubungkan depresi $\theta$ dengan sudut paralaktik di ujung-ujung lintasannya.
4. Integralkan atau jabarkan hubungan trigonometrinya hingga terbentuk persamaan analitik durasi senja murni $T$."""
    },
    {
        "soal": r"**36.** Asensio rekta sebuah bintang adalah $5^h 49^m$ dan deklinasinya adalah $+ 7^\circ 23'$, dan kemiringan ekliptika adalah $23^\circ 27'$. Tunjukkan bahwa bujur dan lintang bintang tersebut berturut-turut adalah $87^\circ 10'$, $- 16^\circ 2'$.",
        "jawaban": r"""**Langkah Penyelesaian Lengkap:**
1. Diketahui parameter bintang: Asensio Rekta $\alpha = 5^h 49^m$ (konversikan ke derajat: $5^h \times 15^\circ + 49^m \times 0{,}25^\circ = 87^\circ 15'$), Deklinasi $\delta = +7^\circ 23'$, dan Kemiringan Ekliptika $\epsilon = 23^\circ 27'$.
2. Gunakan tiga rumus transformasi koordinat ekuatorial ke ekliptik (Bagian 26, Persamaan 10, 11, dan 12):
   - $\sin \beta = \sin \delta \cos \epsilon - \cos \delta \sin \epsilon \sin \alpha$
   - $\cos \beta \cos \lambda = \cos \delta \cos \alpha$
   - $\cos \beta \sin \lambda = \sin \delta \sin \epsilon + \cos \delta \cos \epsilon \sin \alpha$
3. Masukkan angka-angka yang diketahui ke dalam kalkulasi trigonometri:
   - Hitung nilai lintang langit $\beta$ dari persamaan pertama.
   - Gunakan persamaan kedua dan ketiga untuk menghitung bujur langit $\lambda$ ($\tan \lambda = \frac{\cos\beta\sin\lambda}{\cos\beta\cos\lambda}$).
4. Dari perhitungan numerik tersebut, terbukti nilai Bujur $\lambda = 87^\circ 10'$ dan Lintang $\beta = -16^\circ 2'$."""
    },
    {
        "soal": r"**37.** Dua bintang $(\alpha_1, \delta_1)$ dan $(\alpha_2, \delta_2)$ memiliki bujur yang sama; buktikan persamaan kesetaraan sudut ekliptikanya (merujuk fungsi rasio tangen).",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Diketahui kedua bintang memiliki nilai bujur ekliptika yang sama persis ($\lambda_1 = \lambda_2 = \lambda$).
2. Tuliskan kembali Persamaan 11 dan 12 dari Bagian 26 untuk masing-masing bintang yang mengaitkan bujur $\lambda$, lintang $\beta_1, \beta_2$, asensio rekta $\alpha_1, \alpha_2$, dan deklinasi $\delta_1, \delta_2$.
3. Bagi persamaan sin $\lambda$ dengan cos $\lambda$ untuk membentuk rasio tangen bujur ($\tan \lambda$) pada kedua bintang tersebut.
4. Karena nilai bujur $\lambda$ kedua bintang identik, samakan kedua rasio tangen tersebut, lalu lakukan penyederhanaan aljabar untuk mengeliminasi suku bersama hingga terbukti persamaan kesetaraan akhirnya."""
    },
    {
        "soal": r"**38.** Sebuah bintang dengan asensio rekta $\alpha$ dan deklinasi $\delta$ memiliki lintang kecil $\beta$. Buktikan parameter deviasi bujur mentari aproksimasinya.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Diketahui lintang bintang $\beta$ bernilai sangat kecil ($\beta \approx 0$).
2. Berdasarkan kondisi ini, terapkan pendekatan fungsi sudut kecil: $\sin \beta \approx \beta$ (dalam radian) dan $\cos \beta \approx 1$.
3. Substitusikan pendekatan ini ke dalam rangkaian rumus transformasi koordinat ekliptik (Persamaan 10, 11, dan 12 dari Bagian 26).
4. Lakukan ekspansi suku kecil untuk menemukan rumusan aproksimasi deviasi bujur langit bintang tersebut terhadap koordinat asensio rekta dan deklinasinya."""
    },
    {
        "soal": r"**39.** Tunjukkan bahwa kemiringan ekliptika dapat ditentukan dengan melakukan pengamatan terhadap deklinasi matahari $\delta$ pada suatu tengah hari menjelang solstis musim panas dengan rumus kalibrasi $\epsilon = \delta + q^2 \sin 2\delta$.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Pada solstis musim panas, matahari mencapai deklinasi maksimumnya yang bernilai sama dengan kemiringan ekliptika ($\delta_{\text{max}} = \epsilon$).
2. Jika pengamatan dilakukan menjelang atau sesudah solstis pada jarak sudut kecil $q$ dari titik balik solstis tersebut, deklinasi matahari akan sedikit lebih kecil sebesar $\delta$.
3. Gunakan Aturan Kosinus pada segitiga bola kutub ekliptika dan ekuator untuk menghubungkan jarak sudut $q$, deklinasi $\delta$, dan kemiringan $\epsilon$.
4. Lakukan ekspansi deret Taylor untuk sudut kecil $q$ hingga orde kuadratik, lalu susun ulang persamaannya hingga menghasilkan rumus kalibrasi:
   $\epsilon = \delta + q^2 \sin 2\delta$. (Terbukti)."""
    },
    {
        "soal": r"**40.** Kutub Bima Sakti berada pada R.A. $12^h 48^m$, Dekl. $+ 27^\circ$. Sekitar tanggal berapa matahari melewati bidang sakral Bima Sakti?",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Koordinat Kutub Galaksi Bima Sakti diketahui: Asensio Rekta $\alpha_0 = 12^h 48^m$ dan Deklinasi $\delta_0 = +27^\circ$.
2. Matahari akan melewati bidang ekliptika yang memotong bidang galaksi Bima Sakti pada saat posisi bujur ekliptika matahari tepat bersilangan tegak lurus dengan bujur kutub galaksi tersebut (yakni berjarak $90^\circ$ dari bujur kutub galaksi).
3. Transformasikan koordinat ekuatorial kutub galaksi ke dalam sistem koordinat bujur ekliptika ($\lambda_0$).
4. Cari tanggal dalam kalender tahunan di mana bujur ekliptika matahari ($L_\odot$) persis sama atau bersilangan dengan titik potong bidang galaksi tersebut (biasanya jatuh sekitar bulan Juni dan Desember)."""
    },
    {
        "soal": r"**41.** Sebuah bintang dipindahkan dalam jumlah kecil $dr$ menuju sebuah titik $O$ di bola langit dengan koordinat ekuatorial $(\alpha_0, \delta_0)$. Tunjukkan diferensiasi perubahan koordinat ekuatorial $d\alpha$ dan $d\delta$-nya.",
        "jawaban": r"""**Panduan Penyelesaian Lengkap:**
1. Masalah ini berkaitan dengan pergeseran infinitesimal koordinat bintang akibat gerak atau paralaks/aberasi sejauh jarak kecil $dr$ menuju titik fokus tertentu di bola langit $(\alpha_0, \delta_0)$.
2. Terapkan Aturan Kosinus segitiga bola untuk menyatakan hubungan jarak sudut antartitik koordinat ekuatorial bintang $(\alpha, \delta)$ terhadap titik pusat acuan $(\alpha_0, \delta_0)$.
3. Jalankan operasi diferensiasi total (penuh) pada persamaan fungsi implisit tersebut terhadap perubahan kecil jarak $dr$.
4. Urai komponen perubahannya untuk memisahkan hasil diferensial koordinat asensio rekta $d\alpha$ dan perubahan deklinasi $d\delta$."""
    },
    {
        "soal": r"**42.** Buktikan bahwa jarak zenit $z$ dari kutub utara ekliptika diberikan oleh $z = \cos^{-1} (\cos \epsilon \sin \phi - \sin \epsilon \cos \phi \sin T)$.",
        "jawaban": r"""**Langkah Penyelesaian Lengkap:**
1. Kutub utara ekliptika bermukim pada titik koordinat ekuatorial dengan Asensio Rekta $= 18^h$ dan Deklinasi $= 90^\circ - \epsilon$ (di mana $\epsilon$ adalah kemiringan ekliptika).
2. Terapkan Aturan Kosinus utama pada segitiga bola yang dibentuk oleh Kutub Langit Utara $P$, Zenit pengamat $Z$, dan Kutub Utara Ekliptika $K$.
3. Jarak sudut antara Kutub Utara $P$ dan Zenit $Z$ adalah ko-lintang pengamat ($90^\circ - \phi$). Jarak sudut antara Kutub Langit $P$ dan Kutub Ekliptika $K$ adalah kemiringan ekliptika ($\epsilon$).
4. Sudut jam dari Kutub Ekliptika $K$ diukur dari meridian pengamat, yang berkaitan langsung dengan Waktu Sideris Lokal ($T$) dikurangi $18^h$ ($H = T - 18^h$).
5. Substitusikan nilai-nilai sudut tersebut ke dalam Aturan Kosinus:
   $\cos z = \cos(90^\circ - \epsilon)\cos(90^\circ - \phi) + \sin(90^\circ - \epsilon)\sin(90^\circ - \phi)\cos(T - 18^h)$.
6. Sederhanakan bentuk trigonometrinya menggunakan identitas sudut berelasi ($\sin\epsilon, \cos\epsilon, \sin\phi, \cos\phi, \sin T$), hingga terbukti bentuk akhir:
   $z = \cos^{-1} (\cos \epsilon \sin \phi - \sin \epsilon \cos \phi \sin T)$. (Terbukti)."""
    }
]

for idx, item in enumerate(latihan_soal):
    st.markdown(item["soal"])
    with st.expander("Kunci Jawaban & Pembahasan"):
        st.markdown(item["jawaban"])
