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
*(zenith)* menjadi titik pada bola langit yang berada tepat di atas kepala—arahnya dapat didefinisikan dengan menggunakan unting-unting (*plumb-line*). Oleh karena itu, $OZ$ adalah kelanjutan dari garis lurus yang menghubungkan pusat bumi ke $O$. Bidang yang melalui $O$ yang tegak lurus terhadap $OZ$ adalah bidang horizon, yang memotong bola langit pada lingkaran besar $NAS$, yang disebut horizon astronomis atau sekadar horizon. Dengan demikian, pada Gbr. 10, horizon membagi bola langit menjadi dua belahan bola (*hemisphere*), di mana bagian atas adalah belahan bola yang terlihat (*visible hemisphere*), dan bagian bawah tersembunyi dari pengamat oleh bumi. Misalkan $X$ menjadi posisi sebuah bintang di bola langit pada saat tertentu. Setiap lingkaran besar yang ditarik melalui $Z$ disebut lingkaran vertikal (*vertical circle*); khususnya, lingkaran vertikal pada Gbr. 10 yang melalui $X$ adalah $ZXA$. Pada bidang $ZXA$, sudut $AOX$ atau busur lingkaran besar $AX$ disebut ketinggian (*altitude*), yang akan dilambangkan dengan $a$. Karena $OZ$ tegak lurus terhadap bidang horizon, lingkaran besar busur $ZA$ adalah $90^\circ$; oleh karena itu $ZX = 90^\circ - a$. $ZX$ disebut jarak zenit (*zenith distance*, disingkat z.d.) dari bintang $X$ dan akan dilambangkan dengan $z$. Dengan demikian
$$ z = 90^\circ - a \dots\dots(1). $$

Misalkan $LXM$ menjadi lingkaran kecil melalui $X$ yang sejajar dengan horizon; lingkaran ini disebut paralel ketinggian (*parallel of altitude*) dan sedemikian rupa sehingga semua benda langit, yang posisinya pada suatu saat tertentu terletak pada lingkaran kecil ini, memiliki ketinggian yang sama dan juga, berdasarkan (1), memiliki jarak zenit yang sama dengan $X$. Dengan demikian, jika ketinggian atau jarak zenit sebuah bintang diberikan, paralel ketinggian tempat bintang itu harus berada dapat ditentukan secara pasti. Untuk mendefinisikan posisinya secara lengkap pada bola langit, lingkaran vertikal khusus tempat bintang itu berada juga harus ditentukan. Hal ini dilakukan sebagai berikut.

Misalkan $OP$ sejajar dengan sumbu tempat bumi berputar. Jika lintang pengamat adalah utara (seperti pada Gbr. 10), posisi $P$ disebut kutub langit utara (*north celestial pole*), atau sekadar kutub utara (*north pole*). Kita tidak secara langsung menyadari rotasi bumi, tetapi efeknya ditunjukkan dalam rotasi semu bola langit. Bintang-bintang dengan demikian tampak bergerak melintasi langit dan arahnya terus berubah. Di belahan bumi utara, bagaimanapun, ada satu bintang, yang dapat dilihat dengan mata telanjang, yang tampak sangat sedikit berubah. Bintang ini adalah Polaris, atau bintang kutub utara, yang arahnya di langit hampir persis sama dengan arah yang diberikan oleh $OP$. Jika kebetulan ada sebuah bintang yang terletak tepat di $P$ pada bola langit, ketinggian dan arahnya akan tidak berubah sepanjang malam. Kita mendefinisikan lingkaran vertikal melalui $P$, yaitu $ZPN$ (yang memotong horizon di $N$), sebagai lingkaran vertikal utama (*principal vertical circle*) dan titik $N$ sebagai titik utara horizon (*north point of the horizon*).

Titik $S$ pada horizon yang tepat berlawanan dengan $N$ adalah titik selatan (*south point*); titik barat ($W$) dan timur ($E$) points\* memiliki arah yang tegak lurus terhadap arah $N$ dan $S$ ($E$ tidak ditunjukkan pada Gbr. 10). Titik-titik $N, E, S$ dan $W$ disebut titik-titik kardinal (*cardinal points*).

Kita sekarang menentukan posisi sebuah bintang $X$ pada bola langit pada saat tertentu dengan merujuk pada horizon dan lingkaran vertikal utama $ZPN$. Jika bintang berada di bagian barat bola langit (seperti pada Gbr. 10), sudut bola $PZX$ (yang dibentuk oleh lingkaran vertikal utama dan lingkaran vertikal melalui $X$) atau busur lingkaran besar $NA$ disebut azimut (*azimuth*, $W$). Jika bintang berada di bagian timur bola langit, seperti pada Gbr. 11, sudut $PZX$
"""
st.markdown(materi_bab_2_bagian_2, unsafe_allow_html=True)
st.image("Gambar_11.png", caption="Gambar 11: Sistem Azimut (Timur/Barat) dan Titik Kardinal", use_container_width=True)

materi_bab_2_bagian_3 = r"""
atau busur $NB$ adalah azimut ($E$). Dengan demikian pada saat apa pun posisi benda langit pada bola langit dapat dideskripsikan sepenuhnya dengan merujuk pada horizon dan titik utara horizon dalam hal ketinggian dan azimut ($E$ atau $W$) atau, sebagai alternatif, dalam hal jarak zenit dan azimut. Ketika azimut adalah $90^\circ$ $E$ atau $90^\circ$ $W$, bintang tersebut dikatakan berada pada vertikal utama (*prime vertical*), yang dengan demikian merupakan lingkaran vertikal melalui titik timur $E$ atau titik barat $W$.

Karena pada Gbr. 10 dan 11 sudut $POZ$ (atau lingkaran besar busur $PZ$) ekivalen dengan sudut antara jari-jari bumi yang melewati posisi pengamat dan sumbu bumi, maka $P\hat{O}Z$ (atau $PZ$) sama dengan kolintang pengamat atau
$$ PZ = 90^\circ - \phi \dots\dots(2), $$
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

