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
Pada Bab I, kita telah melihat bahwa posisi di permukaan bumi ditentukan sepenuhnya dengan merujuk pada dua lingkaran besar utama, yaitu meridian Greenwich dan ekuator. Prinsip penentuan posisi pada bola langit pada dasarnya serupa, dan terdapat beberapa metode bergantung pada lingkaran besar khusus yang dipilih sebagai lingkaran utama. Metode-metode ini akan diuraikan sebagai berikut.

### 18. Ketinggian (*altitude*) dan azimut.
Misalkan $O$—pengamat di permukaan bumi (yang dianggap berbentuk bola)—menjadi pusat bola langit (Gbr. 10). Misalkan $Z$
"""
st.markdown(materi_bab_2_bagian_1, unsafe_allow_html=True)
st.image("Gambar_10.png", caption="Gambar 10: Sistem Horizon, Zenith, Nadir, dan Horizon Astronomis", use_container_width=True)

materi_bab_2_bagian_2 = r"""
*(zenith)* adalah titik pada bola langit yang berada tepat di atas kepala, yang arahnya dapat didefinisikan menggunakan unting-unting (*plumb-line*). Oleh karena itu, $OZ$ adalah kelanjutan dari garis lurus yang menghubungkan pusat bumi ke $O$. Bidang yang melalui $O$ dan tegak lurus terhadap $OZ$ adalah bidang horizon, yang memotong bola langit pada lingkaran besar $NAS$, yang disebut horizon astronomis atau sekadar horizon. Dengan demikian, pada Gbr. 10, horizon membagi bola langit menjadi dua belahan bola (*hemisphere*); bagian atas adalah belahan bola yang tampak (*visible hemisphere*), sedangkan bagian bawah tersembunyi dari pengamat oleh bumi. Misalkan $X$ adalah posisi sebuah bintang di bola langit pada saat tertentu. Setiap lingkaran besar yang ditarik melalui $Z$ disebut lingkaran vertikal (*vertical circle*); khususnya, lingkaran vertikal pada Gbr. 10 yang melalui $X$ adalah $ZXA$. Pada bidang $ZXA$, sudut $AOX$ atau busur lingkaran besar $AX$ disebut ketinggian (*altitude*), yang dilambangkan dengan $a$. Karena $OZ$ tegak lurus terhadap bidang horizon, besar busur lingkaran besar $ZA$ adalah $90^\circ$; oleh karena itu, $ZX = 90^\circ - a$. $ZX$ disebut jarak zenit (*zenith distance*, disingkat z.d.) dari bintang $X$ dan dilambangkan dengan $z$. Dengan demikian:

$$ z = 90^\circ - a \dots\dots(1) $$

Misalkan $LXM$ adalah lingkaran kecil melalui $X$ yang sejajar dengan horizon; lingkaran ini disebut paralel ketinggian (*parallel of altitude*) dan sedemikian rupa sehingga semua benda langit yang pada suatu saat tertentu terletak di lingkaran kecil ini memiliki ketinggian yang sama dan juga, berdasarkan persamaannya (1), memiliki jarak zenit yang sama dengan $X$. Dengan demikian, jika ketinggian atau jarak zenit sebuah bintang diketahui, paralel ketinggian tempat bintang itu berada dapat ditentukan secara pasti. Untuk mendefinisikan posisinya secara lengkap pada bola langit, lingkaran vertikal khusus tempat bintang itu berada juga harus ditentukan. Hal ini dilakukan sebagai berikut.

Misalkan $OP$ sejajar dengan sumbu rotasi bumi. Jika lintang pengamat adalah utara (seperti pada Gbr. 10), posisi $P$ disebut kutub langit utara (*north celestial pole*), atau sekadar kutub utara (*north pole*). Kita tidak secara langsung menyadari rotasi bumi, tetapi efeknya tampak dalam rotasi semu bola langit. Akibatnya, bintang-bintang tampak bergerak melintasi langit dan arahnya terus berubah. Namun, di belahan bumi utara, ada satu bintang yang dapat dilihat dengan mata telanjang dan tampak sangat sedikit berubah. Bintang ini adalah Polaris, atau bintang kutub utara, yang arahnya di langit hampir persis sama dengan arah yang diberikan oleh $OP$. Jika kebetulan ada sebuah bintang yang terletak tepat di $P$ pada bola langit, ketinggian dan arahnya tidak akan berubah sepanjang malam. Kita mendefinisikan lingkaran vertikal melalui $P$, yaitu $ZPN$ (yang memotong horizon di $N$), sebagai lingkaran vertikal utama (*principal vertical circle*) dan titik $N$ sebagai titik utara horizon (*north point of the horizon*).

Titik $S$ pada horizon yang tepat berlawanan dengan $N$ adalah titik selatan (*south point*); titik barat ($W$) dan timur ($E$) memiliki arah yang tegak lurus terhadap garis $N$ dan $S$ ($E$ tidak ditunjukkan pada Gbr. 10). Titik-titik $N, E, S$, dan $W$ disebut titik-titik kardinal (*cardinal points*).

Kita sekarang menentukan posisi sebuah bintang $X$ pada bola langit pada saat tertentu dengan merujuk pada horizon dan lingkaran vertikal utama $ZPN$. Jika bintang berada di bagian barat bola langit (seperti pada Gbr. 10), sudut bola $PZX$ (yang dibentuk oleh lingkaran vertikal utama dan lingkaran vertikal melalui $X$) atau busur lingkaran besar $NA$ disebut azimut (*azimuth*, $W$). Jika bintang berada di bagian timur bola langit, seperti pada Gbr. 11, sudut $PZX$
"""
st.markdown(materi_bab_2_bagian_2, unsafe_allow_html=True)
st.image("Gambar_11.png", caption="Gambar 11: Sistem Azimut (Timur/Barat) dan Titik Kardinal", use_container_width=True)

materi_bab_2_bagian_3 = r"""
atau busur $NB$ adalah azimut ($E$). Dengan demikian, pada saat apa pun, posisi benda langit pada bola langit dapat dideskripsikan sepenuhnya dengan merujuk pada horizon dan titik utara horizon dalam hal ketinggian dan azimut ($E$ atau $W$), atau sebagai alternatif, dalam hal jarak zenit dan azimut. Ketika azimut bernilai $90^\circ$ $E$ atau $90^\circ$ $W$, bintang tersebut dikatakan berada pada vertikal utama (*prime vertical*), yang merupakan lingkaran vertikal yang melalui titik timur $E$ atau titik barat $W$.

