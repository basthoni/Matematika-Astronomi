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
    - [20. Diagram untuk Belahan Bumi Selatan](#20-diagram-untuk-belahan-bumi-selatan)
    - [21. Bintang Sirkumpolar](#21-bintang-sirkumpolar-circumpolar-stars)
    - [22. Bola Langit Standar / Geosentrik](#22-bola-langit-standar-atau-geosentrik-the-standard-or-geocentric-celestial-sphere)
    """)

# ==========================================
# KONTEN UTAMA BAB II (VERBATIM W.M. SMART)
# ==========================================

materi_bab_2_ bagian_1 = r"""
### 17. Pendahuluan.
Dalam Bab I kita telah melihat bahwa posisi di permukaan bumi ditentukan sepenuhnya dengan merujuk pada dua lingkaran besar utama, yaitu meridian Greenwich dan ekuator. Prinsip penentuan posisi pada bola langit pada dasarnya serupa, dan terdapat beberapa metode tergantung pada lingkaran besar khusus yang dipilih sebagai lingkaran utama. Metode-metode ini sekarang akan diuraikan.

### 18. Ketinggian (*altitude*) dan azimut.
Misalkan $O$—pengamat di permukaan bumi (yang dianggap berbentuk bola)—menjadi pusat bola langit (Gbr. 10). Misalkan $Z$ (*zenit*) menjadi titik pada bola langit yang berada tepat di atas kepala—arahnya dapat didefinisikan dengan menggunakan unting-unting (*plumb-line*). Oleh karena itu, $OZ$ adalah kelanjutan dari garis lurus yang menghubungkan pusat bumi ke $O$. Bidang yang melalui $O$ yang tegak lurus terhadap $OZ$ adalah bidang horizon, yang memotong bola langit pada lingkaran besar $NAS$, yang disebut horizon astronomis atau sekadar horizon. 
"""
st.markdown(materi_bab_2_bagian_1, unsafe_allow_html=True)

st.image("Gambar_10.png", caption="Gambar 10 (Sistem Horizon & Zenith)", use_container_width=True)

materi_bab_2_bagian_2 = r"""
Dengan demikian, pada Gbr. 10, horizon membagi bola langit menjadi dua belahan bola (*hemisphere*), di mana bagian atas adalah belahan bola yang terlihat (*visible hemisphere*), dan bagian bawah tersembunyi dari pengamat oleh bumi. Misalkan $X$ menjadi posisi sebuah bintang di bola langit pada saat tertentu. Setiap lingkaran besar yang ditarik melalui $Z$ disebut lingkaran vertikal (*vertical circle*); khususnya, lingkaran vertikal pada Gbr. 10 yang melalui $X$ adalah $ZXA$. Pada bidang $ZXA$, sudut $AOX$ atau busur lingkaran besar $AX$ disebut ketinggian (*altitude*), yang akan dilambangkan dengan $a$. Karena $OZ$ tegak lurus terhadap bidang horizon, lingkaran besar busur $ZA$ adalah $90^\circ$; oleh karena itu $ZX = 90^\circ - a$. $ZX$ disebut jarak zenit (*zenith distance*, disingkat z.d.) dari bintang $X$ dan akan dilambangkan dengan $z$. Dengan demikian
$$
z = 90^\circ - a \dots\dots(1).
$$

Misalkan $LXM$ menjadi lingkaran kecil melalui $X$ yang sejajar dengan horizon; lingkaran ini disebut paralel ketinggian (*parallel of altitude*) dan sedemikian rupa sehingga semua benda langit, yang posisinya pada suatu saat tertentu terletak pada lingkaran kecil ini, memiliki ketinggian yang sama dan juga, berdasarkan (1), memiliki jarak zenit yang sama dengan $X$. Dengan demikian, jika ketinggian atau jarak zenit sebuah bintang diberikan, paralel ketinggian tempat bintang itu harus berada dapat ditentukan secara pasti. Untuk mendefinisikan posisinya secara lengkap pada bola langit, lingkaran vertikal khusus tempat bintang itu berada juga harus ditentukan. Hal ini dilakukan sebagai berikut.

Misalkan $OP$ sejajar dengan sumbu tempat bumi berputar. Jika lintang pengamat adalah utara (seperti pada Gbr. 10), posisi $P$ disebut kutub langit utara (*north celestial pole*), atau sekadar kutub utara (*north pole*). Kita tidak secara langsung menyadari rotasi bumi, tetapi efeknya ditunjukkan dalam rotasi semu bola langit. Bintang-bintang dengan demikian tampak bergerak melintasi langit dan arahnya terus berubah. Di belahan bumi utara, bagaimanapun, ada satu bintang, yang dapat dilihat dengan mata telanjang, yang tampak sangat sedikit berubah. Bintang ini adalah Polaris, atau bintang kutub utara, yang arahnya di langit hampir persis sama dengan arah yang diberikan oleh $OP$. Jika kebetulan ada sebuah bintang yang terletak tepat di $P$ pada bola langit, ketinggian dan arahnya akan tidak berubah sepanjang malam. Kita mendefinisikan lingkaran vertikal melalui $P$, yaitu $ZPN$ (yang memotong horizon di $N$), sebagai lingkaran vertikal utama (*principal vertical circle*) dan titik $N$ sebagai titik utara horizon (*north point of the horizon*).

Titik $S$ pada horizon yang tepat berlawanan dengan $N$ adalah titik selatan (*south point*); titik barat ($W$) dan timur ($E$) memiliki arah yang tegak lurus terhadap arah $N$ dan $S$ ($E$ tidak ditunjukkan pada Gbr. 10). Titik-titik $N, E, S$ dan $W$ disebut titik-titik kardinal (*cardinal points*).

Kita sekarang menentukan posisi sebuah bintang $X$ pada bola langit pada saat tertentu dengan merujuk pada horizon dan lingkaran vertikal utama $ZPN$. Jika bintang berada di bagian barat bola langit (seperti pada Gbr. 10), sudut bola $PZX$ (yang dibentuk oleh lingkaran vertikal utama dan lingkaran vertikal melalui $X$) atau busur lingkaran besar $NA$ disebut azimut ($W$). Jika bintang berada di bagian timur bola langit, seperti pada Gbr. 11, sudut $PZX$ atau busur $NB$ adalah azimut ($E$).
"""
st.markdown(materi_bab_2_bagian_2, unsafe_allow_html=True)

st.image("Gambar_11.png", caption="Gambar 11 (Azimut Timur dan Titik Kardinal)", use_container_width=True)

materi_bab_2_bagian_3 = r"""
Dengan demikian pada saat apa pun posisi benda langit pada bola langit dapat dideskripsikan sepenuhnya dengan merujuk pada horizon dan titik utara horizon dalam hal ketinggian dan azimut ($E$ atau $W$) atau, sebagai alternatif, dalam hal jarak zenit dan azimut. Ketika azimut adalah $90^\circ$ $E$ atau $90^\circ$ $W$, bintang tersebut dikatakan berada pada vertikal utama (*prime vertical*), yang dengan demikian merupakan lingkaran vertikal melalui titik timur $E$ atau titik barat $W$.

Karena pada Gbr. 10 dan 11 sudut $POZ$ (atau lingkaran besar busur $PZ$) ekivalen dengan sudut antara jari-jari bumi yang melewati posisi pengamat dan sumbu bumi, maka $P\hat{O}Z$ (atau $PZ$) sama dengan kolintang pengamat atau
$$
PZ = 90^\circ - \phi \dots\dots(2),
$$
di mana $\phi$ adalah lintang pengamat. Selain itu $PN = 90^\circ - PZ = \phi$; maka ketinggian kutub sama dengan lintang pengamat.

*(Catatan kaki teks asli: Posisi $W$ dan $E$ relatif terhadap $N$ dan $S$ diperoleh dari pertimbangan bahwa, jika pengamat menghadap ke utara, titik barat berada di sebelah kiri dan titik timur berada di sebelah kanannya).*

### 19. Deklinasi dan sudut jam (*declination and hour angle*).
Seperti pada bagian sebelumnya, misalkan bola langit digambarkan untuk seorang pengamat $O$ pada lintang $\phi$, yang menunjukkan horizon, zenit $Z$ dan kutub utara $P$ (Gbr. 12). Lingkaran besar $RWT$ yang bidangnya tegak lurus terhadap $OP$ adalah ekuator langit (*celestial equator*) dan bidangnya, jelas, sejajar dengan ekuator bumi. Ekuator langit dan horizon berpotongan di dua titik $W$ dan $E$. Sekarang $Z$ adalah kutub dari lingkaran besar $NWS$ dan $P$ adalah kutub dari lingkaran besar $RWT$; oleh karena itu $W$ berjarak $90^\circ$ dari $Z$ dan $P$ dan oleh karena itu berjarak $90^\circ$ dari semua titik pada lingkaran besar melalui $Z$ dan $P$. 
"""
st.markdown(materi_bab_2_bagian_3, unsafe_allow_html=True)

st.image("Gambar_12.png", caption="Gambar 12 (Sistem Ekuator Lokal, Deklinasi & Sudut Jam)", use_container_width=True)

materi_bab_2_bagian_4 = r"""
Dengan kata lain, $W$ adalah kutub dari lingkaran besar $NPZSQ$; maka $NW = 90^\circ$ dan $WS = 90^\circ$. Demikian pula $EN = 90^\circ$ dan $ES = 90^\circ$. Maka $W$ dan $E$ adalah dua titik kardinal yang tersisa, $N$ dan $S$ telah didefinisikan secara eksplisit sebelumnya.

Seperti yang telah disebutkan, rotasi bumi menghasilkan rotasi semu bola langit dari timur ke barat mengelilingi $OP$. Mengikuti hal tersebut, karena bintang-bintang berada pada jarak yang sangat jauh dari bumi, sudut antara garis lurus yang menghubungkan pengamat pada $O$ ke bintang tertentu dan garis lurus $OP$ (sejajar dengan sumbu bumi) tetap tidak berubah. Jika kita mempertimbangkan sebuah bintang $X$, rotasi bumi membuatnya tampak menggambarkan lingkaran kecil $LXM$, sejajar dengan ekuator langit, dalam arah yang ditunjukkan oleh anak panah pada Gbr. 12. Misalkan $PXDQ$ adalah semi-lingkaran besar melalui $X$ dan kutub-kutub bola langit. Maka busur $DX$ disebut deklinasi bintang dan merupakan deklinasi utara jika bintang berada di antara ekuator langit dan kutub utara $P$ (seperti untuk bintang $X$). Deklinasi bintang adalah selatan (seperti untuk $Y$) ketika ia berada di antara ekuator langit dan kutub selatan $Q$. 

Deklinasi dengan demikian analog dengan lintang yang didefinisikan untuk titik-titik di permukaan bumi. Nyatakan deklinasi $X$ dengan $\delta$; maka $DX = \delta$ dan $PX = 90^\circ - \delta$. $PX$ disebut jarak kutub utara (*north polar distance*, N.P.D.) dari bintang. Adalah lebih mudah untuk memperlakukan deklinasi sebagai kuantitas aljabar, sehingga berbagai rumus yang akan diturunkan akan berlaku sama untuk deklinasi utara maupun selatan. Deklinasi utara membawa tanda positif ($+$) dan deklinasi selatan membawa tanda negatif ($-$). Dengan demikian rumus untuk jarak kutub utara, yaitu N.P.D. $= 90^\circ - \delta$, berlaku untuk semua bintang, apa pun deklinasinya.

Deklinasi sebuah bintang diketahui, kita dengan demikian dapat menentukan lingkaran kecil, yang disebut paralel deklinasi (*parallel of declination*), tempat bintang itu harus berada. Untuk memperbaiki posisinya pada bola langit pada saat tertentu, kita memerlukan lingkaran besar referensi lainnya. Ini adalah semi-lingkaran besar $PZRSQ$, yang disebut meridian pengamat (*observer's meridian*). Ketika bintang berada di $L$ pada meridian pengamat, ia dikatakan melakukan transit (*transit*) atau mencapai puncaknya (*culminate*), dan jelas dari Gbr. 12 bahwa ketinggiannya ($SL$) adalah yang terbesar dan jarak zenitnya $ZL$ adalah yang terkecil. Setelah itu, karena rotasi bumi, ia bergerak sepanjang lingkaran kecil $LFM$ memotong horizon di $F$ di mana ia dikatakan terbenam (*set*); ketinggiannya di $F$ tentu saja adalah $0^\circ$ dan jarak zenitnya $90^\circ$. 

Selama interval waktu yang bergantung pada deklinasinya, bintang berada di bawah horizon, mencapai depresi maksimum di bawah horizon di $M$; akhirnya ia mencapai horizon di $G$ di mana ia dikatakan terbit (*rise*). Ketinggiannya berangsur-angsur meningkat, ia kembali setelah interval yang ekuivalen dengan waktu di mana bumi melakukan rotasi penuh mengelilingi sumbunya, ke meridian pengamat di $L$. Pada saat apa pun posisi bintang pada paralel deklinasi ditentukan oleh sudut di $P$ antara meridian pengamat dan meridian ($PXQ$) melalui bintang pada saat itu; sudut ini adalah $RPX$ atau $ZPX$ atau busur $RD$ pada ekuator. Sudut ini, yang dilambangkan dengan $H$, disebut sudut jam (*hour angle*) dan diukur dari meridian pengamat ke arah barat dari $0^\circ$ (di $L$) hingga $360^\circ$ (ketika bintang kembali ke meridian pengamat) atau, seperti yang lebih biasa, dari $0^h$ hingga $24^h$. 

Kita dapat mengekspresikan ini dengan cara yang sedikit berbeda. Ketika bintang sedang transit, meridiannya bertepatan dengan meridian pengamat; setelah itu, meridian bintang bergerak dengan mantap ke arah barat dan, ketika ia telah membuat satu putaran penuh dari bola langit, ia telah menggambarkan sudut $360^\circ$ atau $24^h$ terhadap meridian pengamat. Dari Gbr. 12 terlihat bahwa jika bintang berada di sebelah barat meridian pengamat, yaitu jika azimutnya adalah barat, sudut jam berada di antara $0^\circ$ dan $180^\circ$, yaitu antara $0^h$ dan $12^h$. Demikian pula, jika bintang berada di sebelah timur meridian (azimut timur)—seperti pada Gbr. 13—sudut jam berada di antara $12^h$ dan $24^h$.
"""
st.markdown(materi_bab_2_bagian_4, unsafe_allow_html=True)

st.image("Gambar_13.png", caption="Gambar 13 (Posisi Bintang di Timur Meridian)", use_container_width=True)

materi_bab_2_bagian_5 = r"""
Kita dengan demikian memiliki aturan:
*Jika azimut bintang adalah barat, sudut jam berada di antara $0^h$ dan $12^h$ (dan sebaliknya); jika azimut bintang adalah timur, sudut jam berada di antara $12^h$ dan $24^h$.*

### 20. Diagram untuk belahan bumi selatan.
Diagram yang dijelaskan sejauh ini dalam bab ini merujuk pada bola langit untuk pengamat di lintang utara. Kita sekarang akan mendeskripsikan diagram yang bersesuaian untuk pengamat di belahan bumi selatan. Pada Gbr. 14, kita akan menempatkan zenit pengamat seperti pada diagram sebelumnya. Horizon langit kemudian seperti yang ditunjukkan. Di belahan bumi selatan, kutub langit selatan $Q$ berada di atas horizon. Kemudian, jika $\phi$ melambangkan lintang selatan pengamat, $QZ = 90^\circ - \phi$. Lingkaran vertikal utama sekarang adalah $ZQS$, memotong horizon di titik selatan $S$. Titik utara $N$ kemudian dapat ditempatkan dalam diagram. Ekuator langit dan horizon berpotongan di titik barat dan timur $W$ dan $E$ (yang terakhir tidak ditunjukkan pada Gbr. 14) menurut aturan pada catatan kaki halaman 27. 
"""
st.markdown(materi_bab_2_bagian_5, unsafe_allow_html=True)

st.image("Gambar_14.png", caption="Gambar 14 (Bola Langit Belahan Bumi Selatan)", use_container_width=True)

materi_bab_2_bagian_6 = r"""
Pertimbangkan sebuah bintang $X$ dengan deklinasi selatan. Berkat rotasi bumi, ia akan mendeskripsikan lingkaran kecil $LXM$, paralel terhadap ekuator langit dan terletak di antara ekuator langit dan kutub selatan $Q$. Pada $L$, bintang akan memiliki ketinggian terbesar—ia kemudian berada pada meridian pengamat, yaitu semi-lingkaran $QZRNP$. Akibat rotasi bumi, bintang akan bergerak dari meridian pengamat ke arah barat, yaitu ke arah $LXM$, seperti yang ditunjukkan oleh anak panah pada diagram. Sudut $ZQX$ adalah sudut jam yang diukur, seperti sebelumnya, dari $0^h$ hingga $24^h$ ke arah barat dari meridian pengamat. $QZX$ adalah azimut; dalam hal ini adalah barat. Jika $\delta$ adalah deklinasi (negatif) bintang, maka $DX = -\delta$ dan $QX = 90^\circ + \delta$. Bagian lain dari segitiga bola $QZX$ adalah: $QZ = 90^\circ - \phi$, $ZX = z$ (jarak zenit), $QZX = A$ (azimut) dan $ZQX = H$ (sudut jam). Ketika azimut bintang adalah barat, sudut jam berada di antara $0^h$ dan $12^h$. Ketika azimut bintang adalah timur, diagram yang bersesuaian dapat digambarkan secara serupa; ini diserahkan sebagai latihan bagi siswa; maka akan ditemukan bahwa sudut jam berada di antara $12^h$ dan $24^h$. Aturan yang dinyatakan pada akhir bagian 19 terlihat berlaku untuk lintang selatan maupun utara.

### 21. Bintang sirkumpolar (*circumpolar stars*).
Pertimbangkan bola langit untuk pengamat di lintang utara $\phi$ (Gbr. 15). Paralel deklinasi digambarkan untuk dua bintang $X$ dan $Y$, yang keduanya selalu berada di atas horizon dan akibatnya tidak terbenam. Bintang-bintang seperti itu disebut sirkumpolar bintang. 
"""
st.markdown(materi_bab_2_bagian_6, unsafe_allow_html=True)

st.image("Gambar_15.png", caption="Gambar 15 (Bintang Sirkumpolar)", use_container_width=True)

materi_bab_2_bagian_7 = r"""
Dari gambar tersebut terlihat dengan mudah bahwa syarat agar sebuah bintang tidak terbenam adalah: $PM$ harus kurang dari $PN$; yaitu, jarak kutub utara harus kurang dari lintang, atau dengan kata lain, deklinasi harus lebih besar dari kolintang.

Ketika bintang $X$ berada pada meridian pengamat di $L$, ia berada pada kulminasi atas (*upper culmination*) atau dalam transit (*in transit*); ketika bintang mencapai $M$, ia berada pada kulminasi bawah (*lower culmination*). Ekspresi "kulminasi di atas kutub" (*culmination above pole*) dan "kulminasi di bawah kutub" (*culmination below pole*) sering digunakan. Pada kulminasi atas, jarak zenit bintang adalah $ZL$ atau $(PL - PZ)$, yaitu, $\phi - \delta$. Pada kulminasi bawah, jarak zenit bintang adalah $ZM$ atau $(ZP + PM)$, yaitu, $180^\circ - (\phi + \delta)$. Ketika $\delta = \phi$, kulminasi atas terjadi di zenit. Ketika $\delta > \phi$, kulminasi atas terjadi di antara $P$ dan $Z$, seperti untuk bintang $Y$; maka azimut tidak melebihi $90^\circ$, seperti yang dapat disimpulkan dengan mudah dari diagram. Bintang sirkumpolar selatan dapat dianggap dengan cara yang sama.

### 22. Bola langit standar atau geosentrik (*The standard or geocentric celestial sphere*).
Dalam bagian-bagian sebelumnya, deklinasi bintang pada bola langit yang pusatnya adalah pengamat telah didefinisikan. Karena bintang-bintang berada pada jarak yang hampir tak terhingga besarnya dibandingkan dengan dimensi bumi, deklinasi atau jarak kutub bintang yang didefinisikan dengan cara ini tidak bergantung pada posisi pengamat di permukaan bumi, seperti yang dapat dilihat dengan mudah dari Gbr. 16. (Adalah lebih mudah untuk tujuan kita saat ini untuk berurusan dengan jarak kutub utara bintang daripada deklinasinya.) Pada Gbr. 16, $P_1CQ_1$ adalah sumbu rotasi bumi, $C$ menjadi pusat bumi; $O$ adalah pengamat dan $COZ$ adalah arah zenit di $O$; $OP$ sejajar dengan $CP_1$ dan arah bintang yang bertransit di $O$ adalah $OX$. Berdasarkan definisi, jarak kutub utara bintang untuk pengamat di $O$ adalah $P\hat{O}X$. Jika $CY$ digambar sejajar dengan $OX$, maka $CY$ adalah arah bintang dengan merujuk ke $C$, pusat bumi. 
"""
st.markdown(materi_bab_2_bagian_7, unsafe_allow_html=True)

st.image("Gambar_16.png", caption="Gambar 16 (Perbandingan Posisi Pengamat dan Pusat Bumi)", use_container_width=True)

materi_bab_2_bagian_8 = r"""
Dengan demikian $P_1\hat{C}Y = P\hat{O}X$; dengan kata lain jarak kutub utara bintang (dan akibatnya deklinasinya) adalah sama pada bola langit berpusat di $O$ (atau posisi lain di permukaan bumi) seperti pada bola langit berpusat di $C$. Tetapi ketika benda yang relatif dekat seperti bulan, atau matahari, atau planet diamati, definisi jarak kutub utara (dan karena itu deklinasi) yang diberikan sebelumnya bergantung pada posisi khusus pengamat di bumi. Dengan demikian jika $M$ adalah bulan (Gbr. 16) pada jarak $r$ dari pusat bumi, adalah jelas bahwa $P\hat{O}M = P_1\hat{C}M + O\hat{M}C$; juga $O\hat{M}C$ jelas bergantung pada posisi $O$, sedangkan $P_1CM$ sepenuhnya independen dari $O$. $P_1\hat{C}M$ didefinisikan sebagai jarak kutub utara $M$ yang dengan demikian merupakan sudut antara sumbu bumi dan garis lurus yang menghubungkan pusat bumi ke benda langit. 

Definisi ini sepenuhnya bersifat umum dan berlaku untuk setiap benda langit. Oleh karena itu, pusat bola langit standar (atau bola langit geosentrik, sebagaimana dapat disebut) diambil berada di $C$, pusat bumi (Gbr. 17). 
"""
st.markdown(materi_bab_2_bagian_8, unsafe_allow_html=True)

st.image("Gambar_17.png", caption="Gambar 17 (Bola Langit Geosentrik)", use_container_width=True)

materi_bab_2_bagian_9 = r"""
$CZ$ adalah arah zenit pengamat, diameter $QCP$ berimpit dengan sumbu bumi, $NWSE$ adalah horizon langit (lingkaran besar yang bidangnya tegak lurus terhadap $CZ$), dan $RWTE$ adalah ekuator langit (bidang yang berimpit dengan bidang ekuator bumi).
"""
st.markdown(materi_bab_2_bagian_9, unsafe_allow_html=True)