Deklinasi sebuah bintang diketahui, kita dengan demikian dapat menentukan lingkaran kecil, yang disebut paralel deklinasi (*parallel of declination*), tempat bintang itu harus berada. Untuk memperbaiki posisinya pada bola langit pada saat tertentu, kita memerlukan lingkaran besar referensi lainnya. Ini adalah semi-lingkaran besar $PZRSQ$, yang disebut meridian pengamat (*observer's meridian*). Ketika bintang berada di $L$ pada meridian pengamat, ia dikatakan melakukan transit (*transit*) atau mencapai puncaknya (*culminate*), dan jelas dari Gbr. 12 bahwa ketinggiannya ($SL$) adalah yang terbesar dan jarak zenitnya $ZL$ adalah yang terkecil. Setelah itu, karena rotasi bumi, ia bergerak sepanjang lingkaran kecil $LFM$ memotong horizon di $F$ di mana ia dikatakan terbenam (*set*); ketinggiannya di $F$ tentu saja adalah $0^\circ$ dan jarak zenitnya $90^\circ$. Selama interval waktu yang bergantung pada deklinasinya, bintang berada di bawah horizon, mencapai depresi maksimum di bawah horizon di $M$; akhirnya ia mencapai horizon di $G$ di mana ia dikatakan terbit (*rise*). Ketinggiannya berangsur-angsur meningkat, ia kembali setelah interval yang ekuivalen dengan waktu di mana bumi melakukan rotasi penuh mengelilingi sumbunya, ke meridian pengamat di $L$. Pada saat apa pun posisi bintang pada paralel deklinasi ditentukan oleh sudut di $P$ antara meridian pengamat dan meridian ($PXQ$) melalui bintang pada saat itu; sudut ini adalah $RPX$ atau $ZPX$ atau busur $RD$ pada ekuator. Sudut ini, yang dilambangkan dengan $H$, disebut sudut jam (*hour angle*) dan diukur dari meridian pengamat ke arah barat dari $0^\circ$ (di $L$) hingga $360^\circ$ (ketika bintang kembali ke meridian pengamat) atau, seperti yang lebih biasa, dari $0^h$ hingga $24^h$. Kita dapat mengekspresikan ini dengan cara yang sedikit berbeda. Ketika bintang sedang transit, meridiannya bertepatan dengan meridian pengamat; setelah itu, meridian bintang bergerak dengan mantap ke arah barat dan, ketika ia telah membuat satu putaran penuh dari bola langit, ia telah menggambarkan sudut $360^\circ$ atau $24^h$ terhadap meridian pengamat. Dari Gbr. 12 terlihat bahwa jika bintang berada di sebelah barat meridian pengamat, yaitu jika
"""
st.markdown(materi_bab_2_bagian_4, unsafe_allow_html=True)
st.image("Gambar_13.png", caption="Gambar 13: Diagram Sudut Jam Barat dan Timur Meridian", use_container_width=True)

materi_bab_2_bagian_5 = r"""
azimutnya adalah barat, sudut jamnya berada di antara $0^\circ$ dan $180^\circ$, yaitu antara $0^h$ dan $12^h$. Demikian pula, jika bintang berada di sebelah timur meridian (azimut timur)—seperti pada Gbr. 13—sudut jam berada di antara $12^h$ dan $24^h$. Kita dengan demikian memiliki aturan:
*Jika azimut bintang adalah barat, sudut jam berada di antara $0^h$ dan $12^h$ (dan sebaliknya); jika azimut bintang adalah timur, sudut jam berada di antara $12^h$ dan $24^h$.*

### 20. Diagram untuk belahan bumi selatan.
Diagram yang dijelaskan sejauh ini dalam bab ini merujuk pada bola langit untuk pengamat di lintang utara. Kita sekarang akan mendeskripsikan diagram yang bersesuaian untuk pengamat di belahan bumi selatan. Pada Gbr. 14, kita akan menempatkan zenit pengamat seperti pada diagram sebelumnya. Horizon langit kemudian seperti yang ditunjukkan. Di belahan bumi selatan, kutub langit selatan $Q$ berada di atas horizon. Kemudian, jika $\phi$ melambangkan lintang selatan pengamat, $QZ = 90^\circ - \phi$. Lingkaran vertikal utama sekarang adalah $ZQS$, memotong horizon di titik selatan $S$. Titik utara $N$ kemudian dapat ditempatkan dalam diagram. Ekuator langit dan horizon berpotongan di titik barat dan timur $W$ dan $E$ (yang terakhir tidak ditunjukkan pada Gbr. 14) menurut
"""
st.markdown(materi_bab_2_bagian_5, unsafe_allow_html=True)
st.image("Gambar_14.png", caption="Gambar 14: Bola Langit untuk Pengamat di Belahan Bumi Selatan", use_container_width=True)

materi_bab_2_bagian_6 = r"""
aturan pada catatan kaki halaman 27. Pertimbangkan sebuah bintang $X$ dengan deklinasi selatan. Berkat rotasi bumi, ia akan mendeskripsikan lingkaran kecil $LXM$, paralel terhadap ekuator langit dan terletak di antara ekuator langit dan kutub selatan $Q$. Pada $L$, bintang akan memiliki ketinggian terbesar—ia kemudian berada pada meridian pengamat, yaitu semi-lingkaran $QZRNP$. Akibat rotasi bumi, bintang akan bergerak dari meridian pengamat ke arah barat, yaitu ke arah $LXM$, seperti yang ditunjukkan oleh anak panah pada diagram. Sudut $ZQX$ adalah sudut jam yang diukur, seperti sebelumnya, dari $0^h$ hingga $24^h$ ke arah barat dari meridian pengamat. $QZX$ adalah azimut; dalam hal ini adalah barat. Jika $\delta$ adalah deklinasi (negatif) bintang, maka $DX = -\delta$ dan $QX = 90^\circ + \delta$. Bagian lain dari segitiga bola $QZX$ adalah: $QZ = 90^\circ - \phi$, $ZX = z$ (jarak zenit), $QZX = A$ (azimut) dan $ZQX = H$ (sudut jam). Ketika azimut bintang adalah barat, sudut jam berada di antara $0^h$ dan $12^h$. Ketika azimut bintang adalah timur, diagram yang bersesuaian dapat digambarkan secara serupa; ini diserahkan sebagai latihan bagi siswa; maka akan ditemukan bahwa sudut jam berada di antara $12^h$ dan $24^h$. Aturan yang dinyatakan pada akhir bagian 19 terlihat berlaku untuk lintang selatan maupun utara.

### 21. Bintang sirkumpolar (*circumpolar stars*).
Pertimbangkan bola langit untuk pengamat di lintang utara $\phi$ (Gbr. 15). Paralel deklinasi digambarkan untuk dua bintang $X$ dan $Y$, yang keduanya selalu berada di atas horizon dan akibatnya tidak terbenam. Bintang-bintang seperti itu disebut sirkumpolar
"""
st.markdown(materi_bab_2_bagian_6, unsafe_allow_html=True)
st.image("Gambar_15.png", caption="Gambar 15: Bintang Sirkumpolar yang Tidak Pernah Terbenam", use_container_width=True)

materi_bab_2_bagian_7 = r"""
bintang. Dari gambar tersebut terlihat dengan mudah bahwa syarat agar sebuah bintang tidak terbenam adalah: $PM$ harus kurang dari $PN$; yaitu, jarak kutub utara harus kurang dari lintang, atau dengan kata lain, deklinasi harus lebih besar dari kolintang.

Ketika bintang $X$ berada pada meridian pengamat di $L$, ia berada pada kulminasi atas (*upper culmination*) atau dalam transit (*in transit*); ketika bintang mencapai $M$, ia berada pada kulminasi bawah (*lower culmination*). Ekspresi "kulminasi di atas kutub" (*culmination above pole*) dan "kulminasi di bawah kutub" (*culmination below pole*) sering digunakan. Pada kulminasi atas, jarak zenit bintang adalah $ZL$ atau $(PL - PZ)$, yaitu, $\phi - \delta$. Pada kulminasi bawah, jarak zenit bintang adalah $ZM$ atau $(ZP + PM)$, yaitu, $180^\circ - (\phi + \delta)$. Ketika $\delta = \phi$, kulminasi atas terjadi di zenit. Ketika $\delta > \phi$, kulminasi atas terjadi di antara $P$ dan $Z$, seperti untuk bintang $Y$; maka azimut tidak melebihi $90^\circ$, seperti yang dapat disimpulkan dengan mudah dari diagram. Bintang sirkumpolar selatan dapat dianggap dengan cara yang sama.

### 22. Bola langit standar atau geosentrik (*The standard or geocentric celestial sphere*).
Dalam bagian-bagian sebelumnya, deklinasi bintang pada bola langit yang pusatnya adalah pengamat telah didefinisikan. Karena bintang-bintang berada pada jarak yang hampir tak terhingga besarnya dibandingkan dengan dimensi bumi, deklinasi atau jarak kutub bintang yang didefinisikan dengan cara ini tidak bergantung pada posisi pengamat di permukaan bumi, seperti yang dapat dilihat dengan mudah dari Gbr. 16. (Adalah lebih mudah untuk tujuan kita saat ini untuk berurusan dengan jarak kutub utara bintang daripada deklinasinya.) Pada Gbr. 16, $P_1CQ_1$ adalah sumbu rotasi bumi, $C$ menjadi pusat bumi; $O$ adalah pengamat dan $COZ$ adalah arah zenit di $O$; $OP$ sejajar dengan $CP_1$ dan arah bintang yang
"""
st.markdown(materi_bab_2_bagian_7, unsafe_allow_html=True)
st.image("Gambar_16.png", caption="Gambar 16: Perbandingan Posisi Pengamat di Permukaan dan Pusat Bumi", use_container_width=True)

materi_bab_2_bagian_8 = r"""
bertransit di $O$ adalah $OX$. Berdasarkan definisi, jarak kutub utara bintang untuk pengamat di $O$ adalah $P\hat{O}X$. Jika $CY$ digambar sejajar dengan $OX$, maka $CY$ adalah arah bintang dengan merujuk ke $C$, pusat bumi. Dengan demikian $P_1\hat{C}Y = P\hat{O}X$; dengan kata lain jarak kutub utara bintang (dan akibatnya deklinasinya) adalah sama pada bola langit berpusat di $O$ (atau posisi lain di permukaan bumi) seperti pada bola langit berpusat di $C$. Tetapi ketika benda yang relatif dekat seperti bulan, atau matahari, atau planet diamati, definisi jarak kutub utara (dan karena itu deklinasi) yang diberikan sebelumnya bergantung pada posisi khusus pengamat di bumi. Dengan demikian jika $M$ adalah bulan (Gbr. 16) pada jarak $r$ dari pusat bumi, adalah jelas bahwa $P\hat{O}M = P_1\hat{C}M + O\hat{M}C$; juga $O\hat{M}C$ jelas bergantung pada posisi $O$, sedangkan $P_1CM$ sepenuhnya independen
"""
st.markdown(materi_bab_2_bagian_8, unsafe_allow_html=True)
st.image("Gambar_17.png", caption="Gambar 17: Bola Langit Standar atau Geosentrik Berpusat di Pusat Bumi", use_container_width=True)

materi_bab_2_bagian_9 = r"""
dari $O$. $P_1\hat{C}M$ didefinisikan sebagai jarak kutub utara $M$ yang dengan demikian merupakan sudut antara sumbu bumi dan garis lurus yang menghubungkan pusat bumi ke benda langit. Definisi ini sepenuhnya bersifat umum dan berlaku untuk setiap benda langit. Oleh karena itu, pusat bola langit standar (atau bola langit geosentrik, sebagaimana dapat disebut) diambil berada di $C$, pusat bumi (Gbr. 17). $CZ$ adalah arah zenit pengamat, diameter $QCP$ berimpit dengan sumbu bumi, $NWSE$ adalah horizon langit (lingkaran besar yang bidangnya tegak lurus terhadap $CZ$), dan $RWTE$ adalah ekuator langit (bidang yang berimpit dengan bidang ekuator bumi). busur $PX$ adalah jarak kutub utara dari benda langit sesuai dengan definisi yang baru saja diberikan dan $DX$ adalah deklinasi $\delta$ (N.P.D. $= 90^\circ - \delta$). Meridian pengamat adalah $PZRSQ$, jarak zenit dari benda langit adalah $ZX$ (dilambangkan dengan $z$) dan azimut $A$ (sudut $P\hat{Z}X$) serta sudut jam $H$ (sudut $Z\hat{P}X$) adalah seperti yang telah dideskripsikan sebelumnya. Deklinasi benda-benda langit utama (bulan, matahari, planet-planet dan bintang-bintang paling terang) ditabulasikan di dalam *Astronomical Ephemeris* (publikasi Amerika dan Inggris) dan di dalam efemeris nasional lainnya.

Hereafter, bola langit akan diasumsikan seperti pada Gbr. 17, yaitu, berpusat di $C$, pusat bumi.

### 23. Penyelesaian dari segitiga bola PZX.
Kita akan mempertimbangkan dua masalah umum yang terkait dengan segitiga $PZX$.
(i) Diberikan lintang pengamat $\phi$, deklinasi $\delta$ dan sudut jam $H$ dari benda langit, untuk menghitung jarak zenit dan azimutnya. Berdasarkan rumus **A** (rumus kosinus), karena dua sisi $PZ$ dan $PX$ serta sudut yang diapitnya $ZPX$ diberikan (Gbr. 17), kita memiliki,
$$ \cos ZX = \cos PZ \cos PX + \sin PZ \sin PX \cos ZPX, $$
atau
$$ \cos z = \sin \phi \sin \delta + \cos \phi \cos \delta \cos H \dots\dots(3). $$
Dengan demikian $z$ dapat dihitung secara langsung dari (3) atau dengan cara rumus haversine (bagian 13), yang pada kasus ini dapat ditulis
$$ \text{hav } z = \text{hav } (\phi - \delta) + \cos \phi \cos \delta \text{ hav } H \dots\dots(4). $$
Sekali lagi, dengan **A**,
$$ \cos PX = \cos PZ \cos ZX + \sin PZ \sin ZX \cos PZX, $$
atau
$$ \sin \delta = \sin \phi \cos z + \cos \phi \sin z \cos A \dots\dots(5), $$
dari mana azimut $A$ dapat dihitung. Dalam bentuk haversine (5) dapat ditulis
$$ \cos \phi \cos a \text{ hav } A = \text{hav } (90^\circ - \delta) - \text{hav } (\phi - a) \dots(6), $$
di mana $a$ adalah ketinggian (*altitude*).

(ii) Diberikan lintang pengamat $\phi$, jarak zenit bintang $z$ dan azimut $A$, untuk menghitung deklinasi bintang dan sudut jamnya. Kita diberikan $\phi, z$ dan $A$; maka, melalui (5), kita dapat menghitung deklinasi. Baik persamaan (3) maupun (4) tersedia untuk menghitung sudut jam $H$. Maka dari (3)
$$ \cos H = \cos z \sec \phi \sec \delta - \tan \phi \tan \delta \dots\dots(7). $$

Pertimbangkan sekarang segitiga bola $PZX$ pada Gbr. 13. Sudut $PZX$ adalah azimut (timur). Mengingat bahwa sudut jam diukur di kutub dari meridian pengamat ke arah barat, kita melihat bahwa $Z\hat{P}X = 24^h - H$. Penyelesaian dari segitiga tersebut berlanjut seperti sebelumnya.

### 24. Asensio rekta dan deklinasi.
Dalam metode sudut jam dan deklinasi untuk menentukan posisi sebuah bintang di bola langit hanya satu koordinat, yaitu deklinasi, yang tetap konstan saat bintang melintasi langit, sedangkan sudut jam meningkat secara seragam dari $0^h$ hingga $24^h$. Tetapi
"""
st.markdown(materi_bab_2_bagian_9, unsafe_allow_html=True)
st.image("Gambar_18.png", caption="Gambar 18: Asensio Rekta dan Deklinasi pada Bola Langit", use_container_width=True)

materi_bab_2_bagian_10 = r"""
posisi bintang-bintang di bola langit dapat diibaratkan seperti posisi titik-titik tetap di permukaan bumi dan karenanya dapat dispesifikasikan dengan merujuk pada ekuator langit dan bintang tertentu mana pun di ekuator. Sebagai contoh, pada Gbr. 18, misalkan $\Upsilon$ adalah sebuah bintang ekuatorial dan $X$ adalah bintang lain mana pun; misalkan meridian melalui $X$ memotong ekuator langit di $D$. Karena bintang-bintang melintasi langit kita tahu secara khusus bahwa deklinasi $X$, yaitu, $DX$, tetap konstan dan bahwa konfigurasi relatif dari bintang-bintang juga tetap konstan. Ini berarti bahwa $\Upsilon D$ adalah konstan; dengan kata lain, bahwa sudut antara meridian-meridian dari $\Upsilon$ dan $D$ tetap konstan. Kita dapat menganggap $\Upsilon$ sebagai titik referensi pada ekuator langit; sehubungan dengan $\Upsilon$ dan ekuator langit, kita dapat dengan jelas menentukan posisi bintang $X$ dengan menggunakan busur lingkaran besar $\Upsilon D$ dan deklinasi $DX$. Titik referensi yang dipilih dalam praktik disebut ekuinoks musim semi (*vernal equinox*) atau titik pertama Aries, dan adalah mudah untuk menganggap posisi $\Upsilon$ sebagaimana dispesifikasikan oleh sebuah bintang tertentu di langit. Nanti kita akan mendefinisikan $\Upsilon$ lebih tepat lagi. Busur $\Upsilon D$ atau $\Upsilon\hat{P}X$ disebut asensio rekta (*right ascension*, R.A.) dari bintang $X$ (dilambangkan dengan $\alpha$) dan diukur ke arah timur dari $\Upsilon$ dari $0^h$ hingga $24^h$ (dalam arah panah dekat $\Upsilon$). Arah ini berlawanan dengan arah di mana sudut jam diukur. Dari Gbr. 18, kita melihat bahwa $R\Upsilon = RD + \Upsilon D$. Sekarang $RD$ (atau $R\hat{P}X$) adalah sudut jam $H$ dari $X$ dan $R\Upsilon$ adalah sudut jam dari $\Upsilon$. Sudut jam dari $\Upsilon$ disebut waktu sideris (*sidereal time*, S.T.). Kita memiliki, sebagaimana mestinya,
$$ \text{Sid. time} = \text{H.A. } X + \text{R.A. } X \dots\dots(8), $$
atau
$$ \text{S.T.} = H + \alpha \dots\dots(9). $$
Ketika $\Upsilon$ berada pada meridian pengamat, sudut jam dari $\Upsilon$ adalah $0^h$, yang berarti, waktu sideris adalah $0^h$. Ketika $\Upsilon$ selanjutnya berada pada meridian pengamat, sebuah interval sebesar $24^h$ waktu sideris telah berlalu. Interval ini adalah, tentu saja, sama dengan yang dibutuhkan untuk rotasi penuh bumi pada porosnya dan itu disebut hari sideris (*sidereal day*). Bumi yang berputar, pada kenyataannya, adalah pencatat waktu standar.

### 25. Orbit bumi.
Bumi adalah sebuah planet yang berevolusi mengelilingi matahari dalam lintasan elips atau orbit, matahari yang berada pada fokus $S$ dari elips tersebut (Gbr. 19). Ini adalah hukum gerak planet pertama Kepler. Waktu yang dibutuhkan bumi untuk membuat sebuah revolusi penuh pada orbitnya adalah satu tahun. Seiring bergeraknya bumi dalam orbitnya, arah bumi, seperti yang dilihat dari matahari, terus berubah; akan tetapi, kecepatan sudutnya tidak seragam. Karena pengamatan kita dilakukan dari bumi, maka relatif terhadap bumi matahari tampak mendeskripsikan sebuah orbit elips mengelilingi bumi. Pada Gbr. 20, $C$ adalah pusat bumi dan elips mewakili orbit semu matahari relatif terhadap bumi. Urutan posisi-posisi dari matahari, yaitu $a, e, f, b, g$ di dalam orbit ini, sesuai dengan urutan posisi-posisi $A, E, F, B, G$ dari bumi dalam orbitnya mengelilingi matahari (Gbr. 19). Di dalam perjalanan tahun, matahari dengan demikian
"""
st.markdown(materi_bab_2_bagian_10, unsafe_allow_html=True)

st.image("Gambar_19.png", caption="Gambar 19: Orbit Bumi Mengelilingi Matahari", use_container_width=True)
st.image("Gambar_20.png", caption="Gambar 20: Orbit Semu Matahari Relatif Terhadap Bumi", use_container_width=True)

materi_bab_2_bagian_11 = r"""
tampak membuat sirkuit penuh dari langit berlatar belakangkan bintang-bintang. Bidang orbit ini disebut bidang ekliptika, dan lingkaran besar perpotongan bidang ini dengan bola langit, yang mana pusatnya adalah pusat bumi $C$, disebut ekliptika. Pada Gbr. 21, misalkan $C$ menjadi pusat bola langit di mana ekuator langit $\Upsilon TR$ dan kutub utara $P$ digambar. Kita dapat membayangkan bahwa bintang-bintang dapat dilihat dari pusat bumi, yaitu, dari $C$, dan karenanya mereka akan menempati posisi-posisi pasti pada bola langit di Gbr. 21. Merujuk pada bintang-bintang, bidang ekliptika akan memiliki posisi yang pasti dan, konsekuensinya, ekliptika akan menjadi sebuah lingkaran besar tertentu, yang ditemukan melalui pengamatan miring pada sudut sekitar $23\frac{1}{2}^\circ$ terhadap ekuator langit. Pada Gbr. 21, $\Upsilon \Upsilon M U$ mewakili ekliptika dan
"""
st.markdown(materi_bab_2_bagian_11, unsafe_allow_html=True)
st.image("Gambar_21.jpg", caption="Gambar 21: Ekliptika, Kemiringan, dan Titik Ekuinoks", use_container_width=True)

materi_bab_2_bagian_12 = r"""
kemiringannya terhadap ekuator langit adalah $M\hat{\Upsilon}R$, yang dikenal sebagai kemiringan ekliptika (*obliquity of the ecliptic*). Relatif terhadap bumi, matahari tampak bergerak di bola langit di sepanjang ekliptika—dalam arah $\Upsilon \Upsilon M$—dan dua kali setahun, di $\Upsilon$ dan di $U$, posisinya pada bola langit berimpit dengan persimpangan ekliptika dengan ekuator langit. Di antara $\Upsilon$ dan $M$ dan di antara $M$ dan $U$ matahari berada pada sisi kutub utara dari ekuator; deklinasinya saat itu utara. Demikian pula di antara $U$ dan $\Upsilon$ dan di antara $\Upsilon$ dan $\Upsilon$ deklinasinya adalah selatan. Posisi $\Upsilon$, pada mana deklinasi matahari berubah dari selatan ke utara, adalah ekuinoks musim semi (*vernal equinox*). Dengan cara inilah titik referensi $\Upsilon$, darinya asensio rekta dari bintang-bintang diukur, diperoleh. Jadi jika $X$ adalah sebuah bintang, asensio rektanya adalah $\Upsilon D$ atau $\alpha$ yang diukur sepanjang ekuator dari $\Upsilon$ ke arah timur, dan deklinasinya $\delta$ adalah $DX$. Dari diagram terlihat bahwa asensio rekta dan deklinasi matahari keduanya berubah secara terus-menerus. Ketika matahari berada di $\Upsilon$, asensio rekta dan deklinasinya keduanya nol (ini terjadi sekitar 21 Maret—ekuinoks musim semi); di $M$ asensio rektanya adalah $6^h$ dan deklinasi sekitar $23\frac{1}{2}^\circ$ U (ini terjadi sekitar 21 Juni—solstis musim panas); di $U$ asensio rektanya adalah $12^h$ dan deklinasi $0^\circ$ (ini terjadi sekitar 23 September—ekuinoks musim gugur) dan di bagian titik terendah asensio rektanya adalah $18^h$ dan deklinasi sekitar $23\frac{1}{2}^\circ$ S (ini terjadi sekitar 21 Desember—solstis musim dingin).

### 26. Lintang dan bujur langit.
Posisi sebuah benda langit dapat dirujuk ke ekliptika sebagai lingkaran besar fundamental dan ekuinoks musim semi $\Upsilon$ sebagai titik rujukan utama. Pada Gbr. 21 $K$ adalah kutub utara dari ekliptika dan $KXA$ adalah lingkaran besar yang melewati $X$ dan bertemu ekliptika di $A$. Busur $\Upsilon A$, diukur dari $\Upsilon$ ke $A$ sepanjang ekliptika dalam arah pergerakan tahunan matahari, mis. ke timur, disebut bujur (*longitude*) dari benda langit $X$ dan diukur dari $0^\circ$ hingga $360^\circ$ memutari ekliptika. Busur $AX$ adalah lintang (*latitude*) dan lintang utara dianggap positif dan selatan negatif. Jika kita mengetahui asensio rekta dan deklinasi dari bintang kita dapat memperoleh lintangnya ($\beta$) dan bujurnya ($\lambda$) dari segitiga $KPX$; dan sebaliknya. Sekarang $\Upsilon$ adalah kutub dari lingkaran besar $KPMR$; karenanya $K\hat{P}\Upsilon = 90^\circ$, dan karena $\Upsilon D = \Upsilon\hat{P}X = \alpha$, maka $K\hat{P}X = 90^\circ + \alpha$. Juga $P\hat{K}\Upsilon = 90^\circ$, dan karena $\Upsilon A = \Upsilon\hat{K}X = \lambda$, maka $P\hat{K}X = 90^\circ - \lambda$. Juga $PX = 90^\circ - \delta$ dan $KX = 90^\circ - \beta$. Misalkan $\epsilon$ menyatakan kemiringan ekliptika; ia adalah sudut di antara jari-jari $CM$ dan $CR$; jadi busur $RM = \epsilon$. Tetapi $KM = 90^\circ$ dan $PR = 90^\circ$; karenanya $KP = \epsilon$. Menerapkan rumus-rumus **A**, **B** dan **C**, kita miliki
$$ \cos KX = \cos PX \cos KP + \sin PX \sin KP \cos KPX, $$
$$ \sin KX \sin PKX = \sin PX \sin KPX, $$
$$ \sin KX \cos PKX = \cos PX \sin KP - \sin PX \cos KP \cos KPX, $$
atau
$$ \sin \beta = \sin \delta \cos \epsilon - \cos \delta \sin \epsilon \sin \alpha \dots\dots(10), $$
$$ \cos \beta \cos \lambda = \cos \delta \cos \alpha \dots\dots(11), $$
$$ \cos \beta \sin \lambda = \sin \delta \sin \epsilon + \cos \delta \cos \epsilon \sin \alpha \dots\dots(12). $$

Oleh proses yang serupa, asensio rekta $\alpha$ dan deklinasi $\delta$ dapat diekspresikan dalam bentuk $\beta, \lambda$ dan $\epsilon$. Rumus-rumusnya adalah
$$ \sin \delta = \sin \beta \cos \epsilon + \cos \beta \sin \epsilon \sin \lambda, $$
$$ \cos \delta \cos \alpha = \cos \beta \cos \lambda, $$
$$ \cos \delta \sin \alpha = - \sin \beta \sin \epsilon + \cos \beta \cos \epsilon \sin \lambda. $$

### 27. Waktu Sideris.
Misalkan bumi dan bola langit (berpusat di $C$) digambarkan seperti pada Gbr. 22; misalkan $g$ menandakan posisi Greenwich di permukaan bumi dan $l$ yaitu posisi sembarang tempat lain. Sudut di antara meridian-meridian $plq$ dan $pgq$ adalah, tentu saja, bujur (terestrial) dari $l$; pada kasus ini $l$ adalah barat dari Greenwich. Hasilkan $Cg, Cl$ untuk menemui bola langit di $G$ dan $L$. Maka $G$ dan $L$ adalah zenit dari Greenwich dan $l$ secara berturut-turut. Jika $X$ adalah posisi sebuah benda langit di bola langit pada momen yang diberikan, $G\hat{P}X$ adalah sudut jam dari $X$ untuk seorang pengamat di meridian Greenwich dan $L\hat{P}X$ adalah sudut jam untuk seorang pengamat di meridian $l$. Tetapi $G\hat{P}X = L\hat{P}X + G\hat{P}L$ dan $G\hat{P}L = g\hat{p}l$; karenanya
"""
st.markdown(materi_bab_2_bagian_12, unsafe_allow_html=True)
st.image("Gambar_22.jpg", caption="Gambar 22: Hubungan Waktu Sideris Lokal dan Bujur Terestrial", use_container_width=True)

materi_bab_2_bagian_13 = r"""
$$ \text{H.A. dari } X \text{ di Greenwich} = \text{H.A. dari } X \text{ di } l + \text{bujur (B) dari } l \dots\dots(13). $$
Di dalam rumus ini kita andaikan bahwa bujur dari $l$ diekspresikan dalam ukuran-waktu ($15^\circ = 1^h; 15' = 1^m; 15'' = 1^s$). Rumus (13) adalah yang bersifat umum dan itu jelas berlaku untuk ekuinoks musim semi $\Upsilon$. Kita lalu memperoleh—karena waktu sideris adalah sudut jam dari $\Upsilon$—
$$ \text{Sid. time di Greenwich} = \text{Sid. time di } l \pm \text{bujur dari } l \dots(14), $$
tanda $+$ diambil ketika $l$ berada di barat dari Greenwich dan tanda $-$ ketika $l$ berada di timur dari Greenwich. Waktu sideris di $l$ disebut *local sidereal time* (L.S.T.).

### 28. Waktu matahari rata-rata.
Hari sideris adalah sebuah satuan waktu observatorium dan terbukti secara jelas tidak sesuai pada pengaturan urusan sehari-hari yang mana sebagian besar dikuasai menurut posisi dari matahari di langit. Ketika matahari berada di meridian dari sebuah tempat, itu adalah tengah hari semu (*apparent noon*) di sana; ketika matahari berada selanjutnya di meridian, sebuah hari matahari semu (*apparent solar day*) dikatakan telah berlalu. Interval ini dapat diukur, sebagai contoh, dengan sarana dari sebuah jam yang menjaga waktu sideris yang akurat dan itu ditemukan bahwa suatu hari matahari semu tidaklah konstan. Kita telah melihat bahwa, relatif terhadap bumi, matahari tampak untuk mendeskripsikan sebuah orbit elips di sekeliling bumi dan kecepatan pada mana arahnya di orbit berubah bukanlah konstan. Itu mengikuti bahwa matahari tampak untuk mendeskripsikan ekliptika pada suatu laju yang tidak seragam; dengan kata lain, matahari tampak untuk bergerak dengan agak tidak beraturan berlawanan dengan latar belakang bintang-bintang. Dikarenakan hal ini dan juga karena fakta bahwa ia bergerak di dalam ekliptika dan tidak di sepanjang ekuator langit (lingkaran besar fundamental dengan mana pengukuran dari sudut jam atau waktu dihubungkan) asensio rektanya tidak meningkat secara seragam. Rata-rata hari matahari semu di sepanjang tahun disebut sebuah hari matahari rata-rata (*mean solar day*) dan adalah nyaman untuk mendefinisikan hari matahari rata-rata sebagai interval di antara dua persinggahan berturut-turut melintasi meridian pengamat dari sebuah benda fiktif yang disebut matahari rata-rata (*mean sun*). Matahari rata-rata diasumsikan untuk bergerak di ekuator langit dengan laju yang seragam mengelilingi bumi. Laju ini adalah sedemikian sehingga matahari rata-rata menyelesaikan sebuah revolusi di dalam waktu yang sama seperti halnya itu yang disyaratkan oleh matahari untuk sirkuit lengkap ekliptika. Menurut definisi ini, asensio rekta dari matahari rata-rata (dilambangkan oleh R.A.M.S.) meningkat pada laju yang seragam.

Sekarang jika kita memandang matahari rata-rata sebagai sebuah benda langit biasa, maka pada momen yang diberikan mana pun, kita dapat menganggap bahwa ia memiliki sudut jam tertentu (H.A.M.S.) pada suatu tempat yang diberikan di permukaan bumi. Pada momen ini kita akan mengasumsikan bahwa asensio rektanya diketahui; karenanya dari (8) atau (9),
$$ \text{Sid. time} = \text{H.A.M.S.} + \text{R.A.M.S.} \dots\dots(15). $$
Waktu yang ditunjukkan oleh jam waktu rata-rata, misal, di Greenwich pada momen mana pun hanyalah terhubung ke nilai dari H.A.M.S. di sana, dan jika R.A.M.S. diketahui, (15) membentuk basis dari perbandingan antara waktu sideris dan jam waktu rata-rata. Matahari rata-rata berhubungan dengan matahari sejati menurut prinsip-prinsip tertentu yang mana akan didiskusikan dalam bab yang selanjutnya. Sementara itu akan cukup untuk menyatakan bahwa perbedaan pada momen mana pun di antara asensio rekta dari matahari rata-rata dan dari matahari sejati dapat dihitung; perbedaan ini disebut perataan waktu (*equation of time*)* (dilambangkan dengan $E$). Kita dengan demikian memiliki
$$ E = \text{R.A.M.S.} - \text{R.A. } \odot \dots\dots(16), $$
*(Catatan kaki: * Dalam buku-buku teks yang lebih tua perataan waktu didefinisikan oleh $E = \text{R.A. } \odot - \text{R.A.M.S.}$, tetapi konvensi (16) yang secara umum diadopsi).*

di mana R.A. $\odot$ menunjukkan asensio rekta dari matahari sejati. $E$ dapat menjadi positif atau negatif dan bervariasi dengan cara yang rumit. Komputasi secara detail dari $E$ didiskusikan di dalam bagian 91. Pada Gbr. 23, mari kita misalkan bahwa pada keadaan yang diberikan asensio rekta dan deklinasi dari matahari ($\odot$) diketahui. Misalkan $\Upsilon$ menjadi ekuinoks musim semi pada saat ini sehingga bahwa $R\hat{P}\Upsilon$ atau $R\Upsilon$ adalah sudut jam dari $\Upsilon$, yakni, waktu sideris lokal. Jika ini diketahui, posisi dari $\Upsilon$ pada bola langit dapat secara pasti ditentukan. Posisi matahari lalu dapat diindikasikan pada bola langit. $\Upsilon K = \text{R.A. } \odot$ dan $K\odot$ adalah deklinasi matahari dan kedua hal ini
"""
st.markdown(materi_bab_2_bagian_13, unsafe_allow_html=True)
st.image("Gambar_23.jpg", caption="Gambar 23: Perataan Waktu dan Sudut Jam Matahari Rata-rata", use_container_width=True)

materi_bab_2_bagian_14 = r"""
diasumsikan diketahui. Misalkan nilai dari $E$ adalah positif; maka oleh (16), R.A.M.S. adalah lebih besar dari R.A. $\odot$, dan jika $E$ diketahui posisi matahari rata-rata $M$ pada saat ini dapat diindikasikan di dalam diagram. $R\hat{P}M$ atau $RM$ adalah sudut jam dari $M$ (H.A.M.S.). Jelas dari Gbr. 23 bahwa, karena $RK = RM + MK$, maka
$$ \text{H.A. } \odot = \text{H.A.M.S.} + E \dots\dots(17), $$
yang mana merupakan relasi penting yang menghubungkan H.A.M.S. dan H.A. $\odot$, memampukan kita untuk menghitung sudut jam matahari (H.A. $\odot$) ketika kuantitas-kuantitas lainnya diketahui. Ketika matahari rata-rata berada pada meridian pengamat, maka itu adalah *local mean noon* di sana. Ketika matahari rata-rata berada pada meridian Greenwich, itu adalah *Greenwich mean noon*. Sudut jam dari matahari rata-rata di Greenwich akan dinotasikan di buku ini oleh G.M.A.T. (*Greenwich mean astronomical time*). Ketika

matahari rata-rata ada pada $T$—H.A.M.S. berada saat itu bernilai $12^h$—ia dikatakan menjadi tengah malam rata-rata (*mean midnight*). Ketika G.M.A.T. $= 12^h$, itu adalah tengah malam rata-rata pada Greenwich dan ini adalah momen saat sebuah hari sipil baru di Greenwich dimulai. Waktu rata-rata yang diperhitungkan dari tengah malam pada Greenwich disebut *Greenwich Mean Time* (G.M.T.)*, sekarang ditunjuk sebagai *Universal Time* (U.T.). Adalah jelas bahwa
$$ \text{U.T.} \equiv \text{G.M.T.} = \text{G.M.A.T.} + 12^h \dots\dots(18). $$
Secara serupa, untuk tempat apa pun yang mempertahankan waktu rata-rata yang sesuai dengan meridiannya, kita akan memiliki
$$ \text{Local M.T.} = \text{Local M.A.T.} + 12^h \dots\dots(19) $$
$$ = \text{H.A.M.S.} \pm 12^h \dots\dots(20). $$

Rumus (14) memberikan hubungan di antara waktu sideris pada Greenwich dan waktu sideris di tempat $l$, dan ini jelas dari Gbr. 22 dan dari (18) dan (19) bahwa kita akan mempunyai suatu relasi yang mirip antara waktu rata-rata pada Greenwich dan waktu rata-rata pada tempat tersebut; hal itu adalah
$$ \text{U.T.} \equiv \text{G.M.T.} = \text{Local M.T.} \pm \text{bujur dari } l \dots\dots(21), $$
tanda $+$ yang diambil ketika bujur dari $l$ berada di barat dan tanda $-$ ketika bujur tersebut berada di timur.

Kebingungan niscaya tidak akan terelakkan jika setiap tempat menjaga *local mean time* yang tepat dengan meridiannya, dan oleh karenanya di dalam negara-negara yang kecil suatu waktu rata-rata standar dipilih, bertepatan pada suatu meridian bujur yang khusus (meridian standar), yang mana ada dalam penggunaan secara seragam di seantero negeri. Di Inggris Raya, waktu rata-rata standar tersebut adalah G.M.T. Di negara-negara yang ekstensif seperti Rusia dan Amerika Serikat, dua atau lebih waktu-waktu standar ada dalam penggunaan di dalam zona-zona bujur; di dalam setiap zona, suatu waktu standar yang sesuai untuk meridian pasti di dalam zona tersebut yang dipertahankan. Waktu standar, berdasar sebuah meridian tertentu, kita akan melambangkannya dengan waktu zona (*zone time*, Z.T.). Sistem ini, di dalam efeknya, dipertahankan oleh kapal-kapal di perairan yang mana secara general kurang terganggu oleh komplikasi-komplikasi geografis. Kita memiliki, seperti dalam (21),
$$ \text{U.T.} \equiv \text{G.M.T.} = \text{Z.T.} \pm \text{bujur dari meridian standar} \dots(22). $$

*(Catatan kaki: * Sebelum 1925, G.M.T. digunakan di dalam almanak untuk menandakan *Greenwich mean astronomical time* (G.M.A.T.). Mulai 1925, waktu yang digunakan adalah G.M.T. ($\equiv$ G.C.T.) lalu digantikan, seperti halnya disinggung di atas, oleh U.T. Baru-baru ini, untuk berbagai alasan yang dicantumkan dalam Apendiks E (hlm. 424), U.T. telah diganti di dalam almanak oleh Ephemeris Time (E.T.). Perbedaan di antara U.T. dan E.T. sangatlah sedikit hingga kita akan menggunakan yang terdahulu secara umumnya, terkecuali kalau dinyatakan sebaliknya).*
"""
st.markdown(materi_bab_2_bagian_14, unsafe_allow_html=True)