Karena pada Gbr. 10 dan 11 sudut $POZ$ (atau busur lingkaran besar $PZ$) ekuivalen dengan sudut antara jari-jari bumi yang melewati posisi pengamat dan sumbu bumi, maka $P\hat{O}Z$ (atau $PZ$) sama dengan kolintang pengamat, atau:

$$ PZ = 90^\circ - \phi \dots\dots(2) $$

di mana $\phi$ adalah lintang pengamat. Selain itu, $PN = 90^\circ - PZ = \phi$; maka ketinggian kutub sama dengan lintang pengamat.

*(Catatan kaki: Posisi $W$ dan $E$ relatif terhadap $N$ dan $S$ diperoleh dari pertimbangan bahwa jika pengamat menghadap ke utara, titik barat berada di sebelah kiri dan titik timur berada di sebelah kanannya).*

### 19. Deklinasi dan sudut jam (*declination and hour angle*).
Seperti pada bagian sebelumnya, misalkan bola langit digambarkan untuk seorang pengamat $O$ pada lintang $\phi$, dengan menunjukkan horizon, zenit $Z$, dan kutub utara $P$ (Gbr. 12). Lingkaran besar $RWT$ yang bidangnya tegak lurus terhadap $OP$ adalah ekuator langit (*celestial equator*), yang bidangnya sejajar dengan ekuator bumi. Ekuator langit dan horizon berpotongan di dua titik, yaitu $W$ dan $E$. Karena $Z$ adalah kutub dari lingkaran besar $NWS$ dan $P$ adalah kutub dari lingkaran besar $RWT$, maka $W$ berjarak $90^\circ$ dari $Z$ dan $P$,
"""
st.markdown(materi_bab_2_bagian_3, unsafe_allow_html=True)
st.image("Gambar_12.png", caption="Gambar 12: Sistem Ekuator Lokal (Deklinasi dan Sudut Jam)", use_container_width=True)

materi_bab_2_bagian_4 = r"""
sehingga berjarak $90^\circ$ dari semua titik pada lingkaran besar melalui $Z$ dan $P$. Dengan kata lain, $W$ adalah kutub dari lingkaran besar $NPZSQ$; maka $NW = 90^\circ$ dan $WS = 90^\circ$. Demikian pula, $EN = 90^\circ$ dan $ES = 90^\circ$. Dengan demikian, $W$ dan $E$ adalah dua titik kardinal yang tersisa, sementara $N$ dan $S$ telah didefinisikan sebelumnya.

Sebagaimana telah disebutkan, rotasi bumi menghasilkan rotasi semu bola langit dari timur ke barat mengelilingi sumbu $OP$. Karena bintang-bintang berada pada jarak yang sangat jauh dari bumi, sudut antara garis lurus yang menghubungkan pengamat di $O$ ke bintang tertentu dengan garis lurus $OP$ (yang sejajar dengan sumbu bumi) praktis tidak berubah. Jika kita mempertimbangkan sebuah bintang $X$, rotasi bumi membuatnya tampak menelusuri lingkaran kecil $LXM$ yang sejajar dengan ekuator langit, dalam arah yang ditunjukkan oleh anak panah pada Gbr. 12. Misalkan $PXDQ$ adalah semi-lingkaran besar melalui $X$ dan kutub-kutub bola langit. Busur $DX$ disebut deklinasi bintang, yang bernilai positif (utara) jika bintang berada di antara ekuator langit dan kutub utara $P$ (seperti pada bintang $X$). Deklinasi bernilai negatif (selatan) jika bintang berada di antara ekuator langit dan kutub selatan $Q$ (seperti pada bintang $Y$). Dengan demikian, deklinasi analog dengan lintang pada permukaan bumi. Jika deklinasi $X$ dinyatakan sebagai $\delta$, maka $DX = \delta$ dan $PX = 90^\circ - \delta$. $PX$ disebut jarak kutub utara (*north polar distance*, N.P.D.) dari bintang. Untuk memudahkan, deklinasi diperlakukan sebagai kuantitas aljabar, sehingga rumus-rumus yang diturunkan akan berlaku sama untuk deklinasi utara maupun selatan. Deklinasi utara bertanda positif ($+$) dan deklinasi selatan bertanda negatif ($-$). Dengan cara ini, rumus jarak kutub utara, yaitu N.P.D. $= 90^\circ - \delta$, berlaku untuk semua bintang tanpa memandang deklinasinya.

