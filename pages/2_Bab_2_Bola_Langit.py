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
    - [22. Bola Langit Geosentrik](#22-bola-langit-standar-atau-geosentrik)
    - [23. Penyelesaian Segitiga PZX](#23-penyelesaian-segitiga-bola-pzx)
    - [24. Asensio Rekta dan Deklinasi](#24-asensio-rekta-dan-deklinasi)
    - [25. Orbit Bumi](#25-orbit-bumi)
    - [26. Lintang dan Bujur Langit](#26-lintang-dan-bujur-langit)
    - [27. Waktu Sideris](#27-waktu-sideris)
    - [28. Waktu Matahari Rata-rata](#28-waktu-matahari-rata-rata)
    """)

# ==========================================
# KONTEN UTAMA BAB II (BAGIAN 1 - 9 SEBELUMNYA)
# ==========================================
materi_bab_2_bagian_1 = r"""
### 17. Pendahuluan.
Dalam Bab I kita telah melihat bahwa posisi di permukaan bumi ditentukan sepenuhnya dengan merujuk pada dua lingkaran besar utama, yaitu meridian Greenwich dan ekuator. Prinsip penentuan posisi pada bola langit pada dasarnya serupa, dan terdapat beberapa metode tergantung pada lingkaran besar khusus yang dipilih sebagai lingkaran utama. Metode-metode ini sekarang akan diuraikan.

### 18. Ketinggian (*altitude*) dan azimut.
Misalkan $O$—pengamat di permukaan bumi (yang dianggap berbentuk bola)—menjadi pusat bola langit (Gbr. 10). Misalkan $Z$ (*zenit*) menjadi titik pada bola langit yang berada tepat di atas kepala—arahnya dapat didefinisikan dengan menggunakan unting-unting (*plumb-line*). Oleh karena itu, $OZ$ adalah kelanjutan dari garis lurus yang menghubungkan pusat bumi ke $O$. Bidang yang melalui $O$ yang tegak lurus terhadap $OZ$ adalah bidang horizon, yang memotong bola langit pada lingkaran besar $NAS$, yang disebut horizon astronomis atau sekadar horizon. 
"""
st.markdown(materi_bab_2_bagian_1, unsafe_allow_html=True)
st.image("Gambar_10.png", caption="Gambar 10", use_container_width=True)

materi_bab_2_bagian_2 = r"""
Dengan demikian, pada Gbr. 10, horizon membagi bola langit menjadi dua belahan bola (*hemisphere*), di mana bagian atas adalah belahan bola yang terlihat (*visible hemisphere*), dan bagian bawah tersembunyi dari pengamat oleh bumi. Misalkan $X$ menjadi posisi sebuah bintang di bola langit pada saat tertentu. Setiap lingkaran besar yang ditarik melalui $Z$ disebut lingkaran vertikal (*vertical circle*); khususnya, lingkaran vertikal pada Gbr. 10 yang melalui $X$ adalah $ZXA$. Pada bidang $ZXA$, sudut $AOX$ atau busur lingkaran besar $AX$ disebut ketinggian (*altitude*), yang akan dilambangkan dengan $a$. Karena $OZ$ tegak lurus terhadap bidang horizon, lingkaran besar busur $ZA$ adalah $90^\circ$; oleh karena itu $ZX = 90^\circ - a$. $ZX$ disebut jarak zenit (*zenith distance*, disingkat z.d.) dari bintang $X$ dan akan dilambangkan dengan $z$. Dengan demikian
$$ z = 90^\circ - a \dots\dots(1). $$

Misalkan $LXM$ menjadi lingkaran kecil melalui $X$ yang sejajar dengan horizon; lingkaran ini disebut paralel ketinggian (*parallel of altitude*). Untuk mendefinisikan posisinya secara lengkap pada bola langit, lingkaran vertikal khusus tempat bintang itu berada juga harus ditentukan. Hal ini dilakukan sebagai berikut.

Misalkan $OP$ sejajar dengan sumbu tempat bumi berputar. Jika lintang pengamat adalah utara (seperti pada Gbr. 10), posisi $P$ disebut kutub langit utara (*north celestial pole*), atau sekadar kutub utara. Bintang ini adalah Polaris, atau bintang kutub utara, yang arahnya di langit hampir persis sama dengan arah yang diberikan oleh $OP$. Kita mendefinisikan lingkaran vertikal melalui $P$, yaitu $ZPN$ (yang memotong horizon di $N$), sebagai lingkaran vertikal utama (*principal vertical circle*) dan titik $N$ sebagai titik utara horizon.

Titik $S$ pada horizon yang tepat berlawanan dengan $N$ adalah titik selatan (*south point*); titik barat ($W$) dan timur ($E$) memiliki arah yang tegak lurus terhadap arah $N$ dan $S$ ($E$ tidak ditunjukkan pada Gbr. 10). Titik-titik $N, E, S$ dan $W$ disebut titik-titik kardinal (*cardinal points*).

Kita sekarang menentukan posisi sebuah bintang $X$ pada bola langit pada saat tertentu dengan merujuk pada horizon dan lingkaran vertikal utama $ZPN$. Jika bintang berada di bagian barat bola langit (seperti pada Gbr. 10), sudut bola $PZX$ (yang dibentuk oleh lingkaran vertikal utama dan lingkaran vertikal melalui $X$) atau busur lingkaran besar $NA$ disebut azimut ($W$). Jika bintang berada di bagian timur bola langit, seperti pada Gbr. 11, sudut $PZX$ atau busur $NB$ adalah azimut ($E$).
"""
st.markdown(materi_bab_2_bagian_2, unsafe_allow_html=True)
st.image("Gambar_11.png", caption="Gambar 11", use_container_width=True)

materi_bab_2_bagian_3 = r"""
Dengan demikian pada saat apa pun posisi benda langit pada bola langit dapat dideskripsikan sepenuhnya dengan merujuk pada horizon dan titik utara horizon dalam hal ketinggian dan azimut ($E$ atau $W$) atau, sebagai alternatif, dalam hal jarak zenit dan azimut. Ketika azimut adalah $90^\circ$ $E$ atau $90^\circ$ $W$, bintang tersebut dikatakan berada pada vertikal utama (*prime vertical*), yang dengan demikian merupakan lingkaran vertikal melalui titik timur $E$ atau titik barat $W$.

Karena pada Gbr. 10 dan 11 sudut $POZ$ (atau lingkaran besar busur $PZ$) ekivalen dengan sudut antara jari-jari bumi yang melewati posisi pengamat dan sumbu bumi, maka $P\hat{O}Z$ (atau $PZ$) sama dengan kolintang pengamat atau
$$ PZ = 90^\circ - \phi \dots\dots(2), $$
di mana $\phi$ adalah lintang pengamat. Selain itu $PN = 90^\circ - PZ = \phi$; maka ketinggian kutub sama dengan lintang pengamat.

### 19. Deklinasi dan sudut jam (*declination and hour angle*).
Seperti pada bagian sebelumnya, misalkan bola langit digambarkan untuk seorang pengamat $O$ pada lintang $\phi$, yang menunjukkan horizon, zenit $Z$ dan kutub utara $P$ (Gbr. 12). Lingkaran besar $RWT$ yang bidangnya tegak lurus terhadap $OP$ adalah ekuator langit (*celestial equator*). Ekuator langit dan horizon berpotongan di dua titik $W$ dan $E$. 
"""
st.markdown(materi_bab_2_bagian_3, unsafe_allow_html=True)
st.image("Gambar_12.png", caption="Gambar 12", use_container_width=True)

materi_bab_2_bagian_4 = r"""
Seperti yang telah disebutkan, rotasi bumi menghasilkan rotasi semu bola langit dari timur ke barat mengelilingi $OP$. Misalkan $PXDQ$ adalah semi-lingkaran besar melalui $X$ dan kutub-kutub bola langit. Maka busur $DX$ disebut deklinasi bintang dan merupakan deklinasi utara jika bintang berada di antara ekuator langit dan kutub utara $P$ (seperti untuk bintang $X$). Deklinasi bintang adalah selatan (seperti untuk $Y$) ketika ia berada di antara ekuator langit dan kutub selatan $Q$. 

Deklinasi dengan demikian analog dengan lintang yang didefinisikan untuk titik-titik di permukaan bumi. Nyatakan deklinasi $X$ dengan $\delta$; maka $DX = \delta$ dan $PX = 90^\circ - \delta$. $PX$ disebut jarak kutub utara (*north polar distance*, N.P.D.) dari bintang. 

Untuk memperbaiki posisinya pada bola langit pada saat tertentu, kita memerlukan lingkaran besar referensi lainnya. Ini adalah semi-lingkaran besar $PZRSQ$, yang disebut meridian pengamat (*observer's meridian*). Pada saat apa pun posisi bintang pada paralel deklinasi ditentukan oleh sudut di $P$ antara meridian pengamat dan meridian ($PXQ$) melalui bintang pada saat itu; sudut ini adalah $RPX$ atau $ZPX$ atau busur $RD$ pada ekuator. Sudut ini, yang dilambangkan dengan $H$, disebut sudut jam (*hour angle*) dan diukur dari meridian pengamat ke arah barat dari $0^\circ$ (di $L$) hingga $360^\circ$ atau dari $0^h$ hingga $24^h$. 
"""
st.markdown(materi_bab_2_bagian_4, unsafe_allow_html=True)
st.image("Gambar_13.png", caption="Gambar 13", use_container_width=True)

materi_bab_2_bagian_5 = r"""
Kita dengan demikian memiliki aturan:
*Jika azimut bintang adalah barat, sudut jam berada di antara $0^h$ dan $12^h$ (dan sebaliknya); jika azimut bintang adalah timur, sudut jam berada di antara $12^h$ dan $24^h$.*

### 20. Diagram untuk belahan bumi selatan.
Diagram yang dijelaskan sejauh ini dalam bab ini merujuk pada bola langit untuk pengamat di lintang utara. Kita sekarang akan mendeskripsikan diagram yang bersesuaian untuk pengamat di belahan bumi selatan. Pada Gbr. 14, kita akan menempatkan zenit pengamat seperti pada diagram sebelumnya. Di belahan bumi selatan, kutub langit selatan $Q$ berada di atas horizon. 
"""
st.markdown(materi_bab_2_bagian_5, unsafe_allow_html=True)
st.image("Gambar_14.png", caption="Gambar 14", use_container_width=True)

materi_bab_2_bagian_6 = r"""
### 21. Bintang sirkumpolar (*circumpolar stars*).
Pertimbangkan bola langit untuk pengamat di lintang utara $\phi$ (Gbr. 15). Paralel deklinasi digambarkan untuk dua bintang $X$ dan $Y$, yang keduanya selalu berada di atas horizon dan akibatnya tidak terbenam. Bintang-bintang seperti itu disebut sirkumpolar bintang. 
"""
st.markdown(materi_bab_2_bagian_6, unsafe_allow_html=True)
st.image("Gambar_15.png", caption="Gambar 15", use_container_width=True)

materi_bab_2_bagian_7 = r"""
### 22. Bola langit standar atau geosentrik (*The standard or geocentric celestial sphere*).
Dalam bagian-bagian sebelumnya, deklinasi bintang pada bola langit yang pusatnya adalah pengamat telah didefinisikan. Karena bintang-bintang berada pada jarak yang hampir tak terhingga besarnya dibandingkan dengan dimensi bumi, deklinasi atau jarak kutub bintang yang didefinisikan dengan cara ini tidak bergantung pada posisi pengamat di permukaan bumi (Gbr. 16).
"""
st.markdown(materi_bab_2_bagian_7, unsafe_allow_html=True)
st.image("Gambar_16.png", caption="Gambar 16", use_container_width=True)

materi_bab_2_bagian_8 = r"""
Definisi ini sepenuhnya bersifat umum dan berlaku untuk setiap benda langit. Oleh karena itu, pusat bola langit standar (atau bola langit geosentrik, sebagaimana dapat disebut) diambil berada di $C$, pusat bumi (Gbr. 17). 
"""
st.markdown(materi_bab_2_bagian_8, unsafe_allow_html=True)
st.image("Gambar_17.png", caption="Gambar 17", use_container_width=True)


# ==========================================
# KONTEN UTAMA BAB II (BAGIAN 10 - LANJUTAN BARU)
# ==========================================
materi_bab_2_bagian_10 = r"""
busur $PX$ adalah jarak kutub utara dari benda langit sesuai dengan definisi yang baru saja diberikan dan $DX$ adalah deklinasi $\delta$ (N.P.D. $= 90^\circ - \delta$). Meridian pengamat adalah $PZRSQ$, jarak zenit dari benda langit adalah $ZX$ (dilambangkan dengan $z$) dan azimut $A$ (sudut $P\hat{Z}X$) serta sudut jam $H$ (sudut $Z\hat{P}X$) adalah seperti yang telah dideskripsikan sebelumnya. Deklinasi benda-benda langit utama (bulan, matahari, planet-planet, dan bintang-bintang paling terang) ditabulasikan di dalam *Astronomical Ephemeris* (publikasi Amerika dan Inggris) dan di dalam efemeris nasional lainnya.

Mulai dari sini, bola langit akan diasumsikan seperti pada Gbr. 17, yaitu, berpusat di $C$, pusat bumi.

### 23. Penyelesaian segitiga bola PZX.
Kita akan mempertimbangkan dua masalah umum yang terkait dengan segitiga $PZX$.
(i) Diberikan lintang pengamat $\phi$, deklinasi $\delta$ dan sudut jam $H$ dari benda langit, untuk menghitung jarak zenit dan azimutnya. Berdasarkan rumus **A** (rumus kosinus), karena dua sisi $PZ$ dan $PX$ serta sudut yang diapitnya $ZPX$ diketahui (Gbr. 17), kita peroleh:
$$ \cos ZX = \cos PZ \cos PX + \sin PZ \sin PX \cos ZPX, $$
atau
$$ \cos z = \sin \phi \sin \delta + \cos \phi \cos \delta \cos H \dots\dots(3). $$
Dengan demikian $z$ dapat dihitung secara langsung dari (3) atau melalui rumus haversine (bagian 13), yang pada kasus ini dapat ditulis:
$$ \text{hav } z = \text{hav } (\phi - \delta) + \cos \phi \cos \delta \text{ hav } H \dots\dots(4). $$
Sekali lagi, berdasarkan **A**,
$$ \cos PX = \cos PZ \cos ZX + \sin PZ \sin ZX \cos PZX, $$
atau
$$ \sin \delta = \sin \phi \cos z + \cos \phi \sin z \cos A \dots\dots(5), $$
dari mana azimut $A$ dapat dihitung. Dalam bentuk haversine, persamaan (5) dapat ditulis:
$$ \cos \phi \cos a \text{ hav } A = \text{hav } (90^\circ - \delta) - \text{hav } (\phi - a) \dots\dots(6), $$
di mana $a$ adalah ketinggian (*altitude*).

(ii) Diberikan lintang pengamat $\phi$, jarak zenit bintang $z$, dan azimut $A$, untuk menghitung deklinasi bintang dan sudut jamnya. Kita diberikan $\phi, z$ dan $A$; maka, berdasarkan (5), kita dapat menghitung deklinasi. Baik persamaan (3) maupun (4) tersedia untuk menghitung sudut jam $H$. Maka dari (3):
$$ \cos H = \cos z \sec \phi \sec \delta - \tan \phi \tan \delta \dots\dots(7). $$

Pertimbangkan sekarang segitiga bola $PZX$ pada Gbr. 13. Sudut $PZX$ adalah azimut (timur). Mengingat bahwa sudut jam diukur di kutub dari meridian pengamat ke arah barat, kita melihat bahwa $Z\hat{P}X = 24^h - H$. Penyelesaian segitiga ini dilanjutkan seperti sebelumnya.

### 24. Asensio rekta dan deklinasi.
Dalam metode penentuan posisi bintang pada bola langit menggunakan sudut jam dan deklinasi, hanya satu koordinat, yaitu deklinasi, yang tetap konstan saat bintang melintasi langit, sedangkan sudut jam meningkat secara seragam dari $0^h$ hingga $24^h$. Tetapi 
"""
st.markdown(materi_bab_2_bagian_10, unsafe_allow_html=True)
st.image("Gambar_18.png", caption="Gambar 18", use_container_width=True)

materi_bab_2_bagian_11 = r"""
posisi bintang-bintang di bola langit dapat diibaratkan seperti posisi titik-titik tetap di permukaan bumi dan karenanya dapat dispesifikasikan dengan merujuk pada ekuator langit dan bintang tertentu mana pun di ekuator. Sebagai contoh, pada Gbr. 18, misalkan $\Upsilon$ adalah sebuah bintang ekuatorial dan $X$ adalah bintang lain mana pun; misalkan meridian melalui $X$ memotong ekuator langit di $D$. Karena bintang-bintang melintasi langit, kita tahu secara khusus bahwa deklinasi $X$, yaitu $DX$, tetap konstan dan bahwa konfigurasi relatif bintang-bintang juga tetap konstan. Hal ini berarti bahwa $\Upsilon D$ konstan; dengan kata lain, sudut antara meridian $\Upsilon$ dan $D$ tetap konstan. Kita dapat menganggap $\Upsilon$ sebagai titik referensi pada ekuator langit; terhadap $\Upsilon$ dan ekuator langit, kita dapat dengan jelas menypesifikasikan posisi bintang $X$ menggunakan busur lingkaran besar $\Upsilon D$ dan deklinasi $DX$. 

Titik referensi yang dipilih dalam praktik disebut ekuinoks musim semi (*vernal equinox*) atau titik pertama Aries, dan adalah nyaman untuk menganggap posisi $\Upsilon$ sebagaimana dispesifikasikan oleh sebuah bintang tertentu di langit. Nanti kita akan mendefinisikan $\Upsilon$ dengan lebih presisi. Busur $\Upsilon D$ atau sudut $\Upsilon\hat{P}X$ disebut asensio rekta (*right ascension*, R.A.) dari bintang $X$ (dilambangkan dengan $\alpha$) dan diukur ke arah timur dari $\Upsilon$ dari $0^h$ hingga $24^h$ (sesuai arah panah di dekat $\Upsilon$). Arah ini berlawanan dengan arah pengukuran sudut jam. 

Dari Gbr. 18, kita melihat bahwa $R\Upsilon = RD + \Upsilon D$. Sekarang $RD$ (atau $R\hat{P}X$) adalah sudut jam $H$ dari $X$ dan $R\Upsilon$ adalah sudut jam dari $\Upsilon$. Sudut jam dari $\Upsilon$ disebut waktu sideris (*sidereal time*, S.T.). Oleh karena itu, kita peroleh:
$$ \text{Sid. time} = \text{H.A. } X + \text{R.A. } X \dots\dots(8), $$
atau
$$ \text{S.T.} = H + \alpha \dots\dots(9). $$

Ketika $\Upsilon$ berada pada meridian pengamat, sudut jam dari $\Upsilon$ adalah $0^h$, yang berarti waktu sideris adalah $0^h$. Ketika $\Upsilon$ berada pada meridian pengamat lagi, sebuah interval waktu sideris sebesar $24^h$ telah berlalu. Interval ini, tentu saja, sama dengan waktu yang dibutuhkan bumi untuk melakukan rotasi penuh mengelilingi porosnya, dan disebut hari sideris (*sidereal day*). Bumi yang berputar, pada kenyataannya, adalah penjaga-waktu (*time-keeper*) standar.

### 25. Orbit bumi.
Bumi adalah sebuah planet yang berevolusi mengelilingi matahari dalam lintasan elips atau orbit, di mana matahari terletak pada salah satu fokus $S$ dari elips tersebut (Gbr. 19). Ini adalah hukum pertama Kepler mengenai gerak planet. Waktu yang dibutuhkan bumi untuk melakukan satu revolusi penuh pada orbitnya adalah satu tahun. Seiring bergeraknya bumi dalam orbitnya, arah bumi, jika dilihat dari matahari, terus berubah; namun kecepatan sudutnya tidak seragam. Karena pengamatan kita dilakukan dari bumi, maka secara relatif matahari tampak mendeskripsikan sebuah orbit elips mengelilingi bumi. 

Pada Gbr. 20, $C$ adalah pusat bumi dan elips mewakili orbit semu matahari relatif terhadap bumi. Urutan posisi matahari, yaitu $a, e, f, b, g$ dalam orbit ini, bersesuaian dengan urutan posisi bumi $A, E, F, B, G$ dalam orbitnya mengelilingi matahari (Gbr. 19). Sepanjang tahun, matahari dengan demikian 
"""
st.markdown(materi_bab_2_bagian_11, unsafe_allow_html=True)
st.image("Gambar_19_20.png", caption="Gambar 19 & 20", use_container_width=True)

materi_bab_2_bagian_12 = r"""
tampak melakukan sirkuit penuh melintasi langit dengan latar belakang bintang-bintang. Bidang dari orbit ini disebut bidang ekliptika, dan lingkaran besar perpotongan antara bidang ini dan bola langit, yang pusatnya adalah $C$ (pusat bumi), disebut ekliptika. 

Pada Gbr. 21, misalkan $C$ menjadi pusat bola langit tempat ekuator langit $\Upsilon TR$ dan kutub utara $P$ digambar. Kita dapat membayangkan bahwa bintang-bintang dapat dilihat dari pusat bumi, yaitu dari $C$, dan karenanya mereka akan menempati posisi-posisi pasti pada bola langit di Gbr. 21. Terhadap bintang-bintang, bidang ekliptika akan memiliki posisi yang tetap dan, akibatnya, ekliptika akan menjadi sebuah lingkaran besar tertentu, yang melalui pengamatan ditemukan miring dengan sudut sekitar $23\frac{1}{2}^\circ$ terhadap ekuator langit. 
"""
st.markdown(materi_bab_2_bagian_12, unsafe_allow_html=True)
st.image("Gambar_21.jpg", caption="Gambar 21", use_container_width=True)

materi_bab_2_bagian_13 = r"""
Pada Gbr. 21, $\Upsilon \Upsilon M U$ mewakili ekliptika dan kemiringannya terhadap ekuator langit adalah sudut $M\hat{\Upsilon}R$, yang dikenal sebagai kemiringan ekliptika (*obliquity of the ecliptic*). Relatif terhadap bumi, matahari tampak bergerak di bola langit di sepanjang ekliptika—ke arah $\Upsilon \Upsilon M$—dan dua kali setahun, di $\Upsilon$ dan di $U$, posisinya di bola langit berimpit dengan titik perpotongan ekliptika dan ekuator langit. Di antara $\Upsilon$ dan $M$ serta antara $M$ dan $U$ matahari berada di sisi kutub utara ekuator; deklinasinya saat itu adalah utara. Demikian pula di antara $U$ dan $\Upsilon$ serta antara $\Upsilon$ dan $\Upsilon$ (kembali), deklinasinya adalah selatan. 

Posisi $\Upsilon$, saat di mana deklinasi matahari berubah dari selatan ke utara, adalah ekuinoks musim semi (*vernal equinox*). Dengan cara inilah titik referensi $\Upsilon$, dari mana asensio rekta bintang-bintang diukur, diperoleh. Jadi jika $X$ adalah sebuah bintang, asensio rektanya adalah busur $\Upsilon D$ atau $\alpha$ yang diukur sepanjang ekuator dari $\Upsilon$ ke arah timur, dan deklinasinya $\delta$ adalah $DX$. Dari diagram terlihat bahwa asensio rekta dan deklinasi matahari keduanya terus berubah secara kontinu. Ketika matahari berada di $\Upsilon$, asensio rekta dan deklinasinya keduanya nol (ini terjadi sekitar 21 Maret—ekuinoks musim semi); di $M$ asensio rektanya adalah $6^h$ dan deklinasinya sekitar $23\frac{1}{2}^\circ$ U (ini terjadi sekitar 21 Juni—solstis musim panas); di $U$ asensio rektanya adalah $12^h$ dan deklinasinya $0^\circ$ (ini terjadi sekitar 23 September—ekuinoks musim gugur) dan di bagian titik ekuator terendah asensio rektanya adalah $18^h$ dan deklinasinya sekitar $23\frac{1}{2}^\circ$ S (ini terjadi sekitar 21 Desember—solstis musim dingin).

### 26. Lintang dan bujur langit.
Posisi suatu benda langit dapat dirujuk pada ekliptika sebagai lingkaran besar fundamental dan ekuinoks musim semi $\Upsilon$ sebagai titik referensi utama. Pada Gbr. 21, $K$ adalah kutub utara ekliptika dan $KXA$ adalah sebuah lingkaran besar yang melewati $X$ dan bertemu ekliptika di $A$. Busur $\Upsilon A$, yang diukur dari $\Upsilon$ ke $A$ di sepanjang ekliptika ke arah pergerakan tahunan matahari, yaitu ke timur, disebut bujur (*longitude*) benda langit $X$ (dilambangkan $\lambda$) dan diukur dari $0^\circ$ hingga $360^\circ$ memutari ekliptika. Busur $AX$ adalah lintang (*latitude*, $\beta$) di mana lintang utara dianggap positif dan lintang selatan negatif. 

Jika kita mengetahui asensio rekta dan deklinasi bintang, kita dapat memperoleh lintangnya ($\beta$) dan bujurnya ($\lambda$) dari segitiga $KPX$; dan sebaliknya. Sekarang $\Upsilon$ adalah kutub dari lingkaran besar $KPMR$; oleh karena itu sudut $K\hat{P}\Upsilon = 90^\circ$, dan karena $\Upsilon D = \Upsilon\hat{P}X = \alpha$, maka sudut $K\hat{P}X = 90^\circ + \alpha$. Juga sudut $P\hat{K}\Upsilon = 90^\circ$, dan karena $\Upsilon A = \Upsilon\hat{K}X = \lambda$, maka sudut $P\hat{K}X = 90^\circ - \lambda$. Juga $PX = 90^\circ - \delta$ dan $KX = 90^\circ - \beta$. 

Misalkan $\epsilon$ menyatakan kemiringan ekliptika; ini adalah sudut antara jari-jari $CM$ dan $CR$; jadi busur $RM = \epsilon$. Tetapi $KM = 90^\circ$ dan $PR = 90^\circ$; oleh karena itu $KP = \epsilon$. Dengan menerapkan rumus **A**, **B** dan **C**, kita memperoleh:
$$ \cos KX = \cos PX \cos KP + \sin PX \sin KP \cos KPX, $$
$$ \sin KX \sin PKX = \sin PX \sin KPX, $$
$$ \sin KX \cos PKX = \cos PX \sin KP - \sin PX \cos KP \cos KPX, $$
atau, dengan menyubstitusikan nilai-nilainya:
$$ \sin \beta = \sin \delta \cos \epsilon - \cos \delta \sin \epsilon \sin \alpha \dots\dots(10), $$
$$ \cos \beta \cos \lambda = \cos \delta \cos \alpha \dots\dots(11), $$
$$ \cos \beta \sin \lambda = \sin \delta \sin \epsilon + \cos \delta \cos \epsilon \sin \alpha \dots\dots(12). $$

Melalui proses serupa, asensio rekta $\alpha$ dan deklinasi $\delta$ dapat diekspresikan dalam bentuk $\beta, \lambda$ dan $\epsilon$. Rumus-rumusnya adalah:
$$ \sin \delta = \sin \beta \cos \epsilon + \cos \beta \sin \epsilon \sin \lambda, $$
$$ \cos \delta \cos \alpha = \cos \beta \cos \lambda, $$
$$ \cos \delta \sin \alpha = -\sin \beta \sin \epsilon + \cos \beta \cos \epsilon \sin \lambda. $$

### 27. Waktu sideris.
Misalkan bumi dan bola langit (berpusat di $C$) digambar seperti pada Gbr. 22; misalkan $g$ menyatakan posisi Greenwich di permukaan bumi dan $l$ menyatakan posisi tempat lain. Sudut antara meridian $plq$ dan $pgq$ adalah, tentu saja, bujur (terestrial) dari $l$; dalam contoh ini $l$ berada di barat Greenwich. Perpanjang $Cg, Cl$ untuk bertemu bola langit di $G$ dan $L$. Maka $G$ dan $L$ adalah zenit dari Greenwich dan $l$ secara berturut-turut. Jika $X$ adalah posisi sebuah benda langit di bola langit pada saat tertentu, sudut $G\hat{P}X$ adalah sudut jam dari $X$ untuk pengamat di meridian Greenwich dan sudut $L\hat{P}X$ adalah sudut jam untuk pengamat di meridian $l$. Tetapi $G\hat{P}X = L\hat{P}X + G\hat{P}L$ dan $G\hat{P}L = g\hat{p}l$; dengan demikian
$$ \text{H.A. dari } X \text{ di Greenwich} = \text{H.A. dari } X \text{ di } l + \text{bujur (B) dari } l \dots\dots(13). $$
"""
st.markdown(materi_bab_2_bagian_13, unsafe_allow_html=True)
st.image("Gambar_22.jpg", caption="Gambar 22", use_container_width=True)

materi_bab_2_bagian_14 = r"""
Dalam rumus ini kita mengasumsikan bahwa bujur dari $l$ diekspresikan dalam ukuran-waktu ($15^\circ = 1^h; 15' = 1^m; 15'' = 1^s$). Rumus (13) bersifat umum dan jelas berlaku untuk ekuinoks musim semi $\Upsilon$. Dengan demikian kita memperoleh—karena waktu sideris adalah sudut jam dari $\Upsilon$—
$$ \text{Sid. time di Greenwich} = \text{Sid. time di } l \pm \text{bujur dari } l \dots\dots(14), $$
tanda $+$ diambil ketika $l$ berada di barat Greenwich dan tanda $-$ ketika $l$ berada di timur Greenwich. Waktu sideris di $l$ disebut *local sidereal time* (L.S.T.).

### 28. Waktu matahari rata-rata (*Mean solar time*).
Hari sideris adalah unit waktu observatorium dan jelas tidak cocok untuk mengatur urusan sehari-hari yang pada dasarnya diatur berdasarkan posisi matahari di langit. Ketika matahari berada di meridian suatu tempat, saat itu dinamakan tengah hari semu (*apparent noon*) di sana; ketika matahari berada di meridian itu lagi, satu hari matahari semu (*apparent solar day*) dikatakan telah berlalu. Interval ini dapat diukur, misalnya, dengan jam yang menjaga waktu sideris dengan akurat dan ditemukan bahwa hari matahari semu *tidak konstan*. Kita telah melihat bahwa, relatif terhadap bumi, matahari tampak mendeskripsikan orbit elips mengelilingi bumi dan laju perubahan arahnya di orbit tidaklah konstan. Akibatnya matahari tampak mendeskripsikan ekliptika dengan laju yang tidak seragam; dengan kata lain, matahari tampak bergerak sedikit tidak beraturan dengan latar belakang bintang-bintang. Karena hal ini, dan juga fakta bahwa ia bergerak di ekliptika dan *bukan* di sepanjang ekuator langit (lingkaran besar fundamental yang dikaitkan dengan pengukuran sudut jam atau waktu), asensio rektanya tidak meningkat secara seragam. 

Rata-rata hari matahari semu sepanjang tahun disebut hari matahari rata-rata (*mean solar day*) dan adalah nyaman untuk mendefinisikan hari matahari rata-rata sebagai interval antara dua persinggahan berturut-turut melintasi meridian pengamat oleh sebuah benda fiktif yang disebut matahari rata-rata (*mean sun*). Matahari rata-rata diasumsikan bergerak pada ekuator langit dengan laju seragam mengelilingi bumi. Laju ini sedemikian rupa sehingga matahari rata-rata menyelesaikan revolusinya pada waktu yang sama dengan yang dibutuhkan matahari sejati (*true sun*) untuk menyelesaikan sirkuit penuh ekliptika. Menurut definisi ini, asensio rekta matahari rata-rata (dilambangkan oleh R.A.M.S.) meningkat dengan laju seragam.

Sekarang jika kita menganggap matahari rata-rata sebagai benda langit biasa, maka pada saat tertentu, kita dapat mengasumsikan ia memiliki sudut jam tertentu (H.A.M.S.) pada tempat tertentu di permukaan bumi. Pada saat ini kita akan berasumsi asensio rektanya diketahui; maka dari (8) atau (9),
$$ \text{Sid. time} = \text{H.A.M.S.} + \text{R.A.M.S.} \dots\dots(15). $$
Waktu yang ditunjukkan oleh jam waktu rata-rata, katakanlah di Greenwich pada saat tertentu, secara sederhana terkait dengan nilai H.A.M.S. di sana, dan jika R.A.M.S. diketahui, persamaan (15) membentuk dasar perbandingan antara waktu sideris dan jam waktu rata-rata. Matahari rata-rata berhubungan dengan matahari sejati berdasarkan prinsip-prinsip tertentu yang akan dibahas pada bab selanjutnya. Sementara itu, cukuplah untuk menyatakan bahwa perbedaan pada saat kapan pun antara asensio rekta matahari rata-rata dan matahari sejati dapat dihitung; perbedaan ini disebut perataan waktu (*equation of time*, dilambangkan dengan $E$). Maka kita peroleh
$$ E = \text{R.A.M.S.} - \text{R.A. } \odot \dots\dots(16), $$
*(Catatan: Dalam buku teks lama, perataan waktu didefinisikan sebagai $E = \text{R.A. } \odot - \text{R.A.M.S.}$, tetapi konvensi (16) sekarang secara umum yang diadopsi).*
"""
st.markdown(materi_bab_2_bagian_14, unsafe_allow_html=True)
st.image("Gambar_23.jpg", caption="Gambar 23", use_container_width=True)

materi_bab_2_bagian_15 = r"""
di mana R.A. $\odot$ melambangkan asensio rekta matahari sejati. $E$ dapat bernilai positif atau negatif dan bervariasi dengan cara yang rumit. Komputasi mendetail dari $E$ dibahas dalam bagian 91. 

Pada Gbr. 23, mari kita asumsikan bahwa pada saat tertentu asensio rekta dan deklinasi matahari ($\odot$) diketahui. Misalkan $\Upsilon$ adalah ekuinoks musim semi saat ini sehingga busur $R\hat{P}\Upsilon$ atau $R\Upsilon$ adalah sudut jam dari $\Upsilon$, yaitu waktu sideris lokal. Jika ini diketahui, posisi $\Upsilon$ pada bola langit dapat ditentukan secara pasti. Posisi matahari kemudian dapat ditunjukkan pada bola langit. $\Upsilon K = \text{R.A. } \odot$ dan $K\odot$ adalah deklinasi matahari dan keduanya diasumsikan diketahui. Asumsikan nilai $E$ positif; maka dari (16), R.A.M.S. lebih besar dari R.A. $\odot$, dan jika $E$ diketahui, posisi matahari rata-rata $M$ saat ini dapat diindikasikan di diagram. $R\hat{P}M$ atau $RM$ adalah sudut jam dari $M$ (H.A.M.S.). Jelas dari Gbr. 23 bahwa, karena $RK = RM + MK$, maka
$$ \text{H.A. } \odot = \text{H.A.M.S.} + E \dots\dots(17), $$
yang mana merupakan hubungan penting yang menghubungkan H.A.M.S. dan H.A. $\odot$, memungkinkan kita untuk menghitung sudut jam matahari sejati jika kuantitas-kuantitas yang lain diketahui. 

Ketika matahari rata-rata berada di meridian pengamat, maka saat itu adalah tengah hari rata-rata lokal (*local mean noon*). Ketika matahari rata-rata berada pada meridian Greenwich, itu adalah tengah hari rata-rata Greenwich. Sudut jam dari matahari rata-rata di Greenwich akan dilambangkan dalam buku ini oleh G.M.A.T. (*Greenwich mean astronomical time*). Ketika matahari rata-rata berada di $T$—H.A.M.S. bernilai $12^h$ saat itu—dikatakan sebagai tengah malam rata-rata (*mean midnight*). Ketika G.M.A.T. $= 12^h$, itu adalah tengah malam rata-rata di Greenwich dan ini adalah saat hari sipil (*civil day*) baru di Greenwich dimulai. Waktu rata-rata yang dihitung dari tengah malam di Greenwich disebut *Greenwich Mean Time* (G.M.T.), sekarang didesain sebagai *Universal Time* (U.T.). Jelas bahwa:
$$ \text{U.T.} \equiv \text{G.M.T.} = \text{G.M.A.T.} + 12^h \dots\dots(18). $$

Secara serupa, untuk setiap tempat yang menyimpan waktu rata-rata yang tepat untuk meridiannya, kita akan memiliki:
$$ \text{Local M.T.} = \text{Local M.A.T.} + 12^h \dots\dots(19) $$
$$ = \text{H.A.M.S.} \pm 12^h \dots\dots(20). $$

Rumus (14) memberikan hubungan antara waktu sideris di Greenwich dan waktu sideris di tempat $l$, dan jelas dari Gbr. 22 dan dari persamaan (18) dan (19) bahwa kita akan memiliki hubungan yang serupa antara waktu rata-rata di Greenwich dan waktu rata-rata di tempat $l$; yaitu
$$ \text{U.T.} \equiv \text{G.M.T.} = \text{Local M.T.} \pm \text{bujur dari } l \dots\dots(21), $$
tanda $+$ diambil ketika bujur dari $l$ adalah barat dan tanda $-$ ketika bujur adalah timur.

Kebingungan tidak dapat dihindari jika setiap tempat menyimpan waktu rata-rata lokal yang tepat sesuai meridiannya masing-masing, sehingga di negara-negara kecil sebuah waktu rata-rata standar dipilih, sesuai dengan suatu meridian bujur khusus (meridian standar), yang digunakan secara seragam di seluruh negeri. Di Inggris, waktu rata-rata standar adalah G.M.T. Di negara-negara yang sangat luas seperti Rusia dan Amerika Serikat, dua atau lebih waktu standar digunakan dalam zona-zona bujur; dalam setiap zona, disimpan waktu standar yang tepat untuk suatu meridian yang telah ditentukan. Waktu standar, berdasarkan suatu meridian tertentu ini, akan kita sebut waktu zona (*zone time*, Z.T.). Sistem ini, pada kenyataannya, dipertahankan oleh kapal-kapal di laut yang pada umumnya kurang terganggu oleh komplikasi geografis. Kita memiliki, seperti pada (21),
$$ \text{U.T.} \equiv \text{G.M.T.} = \text{Z.T.} \pm \text{bujur dari meridian standar} \dots\dots(22). $$
"""
st.markdown(materi_bab_2_bagian_15, unsafe_allow_html=True)
