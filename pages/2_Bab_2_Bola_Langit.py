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
    - [29. Contoh Penyelasaian](#29-contoh-example)
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
Dalam Bab I kita telah melihat bahwa posisi di permukaan bumi ditentukan sepenuhnya dengan merujuk pada dua lingkaran besar utama, yaitu meridian Greenwich dan ekuator. Prinsip penentuan posisi pada bola langit pada dasarnya serupa, dan terdapat beberapa metode tergantung pada lingkaran besar khusus yang dipilih sebagai lingkaran utama. Metode-metode ini sekarang akan diuraikan.

### 18. Ketinggian (*altitude*) dan azimut.
Misalkan $O$—pengamat di permukaan bumi (yang dianggap berbentuk bola)—menjadi pusat bola langit (Gbr. 10). Misalkan $Z$
"""
st.markdown(materi_bab_2_bagian_1, unsafe_allow_html=True)
st.image("Gambar_10.png", caption="Gambar 10: Sistem Horizon, Zenith, Nadir, dan Horizon Astronomis", use_container_width=True)

materi_bab_2_bagian_2 = r"""
*(zenith)* menjadi titik pada bola langit yang berada tepat di atas kepala—arahnya dapat didefinisikan dengan menggunakan unting-unting (*plumb-line*). Oleh karena itu, $OZ$ adalah kelanjutan dari garis lurus yang menghubungkan pusat bumi ke $O$. Bidang yang melalui $O$ yang tegak lurus terhadap $OZ$ adalah bidang horizon, yang memotong bola langit pada lingkaran besar $NAS$, yang disebut horizon astronomis atau sekadar horizon. Dengan demikian, pada Gbr. 10, horizon membagi bola langit menjadi dua belahan bola (*hemisphere*), di mana bagian atas adalah belahan bola yang terlihat (*visible hemisphere*), dan bagian bawah tersembunyi dari pengamat oleh bumi. Misalkan $X$ menjadi posisi sebuah bintang di bola langit pada saat tertentu. Setiap lingkaran besar yang ditarik melalui $Z$ disebut lingkaran vertikal (*vertical circle*); khususnya, lingkaran vertikal pada Gbr. 10 yang melalui $X$ adalah $ZXA$. Pada bidang $ZXA$, sudut $AOX$ atau busur lingkaran besar $AX$ disebut ketinggian (*altitude*), yang akan dilambangkan dengan $a$. Karena $OZ$ tegak lurus terhadap bidang horizon, lingkaran besar busur $ZA$ adalah $90^\circ$; oleh karena itu $ZX = 90^\circ - a$. $ZX$ disebut jarak zenit (*zenith distance*, disingkat z.d.) dari bintang $X$ dan akan dilambangkan dengan $z$. Dengan demikian:

$$ z = 90^\circ - a \dots\dots(1) $$

Misalkan $LXM$ menjadi lingkaran kecil melalui $X$ yang sejajar dengan horizon; lingkaran ini disebut paralel ketinggian (*parallel of altitude*) dan sedemikian rupa sehingga semua benda langit, yang posisinya pada suatu saat tertentu terletak pada lingkaran kecil ini, memiliki ketinggian yang sama dan juga, berdasarkan (1), memiliki jarak zenit yang sama dengan $X$. Dengan demikian, jika ketinggian atau jarak zenit sebuah bintang diberikan, paralel ketinggian tempat bintang itu harus berada dapat ditentukan secara pasti. Untuk mendefinisikan posisinya secara lengkap pada bola langit, lingkaran vertikal khusus tempat bintang itu berada juga harus ditentukan. Hal ini dilakukan sebagai berikut.

Misalkan $OP$ sejajar dengan sumbu tempat bumi berputar. Jika lintang pengamat adalah utara (seperti pada Gbr. 10), posisi $P$ disebut kutub langit utara (*north celestial pole*), atau sekadar kutub utara (*north pole*). Kita tidak secara langsung menyadari rotasi bumi, tetapi efeknya ditunjukkan dalam rotasi semu bola langit. Bintang-bintang dengan demikian tampak bergerak melintasi langit dan arahnya terus berubah. Di belahan bumi utara, bagaimanapun, ada satu bintang, yang dapat dilihat dengan mata telanjang, yang tampak sangat sedikit berubah. Bintang ini adalah Polaris, atau bintang kutub utara, yang arahnya di langit hampir persis sama dengan arah yang diberikan oleh $OP$. Jika kebetulan ada sebuah bintang yang terletak tepat di $P$ pada bola langit, ketinggian dan arahnya akan tidak berubah sepanjang malam. Kita mendefinisikan lingkaran vertikal melalui $P$, yaitu $ZPN$ (yang memotong horizon di $N$), sebagai lingkaran vertikal utama (*principal vertical circle*) dan titik $N$ sebagai titik utara horizon (*north point of the horizon*).

Titik $S$ pada horizon yang tepat berlawanan dengan $N$ adalah titik selatan (*south point*); titik barat ($W$) dan timur ($E$) points\* memiliki arah yang tegak lurus terhadap arah $N$ dan $S$ ($E$ tidak ditunjukkan pada Gbr. 10). Titik-titik $N, E, S$ dan $W$ disebut titik-titik kardinal (*cardinal points*).

Kita sekarang menentukan posisi sebuah bintang $X$ pada bola langit pada saat tertentu dengan merujuk pada horizon dan lingkaran vertikal utama $ZPN$. Jika bintang berada di bagian barat bola langit (seperti pada Gbr. 10), sudut bola $PZX$ (yang dibentuk oleh lingkaran vertikal utama dan lingkaran vertikal melalui $X$) atau busur lingkaran besar $NA$ disebut azimut (*azimuth*, $W$). Jika bintang berada di bagian timur bola langit, seperti pada Gbr. 11, sudut $PZX$
"""
st.markdown(materi_bab_2_bagian_2, unsafe_allow_html=True)
st.image("Gambar_11.png", caption="Gambar 11: Sistem Azimut (Timur/Barat) dan Titik Kardinal", use_container_width=True)

materi_bab_2_bagian_3 = r"""
atau busur $NB$ adalah azimut ($E$). Dengan demikian pada saat apa pun posisi benda langit pada bola langit dapat dideskripsikan sepenuhnya dengan merujuk pada horizon dan titik utara horizon dalam hal ketinggian dan azimut ($E$ atau $W$) atau, sebagai alternatif, dalam hal jarak zenit dan azimut. Ketika azimut adalah $90^\circ$ $E$ atau $90^\circ$ $W$, bintang tersebut dikatakan berada pada vertikal utama (*prime vertical*), yang dengan demikian merupakan lingkaran vertikal melalui titik timur $E$ atau titik barat $W$.

Karena pada Gbr. 10 dan 11 sudut $POZ$ (atau lingkaran besar busur $PZ$) ekivalen dengan sudut antara jari-jari bumi yang melewati posisi pengamat dan sumbu bumi, maka $P\hat{O}Z$ (atau $PZ$) sama dengan kolintang pengamat atau:

$$ PZ = 90^\circ - \phi \dots\dots(2) $$

di mana $\phi$ adalah lintang pengamat. Selain itu $PN = 90^\circ - PZ = \phi$; maka ketinggian kutub sama dengan lintang pengamat.

*(Catatan kaki: * Posisi $W$ dan $E$ relatif terhadap $N$ dan $S$ diperoleh dari pertimbangan bahwa, jika pengamat menghadap ke utara, titik barat berada di sebelah kiri dan titik timur berada di sebelah kanannya).*

### 19. Deklinasi dan sudut jam (*declination and hour angle*).
Seperti pada bagian sebelumnya, misalkan bola langit digambarkan untuk seorang pengamat $O$ pada lintang $\phi$, yang menunjukkan horizon, zenit $Z$ dan kutub utara $P$ (Gbr. 12). Lingkaran besar $RWT$ yang bidangnya tegak lurus terhadap $OP$ adalah ekuator langit (*celestial equator*) dan bidangnya, jelas, sejajar dengan ekuator bumi. Ekuator langit dan horizon berpotongan di dua titik $W$ dan $E$. Sekarang $Z$ adalah kutub dari lingkaran besar $NWS$ dan $P$ adalah kutub dari lingkaran besar $RWT$; oleh karena itu $W$ berjarak $90^\circ$ dari $Z$ dan $P$
"""
st.markdown(materi_bab_2_bagian_3, unsafe_allow_html=True)
st.image("Gambar_12.png", caption="Gambar 12: Sistem Ekuator Lokal (Deklinasi dan Sudut Jam)", use_container_width=True)

materi_bab_2_bagian_4 = r"""
dan oleh karena itu berjarak $90^\circ$ dari semua titik pada lingkaran besar melalui $Z$ dan $P$. Dengan kata lain, $W$ adalah kutub dari lingkaran besar $NPZSQ$; maka $NW = 90^\circ$ dan $WS = 90^\circ$. Demikian pula $EN = 90^\circ$ dan $ES = 90^\circ$. Maka $W$ dan $E$ adalah dua titik kardinal yang tersisa, $N$ dan $S$ telah didefinisikan secara eksplisit sebelumnya.

Seperti yang telah disebutkan, rotasi bumi menghasilkan rotasi semu bola langit dari timur ke barat mengelilingi $OP$. Mengikuti hal tersebut, karena bintang-bintang berada pada jarak yang sangat jauh dari bumi, sudut antara garis lurus yang menghubungkan pengamat pada $O$ ke bintang tertentu dan garis lurus $OP$ (sejajar dengan sumbu bumi) tetap tidak berubah. Jika kita mempertimbangkan sebuah bintang $X$, rotasi bumi membuatnya tampak menggambarkan lingkaran kecil $LXM$, sejajar dengan ekuator langit, dalam arah yang ditunjukkan oleh anak panah pada Gbr. 12. Misalkan $PXDQ$ adalah semi-lingkaran besar melalui $X$ dan kutub-kutub bola langit. Maka busur $DX$ disebut deklinasi bintang dan merupakan deklinasi utara jika bintang berada di antara ekuator langit dan kutub utara $P$ (seperti untuk bintang $X$). Deklinasi bintang adalah selatan (seperti untuk $Y$) ketika ia berada di antara ekuator langit dan kutub selatan $Q$. Deklinasi dengan demikian analog dengan lintang yang didefinisikan untuk titik-titik di permukaan bumi. Nyatakan deklinasi $X$ dengan $\delta$; maka $DX = \delta$ dan $PX = 90^\circ - \delta$. $PX$ disebut jarak kutub utara (*north polar distance*, N.P.D.) dari bintang. Adalah lebih mudah untuk memperlakukan deklinasi sebagai kuantitas aljabar, sehingga berbagai rumus yang akan diturunkan akan berlaku sama untuk deklinasi utara maupun selatan. Deklinasi utara membawa tanda positif ($+$) dan deklinasi selatan membawa tanda negatif ($-$). Dengan demikian rumus untuk jarak kutub utara, yaitu N.P.D. $= 90^\circ - \delta$, berlaku untuk semua bintang, apa pun deklinasinya.

Deklinasi sebuah bintang diketahui, kita dengan demikian dapat menentukan lingkaran kecil, yang disebut paralel deklinasi (*parallel of declination*), tempat bintang itu harus berada. Untuk memperbaiki posisinya pada bola langit pada saat tertentu, kita memerlukan lingkaran besar referensi lainnya. Ini adalah semi-lingkaran besar $PZRSQ$, yang disebut meridian pengamat (*observer's meridian*). Ketika bintang berada di $L$ pada meridian pengamat, ia dikatakan melakukan transit (*transit*) atau mencapai puncaknya (*culminate*), dan jelas dari Gbr. 12 bahwa ketinggiannya ($SL$) adalah yang terbesar dan jarak zenitnya $ZL$ adalah yang terkecil. Setelah itu, karena rotasi bumi, ia bergerak sepanjang lingkaran kecil $LFM$ memotong horizon di $F$ di mana ia dikatakan terbenam (*set*); ketinggiannya di $F$ tentu saja adalah $0^\circ$ dan jarak zenitnya $90^\circ$. Selama interval waktu yang bergantung pada deklinasinya, bintang berada di bawah horizon, mencapai depresi maksimum di bawah horizon di $M$; akhirnya ia mencapai horizon di $G$ di mana ia dikatakan terbit (*rise*). Ketinggiannya berangsur-angsur meningkat, ia kembali setelah interval yang ekuivalen dengan waktu di mana bumi melakukan rotasi penuh mengelilingi sumbunya, ke meridian pengamat di $L$. Pada saat apa pun posisi bintang pada paralel deklinasi ditentukan oleh sudut di $P$ antara meridian pengamat dan meridian ($PXQ$) melalui bintang pada saat itu; sudut ini adalah $RPX$ atau $ZPX$ atau busur $RD$ pada ekuator. Sudut ini, yang dilambangkan dengan $H$, disebut sudut jam (*hour angle*) dan diukur dari meridian pengamat ke arah barat dari $0^\circ$ (di $L$) hingga $360^\circ$ (ketika bintang kembali ke meridian pengamat) atau, seperti yang lebih biasa, dari $0^h$ hingga $24^h$. Kita dapat mengekspresikan ini dengan cara yang sedikit berbeda. Ketika bintang sedang transit, meridiannya bertepatan dengan meridian pengamat; setelah itu, meridian bintang bergerak dengan mantap ke arah barat dan, ketika ia telah membuat satu putaran penuh dari bola langit, ia telah menggambarkan sudut $360^\circ$ atau $24^h$ terhadap meridian pengamat. Dari Gbr. 12 terlihat bahwa jika bintang berada di sebelah barat meridian pengamat, yaitu jika:
"""
st.markdown(materi_bab_2_bagian_4, unsafe_allow_html=True)
st.image("Gambar_13.png", caption="Gambar 13: Diagram Sudut Jam Barat dan Timur Meridian", use_container_width=True)

materi_bab_2_bagian_5 = r"""
azimutnya adalah barat, sudut jamnya berada di antara $0^\circ$ dan $180^\circ$, yaitu antara $0^h$ dan $12^h$. Demikian pula, jika bintang berada di sebelah timur meridian (azimut timur)—seperti pada Gbr. 13—sudut jam berada di antara $12^h$ dan $24^h$. Kita dengan demikian memiliki aturan:
*Jika azimut bintang adalah barat, sudut jam berada di antara $0^h$ dan $12^h$ (dan sebaliknya); jika azimut bintang adalah timur, sudut jam berada di antara $12^h$ dan $24^h$.*

### 20. Diagram untuk belahan bumi selatan.
Diagram yang dijelaskan sejauh ini dalam bab ini merujuk pada bola langit untuk pengamat di lintang utara. Kita sekarang akan mendeskripsikan diagram yang bersesuaian untuk pengamat di belahan bumi selatan. Pada Gbr. 14, kita akan menempatkan zenit pengamat seperti pada diagram sebelumnya. Horizon langit kemudian seperti yang ditunjukkan. Di belahan bumi selatan, kutub langit selatan $Q$ berada di atas horizon. Kemudian, jika $\phi$ melambangkan lintang selatan pengamat, $QZ = 90^\circ - \phi$. Lingkaran vertikal utama sekarang adalah $ZQS$, memotong horizon di titik selatan $S$. Titik utara $N$ kemudian dapat ditempatkan dalam diagram. Ekuator langit dan horizon berpotongan di titik barat dan timur $W$ dan $E$ (yang terakhir tidak ditunjukkan pada Gbr. 14) menurut:
"""
st.markdown(materi_bab_2_bagian_5, unsafe_allow_html=True)
st.image("Gambar_14.png", caption="Gambar 14: Bola Langit untuk Pengamat di Belahan Bumi Selatan", use_container_width=True)

materi_bab_2_bagian_6 = r"""
aturan pada catatan kaki halaman 27. Pertimbangkan sebuah bintang $X$ dengan deklinasi selatan. Berkat rotasi bumi, ia akan mendeskripsikan lingkaran kecil $LXM$, paralel terhadap ekuator langit dan terletak di antara ekuator langit dan kutub selatan $Q$. Pada $L$, bintang akan memiliki ketinggian terbesar—ia kemudian berada pada meridian pengamat, yaitu semi-lingkaran $QZRNP$. Akibat rotasi bumi, bintang akan bergerak dari meridian pengamat ke arah barat, yaitu ke arah $LXM$, seperti yang ditunjukkan oleh anak panah pada diagram. Sudut $ZQX$ adalah sudut jam yang diukur, seperti sebelumnya, dari $0^h$ hingga $24^h$ ke arah barat dari meridian pengamat. $QZX$ adalah azimut; dalam hal ini adalah barat. Jika $\delta$ adalah deklinasi (negatif) bintang, maka $DX = -\delta$ dan $QX = 90^\circ + \delta$. Bagian lain dari segitiga bola $QZX$ adalah: $QZ = 90^\circ - \phi$, $ZX = z$ (jarak zenit), $QZX = A$ (azimut) dan $ZQX = H$ (sudut jam). Ketika azimut bintang adalah barat, sudut jam berada di antara $0^h$ dan $12^h$. Ketika azimut bintang adalah timur, diagram yang bersesuaian dapat digambarkan secara serupa; ini diserahkan sebagai latihan bagi siswa; maka akan ditemukan bahwa sudut jam berada di antara $12^h$ dan $24^h$. Aturan yang dinyatakan pada akhir bagian 19 terlihat berlaku untuk lintang selatan maupun utara.

### 21. Bintang sirkumpolar (*circumpolar stars*).
Pertimbangkan bola langit untuk pengamat di lintang utara $\phi$ (Gbr. 15). Paralel deklinasi digambarkan untuk dua bintang $X$ dan $Y$, yang keduanya selalu berada di atas horizon dan akibatnya tidak terbenam. Bintang-bintang seperti itu disebut sirkumpolar:
"""
st.markdown(materi_bab_2_bagian_6, unsafe_allow_html=True)
st.image("Gambar_15.png", caption="Gambar 15: Bintang Sirkumpolar yang Tidak Pernah Terbenam", use_container_width=True)

materi_bab_2_bagian_7 = r"""
bintang. Dari gambar tersebut terlihat dengan mudah bahwa syarat agar sebuah bintang tidak terbenam adalah: $PM$ harus kurang dari $PN$; yaitu, jarak kutub utara harus kurang dari lintang, atau dengan kata lain, deklinasi harus lebih besar dari kolintang.

Ketika bintang $X$ berada pada meridian pengamat di $L$, ia berada pada kulminasi atas (*upper culmination*) atau dalam transit (*in transit*); ketika bintang mencapai $M$, ia berada pada kulminasi bawah (*lower culmination*). Ekspresi "kulminasi di atas kutub" (*culmination above pole*) dan "kulminasi di bawah kutub" (*culmination below pole*) sering digunakan. Pada kulminasi atas, jarak zenit bintang adalah $ZL$ atau $(PL - PZ)$, yaitu, $\phi - \delta$. Pada kulminasi bawah, jarak zenit bintang adalah $ZM$ atau $(ZP + PM)$, yaitu, $180^\circ - (\phi + \delta)$. Ketika $\delta = \phi$, kulminasi atas terjadi di zenit. Ketika $\delta > \phi$, kulminasi atas terjadi di antara $P$ dan $Z$, seperti untuk bintang $Y$; maka azimut tidak melebihi $90^\circ$, seperti yang dapat disimpulkan dengan mudah dari diagram. Bintang sirkumpolar selatan dapat dianggap dengan cara yang sama.

### 22. Bola langit standar atau geosentrik (*The standard or geocentric celestial sphere*).
Dalam bagian-bagian sebelumnya, deklinasi bintang pada bola langit yang pusatnya adalah pengamat telah didefinisikan. Karena bintang-bintang berada pada jarak yang hampir tak terhingga besarnya dibandingkan dengan dimensi bumi, deklinasi atau jarak kutub bintang yang didefinisikan dengan cara ini tidak bergantung pada posisi pengamat di permukaan bumi, seperti yang dapat dilihat dengan mudah dari Gbr. 16. (Adalah lebih mudah untuk tujuan kita saat ini untuk berurusan dengan jarak kutub utara bintang daripada deklinasinya.) Pada Gbr. 16, $P_1CQ_1$ adalah sumbu rotasi bumi, $C$ menjadi pusat bumi; $O$ adalah pengamat dan $COZ$ adalah arah zenit di $O$; $OP$ sejajar dengan $CP_1$ dan arah bintang yang:
"""
st.markdown(materi_bab_2_bagian_7, unsafe_allow_html=True)
st.image("Gambar_16.png", caption="Gambar 16: Perbandingan Posisi Pengamat di Permukaan dan Pusat Bumi", use_container_width=True)

materi_bab_2_bagian_8 = r"""
bertransit di $O$ adalah $OX$. Berdasarkan definisi, jarak kutub utara bintang untuk pengamat di $O$ adalah $P\hat{O}X$. Jika $CY$ digambar sejajar dengan $OX$, maka $CY$ adalah arah bintang dengan merujuk ke $C$, pusat bumi. Dengan demikian $P_1\hat{C}Y = P\hat{O}X$; dengan kata lain jarak kutub utara bintang (dan akibatnya deklinasinya) adalah sama pada bola langit berpusat di $O$ (atau posisi lain di permukaan bumi) seperti pada bola langit berpusat di $C$. Tetapi ketika benda yang relatif dekat seperti bulan, atau matahari, atau planet diamati, definisi jarak kutub utara (dan karena itu deklinasi) yang diberikan sebelumnya bergantung pada posisi khusus pengamat di bumi. Dengan demikian jika $M$ adalah bulan (Gbr. 16) pada jarak $r$ dari pusat bumi, adalah jelas bahwa $P\hat{O}M = P_1\hat{C}M + O\hat{M}C$; juga $O\hat{M}C$ jelas bergantung pada posisi $O$, sedangkan $P_1CM$ sepenuhnya independen:
"""
st.markdown(materi_bab_2_bagian_8, unsafe_allow_html=True)
st.image("Gambar_17.png", caption="Gambar 17: Bola Langit Standar atau Geosentrik Berpusat di Pusat Bumi", use_container_width=True)

materi_bab_2_bagian_9 = r"""
dari $O$. $P_1\hat{C}M$ didefinisikan sebagai jarak kutub utara $M$ yang dengan demikian merupakan sudut antara sumbu bumi dan garis lurus yang menghubungkan pusat bumi ke benda langit. Definisi ini sepenuhnya bersifat umum dan berlaku untuk setiap benda langit. Oleh karena itu, pusat bola langit standar (atau bola langit geosentrik, sebagaimana dapat disebut) diambil berada di $C$, pusat bumi (Gbr. 17). $CZ$ adalah arah zenit pengamat, diameter $QCP$ berimpit dengan sumbu bumi, $NWSE$ adalah horizon langit (lingkaran besar yang bidangnya tegak lurus terhadap $CZ$), dan $RWTE$ adalah ekuator langit (bidang yang berimpit dengan bidang ekuator bumi). busur $PX$ adalah jarak kutub utara dari benda langit sesuai dengan definisi yang baru saja diberikan dan $DX$ adalah deklinasi $\delta$ (N.P.D. $= 90^\circ - \delta$). Meridian pengamat adalah $PZRSQ$, jarak zenit dari benda langit adalah $ZX$ (dilambangkan dengan $z$) dan azimut $A$ (sudut $P\hat{Z}X$) serta sudut jam $H$ (sudut $Z\hat{P}X$) adalah seperti yang telah dideskripsikan sebelumnya. Deklinasi benda-benda langit utama (bulan, matahari, planet-planet dan bintang-bintang paling terang) ditabulasikan di dalam *Astronomical Ephemeris* (publikasi Amerika dan Inggris) dan di dalam efemeris nasional lainnya.

Mulai dari sini, bola langit akan diasumsikan seperti pada Gbr. 17, yaitu, berpusat di $C$, pusat bumi.

### 23. Penyelesaian dari segitiga bola PZX.
Kita akan mempertimbangkan dua masalah umum yang terkait dengan segitiga $PZX$.
(i) Diberikan lintang pengamat $\phi$, deklinasi $\delta$ dan sudut jam $H$ dari benda langit, untuk menghitung jarak zenit dan azimutnya. Berdasarkan rumus **A** (rumus kosinus), karena dua sisi $PZ$ dan $PX$ serta sudut yang diapitnya $ZPX$ diberikan (Gbr. 17), kita memiliki:

$$ \cos ZX = \cos PZ \cos PX + \sin PZ \sin PX \cos ZPX $$

atau

$$ \cos z = \sin \phi \sin \delta + \cos \phi \cos \delta \cos H \dots\dots(3) $$

Dengan demikian $z$ dapat dihitung secara langsung dari (3) atau dengan cara rumus haversine (bagian 13), yang pada kasus ini dapat ditulis:

$$ \text{hav } z = \text{hav } (\phi - \delta) + \cos \phi \cos \delta \text{ hav } H \dots\dots(4) $$

Sekali lagi, dengan **A**:

$$ \cos PX = \cos PZ \cos ZX + \sin PZ \sin ZX \cos PZX $$

atau

$$ \sin \delta = \sin \phi \cos z + \cos \phi \sin z \cos A \dots\dots(5) $$

dari mana azimut $A$ dapat dihitung. Dalam bentuk haversine (5) dapat ditulis:

$$ \cos \phi \cos a \text{ hav } A = \text{hav } (90^\circ - \delta) - \text{hav } (\phi - a) \dots(6) $$

di mana $a$ adalah ketinggian (*altitude*).

(ii) Diberikan lintang pengamat $\phi$, jarak zenit bintang $z$ dan azimut $A$, untuk menghitung deklinasi bintang dan sudut jamnya. Kita diberikan $\phi, z$ dan $A$; maka, melalui (5), kita dapat menghitung deklinasi. Baik persamaan (3) maupun (4) tersedia untuk menghitung sudut jam $H$. Maka dari (3):

$$ \cos H = \cos z \sec \phi \sec \delta - \tan \phi \tan \delta \dots\dots(7) $$

Pertimbangkan sekarang segitiga bola $PZX$ pada Gbr. 13. Sudut $PZX$ adalah azimut (timur). Mengingat bahwa sudut jam diukur di kutub dari meridian pengamat ke arah barat, kita melihat bahwa $Z\hat{P}X = 24^h - H$. Penyelesaian dari segitiga tersebut berlanjut seperti sebelumnya.

### 24. Asensio rekta dan deklinasi.
Dalam metode sudut jam dan deklinasi untuk menentukan posisi sebuah bintang di bola langit hanya satu koordinat, yaitu deklinasi, yang tetap konstan saat bintang melintasi langit, sedangkan sudut jam meningkat secara seragam dari $0^h$ hingga $24^h$. Tetapi:
"""
st.markdown(materi_bab_2_bagian_9, unsafe_allow_html=True)
st.image("Gambar_18.png", caption="Gambar 18: Asensio Rekta dan Deklinasi pada Bola Langit", use_container_width=True)

materi_bab_2_bagian_10 = r"""
posisi bintang-bintang di bola langit dapat diibaratkan seperti posisi titik-titik tetap di permukaan bumi dan karenanya dapat dispesifikasikan dengan merujuk pada ekuator langit dan bintang tertentu mana pun di ekuator. Sebagai contoh, pada Gbr. 18, misalkan $\Upsilon$ adalah sebuah bintang ekuatorial dan $X$ adalah bintang lain mana pun; misalkan meridian melalui $X$ memotong ekuator langit di $D$. Karena bintang-bintang melintasi langit kita tahu secara khusus bahwa deklinasi $X$, yaitu, $DX$, tetap konstan dan bahwa konfigurasi relatif dari bintang-bintang juga tetap konstan. Ini berarti bahwa $\Upsilon D$ adalah konstan; dengan kata lain, bahwa sudut antara meridian-meridian dari $\Upsilon$ dan $D$ tetap konstan. Kita dapat menganggap $\Upsilon$ sebagai titik referensi pada ekuator langit; sehubungan dengan $\Upsilon$ dan ekuator langit, kita dapat dengan jelas menentukan posisi bintang $X$ dengan menggunakan busur lingkaran besar $\Upsilon D$ dan deklinasi $DX$. Titik referensi yang dipilih dalam praktik disebut ekuinoks musim semi (*vernal equinox*) atau titik pertama Aries, dan adalah mudah untuk menganggap posisi $\Upsilon$ sebagaimana dispesifikasikan oleh sebuah bintang tertentu di langit. Nanti kita akan mendefinisikan $\Upsilon$ lebih tepat lagi. Busur $\Upsilon D$ atau $\Upsilon\hat{P}X$ disebut asensio rekta (*right ascension*, R.A.) dari bintang $X$ (dilambangkan dengan $\alpha$) dan diukur ke arah timur dari $\Upsilon$ dari $0^h$ hingga $24^h$ (dalam arah panah dekat $\Upsilon$). Arah ini berlawanan dengan arah di mana sudut jam diukur. Dari Gbr. 18, kita melihat bahwa $R\Upsilon = RD + \Upsilon D$. Sekarang $RD$ (atau $R\hat{P}X$) adalah sudut jam $H$ dari $X$ dan $R\Upsilon$ adalah sudut jam dari $\Upsilon$. Sudut jam dari $\Upsilon$ disebut waktu sideris (*sidereal time*, S.T.). Kita memiliki, sebagaimana mestinya:

$$ \text{Sid. time} = \text{H.A. } X + \text{R.A. } X \dots\dots(8) $$

atau

$$ \text{S.T.} = H + \alpha \dots\dots(9) $$

Ketika $\Upsilon$ berada pada meridian pengamat, sudut jam dari $\Upsilon$ adalah $0^h$, yang berarti, waktu sideris adalah $0^h$. Ketika $\Upsilon$ selanjutnya berada pada meridian pengamat, sebuah interval sebesar $24^h$ waktu sideris telah berlalu. Interval ini adalah, tentu saja, sama dengan yang dibutuhkan untuk rotasi penuh bumi pada porosnya dan itu disebut hari sideris (*sidereal day*). Bumi yang berputar, pada kenyataannya, adalah pencatat waktu standar.

### 25. Orbit bumi.
Bumi adalah sebuah planet yang berevolusi mengelilingi matahari dalam lintasan elips atau orbit, matahari yang berada pada fokus $S$ dari elips tersebut (Gbr. 19). Ini adalah hukum gerak planet pertama Kepler. Waktu yang dibutuhkan bumi untuk membuat sebuah revolusi penuh pada orbitnya adalah satu tahun. Seiring bergeraknya bumi dalam orbitnya, arah bumi, seperti yang dilihat dari matahari, terus berubah; akan tetapi, kecepatan sudutnya tidak seragam. Karena pengamatan kita dilakukan dari bumi, maka relatif terhadap bumi matahari tampak mendeskripsikan sebuah orbit elips mengelilingi bumi. Pada Gbr. 20, $C$ adalah pusat bumi dan elips mewakili orbit semu matahari relatif terhadap bumi. Urutan posisi-posisi dari matahari, yaitu $a, e, f, b, g$ di dalam orbit ini, sesuai dengan urutan posisi-posisi $A, E, F, B, G$ dari bumi dalam orbitnya mengelilingi matahari (Gbr. 19). Di dalam perjalanan tahun, matahari dengan demikian:
"""
st.markdown(materi_bab_2_bagian_10, unsafe_allow_html=True)

st.image("Gambar_19.png", caption="Gambar 19: Orbit Bumi Mengelilingi Matahari", use_container_width=True)
st.image("Gambar_20.png", caption="Gambar 20: Orbit Semu Matahari Relatif Terhadap Bumi", use_container_width=True)

materi_bab_2_bagian_11 = r"""
tampak membuat sirkuit penuh dari langit berlatar belakangkan bintang-bintang. Bidang orbit ini disebut bidang ekliptika, dan lingkaran besar perpotongan bidang ini dengan bola langit, yang mana pusatnya adalah pusat bumi $C$, disebut ekliptika. Pada Gbr. 21, misalkan $C$ menjadi pusat bola langit di mana ekuator langit $\Upsilon TR$ dan kutub utara $P$ digambar. Kita dapat membayangkan bahwa bintang-bintang dapat dilihat dari pusat bumi, yaitu, dari $C$, dan karenanya mereka akan menempati posisi-posisi pasti pada bola langit di Gbr. 21. Merujuk pada bintang-bintang, bidang ekliptika akan memiliki posisi yang pasti dan, konsekuensinya, ekliptika akan menjadi sebuah lingkaran besar tertentu, yang ditemukan melalui pengamatan miring pada sudut sekitar $23\frac{1}{2}^\circ$ terhadap ekuator langit. Pada Gbr. 21, $\Upsilon \Upsilon M U$ mewakili ekliptika dan:
"""
st.markdown(materi_bab_2_bagian_11, unsafe_allow_html=True)
st.image("Gambar_21.jpg", caption="Gambar 21: Ekliptika, Kemiringan, dan Titik Ekuinoks", use_container_width=True)

materi_bab_2_bagian_12 = r"""
kemiringannya terhadap ekuator langit adalah $M\hat{\Upsilon}R$, yang dikenal sebagai kemiringan ekliptika (*obliquity of the ecliptic*). Relatif terhadap bumi, matahari tampak bergerak di bola langit di sepanjang ekliptika—dalam arah $\Upsilon \Upsilon M$—dan dua kali setahun, di $\Upsilon$ dan di $U$, posisinya pada bola langit berimpit dengan persimpangan ekliptika dengan ekuator langit. Di antara $\Upsilon$ dan $M$ dan di antara $M$ dan $U$ matahari berada pada sisi kutub utara dari ekuator; deklinasinya saat itu utara. Demikian pula di antara $U$ dan $\Upsilon$ dan di antara $\Upsilon$ dan $\Upsilon$ deklinasinya adalah selatan. Posisi $\Upsilon$, pada mana deklinasi matahari berubah dari selatan ke utara, adalah ekuinoks musim semi (*vernal equinox*). Dengan cara inilah titik referensi $\Upsilon$, darinya asensio rekta dari bintang-bintang diukur, diperoleh. Jadi jika $X$ adalah sebuah bintang, asensio rektanya adalah $\Upsilon D$ atau $\alpha$ yang diukur sepanjang ekuator dari $\Upsilon$ ke arah timur, dan deklinasinya $\delta$ adalah $DX$. Dari diagram terlihat bahwa asensio rekta dan deklinasi matahari keduanya berubah secara terus-menerus. Ketika matahari berada di $\Upsilon$, asensio rekta dan deklinasinya keduanya nol (ini terjadi sekitar 21 Maret—ekuinoks musim semi); di $M$ asensio rektanya adalah $6^h$ dan deklinasi sekitar $23\frac{1}{2}^\circ$ U (ini terjadi sekitar 21 Juni—solstis musim panas); di $U$ asensio rektanya adalah $12^h$ dan deklinasi $0^\circ$ (ini terjadi sekitar 23 September—ekuinoks musim gugur) dan di bagian titik terendah asensio rektanya adalah $18^h$ dan deklinasi sekitar $23\frac{1}{2}^\circ$ S (ini terjadi sekitar 21 Desember—solstis musim dingin).

### 26. Lintang dan bujur langit.
Posisi sebuah benda langit dapat dirujuk ke ekliptika sebagai lingkaran besar fundamental dan ekuinoks musim semi $\Upsilon$ sebagai titik rujukan utama. Pada Gbr. 21 $K$ adalah kutub utara dari ekliptika dan $KXA$ adalah lingkaran besar yang melewati $X$ dan bertemu ekliptika di $A$. Busur $\Upsilon A$, diukur dari $\Upsilon$ ke $A$ sepanjang ekliptika dalam arah pergerakan tahunan matahari, mis. ke timur, disebut bujur (*longitude*) dari benda langit $X$ dan diukur dari $0^\circ$ hingga $360^\circ$ memutari ekliptika. Busur $AX$ adalah lintang (*latitude*) dan lintang utara dianggap positif dan selatan negatif. Jika kita mengetahui asensio rekta dan deklinasi dari bintang kita dapat memperoleh lintangnya ($\beta$) dan bujurnya ($\lambda$) dari segitiga $KPX$; dan sebaliknya. Sekarang $\Upsilon$ adalah kutub dari lingkaran besar $KPMR$; karenanya $K\hat{P}\Upsilon = 90^\circ$, dan karena $\Upsilon D = \Upsilon\hat{P}X = \alpha$, maka $K\hat{P}X = 90^\circ + \alpha$. Juga $P\hat{K}\Upsilon = 90^\circ$, dan karena $\Upsilon A = \Upsilon\hat{K}X = \lambda$, maka $P\hat{K}X = 90^\circ - \lambda$. Juga $PX = 90^\circ - \delta$ dan $KX = 90^\circ - \beta$. Misalkan $\epsilon$ menyatakan kemiringan ekliptika; ia adalah sudut di antara jari-jari $CM$ dan $CR$; jadi busur $RM = \epsilon$. Tetapi $KM = 90^\circ$ dan $PR = 90^\circ$; karenanya $KP = \epsilon$. Menerapkan rumus-rumus **A**, **B** dan **C**, kita miliki:

$$ \cos KX = \cos PX \cos KP + \sin PX \sin KP \cos KPX $$

$$ \sin KX \sin PKX = \sin PX \sin KPX $$

$$ \sin KX \cos PKX = \cos PX \sin KP - \sin PX \cos KP \cos KPX $$

atau:

$$ \sin \beta = \sin \delta \cos \epsilon - \cos \delta \sin \epsilon \sin \alpha \dots\dots(10) $$

$$ \cos \beta \cos \lambda = \cos \delta \cos \alpha \dots\dots(11) $$

$$ \cos \beta \sin \lambda = \sin \delta \sin \epsilon + \cos \delta \cos \epsilon \sin \alpha \dots\dots(12) $$

Oleh proses yang serupa, asensio rekta $\alpha$ dan deklinasi $\delta$ dapat diekspresikan dalam bentuk $\beta, \lambda$ dan $\epsilon$. Rumus-rumusnya adalah:

$$ \sin \delta = \sin \beta \cos \epsilon + \cos \beta \sin \epsilon \sin \lambda $$

$$ \cos \delta \cos \alpha = \cos \beta \cos \lambda $$

$$ \cos \delta \sin \alpha = - \sin \beta \sin \epsilon + \cos \beta \cos \epsilon \sin \lambda $$

### 27. Waktu Sideris.
Misalkan bumi dan bola langit (berpusat di $C$) digambarkan seperti pada Gbr. 22; misalkan $g$ menandakan posisi Greenwich di permukaan bumi dan $l$ yaitu posisi sembarang tempat lain. Sudut di antara meridian-meridian $plq$ dan $pgq$ adalah, tentu saja, bujur (terestrial) dari $l$; pada kasus ini $l$ adalah barat dari Greenwich. Hasilkan $Cg, Cl$ untuk menemui bola langit di $G$ dan $L$. Maka $G$ dan $L$ adalah zenit dari Greenwich dan $l$ secara berturut-turut. Jika $X$ adalah posisi sebuah benda langit di bola langit pada momen yang diberikan, $G\hat{P}X$ adalah sudut jam dari $X$ untuk seorang pengamat di meridian Greenwich dan $L\hat{P}X$ adalah sudut jam untuk seorang pengamat di meridian $l$. Tetapi $G\hat{P}X = L\hat{P}X + G\hat{P}L$ dan $G\hat{P}L = g\hat{p}l$; karenanya:
"""
st.markdown(materi_bab_2_bagian_12, unsafe_allow_html=True)
st.image("Gambar_22.jpg", caption="Gambar 22: Hubungan Waktu Sideris Lokal dan Bujur Terestrial", use_container_width=True)

materi_bab_2_bagian_13 = r"""
$$ \text{H.A. dari } X \text{ di Greenwich} = \text{H.A. dari } X \text{ di } l + \text{bujur (B) dari } l \dots\dots(13) $$

Di dalam rumus ini kita andaikan bahwa bujur dari $l$ diekspresikan dalam ukuran-waktu ($15^\circ = 1^h; 15' = 1^m; 15'' = 1^s$). Rumus (13) adalah yang bersifat umum dan itu jelas berlaku untuk ekuinoks musim semi $\Upsilon$. Kita lalu memperoleh—karena waktu sideris adalah sudut jam dari $\Upsilon$—:

$$ \text{Sid. time di Greenwich} = \text{Sid. time di } l \pm \text{bujur dari } l \dots(14) $$

tanda $+$ diambil ketika $l$ berada di barat dari Greenwich dan tanda $-$ ketika $l$ berada di timur dari Greenwich. Waktu sideris di $l$ disebut *local sidereal time* (L.S.T.).

### 28. Waktu matahari rata-rata.
Hari sideris adalah sebuah satuan waktu observatorium dan terbukti secara jelas tidak sesuai pada pengaturan urusan sehari-hari yang mana sebagian besar dikuasai menurut posisi dari matahari di langit. Ketika matahari berada di meridian dari sebuah tempat, itu adalah tengah hari semu (*apparent noon*) di sana; ketika matahari berada selanjutnya di meridian, sebuah hari matahari semu (*apparent solar day*) dikatakan telah berlalu. Interval ini dapat diukur, sebagai contoh, dengan sarana dari sebuah jam yang menjaga waktu sideris yang akurat dan itu ditemukan bahwa suatu hari matahari semu tidaklah konstan. Kita telah melihat bahwa, relatif terhadap bumi, matahari tampak untuk mendeskripsikan sebuah orbit elips di sekeliling bumi dan kecepatan pada mana arahnya di orbit berubah bukanlah konstan. Itu mengikuti bahwa matahari tampak untuk mendeskripsikan ekliptika pada suatu laju yang tidak seragam; dengan kata lain, matahari tampak untuk bergerak dengan agak tidak beraturan berlawanan dengan latar belakang bintang-bintang. Dikarenakan hal ini dan juga karena fakta bahwa ia bergerak di dalam ekliptika dan tidak di sepanjang ekuator langit (lingkaran besar fundamental dengan mana pengukuran dari sudut jam atau waktu dihubungkan) asensio rektanya tidak meningkat secara seragam. Rata-rata hari matahari semu di sepanjang tahun disebut sebuah hari matahari rata-rata (*mean solar day*) dan adalah nyaman untuk mendefinisikan hari matahari rata-rata sebagai interval di antara dua persinggahan berturut-turut melintasi meridian pengamat dari sebuah benda fiktif yang disebut matahari rata-rata (*mean sun*). Matahari rata-rata diasumsikan untuk bergerak di ekuator langit dengan laju yang seragam mengelilingi bumi. Laju ini adalah sedemikian sehingga matahari rata-rata menyelesaikan sebuah revolusi di dalam waktu yang sama seperti halnya itu yang disyaratkan oleh matahari untuk sirkuit lengkap ekliptika. Menurut definisi ini, asensio rekta dari matahari rata-rata (dilambangkan oleh R.A.M.S.) meningkat pada laju yang seragam.

Sekarang jika kita memandang matahari rata-rata sebagai sebuah benda langit biasa, maka pada momen yang diberikan mana pun, kita dapat menganggap bahwa ia memiliki sudut jam tertentu (H.A.M.S.) pada suatu tempat yang diberikan di permukaan bumi. Pada momen ini kita akan mengasumsikan bahwa asensio rektanya diketahui; karenanya dari (8) atau (9):

$$ \text{Sid. time} = \text{H.A.M.S.} + \text{R.A.M.S.} \dots\dots(15) $$

Waktu yang ditunjukkan oleh jam waktu rata-rata, misal, di Greenwich pada momen mana pun hanyalah terhubung ke nilai dari H.A.M.S. di sana, dan jika R.A.M.S. diketahui, (15) membentuk basis dari perbandingan antara waktu sideris dan jam waktu rata-rata. Matahari rata-rata berhubungan dengan matahari sejati menurut prinsip-prinsip tertentu yang mana akan didiskusikan dalam bab yang selanjutnya. Sementara itu akan cukup untuk menyatakan bahwa perbedaan pada momen mana pun di antara asensio rekta dari matahari rata-rata dan dari matahari sejati dapat dihitung; perbedaan ini disebut perataan waktu (*equation of time*)* (dilambangkan dengan $E$). Kita dengan demikian memiliki:

$$ E = \text{R.A.M.S.} - \text{R.A. } \odot \dots\dots(16) $$

*(Catatan kaki: * Dalam buku-buku teks yang lebih tua perataan waktu didefinisikan oleh $E = \text{R.A. } \odot - \text{R.A.M.S.}$, tetapi konvensi (16) yang secara umum diadopsi).*

di mana R.A. $\odot$ menunjukkan asensio rekta dari matahari sejati. $E$ dapat menjadi positif atau negatif dan bervariasi dengan cara yang rumit. Komputasi secara detail dari $E$ didiskusikan di dalam bagian 91. Pada Gbr. 23, mari kita misalkan bahwa pada keadaan yang diberikan asensio rekta dan deklinasi dari matahari ($\odot$) diketahui. Misalkan $\Upsilon$ menjadi ekuinoks musim semi pada saat ini sehingga bahwa $R\hat{P}\Upsilon$ atau $R\Upsilon$ adalah sudut jam dari $\Upsilon$, yakni, waktu sideris lokal. Jika ini diketahui, posisi dari $\Upsilon$ pada bola langit dapat secara pasti ditentukan. Posisi matahari lalu dapat diindikasikan pada bola langit. $\Upsilon K = \text{R.A. } \odot$ dan $K\odot$ adalah deklinasi matahari dan kedua hal ini:
"""
st.markdown(materi_bab_2_bagian_13, unsafe_allow_html=True)
st.image("Gambar_23.jpg", caption="Gambar 23: Perataan Waktu dan Sudut Jam Matahari Rata-rata", use_container_width=True)

materi_bab_2_bagian_14 = r"""
diasumsikan diketahui. Misalkan nilai dari $E$ adalah positif; maka oleh (16), R.A.M.S. adalah lebih besar dari R.A. $\odot$, dan jika $E$ diketahui posisi matahari rata-rata $M$ pada saat ini dapat diindikasikan di dalam diagram. $R\hat{P}M$ atau $RM$ adalah sudut jam dari $M$ (H.A.M.S.). Jelas dari Gbr. 23 bahwa, karena $RK = RM + MK$, maka:

$$ \text{H.A. } \odot = \text{H.A.M.S.} + E \dots\dots(17) $$

yang mana merupakan relasi penting yang menghubungkan H.A.M.S. dan H.A. $\odot$, memampukan kita untuk menghitung sudut jam matahari (H.A. $\odot$) ketika kuantitas-kuantitas lainnya diketahui. Ketika matahari rata-rata berada pada meridian pengamat, maka itu adalah *local mean noon* di sana. Ketika matahari rata-rata berada pada meridian Greenwich, itu adalah *Greenwich mean noon*. Sudut jam dari matahari rata-rata di Greenwich akan dinotasikan di buku ini oleh G.M.A.T. (*Greenwich mean astronomical time*). Ketika

matahari rata-rata ada pada $T$—H.A.M.S. berada saat itu bernilai $12^h$—ia dikatakan menjadi tengah malam rata-rata (*mean midnight*). Ketika G.M.A.T. $= 12^h$, itu adalah tengah malam rata-rata pada Greenwich dan ini adalah momen saat sebuah hari sipil baru di Greenwich dimulai. Waktu rata-rata yang diperhitungkan dari tengah malam pada Greenwich disebut *Greenwich Mean Time* (G.M.T.)*, sekarang ditunjuk sebagai *Universal Time* (U.T.). Adalah jelas bahwa:

$$ \text{U.T.} \equiv \text{G.M.T.} = \text{G.M.A.T.} + 12^h \dots\dots(18) $$

Secara serupa, untuk tempat apa pun yang mempertahankan waktu rata-rata yang sesuai dengan meridiannya, kita akan memiliki:

$$ \text{Local M.T.} = \text{Local M.A.T.} + 12^h \dots\dots(19) $$

$$ = \text{H.A.M.S.} \pm 12^h \dots\dots(20) $$

Rumus (14) memberikan hubungan di antara waktu sideris pada Greenwich dan waktu sideris di tempat $l$, dan ini jelas dari Gbr. 22 dan dari (18) dan (19) bahwa kita akan mempunyai suatu relasi yang mirip antara waktu rata-rata pada Greenwich dan waktu rata-rata pada tempat tersebut; hal itu adalah:

$$ \text{U.T.} \equiv \text{G.M.T.} = \text{Local M.T.} \pm \text{bujur dari } l \dots\dots(21) $$

tanda $+$ yang diambil ketika bujur dari $l$ berada di barat dan tanda $-$ ketika bujur tersebut berada di timur.

Kebingungan niscaya tidak akan terelakkan jika setiap tempat menjaga *local mean time* yang tepat dengan meridiannya, dan oleh karenanya di dalam negara-negara yang kecil suatu waktu rata-rata standar dipilih, bertepatan pada suatu meridian bujur yang khusus (meridian standar), yang mana ada dalam penggunaan secara seragam di seantero negeri. Di Inggris Raya, waktu rata-rata standar tersebut adalah G.M.T. Di negara-negara yang ekstensif seperti Rusia dan Amerika Serikat, dua atau lebih waktu-waktu standar ada dalam penggunaan di dalam zona-zona bujur; di dalam setiap zona, suatu waktu standar yang sesuai untuk meridian pasti di dalam zona tersebut yang dipertahankan. Waktu standar, berdasar sebuah meridian tertentu, kita akan melambangkannya dengan waktu zona (*zone time*, Z.T.). Sistem ini, di dalam efeknya, dipertahankan oleh kapal-kapal di perairan yang mana secara general kurang terganggu oleh komplikasi-komplikasi geografis. Kita memiliki, seperti dalam (21):

$$ \text{U.T.} \equiv \text{G.M.T.} = \text{Z.T.} \pm \text{bujur dari meridian standar} \dots(22) $$

*(Catatan kaki: * Sebelum 1925, G.M.T. digunakan di dalam almanak untuk menandakan *Greenwich mean astronomical time* (G.M.A.T.). Mulai 1925, waktu yang digunakan adalah G.M.T. ($\equiv$ G.C.T.) lalu digantikan, seperti halnya disinggung di atas, oleh U.T. Baru-baru ini, untuk berbagai alasan yang dicantumkan dalam Apendiks E (hlm. 424), U.T. telah diganti di dalam almanak oleh Ephemeris Time (E.T.). Perbedaan di antara U.T. dan E.T. sangatlah sedikit hingga kita akan menggunakan yang terdahulu secara umumnya, terkecuali kalau dinyatakan sebaliknya).*

### 29. Contoh (*Example*).
Kita akan menggunakan sebagai ilustrasi masalah berikut dari tipe yang umum dan penting. Di sebuah tempat pada bujur $163^\circ 14' \text{ T}$, diharuskan untuk menghitung sudut jam matahari ($\text{H.A. } \odot$) yang sesuai dengan pengamatan yang dilakukan pada waktu zona $8^h 46^m 22^s$ pada 10 Maret 1975; waktu zona tersebut adalah waktu meridian standar dari $165^\circ \text{ T} (11^h \text{ T})$.

Langkah pertama adalah menurunkan U.T. pada saat pengamatan dilakukan. Kita peroleh:

Waktu zona: $8^h 46^m 22^s$ 10 Maret
Bujur meridian standar: $- 11^h$
U.T. = $21^h 46^m 22^s$ 9 Maret

Kita mengurangkan $11^h$ dari waktu zona sesuai dengan rumus (22). (Jelasnya, kita dapat menulis waktu zona sebagai $32^h 46^m 22^s$ 9 Maret.)

Kita selanjutnya mencari waktu rata-rata lokal (*local mean time*—yaitu, waktu rata-rata yang bersesuaian dengan bujur tempat tersebut) dengan menggunakan (21).

U.T.: $21^h 46^m 22^s$ 9 Maret
Bujur tempat (T): $+ 10^h 52^m 56^s$
Local M.T. = $32^h 39^m 18^s$ 9 Maret
Local M.T. = $8^h 39^m 18^s$ 10 Maret

Rumus (20) memampukan kita untuk menuliskan H.A.M.S. (sudut jam dari matahari rata-rata di tempat tersebut); yaitu:

$$ \text{H.A.M.S.} = 20^h 39^m 18^s. $$

Langkah berikutnya adalah menerapkan perataan waktu terhadap H.A.M.S. Dari *Astronomical Ephemeris* ditemukan, melalui interpolasi, bahwa pada U.T. $21^h 46^m 22^s$, 9 Maret, $E = -10^m 36^s$.

Maka, berdasarkan (17),

$$ \text{H.A. } \odot = 20^h 39^m 18^s - 10^m 36^s, $$

atau

$$ \text{H.A. } \odot = 20^h 28^m 42^s. $$

### 30. Sudut jam dari sebuah benda langit.
Untuk menghitung sudut jam dari benda langit apa pun ($X$) selain matahari, kita melangkah sebagai berikut. Oleh (8) dan (14) kita peroleh:

$$ \text{L.S.T.} = \text{H.A. } X + \text{R.A. } X $$

dan

$$ \text{G.S.T.} = \text{L.S.T.} \pm l, $$

sehingga

$$ \text{H.A. } X + \text{R.A. } X = \text{G.S.T.} \pm l \dots\dots(23). $$

Di dalam *Astronomical Ephemeris*, waktu sideris Greenwich ditabulasikan pada $0^h$ U.T. untuk setiap hari sepanjang tahun. Karena, berdasarkan (15),

$$ \text{Sid. time} = \text{H.A.M.S.} + \text{R.A.M.S.}, $$

kita peroleh:

$$ \text{R.A.M.S. pada U.T. } 0^h \text{ untuk hari apa pun} = \text{waktu sideris Greenwich yang ditabulasikan pada U.T. } 0^h \text{ untuk hari tersebut } - 12^h. $$

*R.A.M.S. meningkat secara seragam pada laju $3^m 56^s.56$ per hari matahari rata-rata atau pada laju $9^s.856$ per jam matahari rata-rata*; melalui ini kita dapat menghitung R.A.M.S. untuk U.T. mana pun yang diberikan. Tabel-tabel diberikan di dalam almanak untuk memfasilitasi perhitungan ini.

Penggunaan rumus (23) diilustrasikan dengan paling baik menggunakan sebuah contoh. Diharuskan untuk menghitung sudut jam dari Betelgeuse ($\alpha$ Orionis) pada waktu zona $18^h 35^m 46^s$ pada 26 Januari 1975, di sebuah tempat yang bujurnya adalah $64^\circ 28' 49'' \text{ B}$. (Zona $+ 4^h$: ini berarti bahwa meridian standar dari zona tersebut adalah $4^h \text{ B}$ atau $60^\circ \text{ B}$.)

Waktu zona: $18^h 35^m 46^s$ Januari 26
Zona: $+ 4^h$
U.T.: $22^h 35^m 46^s$ Januari 26
Koreksi waktu sideris: $3^m 43^s$ ($3^m 56^s.56$ per hari)
Total: $22^h 39^m 29^s$
G.S.T. pada $0^h$ U.T.: $8^h 18^m 39^s$ (Dari A.E.)
G.S.T.: $30^h 58^m 08^s$
Bujur tempat (B): $- 4^h 17^m 55^s$
L.S.T.: $26^h 40^m 13^s$
Kurangi R.A. dari Betelgeuse: $5^h 53^m 49^s$ (Dari A.E.)
**H.A. dari Betelgeuse: $20^h 46^m 24^s$**

### 31. Terbit dan terbenam.
Pertimbangkan Gbr. 24. Benda langit $X$ dikatakan terbenam pada $F$, titik di mana ia mencapai horizon. Maka jarak zenit adalah $90^\circ$, yakni, $ZF = 90^\circ$. Misalkan $H$ menjadi sudut jam dari $X$ pada saat terbenam, sehingga $Z\hat{P}F = H$. Juga $PF = 90^\circ - \delta$. Misalkan $A$ menjadi azimut saat terbenam ($P\hat{Z}F$) dan $\phi$ lintangnya.

Dari rumus A,

$$ \cos ZF = \cos PZ \cos PF + \sin PZ \sin PF \cos ZPF, $$

atau

$$ \cos 90^\circ = \sin \phi \sin \delta + \cos \phi \cos \delta \cos H, $$

sehingga, karena $\cos 90^\circ = 0$,

$$ \cos H = - \tan \phi \tan \delta \dots\dots(24), $$

dari mana sudut jam pada saat terbenam dapat dihitung.
Juga dari A,

$$ \cos PF = \cos PZ \cos ZF + \sin PZ \sin ZF \cos PZF, $$

atau

$$ \sin \delta = 0 + \cos \phi \cos A, $$

sehingga

$$ \cos A = \sin \delta \sec \phi \dots\dots(25), $$

dari mana azimut pada saat terbenam dapat dihitung.
"""
st.markdown(materi_bab_2_bagian_14, unsafe_allow_html=True)
st.image("Gambar_24.jpg", caption="Gambar 24: Posisi Benda Langit Saat Terbenam di Horizon", use_container_width=True)

materi_bab_2_bagian_15 = r"""
Di lintang utara, terlihat baik dari persamaan-persamaan (24) dan (25), atau dari Gbr. 24, bahwa jika deklinasinya adalah utara maka sudut jam pada saat terbenam adalah di antara $6^h$ dan $12^h$ dan bahwa azimutnya adalah kurang dari $90^\circ$ (yakni, benda tersebut terbenam di antara barat dan utara); dan bahwa jika deklinasinya adalah selatan, sudut jam pada saat terbenam adalah di antara $0^h$ dan $6^h$ dan benda tersebut terbenam di antara selatan dan barat. Masalah ini karena menyangkut terbitnya suatu benda langit dapat diperlakukan dengan cara yang serupa. Ketika lintang pengamat adalah selatan, prosedurnya serupa.

Jika benda langit yang bersangkutan adalah sebuah bintang, sudut jam pada saat terbenam memberikan interval antara transit meridian dan terbenam yang diekspresikan dalam waktu sideris. Jika benda langit tersebut adalah matahari, interval antara transit meridian dan terbenam diekspresikan dalam waktu matahari semu. Tetapi selama interval ini posisi relatif dari matahari dan matahari rata-rata hanya akan berubah sedikit (dengan kata lain, perubahan dalam perataan waktu biasanya dapat diabaikan kecuali jika akurasi ekstrem diinginkan), dan dengan demikian interval tersebut dapat dideskripsikan, untuk semua tujuan praktis, dalam bentuk waktu rata-rata. Dengan demikian, jika dari rumus (24) sudut jam $H$ pada saat terbenam ditemukan menjadi $7^h 30^m$, maka interval antara transit meridian matahari dan terbenam adalah $7^h 30^m$ waktu matahari rata-rata. Dengan mengabaikan pertimbangan akan perubahan apa pun dalam deklinasi matahari, kita menyimpulkan bahwa ini juga merupakan interval antara matahari terbit dan persinggahan meridian. Dengan demikian matahari berada di atas horizon selama $15^h$ dan di bawah horizon selama $9^h$. Sebenarnya, tentu saja, deklinasi matahari umumnya sedikit berbeda pada saat matahari terbit dari pada saat matahari terbenam dikarenakan gerakannya di sepanjang ekliptika dan efeknya dapat dihitung.

Rumus (24) menunjukkan bahwa jika $\phi > 90^\circ - \delta$, $\cos H$, secara numerik, lebih besar dari kesatuan, sehingga persamaan tersebut gagal untuk memberikan sebuah nilai untuk $H$. Dalam contoh ini, matahari tidak terbenam di lintang dan pada hari-hari sedemikian sehingga $\phi > 90^\circ - \delta$, seperti yang juga dapat diverifikasi dari sebuah diagram. Pada hari pertengahan musim panas (*midsummer day*), deklinasi utara matahari adalah yang terbesar; saat itu sekitar $23\frac{1}{2}^\circ \text{ U}$, sehingga di lintang utara dari $66\frac{1}{2}^\circ \text{ U}$, matahari berada di atas horizon pada hari itu tanpa terbenam.* Di kutub utara, karena $\phi > 90^\circ - \delta$, asalkan $\delta$ adalah utara, matahari berada di atas horizon secara terus-menerus antara 21 Maret dan 21 September; selama sisa enam bulan, matahari berada di bawah horizon. Paralel $66\frac{1}{2}^\circ \text{ U}$ disebut *Lingkaran Arktik* (*Arctic Circle*) dan paralel yang bersesuaian di belahan bumi selatan ($66\frac{1}{2}^\circ \text{ S}$) adalah *Lingkaran Antarktika* (*Antarctic Circle*).

*(Catatan kaki: * Karenanya ungkapan tersebut, matahari tengah malam (the midnight sun).)*

### 32. Laju perubahan jarak zenit dan azimut.
Misalkan $X$ pada Gbr. 25 menjadi posisi suatu benda langit pada bola langit pada momen tertentu dan $Y$ posisinya sedikit lebih lambat. Asumsikan deklinasi menjadi konstan sehingga $X$ dan $Y$ terletak pada lingkaran kecil $LM$ (paralel deklinasi), darinya $P$ adalah kutubnya. Gambarlah busur-busur lingkaran besar $PX, PY, ZX, ZY$. Misalkan $UX$ menjadi busur dari lingkaran kecil darinya $Z$ adalah kutubnya; maka $ZX = ZU$. Misalkan $Z\hat{P}X = H$ dan $Z\hat{P}Y = H + \Delta H$, sehingga $X\hat{P}Y = \Delta H$. Misalkan $P\hat{Z}X = A$ dan $X\hat{Z}Y = \Delta A$; $ZX = z$ dan $ZY = z + \Delta z$. Maka $UY = \Delta z$. Karena $XY$ diandaikan sebagai busur yang kecil, kita dapat mengasumsikan bahwa $UXY$ adalah segitiga bidang, bersudut siku-siku di $U$.
"""
st.markdown(materi_bab_2_bagian_15, unsafe_allow_html=True)
st.image("Gambar_25.jpg", caption="Gambar 25: Perubahan Kecil Posisi Benda Langit dalam Jarak Zenit dan Azimut", use_container_width=True)

materi_bab_2_bagian_16 = r"""
Saat benda langit bergerak, dikarenakan gerak harian, dari $X$ ke $Y$ jarak zenitnya meningkat sebesar $\Delta z$, sudut jamnya sebesar $\Delta H$ dan azimutnya menurun sebesar $\Delta A$.

Berdasarkan rumus (1) dari bagian 3 (hlm. 4),

$$ XY = X\hat{P}Y \sin PX = \Delta H \cos \delta, $$

dan

$$ UX = X\hat{Z}Y \sin ZX = \Delta A \sin z. $$

Misalkan $\eta$ menandakan sudut $PXZ$; $\eta$ disebut sudut paralaktik (*parallactic angle*). Kemudian, karena $Y$ sangat dekat dengan $X$, kita dapat menganggap $P\hat{Y}Z$ sebagai $\eta$. Maka

$$ UY = XY \cos U\hat{Y}X, $$

dan

$$ UX = XY \sin U\hat{Y}X. $$

Sekarang $P\hat{Y}Z = \eta$ dan $P\hat{Y}X = 90^\circ$; karenanya

$$ UY = \Delta z = \Delta H \cos \delta \sin \eta, $$

dan

$$ UX = \Delta A \sin z = \Delta H \cos \delta \cos \eta. $$

Sekarang di dalam segitiga bola $PXZ$, berdasarkan rumus B,

$$ \cos \delta \sin \eta = \sin A \cos \phi, $$

dan, berdasarkan rumus C,

$$ \cos \delta \cos \eta = \sin \phi \sin z - \cos \phi \cos z \cos A. $$

Karenanya

$$ \Delta z = \Delta H \sin A \cos \phi \dots\dots(26), $$

dan

$$ \Delta A = \Delta H (\sin \phi - \cos \phi \cot z \cos A) \dots\dots(27). $$

Di dalam rumus-rumus ini, $\Delta H, \Delta z$ dan $\Delta A$ diandaikan diekspresikan dalam ukuran sirkular. Misalkan $\Delta H^s$ melambangkan jumlah sekon waktu dalam $\Delta H$ radian; misalkan $\Delta z'', \Delta A''$ melambangkan jumlah detik busur dalam radian $\Delta z, \Delta A$ secara berturut-turut. Maka, berdasarkan prinsip-prinsip bagian 15, hlm. 22,

$$ \Delta z = \Delta z'' \sin 1''; \quad \Delta A = \Delta A'' \sin 1''; \quad \Delta H = \Delta H^s \sin 1^s, $$

dan, karena $\sin 1^s = 15 \sin 1''$, kita memiliki

$$ \Delta z'' = 15 \Delta H^s \sin A \cos \phi, $$

$$ \Delta A'' = 15 \Delta H^s (\sin \phi - \cos \phi \cot z \cos A). $$

Jika $\Delta H^s = 1$ sekon, persamaan-persamaan ini masing-masing menyatakan bahwa jarak zenit meningkat pada laju $15 \sin A \cos \phi$ detik busur per sekon waktu dan bahwa azimut menurun pada laju $15 [\sin \phi - \cos \phi \cot z \cos A]$ detik busur per sekon waktu.

Jika benda langit tersebut adalah sebuah bintang, laju-laju perubahan jarak zenit dan azimut diekspresikan dalam bentuk detik busur per sekon waktu sideris; dalam kasus matahari, laju-laju tersebut adalah dalam bentuk detik busur per sekon waktu matahari semu atau dengan presisi yang cukup, waktu matahari rata-rata.

Hasil-hasil yang baru saja diperoleh dapat diturunkan dengan mudah melalui metode kalkulus, sebagai berikut. Dari segitiga $PZX$, berdasarkan rumus A,

$$ \cos z = \sin \delta \sin \phi + \cos \delta \cos \phi \cos H, $$

di mana $\delta$ dan $\phi$ diandaikan konstan. Melalui diferensiasi

$$ \sin z \frac{dz}{dH} = \cos \delta \cos \phi \sin H. $$

Berdasarkan B,

$$ \sin z \sin A = \sin H \cos \delta \dots\dots(28); $$

$$ \therefore \frac{dz}{dH} = \sin A \cos \phi \dots\dots(29), $$

yang mana pada intinya sama dengan (26). Jika $z$ dan $H$ diekspresikan secara berturut-turut dalam bentuk detik busur dan sekon waktu,

$$ \frac{dz}{dH} = 15 \sin A \cos \phi. $$

Diferensiasikan (28)—di mana $z, A$ dan $H$ adalah variabel-variabel—terhadap $H$. Maka

$$ \sin z \cos A \frac{dA}{dH} = \cos H \cos \delta - \sin A \cos z \frac{dz}{dH} $$

$$ = \cos H \cos \delta - \sin^2 A \cos z \cos \phi, $$

dengan menggunakan (29).
Juga, oleh C,

$$ \cos \delta \cos H = \cos z \cos \phi - \sin z \sin \phi \cos A; $$

$$ \therefore \sin z \cos A \frac{dA}{dH} = \cos^2 A \cos z \cos \phi - \sin z \sin \phi \cos A; $$

$$ \therefore \frac{dA}{dH} = -(\sin \phi - \cot z \cos A \cos \phi), $$

atau, jika $A$ dan $H$ diekspresikan secara berturut-turut dalam detik busur dan sekon waktu, rumus terakhir ini menjadi

$$ \frac{dA}{dH} = -15(\sin \phi - \cot z \cos A \cos \phi), $$

yang mana adalah yang telah diturunkan sebelumnya.

### 33. Senja dan Fajar (*Twilight*).
Setelah matahari terbenam, cahaya matahari tidak langsung, yang dipantulkan dan dihamburkan oleh atmosfer bagian atas, masih terus menyinari bumi, namun semakin meredup saat matahari tenggelam lebih jauh ke bawah horizon. Ketika matahari berada $18^\circ$ di bawah horizon (jarak zenitnya saat itu $108^\circ$) iluminasi tidak langsung ini telah menjadi cukup dapat diabaikan. Interval antara matahari terbenam dan waktu ketika jarak zenit matahari telah meningkat menjadi $108^\circ$ disebut durasi senja (*evening twilight*). Dengan cara yang serupa, kita mendefinisikan durasi fajar (*morning twilight*). Durasi senja, sebagai contoh, dapat dihitung sebagai berikut. Pada Gbr. 26, $LFM$ adalah paralel deklinasi matahari (karena tidak ada akurasi besar yang diperlukan dalam perhitungan khusus ini, kita mengabaikan perubahan dalam deklinasi matahari selama hari khusus yang bersangkutan) dan $JGK$ adalah sebuah lingkaran kecil, sejajar dengan horizon, yang setiap titiknya adalah $108^\circ$ dari $Z$. Lingkaran kecil ini memotong paralel deklinasi di $G$. Maka interval waktu yang diperlukan bagi matahari untuk bergerak dari $F$ ke $G$, yakni $F\hat{P}G$, adalah durasi senja. Sekarang $F\hat{P}G = Z\hat{P}G - Z\hat{P}F$; karena $Z\hat{P}F$ adalah sudut jam dari matahari terbenam ia dapat dihitung oleh rumus (24). Sekarang di dalam segitiga $ZPG$, kita memiliki: $ZG = 108^\circ$, $PZ = 90^\circ - \phi$ dan $PG = 90^\circ - \delta$; karenanya, berdasarkan A,

$$ \cos 108^\circ = \sin \phi \sin \delta + \cos \phi \cos \delta \cos Z\hat{P}G, $$

yang memungkinkan perhitungan dari $Z\hat{P}G$ untuk dilakukan. Nilai dari $\delta$, yang digunakan dalam rumus ini, tentu saja bergantung pada hari tertentu dari tahun yang bersangkutan. Dengan demikian durasi senja ditemukan.
"""
st.markdown(materi_bab_2_bagian_16, unsafe_allow_html=True)
st.image("Gambar_26.jpg", caption="Gambar 26: Diagram Durasi Senja (Evening Twilight)", use_container_width=True)

materi_bab_2_bagian_17 = r"""
Jelas dari Gbr. 26 bahwa senja akan berakhir jika $NM$ lebih besar dari $NJ$, dengan kata lain, jika pada tengah malam semu matahari berada lebih dari $18^\circ$ di bawah horizon. Sekarang $NT = 90^\circ - \phi$ dan $MT = \delta$; $\therefore NM = 90^\circ - \phi - \delta$. Karenanya senja berakhir jika $90^\circ - \phi - \delta > 18^\circ$, atau jika $\delta < 72^\circ - \phi$. Sebagai contoh, di lintang $60^\circ \text{ U}$, senja akan berakhir jika $\delta < 12^\circ$. Ketika $\delta$ lebih besar dari $12^\circ$, jarak zenit matahari adalah kurang dari $108^\circ$ antara terbenam dan tengah malam semu, dan juga antara tengah malam semu dan matahari terbit; oleh karena itu, di $60^\circ \text{ U}$ tidak pernah benar-benar gelap pada hari-hari di tahun itu ketika deklinasi matahari melebihi $12^\circ \text{ U}$. Hari-hari ini adalah di antara 23 April dan 22 Agustus.

---

### LATIHAN SOAL (*EXERCISES*)

[Simbol-simbol yang digunakan:
$\phi = \text{lintang pengamat (latitude of observer)},$
$A = \text{azimut benda langit (azimuth of heavenly body)},$
$H = \text{sudut jam (hour angle)},$
$z = \text{jarak zenit (zenith distance)},$
$\epsilon = \text{kemiringan ekliptika (obliquity of the ecliptic)}.$]

**1.** Jika $z_1$ dan $z_2$ adalah jarak zenit sebuah bintang pada meridian dan pada vertikal utama secara berturut-turut, buktikan bahwa

$$ \text{(i)} \quad \cot \delta = \operatorname{cosec} z_1 \sec z_2 - \cot z_1, $$

$$ \text{(ii)} \quad \cot \phi = \cot z_1 - \operatorname{cosec} z_1 \cos z_2, $$

di mana $\delta$ adalah deklinasi bintang tersebut.  *[Lond. 1929.]*

**2.** Jika $\psi$ adalah sudut yang dibentuk oleh lintasan sebuah bintang pada saat terbit dengan horizon, buktikan bahwa

$$ \cos \psi = \sin \phi \sec \delta. $$

**3.** Jika $h, H$ adalah sudut jam sebuah bintang, berdeklinasi $+ \delta$, pada vertikal utama (barat) dan pada saat terbenam secara berturut-turut, untuk sebuah tempat di lintang utara, tunjukkan bahwa

$$ \cos h \cos H + \tan^2 \delta = 0. $$

Hitunglah interval (benar hingga $0.1$ menit dari waktu matahari rata-rata) untuk sebuah tempat di lintang $36^\circ \text{ U}$ antara persinggahan Aldebaran (deklinasi $+ 16^\circ 22'$) melintasi vertikal utama (barat) dan saat terbenamnya. *[Lond. 1926.]*

**4.** Sebuah perahu yang melaju pada kecepatan 5 knot dikemudikan terus-menerus ke arah sebuah bintang. Buktikan bahwa jarak tempuh menuju ke arah barat adalah kira-kira $\frac{1}{3} (z_2^\circ - z_1^\circ) \sec \phi$ mil, di mana $z_1^\circ$ dan $z_2^\circ$ adalah jarak zenit awal dan akhir, dalam derajat, dari bintang tersebut dan $\phi$ lintang rata-ratanya. *[M.T. 1917.]*

**5.** Jika kolintangnya adalah $C$, buktikan bahwa

$$ C = x + \cos^{-1} (\cos z \sec y), $$

di mana

$$ \tan x = \cot \delta \cos H, $$

$$ \sin y = \cos \delta \sin H, $$

dengan $H$ menjadi sudut jamnya.

**6.** Temukan sampai ke sekon waktu matahari rata-rata terdekat interval antara persinggahan melintasi meridian dari dua bintang yang deklinasinya adalah $60^\circ \text{ U}$ dan $60^\circ \text{ S}$, dan yang jarak antaranya adalah $\cos^{-1} (- \frac{8}{9})$. (Asumsikan bahwa 1 tahun adalah $365\frac{1}{4}$ hari.) *[M.T. 1923.]*

**7.** Jika deklinasi $\delta$ dari sebuah bintang lebih besar dari lintang $\phi$, buktikan bahwa azimut terlebar dari bintang tersebut di timur atau di barat adalah

$$ \sin^{-1} (\cos \delta \sec \phi). $$

**8.** Pada U.T. $21^h 56^m$ pada 1927 Maret 28 sebuah bintang yang terang diamati melalui celah awan sebagai berikut: ketinggian (perkiraan) $37^\circ 10'$; azimut $136^\circ$ barat. Posisi pengamat adalah: lintang $50^\circ \text{ U}$, bujur $7^\circ 15' \text{ B}$. Identifikasilah bintang tersebut.
(R.A.M.S. adalah $0^h 21^m$ kira-kira.) *[Lond. 1927.]*

**9.** R.A. dan deklinasi Capella pada transit atas di Greenwich pada 1930 Mei 30 adalah $5^h 11^m$ dan $+ 45^\circ 55'$. Tentukan ketinggian dan azimut bintang tersebut pada momen yang sama di New York, Observatorium Universitas Columbia, Lintang $40^\circ 49' \text{ U}$, Bujur $4^h 56^m \text{ B}$.

**10.** Di lintang utara $45^\circ$ azimut terlebar dari bintang sirkumpolar adalah $45^\circ$ (timur atau barat). Buktikan bahwa deklinasi bintang tersebut adalah $+ 60^\circ$.

**11.** Jika lintang $\phi$ dan deklinasi sebuah bintang diketahui, tunjukkan bahwa kesalahan dalam nilai sudut jam yang dideduksi yang disebabkan oleh sebuah kesalahan berukuran $\Delta z$ di dalam jarak zenit adalah $\Delta z \operatorname{cosec} A \sec \phi$, di mana $A$ adalah azimut bintang tersebut.

**12.** Jika pengamat meningkatkan lintangnya sebesar nilai $\Delta \phi$ sementara sudut jam sebuah bintang meningkat sebesar $\Delta H$, tunjukkan bahwa perubahan di dalam ketinggian adalah

$$ \Delta \phi \cos A - \Delta H \sin A \cos \phi. $$

**13.** $a$ dan $a + \Delta a$ adalah ketinggian matahari yang diamati secara serentak pada dua tempat yang bertetangga di meridian yang sama. Jika $\phi$ adalah lintang dari salah satu tempat dan $\delta$ adalah deklinasi matahari, buktikan bahwa selisih dari lintang antara tempat-tempat tersebut adalah kira-kira

$$ \Delta a \cos a \cos \phi / (\sin \delta - \sin a \sin \phi). \quad [Ball.] $$

**14.** Dua buah bintang $(\alpha, \delta)$ dan $(\alpha', \delta')$ diamati pada momen yang sama di atas lingkaran vertikal yang sama. Jika $H$ adalah sudut jam dari bintang pertama, buktikan bahwa

$$ \cos (\chi + H) = \tan \phi \cos \chi \cot \delta, $$

di mana $\chi$ diberikan oleh

$$ \tan \frac{1}{2} (\alpha - \alpha' - 2\chi) = \frac{\sin (\delta' - \delta)}{\sin (\delta' + \delta)} \cot \frac{1}{2} (\alpha' - \alpha). $$

**15.** Jika $x$ adalah panjang bayangan yang dilemparkan pada permukaan tanah mendatar oleh sebuah tiang vertikal saat tengah hari semu pada suatu ekuinoks, dan jika $y$ adalah panjang bayangan yang dilemparkan oleh tiang yang sama saat solstis musim panas ketika matahari berada pada vertikal utama, tunjukkan bahwa

$$ x = y \tan \psi \tan \phi, $$

di mana

$$ \sin \psi = \sin \epsilon \operatorname{cosec} \phi. \quad [Lond. 1928.] $$

**16.** Sebuah dinding lurus dengan ketinggian $h$ membentang ke arah $\theta$ derajat barat dari selatan. Buktikan bahwa pada suatu ekuinoks, dinding tersebut tidak melemparkan bayangan ketika sudut jam matahari $H$ diberikan oleh

$$ \tan H = \sin \phi \tan \theta, $$

dan bahwa pada tengah hari semu, kelebaran bayangan tersebut adalah $h \tan \phi \sin \theta$.

**17.** Seorang pengamat di lintang $50^\circ$ melihat sebuah bintang terbenam tepat di barat di belakang punggung bukit (*ridge*) rendah berjarak satu mil, yang melandai turun ke utara pada inklinasi $30^\circ$ terhadap horizontal. Buktikan bahwa dengan melangkah satu *yard* ke kanan, ia akan melihat bintang tersebut sekitar $22$ detik lebih lama. *[M.T. 1913.]*

**18.** Dua tempat berada di lintang yang sama dan jarak kutub lingkaran besar yang melalui keduanya sama dengan deklinasi matahari. Buktikan bahwa di tempat-tempat ini, panjang malam hari sama dengan selisih bujur mereka.
"""
st.markdown(materi_bab_2_bagian_17, unsafe_allow_html=True)

materi_bab_2_bagian_18 = r"""
**19.** Misalkan $\alpha, \delta$ adalah koordinat sebuah bintang terhadap suatu lingkaran besar $S$, dan $\alpha', \delta'$ adalah koordinat bintang yang sama terhadap lingkaran besar lainnya $S'$. Jika $i$ adalah inklinasi $S'$ terhadap $S$ dan jika *ascending node* dari $S'$ pada $S$ memiliki koordinat $(\theta, 0)$ pada sistem pertama dan $(\theta', 0)$ pada sistem kedua, tunjukkan bahwa

$$ \cos \delta' \cos (\alpha' - \theta') = \cos \delta \cos (\alpha - \theta), $$

$$ \cos \delta' \sin (\alpha' - \theta') = \sin \delta \sin i + \cos \delta \cos i \sin (\alpha - \theta), $$

$$ \sin \delta' = \sin \delta \cos i - \cos \delta \sin i \sin (\alpha - \theta). $$

Jika $\alpha = 75^\circ, \delta = 15^\circ, \theta = 215^\circ, \theta' = 115^\circ, i = 23^\circ 30'$, tunjukkan bahwa dari persamaan-persamaan terakhir $\alpha' = 327^\circ 12', \delta' = 29^\circ 0'$.

**20.** Tunjukkan bahwa jika $a$ adalah ketinggian bintang kutub, $H$ sudut jam dan $p$ (dalam detik busur) jarak kutubnya, lintangnya kira-kira diberikan oleh

$$ \phi = a - p \cos H + \frac{1}{2} p^2 \sin^2 H \tan a \sin 1''. $$

**21.** Sebuah benda langit (deklinasi $\delta$) berada pada sudut kecil $H$ dari meridian. Buktikan bahwa jarak zenit $z$ diberikan kira-kira oleh

$$ z = \phi - \delta + a_1 - a_2, $$

di mana $a_1$ (diekspresikan dalam menit busur) diberikan oleh

$$ a_1 = \frac{2 \cos \phi \cos \delta}{\sin (\phi - \delta)} \sin^2 \frac{H}{2} \operatorname{cosec} 1', $$

dan

$$ a_2 = \frac{1}{2} a_1^2 \cot (\phi - \delta) \sin 1'. $$

**22.** Jika $a$ adalah ketinggian matahari di vertikal utama pada suatu tempat di lintang $\phi$ dan $L$ adalah bujurnya, buktikan bahwa

$$ \phi = \sin^{-1} (\sin L \sin \epsilon \operatorname{cosec} a). \quad [Ball.] $$

**23.** Buktikan bahwa, di lintang $45^\circ$, interval antara momen ketika azimut sebuah bintang adalah $90^\circ$ timur dan momen terbenam adalah konstan.

**24.** Jika $\delta$ adalah deklinasi sebuah bintang dan $A$ azimut maksimumnya, tunjukkan bahwa dalam $t$ sekon waktu dari momen ketika azimutnya adalah $A$, azimut tersebut telah berubah sebesar

$$ \frac{1}{2} 15^2 t^2 \sin 1'' \sin^2 \delta \tan A \quad \text{detik busur.} $$

**25.** Jika $\eta$ adalah sudut paralaktik dan $\phi$ serta $\delta$ adalah konstan, buktikan bahwa

$$ \text{(i)} \quad \frac{d\eta}{dH} = - \cos \phi \cos A \operatorname{cosec} z; $$

$$ \text{(ii)} \quad \frac{d^2z}{dH^2} = \frac{d\eta}{dH} \cos \delta \cos \eta; $$

$$ \text{(iii)} \quad \frac{d^2A}{dH^2} = - \frac{\cos \delta}{\sin^2 z} \left( \cos z \cos \eta \frac{dz}{dH} + \sin z \sin \eta \frac{d\eta}{dH} \right). $$

**26.** Jika $H$ adalah sudut jam sebuah bintang pada saat terbit, tunjukkan bahwa

$$ \tan^2 \frac{H}{2} = \frac{\cos (\phi - \delta)}{\cos (\phi + \delta)}. $$

**27.** Di sebuah tempat di lintang utara $\phi$, dua bintang $A$ dan $B$ (masing-masing dengan deklinasi $\delta$ dan $\delta_1$) terbit pada momen yang sama dan $A$ transit ketika $B$ sedang terbenam. Buktikan bahwa

$$ \tan \phi \tan \delta = 1 - 2 \tan^2 \phi \tan^2 \delta_1. $$

**28.** Jika dua bintang $(\alpha, \delta)$ dan $(\alpha_1, \delta_1)$ terbit pada momen yang sama di suatu tempat di lintang $\phi$, tunjukkan bahwa

$$ \cot^2 \phi \sin^2 (\alpha_1 - \alpha) = \tan^2 \delta + \tan^2 \delta_1 - 2 \tan \delta \tan \delta_1 \cos (\alpha_1 - \alpha). \quad [Ball.] $$

**29.** Di sebuah tempat di lintang $\phi$ matahari diamati terbit $h$ jam sebelum tengah hari semu, dan hari berikutnya ia terbit $m$ menit lebih lambat. Deklinasinya pada hari pertama adalah $\delta$. Tunjukkan bahwa jarak dalam menit busur antara dua titik terbit tersebut adalah

$$ 15 m \cos^2 \delta \operatorname{cosec} \phi. \quad [Coll. Exam.] $$

**30.** Jika senja berakhir ketika pusat matahari berada $18^\circ$ di bawah horizon, tunjukkan bahwa di ekuator durasi senja diberikan dalam jam oleh

$$ \frac{12}{\pi} \sin^{-1} (\sin 18^\circ \sec \delta). $$

Gunakan rumus ini untuk menghitung durasi senja pada solstis musim panas. *[Lond. 1930.]*

**31.** Tunjukkan bahwa di suatu tempat di lintang $\phi$ durasi terpendek dari senja dan fajar, diekspresikan dalam jam, adalah

$$ \frac{12}{\pi} \sin^{-1} (\sin 9^\circ \sec \phi), $$

di mana $\sin^{-1} (\sin 9^\circ \sec \phi)$ diekspresikan dalam derajat. *[Ball.]*

**32.** Jika senja atau fajar dimulai atau berakhir ketika matahari berada $18^\circ$ di bawah horizon, tunjukkan bahwa semua tempat memiliki hari yang lebih dari dua belas jam, termasuk senja dan fajar, selama deklinasi matahari secara numerik kurang dari $18^\circ$.

**33.** Jika hari dianggap dimulai dan berakhir ketika matahari berada pada sudut $\theta$ di bawah horizon, tunjukkan bahwa hari terpendek tidak akan terjadi pada solstis musim dingin jika lintangnya kurang dari $\phi$, di mana

$$ \sin \phi = \sin \epsilon \sin \theta, $$

dan $\epsilon$ adalah kemiringan ekliptika. *[M.T. 1917.]*

**34.** Dengan mengasumsikan bahwa matahari bergerak secara seragam di ekliptika, menyelesaikan satu putaran dalam 365 hari, tunjukkan bahwa jumlah malam di mana terdapat senja dan fajar bahkan pada tengah malam di sebuah tempat di lintang $\phi$ adalah bilangan bulat terdekat yang lebih besar dari

$$ \frac{365}{\pi} \cos^{-1} \{ \cos (\phi + 18^\circ) / \sin \epsilon \}, $$

senja dan fajar dimulai atau berakhir ketika matahari berada $18^\circ$ di bawah horizon. *[Coll. Exam.]*

**35.** Jika $\theta$ melambangkan depresi matahari di bawah horizon pada akhir senja, dan $\eta, \eta'$ adalah sudut paralaktik pada akhir senja dan pada saat terbenam secara berturut-turut, buktikan bahwa durasi ($T$) dari senja diberikan oleh

$$ 2 \sin^2 \frac{T}{2} \cos^2 \phi = 1 - \cos \theta \cos (\eta' - \eta). $$

**36.** Asensio rekta sebuah bintang adalah $5^h 49^m$ dan deklinasinya adalah $+ 7^\circ 23'$, dan kemiringan ekliptika adalah $23^\circ 27'$. Tunjukkan bahwa bujur dan lintang bintang tersebut berturut-turut adalah $87^\circ 10'$, $- 16^\circ 2'$.

**37.** Dua bintang $(\alpha_1, \delta_1)$ dan $(\alpha_2, \delta_2)$ memiliki bujur yang sama; buktikan bahwa

$$ \sin (\alpha_1 - \alpha_2) = \tan \epsilon (\cos \alpha_1 \tan \delta_2 - \cos \alpha_2 \tan \delta_1). $$

**38.** Sebuah bintang dengan asensio rekta $\alpha$ dan deklinasi $\delta$ memiliki lintang kecil $\beta$. Buktikan bahwa bujur matahari, ketika R.A.-nya adalah $\alpha$, berbeda dari bujur bintang tersebut kira-kira sebesar $\beta \sin \delta \cot \alpha$.

**39.** Tunjukkan bahwa kemiringan ekliptika dapat ditentukan dengan melakukan pengamatan terhadap deklinasi matahari $\delta$ pada suatu tengah hari menjelang solstis musim panas dengan menggunakan rumus $\epsilon = \delta + q^2 \sin 2\delta$, di mana $q$ adalah setengah dari defisit dari sudut siku-siku dari asensio rekta matahari. *[M.T. 1924.]*

**40.** Kutub Bima Sakti berada pada R.A. $12^h 48^m$, Dekl. $+ 27^\circ$. Sekitar tanggal berapa matahari melewati Bima Sakti? (Kemiringan ekliptika $= 23^\circ 27'$.) *[M.T. 1925.]*

**41.** Sebuah bintang dipindahkan dalam jumlah kecil $dr$ menuju sebuah titik $O$ di bola langit dengan koordinat ekuatorial $(\alpha_0, \delta_0)$. Tunjukkan bahwa perubahan yang dihasilkan pada koordinat ekuatorial bintang $(\alpha, \delta)$ diberikan oleh

$$ \cos \delta \, d\alpha = \cos \delta_0 \sin (\alpha - \alpha_0) \operatorname{cosec} r \, dr, $$

$$ d\delta = (\cos \delta_0 \sin \delta \cos (\alpha - \alpha_0) - \sin \delta_0 \cos \delta) \operatorname{cosec} r \, dr, $$

di mana $r$ adalah panjang busur pada bola langit dari bintang ke titik $O$. *[Glas. 1974.]*

**42.** Buktikan bahwa jarak zenit $z$ dari kutub utara ekliptika diberikan oleh

$$ z = \cos^{-1} (\cos \epsilon \sin \phi - \sin \epsilon \cos \phi \sin T). $$

Di sini $\epsilon$ adalah kemiringan ekliptika, $\phi$ adalah lintang pengamat, dan $T$ adalah waktu sideris lokal.
"""
st.markdown(materi_bab_2_bagian_18, unsafe_allow_html=True)