Ketika deklinasi sebuah bintang diketahui, kita dapat menentukan lingkaran kecil tempat bintang itu berada, yang disebut paralel deklinasi (*parallel of declination*). Untuk menentukan posisinya secara pasti pada bola langit pada suatu saat tertentu, kita memerlukan satu lingkaran besar referensi lagi, yaitu semi-lingkaran besar $PZRSQ$ yang disebut meridian pengamat (*observer's meridian*). Ketika bintang berada di titik $L$ pada meridian pengamat, ia dikatakan melakukan transit (*transit*) atau mencapai kulminasi (*culminate*). Dari Gbr. 12, terlihat jelas bahwa ketinggiannya ($SL$) adalah yang maksimum dan jarak zenitnya ($ZL$) adalah yang minimum. Setelah itu, akibat rotasi bumi, bintang bergerak sepanjang lingkaran kecil $LFM$ dan memotong horizon di titik $F$, di mana ia dikatakan terbenam (*set*); ketinggiannya di $F$ tentu saja $0^\circ$ dan jarak zenitnya $90^\circ$. Selama suatu interval waktu yang bergantung pada deklinasinya, bintang berada di bawah horizon hingga mencapai titik depresi maksimum di bawah horizon di $M$, sebelum akhirnya mencapai horizon di $G$ di mana ia terbit (*rise*). Ketinggiannya kemudian berangsur-angsur meningkat hingga kembali ke meridian pengamat di $L$ setelah interval waktu yang ekuivalen dengan satu putaran penuh bumi pada sumbunya. Pada saat apa pun, posisi bintang pada paralel deklinasi ditentukan oleh sudut di $P$ antara meridian pengamat dan meridian ($PXQ$) yang melewati bintang pada saat tersebut; sudut ini adalah $RPX$ atau $ZPX$, atau busur $RD$ pada ekuator. Sudut ini, yang dilambangkan dengan $H$, disebut sudut jam (*hour angle*), diukur dari meridian pengamat ke arah barat dari $0^\circ$ (di $L$) hingga $360^\circ$ (ketika bintang kembali ke meridian pengamat), atau yang lebih lumrah, dari $0^h$ hingga $24^h$. Konsep ini dapat dijelaskan sedikit berbeda: ketika bintang sedang transit, meridiannya bertepatan dengan meridian pengamat; setelah itu, meridian bintang bergerak ke arah barat, dan ketika telah melakukan satu putaran penuh mengelilingi bola langit, ia telah menyapu sudut $360^\circ$ atau $24^h$ terhadap meridian pengamat. Dari Gbr. 12, tampak bahwa jika bintang berada di sebelah barat meridian pengamat—artinya
"""
st.markdown(materi_bab_2_bagian_4, unsafe_allow_html=True)
st.image("Gambar_13.png", caption="Gambar 13: Diagram Sudut Jam Barat dan Timur Meridian", use_container_width=True)

materi_bab_2_bagian_5 = r"""
azimutnya adalah barat—sudut jamnya bernilai di antara $0^\circ$ dan $180^\circ$ (antara $0^h$ dan $12^h$). Sebaliknya, jika bintang berada di sebelah timur meridian (azimut timur), seperti pada Gbr. 13, sudut jamnya bernilai di antara $12^h$ dan $24^h$. Dari sini kita memperoleh aturan:
*Jika azimut bintang adalah barat, sudut jamnya berada di antara $0^h$ dan $12^h$ (dan sebaliknya); jika azimut bintang adalah timur, sudut jamnya berada di antara $12^h$ dan $24^h$.*

### 20. Diagram untuk belahan bumi selatan.
Diagram yang dibahas sejauh ini merujuk pada bola langit untuk pengamat di lintang utara. Sekarang kita akan mendeskripsikan diagram yang bersesuaian untuk pengamat di belahan bumi selatan. Pada Gbr. 14, zenit pengamat ditempatkan seperti pada diagram sebelumnya, dengan horizon langit seperti yang digambarkan. Di belahan bumi selatan, kutub langit selatan $Q$ berada di atas horizon. Jika $\phi$ melambangkan lintang selatan pengamat, maka $QZ = 90^\circ - \phi$. Lingkaran vertikal utama sekarang adalah $ZQS$, yang memotong horizon di titik selatan $S$, sehingga titik utara $N$ dapat ditentukan posisinya dalam diagram. Ekuator langit dan horizon berpotongan di titik barat dan timur $W$ dan $E$ (titik $E$ tidak ditampilkan pada Gbr. 14) sesuai dengan
"""
st.markdown(materi_bab_2_bagian_5, unsafe_allow_html=True)
st.image("Gambar_14.png", caption="Gambar 14: Bola Langit untuk Pengamat di Belahan Bumi Selatan", use_container_width=True)

materi_bab_2_bagian_6 = r"""
aturan pada catatan kaki halaman 27. Pertimbangkan sebuah bintang $X$ dengan deklinasi selatan. Akibat rotasi bumi, bintang ini menelusuri lingkaran kecil $LXM$ yang sejajar dengan ekuator langit dan terletak di antara ekuator langit dan kutub selatan $Q$. Di titik $L$, bintang mencapai ketinggian maksimumnya ketika berada pada meridian pengamat (semi-lingkaran $QZRNP$). Dari meridian pengamat, bintang bergerak ke arah barat menyusuri $LXM$, seperti ditunjukkan oleh anak panah pada diagram. Sudut $ZQX$ adalah sudut jam yang diukur dari $0^h$ hingga $24^h$ ke arah barat dari meridian pengamat. Sementara itu, $QZX$ adalah azimutnya, yang dalam kasus ini bernilai barat. Jika $\delta$ adalah deklinasi (negatif) bintang tersebut, maka $DX = -\delta$ dan $QX = 90^\circ + \delta$. Unsur-unsur lain dari segitiga bola $QZX$ adalah: $QZ = 90^\circ - \phi$, $ZX = z$ (jarak zenit), $QZX = A$ (azimut), dan $ZQX = H$ (sudut jam). Ketika azimut bintang bernilai barat, sudut jamnya berada di antara $0^h$ dan $12^h$. Ketika azimutnya timur, diagram serupa dapat digambarkan—yang pembuktiannya diserahkan sebagai latihan bagi pembaca—di mana sudut jamnya akan bernilai di antara $12^h$ dan $24^h$. Aturan yang dinyatakan pada akhir Bagian 19 terbukti berlaku untuk lintang selatan maupun utara.

### 21. Bintang sirkumpolar (*circumpolar stars*).
Perhatikan bola langit untuk pengamat di lintang utara $\phi$ (Gbr. 15). Paralel deklinasi digambarkan untuk dua bintang $X$ dan $Y$, yang keduanya senantiasa berada di atas horizon sehingga tidak pernah terbenam. Bintang semacam ini disebut bintang sirkumpolar:
"""
st.markdown(materi_bab_2_bagian_6, unsafe_allow_html=True)
st.image("Gambar_15.png", caption="Gambar 15: Bintang Sirkumpolar yang Tidak Pernah Terbenam", use_container_width=True)

materi_bab_2_bagian_7 = r"""
Dari gambar tersebut, terlihat jelas bahwa syarat agar sebuah bintang tidak terbenam adalah busur $PM$ harus lebih kecil daripada $PN$; dengan kata lain, jarak kutub utara harus lebih kecil daripada lintang, atau deklinasinya harus lebih besar daripada kolintang.

Ketika bintang $X$ berada pada meridian pengamat di titik $L$, ia berada pada kulminasi atas (*upper culmination*) atau dalam transit (*in transit*); ketika bintang mencapai titik $M$, ia berada pada kulminasi bawah (*lower culmination*). Istilah "kulminasi di atas kutub" (*culmination above pole*) dan "kulminasi di bawah kutub" (*culmination below pole*) sering digunakan. Pada kulminasi atas, jarak zenit bintang adalah $ZL$ atau $(PL - PZ)$, yakni $\phi - \delta$. Pada kulminasi bawah, jarak zenit bintang adalah $ZM$ atau $(ZP + PM)$, yakni $180^\circ - (\phi + \delta)$. Ketika $\delta = \phi$, kulminasi atas terjadi tepat di zenit. Ketika $\delta > \phi$, kulminasi atas terjadi di antara $P$ dan $Z$ (seperti pada bintang $Y$), sehingga azimutnya tidak melebihi $90^\circ$, sebagaimana dapat disimpulkan dengan mudah dari diagram. Bintang sirkumpolar selatan dapat dianalisis dengan cara yang serupa.

### 22. Bola langit standar atau geosentrik (*The standard or geocentric celestial sphere*).
Dalam bagian-bagian sebelumnya, deklinasi bintang didefinisikan berdasarkan bola langit yang berpusat pada pengamat. Karena bintang-bintang berada pada jarak yang sangat jauh jika dibandingkan dengan ukuran bumi, deklinasi atau jarak kutub bintang yang diperoleh dengan cara ini tidak bergantung pada posisi pengamat di permukaan bumi, seperti yang tampak pada Gbr. 16. (Untuk keperluan saat ini, lebih mudah menggunakan jarak kutub utara bintang daripada deklinasinya.) Pada Gbr. 16, $P_1CQ_1$ adalah sumbu rotasi bumi dengan $C$ sebagai pusat bumi; $O$ adalah pengamat dan $COZ$ adalah arah zenit di $O$; $OP$ sejajar dengan $CP_1$, dan arah bintang yang
"""
st.markdown(materi_bab_2_bagian_7, unsafe_allow_html=True)
st.image("Gambar_16.png", caption="Gambar 16: Perbandingan Posisi Pengamat di Permukaan dan Pusat Bumi", use_container_width=True)

materi_bab_2_bagian_8 = r"""
bertransit di $O$ adalah $OX$. Berdasarkan definisi, jarak kutub utara bintang bagi pengamat di $O$ adalah sudut $P\hat{O}X$. Jika $CY$ digambar sejajar dengan $OX$, maka $CY$ menyatakan arah bintang dengan merujuk pada pusat bumi $C$. Dengan demikian, $P_1\hat{C}Y = P\hat{O}X$; dengan kata lain, jarak kutub utara bintang (dan akibatnya deklinasinya) bernilai sama pada bola langit yang berpusat di $O$ maupun di pusat bumi $C$. Namun, ketika mengamati benda yang relatif dekat seperti bulan, matahari, atau planet, definisi jarak kutub utara (dan deklinasi) tersebut bergantung pada posisi spesifik pengamat di bumi. Sebagai contoh, jika $M$ adalah bulan (Gbr. 16) pada jarak $r$ dari pusat bumi, jelas bahwa $P\hat{O}M = P_1\hat{C}M + O\hat{M}C$. Sudut $O\hat{M}C$ bergantung pada posisi pengamat $O$, sedangkan $P_1\hat{C}M$ sepenuhnya independen
"""
st.markdown(materi_bab_2_bagian_8, unsafe_allow_html=True)
st.image("Gambar_17.png", caption="Gambar 17: Bola Langit Standar atau Geosentrik Berpusat di Pusat Bumi", use_container_width=True)

materi_bab_2_bagian_9 = r"""
dari posisi $O$. Sudut $P_1\hat{C}M$ didefinisikan sebagai jarak kutub utara $M$, yang merupakan sudut antara sumbu bumi dan garis lurus yang menghubungkan pusat bumi ke benda langit tersebut. Definisi ini bersifat umum dan berlaku untuk setiap benda langit. Oleh karena itu, pusat bola langit standar (atau bola langit geosentrik) ditetapkan berada di $C$, yaitu pusat bumi (Gbr. 17). $CZ$ adalah arah zenit pengamat, diameter $QCP$ berimpit dengan sumbu bumi, $NWSE$ adalah horizon langit (lingkaran besar yang bidangnya tegak lurus terhadap $CZ$), dan $RWTE$ adalah ekuator langit (bidang yang berimpit dengan ekuator bumi). Busur $PX$ adalah jarak kutub utara benda langit sesuai dengan definisi baru tersebut, dan $DX$ adalah deklinasi $\delta$ (di mana N.P.D. $= 90^\circ - \delta$). Meridian pengamat adalah $PZRSQ$, jarak zenit benda langit adalah $ZX$ (dilambangkan dengan $z$), sementara azimut $A$ (sudut $P\hat{Z}X$) dan sudut jam $H$ (sudut $Z\hat{P}X$) didefinisikan seperti sebelumnya. Deklinasi benda-benda langit utama (bulan, matahari, planet, dan bintang-bintang terang) ditabulasikan dalam *Astronomical Ephemeris* (publikasi Inggris dan Amerika) serta efemeris nasional lainnya.

Mulai bagian ini seterusnya, bola langit akan diasumsikan berpusat di $C$, yakni pusat bumi (Gbr. 17).

### 23. Penyelesaian dari segitiga bola PZX.
Kita akan membahas dua masalah utama yang berkaitan dengan segitiga bola $PZX$:
(i) Diberikan lintang pengamat $\phi$, deklinasi $\delta$, dan sudut jam $H$ dari suatu benda langit, hitunglah jarak zenit dan azimutnya. Berdasarkan rumus kosinus (**Rumus A**), karena dua sisi $PZ$ dan $PX$ beserta sudut apitnya $ZPX$ diketahui (Gbr. 17), kita memperoleh:

$$ \cos ZX = \cos PZ \cos PX + \sin PZ \sin PX \cos ZPX $$

atau

$$ \cos z = \sin \phi \sin \delta + \cos \phi \cos \delta \cos H \dots\dots(3) $$

Dengan demikian, $z$ dapat dihitung secara langsung dari persamaan (3) atau melalui rumus haversine (Bagian 13), yang dalam hal ini dapat ditulis sebagai:

$$ \text{hav } z = \text{hav } (\phi - \delta) + \cos \phi \cos \delta \text{ hav } H \dots\dots(4) $$

Selanjutnya, dengan menggunakan **Rumus A**:

$$ \cos PX = \cos PZ \cos ZX + \sin PZ \sin ZX \cos PZX $$

atau

$$ \sin \delta = \sin \phi \cos z + \cos \phi \sin z \cos A \dots\dots(5) $$

dari mana azimut $A$ dapat dihitung. Dalam bentuk haversine, persamaan (5) dapat ditulis:

$$ \cos \phi \cos a \text{ hav } A = \text{hav } (90^\circ - \delta) - \text{hav } (\phi - a) \dots(6) $$

di mana $a$ adalah ketinggian (*altitude*).

(ii) Diberikan lintang pengamat $\phi$, jarak zenit bintang $z$, dan azimutnya $A$, hitunglah deklinasi bintang dan sudut jamnya. Berdasarkan persamaan (5), karena $\phi, z$, dan $A$ diketahui, kita dapat menghitung deklinasi $\delta$. Persamaan (3) atau (4) kemudian dapat digunakan untuk menghitung sudut jam $H$. Dari persamaan (3), kita peroleh:

$$ \cos H = \cos z \sec \phi \sec \delta - \tan \phi \tan \delta \dots\dots(7) $$

Perhatikan kembali segitiga bola $PZX$ pada Gbr. 13. Sudut $PZX$ adalah azimut timur. Mengingat sudut jam diukur di kutub dari meridian pengamat ke arah barat, maka $Z\hat{P}X = 24^h - H$. Penyelesaian segitiga tersebut dilanjutkan dengan cara yang sama.

### 24. Asensio rekta dan deklinasi.
Dalam metode sudut jam dan deklinasi untuk menentukan posisi bintang di bola langit, hanya satu koordinat (deklinasi) yang tetap konstan saat bintang melintasi langit, sementara sudut jamnya meningkat secara seragam dari $0^h$ hingga $24^h$. Namun,
"""
st.markdown(materi_bab_2_bagian_9, unsafe_allow_html=True)
st.image("Gambar_18.png", caption="Gambar 18: Asensio Rekta dan Deklinasi pada Bola Langit", use_container_width=True)

materi_bab_2_bagian_10 = r"""
posisi bintang-bintang di bola langit dapat dianalogikan seperti titik-titik tetap di permukaan bumi, sehingga dapat dispesifikasikan dengan merujuk pada ekuator langit dan suatu titik referensi tertentu di ekuator tersebut. Sebagai contoh, pada Gbr. 18, misalkan $\Upsilon$ adalah titik referensi di ekuator dan $X$ adalah sebuah bintang; misalkan pula meridian yang melalui $X$ memotong ekuator langit di titik $D$. Seiring pergerakan bintang-bintang melintasi langit, kita tahu bahwa deklinasi bintang $X$ (yakni $DX$) bernilai konstan dan konfigurasi relatif antar bintang juga tetap. Ini berarti busur $\Upsilon D$ bernilai konstan; dengan kata lain, sudut antara meridian $\Upsilon$ dan meridian $D$ tetap tidak berubah. Kita dapat menjadikan $\Upsilon$ sebagai titik acuan pada ekuator langit, dan dengan merujuk padanya, kita dapat menentukan posisi bintang $X$ menggunakan busur lingkaran besar $\Upsilon D$ dan deklinasi $DX$. Titik acuan yang dipilih dalam praktik astronomi disebut ekuinoks musim semi (*vernal equinox*) atau titik pertama Aries, yang posisinya dapat dikaitkan dengan bintang tertentu di langit (kita akan mendefinisikannya secara lebih tepat nanti). Busur $\Upsilon D$ atau sudut $\Upsilon\hat{P}X$ disebut asensio rekta (*right ascension*, R.A.) dari bintang $X$ (dilambangkan dengan $\alpha$), yang diukur ke arah timur dari $\Upsilon$ dari $0^h$ hingga $24^h$ (searah dengan anak panah di dekat $\Upsilon$). Arah pengukuran ini berlawanan dengan arah pengukuran sudut jam. Dari Gbr. 18, terlihat bahwa $R\Upsilon = RD + \Upsilon D$. Di sini, $RD$ (atau $R\hat{P}X$) adalah sudut jam $H$ dari bintang $X$, dan $R\Upsilon$ adalah sudut jam dari titik $\Upsilon$. Sudut jam dari $\Upsilon$ ini disebut waktu sideris (*sidereal time*, S.T.). Dengan demikian, kita memperoleh hubungan yang semestinya:

$$ \text{Sid. time} = \text{H.A. } X + \text{R.A. } X \dots\dots(8) $$

atau

$$ \text{S.T.} = H + \alpha \dots\dots(9) $$

Ketika titik $\Upsilon$ berada pada meridian pengamat, sudut jamnya bernilai $0^h$, yang berarti waktu sideris bernilai $0^h$. Ketika titik $\Upsilon$ kembali berada pada meridian pengamat setelah satu putaran, selang waktu sebesar $24^h$ waktu sideris telah berlalu. Selang waktu ini persis sama dengan waktu yang dibutuhkan bumi untuk melakukan satu rotasi penuh pada sumbunya, yang disebut hari sideris (*sidereal day*). Pada kenyataannya, bumi yang berputar bertindak sebagai penunjuk waktu standar.

### 25. Orbit bumi.
Bumi adalah sebuah planet yang mengelilingi matahari dalam lintasan berbentuk elips atau orbit, dengan matahari berada pada salah satu fokus $S$ dari elips tersebut (Gbr. 19). Ini adalah hukum gerak planet pertama Kepler. Waktu yang dibutuhkan bumi untuk menyelesaikan satu revolusi penuh di orbitnya adalah satu tahun. Seiring pergerakan bumi di orbitnya, arah pandang ke matahari dari bumi terus berubah, dan kecepatan sudutnya tidak seragam. Karena pengamatan kita dilakukan dari bumi, maka relatif terhadap bumi, matahari tampak mendeskripsikan orbit elips mengelilingi bumi. Pada Gbr. 20, $C$ adalah pusat bumi dan elips tersebut mewakili orbit semu matahari relatif terhadap bumi. Urutan posisi matahari ($a, e, f, b, g$) pada orbit semu ini bersesuaian dengan urutan posisi bumi ($A, E, F, B, G$) dalam orbitnya mengelilingi matahari (Gbr. 19). Selama kurun waktu satu tahun, matahari dengan demikian
"""
st.markdown(materi_bab_2_bagian_10, unsafe_allow_html=True)

st.image("Gambar_19.png", caption="Gambar 19: Orbit Bumi Mengelilingi Matahari", use_container_width=True)
st.image("Gambar_20.png", caption="Gambar 20: Orbit Semu Matahari Relatif Terhadap Bumi", use_container_width=True)

materi_bab_2_bagian_11 = r"""
tampak melakukan satu putaran penuh di langit dengan latar belakang bintang-bintang. Bidang orbit ini disebut bidang ekliptika, dan perpotongan bidang ini dengan bola langit yang berpusat di $C$ (pusat bumi) membentuk lingkaran besar yang disebut ekliptika. Pada Gbr. 21, misalkan $C$ adalah pusat bola langit tempat ekuator langit $\Upsilon TR$ dan kutub utara $P$ digambarkan. Jika bintang-bintang diamati dari pusat bumi $C$, mereka akan menempati posisi-posisi tertentu pada bola langit tersebut. Relatif terhadap bintang-bintang, bidang ekliptika memiliki posisi yang tetap, sehingga ekliptika membentuk lingkaran besar tertentu yang miring pada sudut sekitar $23\frac{1}{2}^\circ$ terhadap ekuator langit. Pada Gbr. 21, $\Upsilon \Upsilon M U$ merepresentasikan ekliptika dan
"""
st.markdown(materi_bab_2_bagian_11, unsafe_allow_html=True)
st.image("Gambar_21.jpg", caption="Gambar 21: Ekliptika, Kemiringan, dan Titik Ekuinoks", use_container_width=True)

materi_bab_2_bagian_12 = r"""
kemiringannya terhadap ekuator langit adalah sudut $M\hat{\Upsilon}R$, yang dikenal sebagai kemiringan ekliptika (*obliquity of the ecliptic*). Relatif terhadap bumi, matahari tampak bergerak di sepanjang ekliptika dalam arah $\Upsilon \Upsilon M$, dan dua kali setahun—yaitu di titik $\Upsilon$ dan $U$—posisinya pada bola langit berimpit dengan perpotongan antara ekliptika dan ekuator langit. Di antara titik $\Upsilon$ dan $M$ serta antara $M$ dan $U$, matahari berada di sebelah utara ekuator, sehingga deklinasinya bernilai positif (utara). Sebaliknya, di antara $U$ dan $\Upsilon$ serta antara $\Upsilon$ dan $\Upsilon$, deklinasinya bernilai negatif (selatan). Posisi $\Upsilon$ di mana deklinasi matahari berubah dari selatan menjadi utara disebut ekuinoks musim semi (*vernal equinox*). Dari sinilah titik referensi $\Upsilon$ untuk mengukur asensio rekta bintang-bintang diperoleh. Jadi, jika $X$ adalah sebuah bintang, asensio rektanya adalah busur $\Upsilon D$ atau $\alpha$ yang diukur sepanjang ekuator dari $\Upsilon$ ke arah timur, dan deklinasinya $\delta$ adalah $DX$. Dari diagram, terlihat bahwa asensio rekta dan deklinasi matahari terus-menerus berubah. Ketika matahari berada di $\Upsilon$ (sekitar 21 Maret—ekuinoks musim semi), asensio rekta dan deklinasinya bernilai nol; di $M$ (sekitar 21 Juni—solstis musim panas), asensio rektanya $6^h$ dan deklinasinya sekitar $23\frac{1}{2}^\circ \text{ U}$; di $U$ (sekitar 23 September—ekuinoks musim gugur), asensio rektanya $12^h$ dan deklinasinya $0^\circ$; dan pada titik terendahnya (sekitar 21 Desember—solstis musim dingin), asensio rektanya $18^h$ dan deklinasinya sekitar $23\frac{1}{2}^\circ \text{ S}$.

### 26. Lintang dan bujur langit.
Posisi suatu benda langit dapat dirujuk ke ekliptika sebagai lingkaran besar fundamental dengan ekuinoks musim semi $\Upsilon$ sebagai titik acuan utama. Pada Gbr. 21, $K$ adalah kutub utara ekliptika dan $KXA$ adalah lingkaran besar yang melalui $X$ dan memotong ekliptika di titik $A$. Busur $\Upsilon A$, yang diukur dari $\Upsilon$ ke $A$ sepanjang ekliptika searah dengan pergerakan tahunan matahari (ke timur), disebut bujur (*longitude*) benda langit $X$ dan diukur dari $0^\circ$ hingga $360^\circ$ mengelilingi ekliptika. Busur $AX$ adalah lintang (*latitude*), di mana lintang utara dianggap positif dan lintang selatan negatif. Jika asensio rekta dan deklinasi suatu bintang diketahui, kita dapat menentukan lintang ($\beta$) dan bujurnya ($\lambda$) melalui segitiga bola $KPX$, begitu pula sebaliknya. Karena $\Upsilon$ adalah kutub dari lingkaran besar $KPMR$, maka $K\hat{P}\Upsilon = 90^\circ$. Karena $\Upsilon D = \Upsilon\hat{P}X = \alpha$, maka $K\hat{P}X = 90^\circ + \alpha$. Demikian pula, $P\hat{K}\Upsilon = 90^\circ$, dan karena $\Upsilon A = \Upsilon\hat{K}X = \lambda$, maka $P\hat{K}X = 90^\circ - \lambda$. Selain itu, $PX = 90^\circ - \delta$ dan $KX = 90^\circ - \beta$. Jika $\epsilon$ menyatakan kemiringan ekliptika—yakni sudut antara jari-jari $CM$ dan $CR$—maka busur $RM = \epsilon$. Karena $KM = 90^\circ$ dan $PR = 90^\circ$, maka $KP = \epsilon$. Dengan menerapkan rumus-rumus **A**, **B**, dan **C**, kita memperoleh:

$$ \cos KX = \cos PX \cos KP + \sin PX \sin KP \cos KPX $$

$$ \sin KX \sin PKX = \sin PX \sin KPX $$

$$ \sin KX \cos PKX = \cos PX \sin KP - \sin PX \cos KP \cos KPX $$

atau:

$$ \sin \beta = \sin \delta \cos \epsilon - \cos \delta \sin \epsilon \sin \alpha \dots\dots(10) $$

$$ \cos \beta \cos \lambda = \cos \delta \cos \alpha \dots\dots(11) $$

$$ \cos \beta \sin \lambda = \sin \delta \sin \epsilon + \cos \delta \cos \epsilon \sin \alpha \dots\dots(12) $$

Melalui proses serupa, asensio rekta $\alpha$ dan deklinasi $\delta$ dapat dinyatakan dalam bentuk $\beta, \lambda$, dan $\epsilon$ melalui rumus berikut:

$$ \sin \delta = \sin \beta \cos \epsilon + \cos \beta \sin \epsilon \sin \lambda $$

$$ \cos \delta \cos \alpha = \cos \beta \cos \lambda $$

$$ \cos \delta \sin \alpha = - \sin \beta \sin \epsilon + \cos \beta \cos \epsilon \sin \lambda $$

### 27. Waktu Sideris.
Misalkan bumi dan bola langit (berpusat di $C$) digambarkan seperti pada Gbr. 22; misalkan $g$ menandakan posisi Greenwich di permukaan bumi dan $l$ adalah posisi tempat lain. Sudut antara meridian $plq$ dan $pgq$ adalah bujur terestrial dari tempat $l$, yang dalam hal ini berada di sebelah barat Greenwich. Tarik garis $Cg$ dan $Cl$ hingga memotong bola langit di $G$ dan $L$, yang berturut-turut merupakan zenit bagi Greenwich dan $l$. Jika $X$ adalah posisi suatu benda langit pada saat tertentu, maka $G\hat{P}X$ adalah sudut jam $X$ untuk pengamat di meridian Greenwich, dan $L\hat{P}X$ adalah sudut jam untuk pengamat di meridian $l$. Karena $G\hat{P}X = L\hat{P}X + G\hat{P}L$ dan $G\hat{P}L = g\hat{p}l$, maka:
"""
st.markdown(materi_bab_2_bagian_12, unsafe_allow_html=True)
st.image("Gambar_22.jpg", caption="Gambar 22: Hubungan Waktu Sideris Lokal dan Bujur Terestrial", use_container_width=True)

materi_bab_2_bagian_13 = r"""
$$ \text{H.A. dari } X \text{ di Greenwich} = \text{H.A. dari } X \text{ di } l + \text{bujur (dalam waktu) dari } l \dots\dots(13) $$

Dalam rumus ini, bujur dari $l$ diasumsikan diekspresikan dalam satuan waktu ($15^\circ = 1^h; 15' = 1^m; 15'' = 1^s$). Rumus (13) bersifat umum dan berlaku pula untuk ekuinoks musim semi $\Upsilon$. Mengingat waktu sideris adalah sudut jam dari titik $\Upsilon$, kita memperoleh:

$$ \text{Sid. time di Greenwich} = \text{Sid. time di } l \pm \text{bujur dari } l \dots(14) $$

di mana tanda $+$ digunakan jika $l$ berada di sebelah barat Greenwich, dan tanda $-$ jika $l$ berada di sebelah timur Greenwich. Waktu sideris di tempat $l$ disebut waktu sideris lokal (*local sidereal time*, L.S.T.).

### 28. Waktu matahari rata-rata.
Hari sideris adalah satuan waktu observatorium yang terbukti tidak praktis untuk urusan kehidupan sehari-hari yang sebagian besar diatur oleh posisi matahari di langit. Ketika matahari berada di meridian suatu tempat, saat itu adalah tengah hari semu (*apparent noon*); ketika matahari kembali ke meridian tersebut, satu hari matahari semu (*apparent solar day*) telah berlalu. Interval ini dapat diukur menggunakan jam berskala waktu sideris yang akurat, dan terbukti bahwa durasi hari matahari semu tidak konstan. Seperti yang telah kita ketahui, relatif terhadap bumi, matahari tampak menelusuri orbit elips, dan kecepatan perubahannya di orbit tidak seragam. Akibatnya, matahari tampak bergerak di sepanjang ekliptika dengan laju yang tidak beraturan terhadap latar belakang bintang-bintang. Ditambah lagi dengan kenyataan bahwa matahari bergerak di ekliptika—bukan di ekuator langit (lingkaran besar acuan tempat pengukuran sudut jam dihubungkan)—asensio rektanya tidak meningkat secara seragam. Rata-rata dari hari-hari matahari semu sepanjang tahun disebut hari matahari rata-rata (*mean solar day*). Untuk kenyamanan, hari matahari rata-rata didefinisikan sebagai selang waktu antara dua transit berturut-turut pada meridian pengamat oleh benda fiktif yang disebut matahari rata-rata (*mean sun*). Matahari rata-rata ini diasumsikan bergerak di ekuator langit dengan laju seragam mengelilingi bumi, dengan kecepatan sedemikian rupa sehingga ia menyelesaikan satu revolusi dalam waktu yang sama dengan waktu yang dibutuhkan matahari sejati untuk menyelesaikan satu putaran penuh di ekliptika. Berdasarkan definisi ini, asensio rekta matahari rata-rata (dilambangkan dengan R.A.M.S.) bertambah secara seragam.

Jika kita memandang matahari rata-rata sebagai benda langit biasa, pada momen apa pun ia memiliki sudut jam tertentu (H.A.M.S.) di suatu tempat di permukaan bumi. Jika asensio rektanya diketahui pada saat itu, maka dari persamaan (8) atau (9) kita peroleh:

$$ \text{Sid. time} = \text{H.A.M.S.} + \text{R.A.M.S.} \dots\dots(15) $$

Waktu yang ditunjukkan oleh jam waktu rata-rata (misalnya di Greenwich) berkaitan langsung dengan nilai H.A.M.S. di tempat tersebut. Jika R.A.M.S. diketahui, persamaan (15) menjadi dasar perbandingan antara waktu sideris dan jam waktu rata-rata. Hubungan antara matahari rata-rata dan matahari sejati akan dibahas pada bab berikutnya. Untuk saat ini, cukup diketahui bahwa selisih antara asensio rekta matahari rata-rata dan matahari sejati pada saat apa pun dapat dihitung; selisih ini disebut perataan waktu (*equation of time*)*, dilambangkan dengan $E$:

$$ E = \text{R.A.M.S.} - \text{R.A. } \odot \dots\dots(16) $$

*(Catatan kaki: Dalam buku-buku teks lama, perataan waktu didefinisikan sebagai $E = \text{R.A. } \odot - \text{R.A.M.S.}$, namun konvensi (16) adalah yang kini umum digunakan).*

di mana R.A. $\odot$ menyatakan asensio rekta matahari sejati. $E$ dapat bernilai positif atau negatif serta bervariasi secara kompleks (penghitungan detail mengenai $E$ dibahas di Bagian 91). Pada Gbr. 23, misalkan pada suatu waktu asensio rekta dan deklinasi matahari ($\odot$) diketahui. Misalkan $\Upsilon$ adalah ekuinoks musim semi saat itu, sehingga $R\hat{P}\Upsilon$ atau $R\Upsilon$ adalah sudut jam $\Upsilon$ (yakni waktu sideris lokal). Dengan diketahuinya nilai ini, posisi $\Upsilon$ dan matahari pada bola langit dapat ditentukan. Di sini $\Upsilon K = \text{R.A. } \odot$ dan $K\odot$ adalah deklinasi matahari.
"""
st.markdown(materi_bab_2_bagian_13, unsafe_allow_html=True)
st.image("Gambar_23.jpg", caption="Gambar 23: Perataan Waktu dan Sudut Jam Matahari Rata-rata", use_container_width=True)

materi_bab_2_bagian_14 = r"""
Misalkan nilai $E$ bernilai positif; berdasarkan persamaan (16), R.A.M.S. lebih besar daripada R.A. $\odot$, sehingga posisi matahari rata-rata $M$ dapat ditentukan pada diagram. Sudut $R\hat{P}M$ atau $RM$ adalah sudut jam matahari rata-rata (H.A.M.S.). Dari Gbr. 23, karena $RK = RM + MK$, terlihat bahwa:

$$ \text{H.A. } \odot = \text{H.A.M.S.} + E \dots\dots(17) $$

Relasi ini sangat penting untuk menghubungkan H.A.M.S. dan H.A. $\odot$, sehingga kita dapat menghitung sudut jam matahari sejati ketika kuantitas lainnya diketahui. Ketika matahari rata-rata berada di meridian pengamat, saat itu adalah tengah hari rata-rata lokal (*local mean noon*). Ketika matahari rata-rata berada di meridian Greenwich, saat itu adalah tengah hari rata-rata Greenwich. Sudut jam matahari rata-rata di Greenwich dinotasikan sebagai G.M.A.T. (*Greenwich mean astronomical time*). Ketika matahari rata-rata berada di titik $T$—di mana H.A.M.S. bernilai $12^h$—ia disebut tengah malam rata-rata (*mean midnight*). Ketika G.M.A.T. $= 12^h$, saat itu adalah tengah malam rata-rata di Greenwich, yang menandai dimulainya hari sipil baru di Greenwich. Waktu rata-rata yang dihitung dari tengah malam di Greenwich disebut *Greenwich Mean Time* (G.M.T.)*, yang sekarang ditetapkan sebagai *Universal Time* (U.T.). Jelas bahwa:

$$ \text{U.T.} \equiv \text{G.M.T.} = \text{G.M.A.T.} + 12^h \dots\dots(18) $$

Demikian pula, untuk tempat mana pun yang menggunakan waktu rata-rata berdasarkan meridiannya:

$$ \text{Local M.T.} = \text{Local M.A.T.} + 12^h \dots\dots(19) $$

$$ = \text{H.A.M.S.} \pm 12^h \dots\dots(20) $$

Persamaan (14) memberikan hubungan antara waktu sideris di Greenwich dan waktu sideris di tempat $l$. Dari Gbr. 22 serta persamaan (18) dan (19), hubungan serupa juga berlaku antara waktu rata-rata di Greenwich dan waktu rata-rata lokal di tempat tersebut:

$$ \text{U.T.} \equiv \text{G.M.T.} = \text{Local M.T.} \pm \text{bujur dari } l \dots\dots(21) $$

di mana tanda $+$ digunakan jika bujur $l$ berada di barat dan tanda $-$ jika berada di timur.

Kebingungan pasti akan timbul jika setiap tempat menggunakan waktu rata-rata yang persis sesuai dengan meridian lokalnya. Oleh karena itu, di negara-negara yang relatif kecil, dipilih satu waktu rata-rata standar yang berkorespondensi dengan meridian bujur khusus (meridian standar) untuk digunakan secara seragam di seluruh negeri. Di Inggris Raya, waktu standar tersebut adalah G.M.T. Di negara yang luas seperti Rusia atau Amerika Serikat, digunakan dua atau lebih waktu standar berdasarkan zona bujur; di setiap zona, waktu standar yang disesuaikan dengan meridian tertentu dalam zona tersebut akan dipertahankan. Waktu standar yang didasarkan pada meridian tertentu ini disebut waktu zona (*zone time*, Z.T.). Sistem ini secara umum juga digunakan oleh kapal-kapal di laut untuk menghindari komplikasi geografis. Hubungannya adalah sebagai berikut:

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
st.markdown(materi_bab_2_bagian_17, unsafe_allow_html=True)
