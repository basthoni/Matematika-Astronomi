import streamlit as st

st.set_page_config(page_title="Bab 1 - Trigonometri Bola", page_icon="📖", layout="wide")

# CSS Khusus untuk membuat teks rata kanan-kiri (Justify)
st.markdown("""
<style>
div[data-testid="stMarkdownContainer"] p {
    text-align: justify;
}
</style>
""", unsafe_allow_html=True)

st.title("BAB I")
st.header("TRIGONOMETRI BOLA")
st.divider()

# ==========================================
# DAFTAR ISI (SIDEBAR NAVIGATION)
# ==========================================
with st.sidebar:
    st.markdown("### 📑 Daftar Isi Bab 1")
    st.markdown("""
    - [1. Pendahuluan](#1-pendahuluan)
    - [2. Segitiga bola](#2-segitiga-bola)
    - [3. Panjang busur lingkaran kecil](#3-panjang-busur-lingkaran-kecil)
    - [4. Lintang dan bujur terestrial](#4-lintang-dan-bujur-terestrial)
    - [5. Rumus kosinus](#5-rumus-kosinus-the-cosine-formula)
    - [6. Rumus sinus](#6-rumus-sinus-the-sine-formula)
    - [7. Rumus Analogi](#7-rumus-analogi-the-analogue-formula)
    - [8. Rumus empat bagian](#8-rumus-empat-bagian-the-four-parts-formula)
    - [9. Pembuktian alternatif](#9-pembuktian-alternatif-dari-rumus-a-b-dan-c)
    - [10. Segitiga siku-siku & kuadran](#10-segitiga-siku-siku-dan-kuadran-right-angled-and-quadrantal-triangles)
    - [11. Rumus Polar](#11-rumus-polar)
    - [12. Contoh numerik](#12-contoh-numerik)
    - [13. Rumus haversine](#13-rumus-haversine)
    - [14. Metode lain](#14-metode-lain-another-method)
    - [15. Rasio sudut kecil](#15-rasio-rasio-trigonometri-untuk-sudut-sudut-kecil)
    - [16. Analogi Delambre & Napier](#16-analogi-analogi-delambre-dan-napier)
    - [Latihan Soal](#latihan-soal-exercises)
    """)

# ==========================================
# HALAMAN 1 - 10 (Sesuai Koreksi Verbatim)
# ==========================================
materi_bab_1_hal_1_2 = r"""
### 1. Pendahuluan
Ketika kita memandang bintang-bintang di malam yang cerah, kita mendapatkan kesan yang lazim bahwa mereka semua adalah titik-titik cahaya yang berkilauan, yang seolah-olah terletak di permukaan sebuah bola raksasa di mana masing-masing pengamat menjadi pusatnya. Mata telanjang tentu saja gagal memberikan indikasi apa pun mengenai jarak bintang-bintang tersebut dari kita; namun, hal ini memungkinkan kita untuk membuat perkiraan tentang sudut yang dibentuk di titik pengamat oleh setiap pasang bintang, dan dengan instrumen yang tepat, sudut-sudut ini dapat diukur dengan presisi yang sangat tinggi. Astronomi Bola pada dasarnya berkaitan dengan **arah** di mana bintang-bintang tersebut dilihat, dan sangatlah mudah untuk mendefinisikan arah-arah ini dalam bentuk posisi di permukaan sebuah bola—yakni **bola langit** (*celestial sphere*)—di mana garis lurus yang menghubungkan pengamat ke bintang-bintang berpotongan dengan permukaan ini. Dalam pengertian inilah ungkapan umum "posisi sebuah bintang di bola langit" harus ditafsirkan. Jari-jari bola langit ini sepenuhnya bersifat sembarang. Fondasi dari Astronomi Bola adalah geometri bola.

### 2. Segitiga bola
Setiap bidang yang melewati pusat sebuah bola akan memotong permukaan bola tersebut membentuk sebuah lingkaran yang disebut sebagai **lingkaran besar** (*great circle*). Bidang lain mana pun yang memotong bola tetapi tidak melewati titik pusat juga akan memotong permukaan membentuk sebuah lingkaran, yang dalam hal ini disebut sebagai **lingkaran kecil** (*small circle*). 

Pada Gambar 1, EAB adalah sebuah lingkaran besar, karena bidangnya melewati O, yaitu pusat bola. Misalkan QOP adalah diameter bola yang tegak lurus terhadap bidang lingkaran besar EAB. Misalkan R adalah titik mana pun pada OP dan asumsikan sebuah bidang ditarik melalui R sejajar dengan bidang EAB; permukaan bola tersebut kemudian dipotong membentuk lingkaran kecil FCD. Berdasarkan konstruksinya, OP juga tegak lurus terhadap bidang FCD. Titik-titik ujung P dan Q dari diameter tegak lurus QOP ini disebut sebagai **kutub** (*poles*) dari lingkaran besar dan dari lingkaran kecil yang sejajar tersebut. Sekarang misalkan PCAQ adalah sembarang lingkaran besar yang melewati kutub P dan Q serta memotong lingkaran kecil FCD dan lingkaran besar EAB berturut-turut di C dan A. Demikian pula, PDB adalah bagian dari lingkaran besar lain yang melewati P dan Q. Untuk memudahkan, kita dapat merujuk pada suatu lingkaran besar tertentu cukup dengan menyebutkan bagian mana pun dari garis kelilingnya. Ketika dua lingkaran besar berpotongan di satu titik, mereka dikatakan membentuk sebuah **sudut bola** (*spherical angle*) yang didefinisikan sebagai berikut. Perhatikan dua lingkaran besar PA dan PB yang berpotongan di P. Tarik garis PS dan PT, yang merupakan garis singgung terhadap keliling PA dan PB berturut-turut.
"""
st.markdown(materi_bab_1_hal_1_2, unsafe_allow_html=True)

st.image("Gambar_1.png", caption="Gambar 1", use_container_width=True)

materi_bab_1_hal_2_4 = r"""
PT, berdasarkan konstruksinya, tegak lurus terhadap jari-jari OP dari lingkaran besar PB dan, karena berada di bidang PBO, maka sejajar dengan jari-jari OB. Demikian pula PS sejajar dengan jari-jari OA. Sudut SPT mendefinisikan sudut bola di P antara dua lingkaran besar PA dan PB, dan nilainya sama dengan sudut AOB, di mana AB adalah busur yang terpotong pada lingkaran besar, di mana P adalah kutubnya, di antara dua lingkaran besar PA dan PB. Perlu ditekankan bahwa sudut bola hanya didefinisikan dengan mengacu pada dua lingkaran besar yang berpotongan.

Jika kita diberikan sembarang tiga titik pada permukaan sebuah bola, maka bola tersebut dapat dibelah dua sehingga ketiga titik tersebut terletak di belahan bola yang sama. Jika titik-titik tersebut dihubungkan oleh busur-busur lingkaran besar yang semuanya terletak pada belahan bola ini, bangun yang diperoleh disebut **segitiga bola** (*spherical triangle*). Jadi, pada Gambar 1, tiga titik A, X, dan Y di permukaan bola dihubungkan oleh busur lingkaran besar untuk membentuk segitiga bola AXY. AX, AY, dan XY adalah **sisi-sisi** dan sudut bola di A, X, dan Y adalah sudut-sudut dari segitiga bola tersebut. Sebenarnya, jika R adalah jari-jari bola, panjang busur lingkaran besar AY dirumuskan dengan:

$$
AY = R \times \text{sudut } AOY,
$$

di mana sudut AOY dinyatakan dalam ukuran melingkar, yaitu dalam radian. Karena untuk semua busur lingkaran besar pada bola jari-jari R adalah konstan, maka memudahkan jika kita menganggap panjangnya sebagai satu kesatuan (*unity*). Busur AY kemudian secara sederhana adalah sudut yang dibentuknya di pusat bola. Jika AY adalah, katakanlah, seperdelapan dari keliling lingkaran besar utuh yang melalui A dan Y, maka sisi AY adalah $\pi/4$ dalam ukuran melingkar dan tidak ada ambiguitas jika dinyatakan sebagai $45^\circ$; demikian pula untuk sisi-sisi segitiga yang tersisa. Berdasarkan definisi segitiga bola, tidak ada sisi yang dapat sama dengan atau lebih besar dari $180^\circ$. Sebagai contoh lain, PAB adalah segitiga bola di mana dua sisinya, PA dan PB, masing-masing membentuk sudut $\pi/2$ radian atau $90^\circ$ di O; dalam contoh ini kita katakan bahwa PA dan PB masing-masing sama dengan $\pi/2$ radian atau $90^\circ$. Tetapi PCD *bukanlah* segitiga bola, karena busur CD bukanlah bagian dari lingkaran besar. Oleh karena itu, rumus-rumus yang akan diturunkan untuk segitiga bola tidak akan berlaku untuk bangun seperti PCD.

### 3. Panjang busur lingkaran kecil
Perhatikan, pada Gambar 1, busur lingkaran kecil CD. Panjangnya dirumuskan dengan:

$$
CD = RC \times \text{sudut } CRD.
$$

Selain itu, panjang busur lingkaran besar AB dirumuskan dengan:

$$
AB = OA \times \text{sudut } AOB.
$$

Tetapi karena bidang FCD sejajar dengan bidang EAB, maka $C\hat{R}D = A\hat{O}B$, karena RC, RD berturut-turut sejajar dengan OA, OB. Oleh karena itu:

$$
CD = \frac{RC}{OA} \cdot AB.
$$

Tetapi, karena OA = OC (jari-jari bola), kita peroleh:

$$
CD = \frac{RC}{OC} \cdot AB.
$$

Sekarang RC tegak lurus terhadap OR; $\therefore RC = OC \cos R\hat{C}O$. Dari kesejajaran RC dan OA, $R\hat{C}O = A\hat{O}C$. Oleh karena itu:

$$
CD = AB \cos A\hat{O}C.
$$

Sekarang AOC adalah sudut yang dibentuk di pusat bola oleh busur lingkaran besar AC. Rumus tersebut kemudian dapat ditulis sebagai:

$$
CD = AB \cos AC,
$$

atau, karena PA = $90^\circ$,

$$
CD = AB \sin PC \dots\dots(1).
$$

### 4. Lintang dan bujur terestrial
Konsep-konsep yang diperkenalkan sejauh ini sekarang akan diilustrasikan dengan mengacu pada bumi. Untuk banyak masalah praktis, bumi dapat dianggap sebagai benda bola yang berputar pada poros diameternya PQ (Gambar 2). P adalah kutub utara dan Q adalah kutub selatan. Lingkaran besar yang bidangnya tegak lurus terhadap PQ disebut **ekuator**. Setiap setengah-lingkaran besar yang dibatasi oleh P dan Q adalah sebuah
"""
st.markdown(materi_bab_1_hal_2_4, unsafe_allow_html=True)

st.image("Gambar_2.png", caption="Gambar 2", use_container_width=True)

materi_bab_1_hal_5_6 = r"""
**meridian**. Secara khusus, meridian yang melewati instrumen fundamental (lingkaran transit) di Observatorium Greenwich, berdasarkan kesepakatan universal, dianggap sebagai meridian utama atau meridian standar; misalkan meridian tersebut adalah PGKQ pada Gambar 2, yang memotong ekuator di K. Misalkan PHLQ adalah meridian lain yang memotong ekuator di L. Sudut KOL didefinisikan sebagai **bujur** (*longitude*) dari meridian PHQ dan sama halnya dapat dideskripsikan sebagai busur ekuatorial KL atau sudut bola KPL. Bujur diukur dari $0^\circ$ hingga $180^\circ$ ke arah timur dari meridian Greenwich dan dari $0^\circ$ hingga $180^\circ$ ke arah barat, mengikuti arah panah di dekat K pada Gambar 2. Jadi, dari gambar tersebut, bujur dari meridian PHQ adalah sekitar $100^\circ$ timur (E) dan dari meridian PMQ adalah sekitar $60^\circ$ barat (W). Semua tempat di meridian yang sama memiliki bujur yang sama, dan meridian tempat suatu tempat tertentu berada dispesifikasikan dengan mengacu pada meridian utama PGQ. Untuk menentukan secara lengkap posisi suatu tempat di permukaan bumi, kita perlu mendeskripsikan posisinya pada meridian bujurnya. Hal ini dilakukan dengan mengacu pada ekuator. Perhatikan suatu tempat J di meridian PHQ. Meridian yang melewati J memotong ekuator di L dan sudut LOJ, atau busur lingkaran besar LJ, disebut sebagai **lintang** (*latitude*) dari J. Jika J berada di antara ekuator dan kutub utara P, seperti pada Gambar 2, lintangnya disebut lintang utara (N); suatu tempat seperti R, di antara ekuator dan kutub selatan Q, disebut memiliki lintang selatan (S). Dengan cara ini, posisi titik mana pun di permukaan bumi dirujuk pada dua lingkaran besar yang mendasar, yaitu ekuator dan meridian Greenwich.

Misalkan $\phi$ melambangkan lintang J; maka $L\hat{O}J$ atau $LJ = \phi$. Karena OP tegak lurus terhadap bidang ekuator, $P\hat{O}L = 90^\circ$ dan oleh karena itu $POJ = 90^\circ - \phi$. Sudut POJ atau busur bola PJ adalah kolintang (*colatitude*) dari J. Kita peroleh dengan demikian:

$$
\text{Colat.} = 90^\circ - \text{Lat.}
$$

Semua tempat yang memiliki lintang yang sama terletak pada lingkaran kecil yang sejajar dengan ekuator, disebut sebagai *paralel lintang* (*parallel of latitude*). Dengan demikian, semua tempat dengan lintang yang sama dengan Greenwich terletak pada lingkaran kecil MGHX. Jika $\theta$ melambangkan lintang Greenwich, maka berdasarkan rumus (1) panjang busur lingkaran kecil HX, misalnya, diberikan dalam bentuk panjang busur ekuatorial yang bersesuaian LY oleh:

$$
HX = LY \cos \theta \dots\dots(2).
$$

Untuk memberikan presisi yang lebih besar terhadap makna rumus ini, kita mempertimbangkan unit-unit di mana jarak pada permukaan bumi dinyatakan. Yang paling sederhana adalah yang didefinisikan sebagai jarak lingkaran besar di antara dua titik yang membentuk sudut satu menit busur di pusat bumi—unit ini dikenal sebagai **mil laut** (*nautical mile*) dan setara dengan 6080 kaki (kita mengabaikan variasi kecil dalam nilai ini karena fakta bahwa bumi tidak sepenuhnya bulat sempurna). Jika perbedaan bujur antara dua tempat yang mana pun di paralel lintang yang sama diketahui, misal LY, maka LY dapat dinyatakan sebagai sekian menit busur dan angka ini adalah jumlah mil laut di antara dua titik L dan Y di ekuator. Rumus (2) kemudian menyediakan sarana untuk menghitung jarak antara H dan X yang dinyatakan dalam mil laut (atau menit busur) dan *diukur sepanjang paralel lintang*.

### 5. Rumus kosinus (The cosine-formula)
Misalkan ABC adalah sebuah segitiga bola (Gambar 3). Nyatakan sisi-sisinya BC, CA, AB masing-masing dengan a, b, dan c. Kemudian, berdasarkan definisi kita,
"""
st.markdown(materi_bab_1_hal_5_6, unsafe_allow_html=True)

st.image("Gambar_3.png", caption="Gambar 3", use_container_width=True)

materi_bab_1_hal_7_10 = r"""
sisi a diukur dari sudut BOC yang dibentuk di pusat O dari bola oleh busur lingkaran besar BC. Demikian pula, b dan c diukur masing-masing oleh sudut AOC dan AOB. Misalkan AD adalah garis singgung di A ke lingkaran besar AB dan AE adalah garis singgung di A ke lingkaran besar AC. Maka jari-jari OA tegak lurus terhadap AD dan AE. Berdasarkan konstruksi, AD terletak pada bidang lingkaran besar AB; oleh karena itu, jika jari-jari OB diperpanjang, ia akan memotong garis singgung AD di suatu titik D. Demikian pula, jari-jari OC saat diperpanjang akan bertemu dengan garis singgung AE di E. Sekarang sudut bola BAC didefinisikan sebagai sudut antara garis singgung di A terhadap lingkaran besar AB dan AC, sehingga sudut bola $BAC = D\hat{A}E$. Sudut bola BAC akan dilambangkan secara sederhana dengan A, sehingga $D\hat{A}E = A$.

Sekarang, pada segitiga bidang datar OAD, $O\hat{A}D$ bernilai $90^\circ$ dan $A\hat{O}D$, yang identik dengan $A\hat{O}B$, bernilai c. Maka kita peroleh:

$$
\begin{aligned}
AD &= OA \tan c ; \\
OD &= OA \sec c \dots\dots(3).
\end{aligned}
$$

Dari segitiga bidang datar OAE, secara serupa, kita peroleh:

$$
\begin{aligned}
AE &= OA \tan b ; \\
OE &= OA \sec b \dots\dots(4).
\end{aligned}
$$

Dari segitiga bidang datar DAE, kita peroleh:

$$
DE^2 = AD^2 + AE^2 - 2AD \cdot AE \cos D\hat{A}E,
$$

atau

$$
DE^2 = OA^2 [\tan^2 c + \tan^2 b - 2 \tan b \tan c \cos A] \dots\dots(5).
$$

Dari segitiga bidang datar DOE,

$$
DE^2 = OD^2 + OE^2 - 2OD \cdot OE \cos D\hat{O}E.
$$

Tetapi $D\hat{O}E = B\hat{O}C = a$;

$$
\therefore DE^2 = OA^2 [\sec^2 c + \sec^2 b - 2 \sec b \sec c \cos a] \dots\dots(6).
$$

Oleh karena itu, dari persamaan (5) dan (6),

$$
\sec^2 c + \sec^2 b - 2 \sec b \sec c \cos a = \tan^2 c + \tan^2 b - 2 \tan b \tan c \cos A.
$$
"""
st.markdown(materi_bab_1_hal_7_10, unsafe_allow_html=True)

with st.expander("Syarah: Penurunan Rumus Kosinus Fundamental"):
    st.markdown(r"""
    Buku teks melakukan lompatan penyederhanaan aljabar dari persamaan (5) dan (6) menuju hasil akhirnya. Berikut uraian detailnya:
    1. Samakan kedua persamaan $DE^2$: $\sec^2 c + \sec^2 b - 2 \sec b \sec c \cos a = \tan^2 c + \tan^2 b - 2 \tan b \tan c \cos A$
    2. Gunakan identitas Pythagoras $\sec^2 \theta = 1 + \tan^2 \theta$ pada ruas kiri: $(1 + \tan^2 c) + (1 + \tan^2 b) - 2 \sec b \sec c \cos a = \tan^2 c + \tan^2 b - 2 \tan b \tan c \cos A$
    3. Coret nilai $\tan^2 c$ dan $\tan^2 b$ di kedua ruas, kemudian kurangi kedua ruas dengan 2.
    4. Setelah itu bagi seluruh persamaan dengan $-2$, sehingga menyisakan: $\sec b \sec c \cos a = \tan b \tan c \cos A$ 
    5. Ubah ke bentuk rasio dasar: $\left(\frac{1}{\cos b \cos c}\right) \cos a = \left(\frac{\sin b \sin c}{\cos b \cos c}\right) \cos A$
    6. Kalikan seluruh ruas dengan $(\cos b \cos c)$ sehingga penyebutnya hilang.
    7. Pindah ruaskan persamaan sehingga terbukti: $\cos a = \cos b \cos c + \sin b \sin c \cos A$.
    """)

materi_bab_1_hal_7_10_lanjut = r"""
Sekarang $\sec^2 c = 1 + \tan^2 c$, $\sec^2 b = 1 + \tan^2 b$, dan setelah beberapa penyederhanaan kita memperoleh:

$$
\cos a = \cos b \cos c + \sin b \sin c \cos A \dots\dots(A).
$$

Ini adalah rumus fundamental dari trigonometri bola dan pada halaman-halaman selanjutnya akan disebut sebagai **rumus kosinus** (*cosine-formula*) atau rumus **A**. Jelas terdapat dua rumus pendampingnya; mereka adalah:

$$
\begin{aligned}
\cos b &= \cos c \cos a + \sin c \sin a \cos B \dots\dots(7), \\
\cos c &= \cos a \cos b + \sin a \sin b \cos C \dots\dots(8).
\end{aligned}
$$

Dari ketiga rumus—**A**, (7) dan (8)—semua rumus trigonometri bola lain yang digunakan dapat diturunkan. Rumus fundamental memiliki dua penerapan praktis secara langsung:
(1) Jika dua sisi, misal b dan c, dan sudut yang diapit A dari segitiga bola ABC diketahui, rumus **A** memungkinkan penghitungan atas sisi ketiga a dilakukan.
(2) Jika ketiga sisi diketahui, sudut-sudut segitiga dapat ditemukan secara berurutan dengan menggunakan **A**, (7) dan (8).

Karena, seandainya nilai A yang dicari; maka melalui **A**:

$$
\cos A = \text{cosec } b \text{ cosec } c [\cos a - \cos b \cos c] \dots\dots(9).
$$

Rumus (9) dapat digantikan dengan bentuk yang lebih cocok untuk penghitungan logaritmik sebagai berikut. Karena $\cos A = 1 - 2 \sin^2 \frac{A}{2}$, kita peroleh, dari **A**,

$$
\begin{aligned}
\cos a &= \cos b \cos c + \sin b \sin c \left(1 - 2 \sin^2 \frac{A}{2}\right) \\
&= \cos (b - c) - 2 \sin b \sin c \sin^2 \frac{A}{2},
\end{aligned}
$$

atau

$$
\cos (b - c) - \cos a = 2 \sin b \sin c \sin^2 \frac{A}{2};
$$

$$
\therefore 2 \sin \frac{a + (b - c)}{2} \sin \frac{a - (b - c)}{2} = 2 \sin b \sin c \sin^2 \frac{A}{2}.
$$

Misalkan s didefinisikan dengan:

$$
2s = a + b + c \dots\dots(10).
$$

Maka $a + b - c = 2 (s - c)$ dan $a - b + c = 2 (s - b)$.
Oleh karena itu:

$$
\begin{aligned}
\sin (s - b) \sin (s - c) &= \sin b \sin c \sin^2 \frac{A}{2}; \\
\therefore \sin \frac{A}{2} &= \sqrt{\frac{\sin (s - b) \sin (s - c)}{\sin b \sin c}} \dots\dots(11).
\end{aligned}
$$

Bentuk ini berguna dalam pengerjaan numerik. Terdapat dua persamaan serupa yang memberikan $\sin \frac{B}{2}$ dan $\sin \frac{C}{2}$.

Jika kita menulis $\cos A = 2 \cos^2 \frac{A}{2} - 1$ ke dalam rumus **A** dan memprosesnya seperti sebelumnya, kita akan memperoleh:

$$
\cos \frac{A}{2} = \sqrt{\frac{\sin s \sin (s - a)}{\sin b \sin c}} \dots\dots(12)
$$

dengan dua persamaan serupa yang memberikan $\cos \frac{B}{2}$ dan $\cos \frac{C}{2}$.

Melalui pembagian persamaan (11) dan (12) kita peroleh:

$$
\tan \frac{A}{2} = \sqrt{\frac{\sin (s - b) \sin (s - c)}{\sin s \sin (s - a)}} \dots\dots(13).
$$

Terdapat dua persamaan serupa, yang memberikan $\tan \frac{B}{2}$ dan $\tan \frac{C}{2}$. 
Persamaan (11), (12) maupun (13) mana pun dapat digunakan untuk menghitung A, jika ketiga sisinya diketahui.

### 6. Rumus sinus (The sine-formula)
Kita sekarang akan menurunkan apa yang dikenal sebagai rumus sinus. Dari rumus kosinus A, kita peroleh:

$$
\sin b \sin c \cos A = \cos a - \cos b \cos c.
$$

Dengan mengkuadratkannya, kita memperoleh:

$$
\sin^2 b \sin^2 c \cos^2 A = \cos^2 a - 2 \cos a \cos b \cos c + \cos^2 b \cos^2 c.
$$

Sisi sebelah kiri dapat ditulis sebagai:

$$
\sin^2 b \sin^2 c - \sin^2 b \sin^2 c \sin^2 A,
$$

atau

$$
1 - \cos^2 b - \cos^2 c + \cos^2 b \cos^2 c - \sin^2 b \sin^2 c \sin^2 A.
$$
"""
st.markdown(materi_bab_1_hal_7_10_lanjut, unsafe_allow_html=True)

with st.expander("Syarah: Proses Aljabar Menuju Rumus Sinus"):
    st.markdown(r"""
    Buku mengasumsikan pembaca memahami bahwa pada ruas kiri:
    $\sin^2 b \sin^2 c \cos^2 A$ dapat diubah dengan substitusi $\cos^2 A = 1 - \sin^2 A$.
    Sehingga menjadi $\sin^2 b \sin^2 c (1 - \sin^2 A) = \sin^2 b \sin^2 c - \sin^2 b \sin^2 c \sin^2 A$.
    Kemudian, pada bentuk substitusi kedua, buku mengganti $\sin^2 b \sin^2 c$ dengan $(1-\cos^2 b)(1-\cos^2 c)$, yang apabila dikalikan akan menghasilkan $1 - \cos^2 b - \cos^2 c + \cos^2 b \cos^2 c$.
    """)

materi_bab_1_hal_7_10_akhir = r"""
Oleh karena itu:

$$
\sin^2 b \sin^2 c \sin^2 A = 1 - \cos^2 a - \cos^2 b - \cos^2 c + 2 \cos a \cos b \cos c.
$$

Misalkan suatu besaran positif X didefinisikan dengan:

$$
X^2 \sin^2 a \sin^2 b \sin^2 c = 1 - \cos^2 a - \cos^2 b - \cos^2 c + 2 \cos a \cos b \cos c.
$$

Maka, dari persamaan sebelumnya,

$$
\frac{\sin^2 A}{\sin^2 a} = X^2,
$$

sehingga

$$
X = \pm \frac{\sin A}{\sin a}.
$$

Tetapi dalam segitiga bola, masing-masing sisinya kurang dari $180^\circ$, dan hal ini juga berlaku untuk sudut-sudutnya. Karena $\sin \theta$ bernilai positif untuk semua nilai $\theta$ antara $0^\circ$ dan $180^\circ$, tanda minus pada persamaan di atas tidak dapat diterima (*inadmissible*), dan kita peroleh:

$$
X = \frac{\sin A}{\sin a}.
$$

Dengan memproses persamaan (7) dan (8) menggunakan cara yang serupa, kita akan memperoleh:

$$
X = \frac{\sin B}{\sin b} = \frac{\sin C}{\sin c}.
$$

Oleh karena itu:

$$
\frac{\sin A}{\sin a} = \frac{\sin B}{\sin b} = \frac{\sin C}{\sin c} \dots\dots(B).
$$

Hasil ini akan kita rujuk sebagai **rumus sinus** (*sine-formula*) atau rumus **B**.
Rumus **B** memberikan suatu relasi antara sembarang dua sisi dari sebuah segitiga dan dua sudut yang berhadapan (*opposite*) dengan sisi-sisi tersebut. Namun, ia harus digunakan dengan kehati-hatian (*circumspection*) dalam perhitungan numerik; karena, andaikan kedua sisi a dan b beserta sudut B diketahui, maka melalui **B**:

$$
\sin A = \frac{\sin a \sin B}{\sin b},
$$

dari mana nilai $\sin A$ dapat dihitung. Tetapi $\sin(180^\circ - A) = \sin A$, dan tanpa informasi tambahan adalah tidak mungkin untuk memutuskan mana di antara dua sudut $A$ atau $180^\circ - A$ yang merepresentasikan solusi yang benar. Ambiguitas analogis pada trigonometri bidang datar dapat diingatkan kembali ke perhatian pembaca.

### 7. Rumus Analogi (The analogue formula)
Tuliskan persamaan (7) ke dalam bentuk:

$$
\begin{aligned}
\sin c \sin a \cos B &= \cos b - \cos c \cos a \\
&= \cos b - \cos c (\cos b \cos c + \sin b \sin c \cos A) \\
&= \sin^2 c \cos b - \sin b \sin c \cos c \cos A.
\end{aligned}
$$

Oleh karena itu, dengan membaginya dengan $\sin c$, kita peroleh:

$$
\sin a \cos B = \cos b \sin c - \sin b \cos c \cos A \dots\dots(C),
$$

sebuah relasi yang melibatkan ketiga sisi dan dua sudut.
Kita dapat dengan mudah membuktikan dengan cara yang serupa, dimulai dari persamaan (8), bahwa:

$$
\sin a \cos C = \cos c \sin b - \sin c \cos b \cos A \dots\dots(14).
$$

Seperti yang telah kita lihat, rumus kosinus **A** memberikan nilai $\cos a$ dalam bentuk b, c, dan sudut apit A. Rumus-rumus **C** dan (14) adalah, dalam beberapa hal, analog dengan **A** karena rumus tersebut memberikan nilai $\sin a \times \text{kosinus}$ dari salah satu
"""
st.markdown(materi_bab_1_hal_7_10_akhir, unsafe_allow_html=True)


# ==========================================
# HALAMAN 11 - 20 (Materi Baru)
# ==========================================
materi_bab_1_hal_11_12 = r"""
dua sudut B dan C, yang berdekatan dengan sisi a, dalam bentuk b, c dan A. Kita, oleh karena itu, akan merujuk pada rumus **C** atau (14) sebagai rumus analogi.

Rumus **C** juga dapat dibuktikan sebagai berikut. Misalkan sisi c dari segitiga ABC kurang dari $90^\circ$ (kasus ketika c berada di antara $90^\circ$ dan $180^\circ$ dibiarkan sebagai latihan bagi mahasiswa). Perpanjang busur lingkaran besar BA ke D sehingga BD adalah $90^\circ$ (Gbr. 4).
"""
st.markdown(materi_bab_1_hal_11_12, unsafe_allow_html=True)

st.image("Gambar_4.png", caption="Gambar 4", use_container_width=True)

materi_bab_1_hal_11_12_lanjut = r"""
Maka $AD = 90^\circ - c$ dan $C\hat{A}D = 180^\circ - A$. Hubungkan C dan D dengan sebuah busur lingkaran besar dan nyatakan dengan $x$. Dari segitiga DAC, berdasarkan **A**,

$$
\cos x = \cos(90^\circ - c) \cos b + \sin(90^\circ - c) \sin b \cos(180^\circ - A),
$$

atau

$$
\cos x = \sin c \cos b - \cos c \sin b \cos A \dots\dots(15).
$$
"""
st.markdown(materi_bab_1_hal_11_12_lanjut, unsafe_allow_html=True)

with st.expander("Syarah: Perubahan Trigonometri pada Rumus Analogi"):
    st.markdown(r"""
    Buku melompati penjelasan identitas relasi sudut trigonometri. Perubahan dari baris pertama ke persamaan (15) terjadi karena:
    1. $\cos(90^\circ - c) = \sin c$
    2. $\sin(90^\circ - c) = \cos c$
    3. $\cos(180^\circ - A) = -\cos A$
    
    Substitusi ketiga identitas ini secara langsung menghasilkan persamaan (15).
    """)

materi_bab_1_hal_11_12_akhir = r"""
Dari segitiga DBC, berdasarkan **A**,

$$
\cos x = \cos 90^\circ \cos a + \sin 90^\circ \sin a \cos B,
$$

atau

$$
\cos x = \sin a \cos B \dots\dots(16),
$$

dan oleh karena itu dari (15) dan (16)

$$
\sin a \cos B = \cos b \sin c - \sin b \cos c \cos A,
$$

yang mana merupakan rumus **C**.

### 8. Rumus empat bagian (The four-parts formula)
Rumus berguna lainnya, yang dikenal sebagai rumus empat bagian, sekarang akan diturunkan. Pada segitiga bola ABC (Gbr. 5) perhatikan empat bagian berurutan B, a, C, b. Sudut C diapit oleh dua sisi a dan b dan disebut "sudut dalam" (*inner angle*). Sisi a diapit oleh dua sudut B dan C dan disebut "sisi dalam" (*inner side*). Masukkan B dan C menggunakan rumus kosinus; maka kita peroleh:
"""
st.markdown(materi_bab_1_hal_11_12_akhir, unsafe_allow_html=True)

st.image("Gambar_5.png", caption="Gambar 5", use_container_width=True)

materi_bab_1_hal_12_13 = r"""
$$
\begin{aligned}
\cos b &= \cos a \cos c + \sin a \sin c \cos B \dots\dots(17), \\
\cos c &= \cos b \cos a + \sin b \sin a \cos C \dots\dots(18).
\end{aligned}
$$

Substitusikan nilai $\cos c$ yang diberikan oleh (18) ke sisi sebelah kanan dari (17); maka

$$
\begin{aligned}
\cos b &= \cos a (\cos b \cos a + \sin b \sin a \cos C) + \sin a \sin c \cos B; \\
\therefore \cos b \sin^2 a &= \cos a \sin b \sin a \cos C + \sin a \sin c \cos B.
\end{aligned}
$$
"""
st.markdown(materi_bab_1_hal_12_13, unsafe_allow_html=True)

with st.expander("Syarah: Penurunan Aljabar pada Rumus Empat Bagian"):
    st.markdown(r"""
    Buku melompati langkah aljabar dari baris substitusi ke baris $\cos b \sin^2 a$. Berikut rinciannya:
    1. Kalikan $\cos a$ ke dalam kurung: $\cos b = \cos^2 a \cos b + \cos a \sin b \sin a \cos C + \sin a \sin c \cos B$.
    2. Pindahkan suku $\cos^2 a \cos b$ ke ruas kiri: $\cos b - \cos^2 a \cos b = \cos a \sin b \sin a \cos C + \dots$
    3. Faktorkan ruas kiri: $\cos b(1 - \cos^2 a)$.
    4. Menggunakan identitas $(1 - \cos^2 a) = \sin^2 a$, ruas kiri berubah menjadi $\cos b \sin^2 a$.
    """)

materi_bab_1_hal_12_13_lanjut = r"""
Bagi seluruh ruas dengan $\sin a \sin b$; maka

$$
\cot b \sin a = \cos a \cos C + \frac{\sin c}{\sin b} \cos B.
$$

Tetapi dari rumus sinus **B**,

$$
\frac{\sin c}{\sin b} = \frac{\sin C}{\sin B}.
$$

Oleh karena itu,

$$
\cos a \cos C = \sin a \cot b - \sin C \cot B \dots\dots(D),
$$

yang dapat diubah ke dalam bentuk kata-kata, sebagai bantuan ingatan, sebagai berikut:

**$\cos(\text{sisi dalam}) \cdot \cos(\text{sudut dalam}) = \sin(\text{sisi dalam}) \cdot \cot(\text{sisi lain}) - \sin(\text{sudut dalam}) \cdot \cot(\text{sudut lain}).$**

### 9. Pembuktian alternatif dari rumus A, B dan C.
Rumus-rumus **B**, **C** dan **D** telah diturunkan melalui transformasi aljabar dari rumus fundamental. Pembuktian lain dari masing-masing **A**, **B** dan **C** sekarang akan diperoleh secara singkat dari suatu konstruksi geometris yang sederhana dan instruktif. Misalkan ABC (Gbr. 6) adalah sebuah segitiga bola dan O adalah pusat dari bola. Hubungkan O ke titik-titik sudut
"""
st.markdown(materi_bab_1_hal_12_13_lanjut, unsafe_allow_html=True)

st.image("Gambar_6.png", caption="Gambar 6", use_container_width=True)

materi_bab_1_hal_13_15 = r"""
dan ambil sembarang titik P pada OC. Dari P tarik PQ tegak lurus terhadap OA dan PR tegak lurus terhadap OB. Di bidang OAB, tarik QS tegak lurus terhadap OA dan RS tegak lurus terhadap OB. Garis-garis tegak lurus ini bertemu di S. Hubungkan PS dan OS. Jika kita menarik garis-garis singgung di A ke busur-busur lingkaran besar AB dan AC, garis-garis singgung ini, berdasarkan definisi, mengapit sudut bola A. Tetapi QS dan QP, berdasarkan konstruksi, sejajar dengan garis-garis singgung tersebut. Oleh karena itu $P\hat{Q}S = A$. Demikian pula $P\hat{R}S = B$. Juga $C\hat{O}B = a$, $C\hat{O}A = b$ dan $A\hat{O}B = c$.

Langkah pertama adalah membuktikan bahwa PS tegak lurus terhadap bidang AOB. Berdasarkan konstruksi, OQ tegak lurus terhadap PQ maupun QS; oleh karena itu OQ tegak lurus terhadap bidang PQS; karena itu OQ tegak lurus terhadap PS yang mana merupakan sebuah garis yang terletak di dalam bidang PQS. Demikian pula, OR tegak lurus terhadap PS. Jadi PS tegak lurus terhadap OQ maupun OR dan karenanya tegak lurus terhadap setiap garis di dalam bidang OQ dan OR, yaitu, PS tegak lurus terhadap bidang OAB dan, secara khusus, terhadap OS, SQ dan SR. Jadi PQS dan PRS adalah segitiga-segitiga siku-siku.

(1) Kita peroleh, dari segitiga siku-siku OQP dan ORP,

$$
\begin{aligned}
PQ &= OP \sin b ; \quad PR = OP \sin a \dots\dots(19). \\
OQ &= OP \cos b ; \quad OR = OP \cos a \dots\dots(20).
\end{aligned}
$$

Misalkan x melambangkan sudut SOQ; maka $R\hat{O}S = c - x$.
Sekarang $OS = OQ \sec x$ dan $OS = OR \sec (c - x)$.
Oleh karena itu $OR \cos x = OQ \cos (c - x)$;

$$
\begin{aligned}
\therefore \text{dengan (20), } OP \cos a \cos x &= OP \cos b \cos (c - x); \\
\therefore \cos a &= \cos b \cos c + \cos b \sin c \tan x.
\end{aligned}
$$
"""
st.markdown(materi_bab_1_hal_13_15, unsafe_allow_html=True)

with st.expander("Syarah: Ekspansi Aljabar Sudut Geometris"):
    st.markdown(r"""
    Pada baris terakhir, ekspresi $\cos b \cos(c-x)$ dijabarkan menggunakan identitas selisih kosinus:
    $\cos(c-x) = \cos c \cos x + \sin c \sin x$.
    Sehingga persamaan menjadi: $OP \cos a \cos x = OP \cos b (\cos c \cos x + \sin c \sin x)$.
    Bagi kedua ruas dengan $(OP \cos x)$ untuk memperoleh: $\cos a = \cos b \cos c + \cos b \sin c \left(\frac{\sin x}{\cos x}\right)$, atau $\cos a = \cos b \cos c + \cos b \sin c \tan x$.
    """)

materi_bab_1_hal_14_15_lanjut = r"""
Tetapi

$$
\tan x = \frac{QS}{OQ} = \frac{PQ \cos A}{OQ} = \tan b \cos A,
$$

dan oleh karena itu 

$$
\cos a = \cos b \cos c + \sin b \sin c \cos A,
$$

yang mana adalah rumus **A**.

(2) Lagi, dari segitiga-segitiga siku-siku PQS dan PRS,

$$
\begin{aligned}
PS &= PQ \sin PQS = PQ \sin A, \\
\text{dan} \quad PS &= PR \sin PRS = PR \sin B.
\end{aligned}
$$

Oleh karena itu 

$$
PQ \sin A = PR \sin B,
$$

dan $\therefore$ dengan (19),

$$
OP \sin b \sin A = OP \sin a \sin B,
$$

dari mana rumus **B** mengikutinya.

(3) Kita peroleh, dari segitiga-segitiga siku-siku OSQ dan OSR,

$$
\begin{aligned}
QS &= OS \sin x \text{ dan } RS = OS \sin(c - x); \\
\therefore RS \sin x &= QS (\sin c \cos x - \cos c \sin x), \\
\text{atau} \quad RS &= QS (\sin c \cot x - \cos c).
\end{aligned}
$$

Sekarang 

$$
\begin{aligned}
RS &= PR \cos B = OP \sin a \cos B, \\
\text{dan} \quad QS &= PQ \cos A = OP \sin b \cos A, \\
\text{dan} \quad QS \cot x &= OQ = OP \cos b.
\end{aligned}
$$

Oleh karena itu 

$$
\sin a \cos B = \cos b \sin c - \sin b \cos c \cos A,
$$

yang mana adalah rumus **C**.
"""
st.markdown(materi_bab_1_hal_14_15_lanjut, unsafe_allow_html=True)

with st.expander("Syarah: Substitusi ke Rumus C"):
    st.markdown(r"""
    Nilai $QS \cot x = OQ$ didapatkan secara langsung dari definisi tangen sebelumnya di mana $\tan x = \frac{QS}{OQ}$. Maka secara otomatis $\cot x = \frac{OQ}{QS}$, sehingga jika dikali silang menjadi $QS \cot x = OQ$.
    Dengan mensubstitusikan semua relasi panjang ini ke dalam persamaan $RS = QS \sin c \cot x - QS \cos c$, kita langsung mendapatkan bentuk baku Rumus C.
    """)

materi_bab_1_hal_14_16 = r"""
### 10. Segitiga siku-siku dan kuadran (Right-angled and quadrantal triangles)
Ketika salah satu dari sudut bola adalah $90^\circ$, rumus-rumus **A**, **B**, **C** dan **D** mengambil bentuk yang sederhana. Hal ini juga menjadi kasus yang sama ketika salah satu sisi dari sebuah segitiga bola bernilai $90^\circ$—segitiga ini kemudian disebut sebagai bentuk **kuadran** (*quadrantal*). Aturan-aturan telah diberikan oleh Napier yang dengannya berbagai rumus sederhana dapat dituliskan secara langsung. Aturan-aturan tersebut, bagaimanapun juga, memaksakan beban tambahan pada ingatan dan adalah jauh lebih sederhana untuk mengaplikasikan salah satu dari rumus utama **A** sampai **D** pada segitiga siku-siku atau kuadran tertentu yang dimaksud. Aturan-aturannya adalah sebagai berikut:
"""
st.markdown(materi_bab_1_hal_14_16, unsafe_allow_html=True)

st.image("Gambar_7.png", caption="Gambar 7", use_container_width=True)

materi_bab_1_hal_15_16_lanjut = r"""
(1) Segitiga siku-siku di mana $C = 90^\circ$. Susun di dalam sebuah lingkaran lima "bagian melingkar" (*circular parts*) $a, b, 90^\circ - A, 90^\circ - c, 90^\circ - B$, seperti pada Gbr. 7. Jika salah satu dari bagian melingkar dipilih sebagai "tengah" (*middle*), dua bagian yang mengapit disebut "yang berdekatan" (*adjacents*) dan dua bagian lainnya disebut "yang berhadapan" (*opposites*). Aturan-aturannya kemudian adalah:

**$\sin(\text{tengah}) = \text{hasil kali tangen dari yang berdekatan};$**<br>
**$\sin(\text{tengah}) = \text{hasil kali kosinus dari yang berhadapan}.$**

(2) Segitiga kuadran di mana $c = 90^\circ$. Susun di luar lingkaran (Gbr. 7) lima "bagian melingkar" $A, B, 90^\circ - a, C - 90^\circ, 90^\circ - b$. Maka kedua aturannya adalah sama seperti untuk segitiga siku-siku.

### 11. Rumus Polar
Rumus berguna tertentu dapat diperoleh melalui segitiga polar yang dikonstruksikan sebagai berikut (Gbr. 8). Misalkan ABC adalah sebuah segitiga bola. Lingkaran besar yang memuat busur BC memiliki dua buah kutub, satu di masing-masing belahan yang di mana bola tersebut dibelah oleh lingkaran besar itu.
"""
st.markdown(materi_bab_1_hal_15_16_lanjut, unsafe_allow_html=True)

st.image("Gambar_8.png", caption="Gambar 8", use_container_width=True)

materi_bab_1_hal_15_17 = r"""
Misalkan A' adalah kutub di belahan bumi di mana A berada. Demikian pula B' dan C' adalah kutub-kutub yang sesuai dari CA dan AB. Perpanjang BC kedua arahnya untuk bertemu dengan A'B' dan A'C' masing-masing di L dan M. Maka, karena A' adalah kutub dari lingkaran besar LBCM, sudut bola B'A'C' (atau secara sederhana A') bernilai sama dengan busur LM. Lagi, B' adalah kutub dari AC, artinya, jarak sudut B' dari titik mana pun di AC adalah $90^\circ$; demikian pula jarak sudut A' dari titik mana pun di BC adalah $90^\circ$. Oleh karena itu jarak sudut C dari B' dan dari A' masing-masing adalah $90^\circ$; dengan kata lain, C adalah kutub dari A'B'. Karenanya $CL = 90^\circ$, dan demikian pula $BM = 90^\circ$. Sekarang $LM = LB + BM = LB + 90^\circ$. Juga $BC = a$; $\therefore LB = 90^\circ - a$. Karenanya $A' = 180^\circ - a$. Secara serupa $B' = 180^\circ - b$ dan $C' = 180^\circ - c$. Kita memperoleh dengan cara yang sama:

$$
a' = 180^\circ - A; \quad b' = 180^\circ - B; \quad c' = 180^\circ - C.
$$

Sekarang terapkan rumus **A** pada segitiga A'B'C' dan kita peroleh, misalnya,

$$
\cos a' = \cos b' \cos c' + \sin b' \sin c' \cos A'.
$$

Dengan menggunakan relasi yang baru saja ditemukan, kita memperoleh dari persamaan ini:

$$
-\cos A = \cos B \cos C - \sin B \sin C \cos a,
$$

yang mana adalah sebuah rumus untuk segitiga ABC, memberikan sudut A dalam bentuk dua sudut sisanya dan sisi yang diapit. Prosedur dalam contoh ini dapat diperluas ke salah satu rumus utama yang telah kita turunkan, dengan menuliskan $180^\circ - a$ untuk A, $180^\circ - b$ untuk B, dst., di dalam rumus **A** hingga **D**.

### 12. Contoh numerik.
Untuk mengilustrasikan solusi numerik dari suatu segitiga bola, kita akan mempertimbangkan permasalahan berikut. Pada Gbr. 9 misalkan A dan B merepresentasikan dua tempat, di lintang utara, pada permukaan bumi; lintangnya masing-masing adalah $24^\circ 18' \text{ N}$ dan $36^\circ 47' \text{ N}$, dan bujurnya masing-masing adalah $133^\circ 39' \text{ E}$ dan $125^\circ 24' \text{ W}$; 
"""
st.markdown(materi_bab_1_hal_15_17, unsafe_allow_html=True)

st.image("Gambar_9.png", caption="Gambar 9", use_container_width=True)

materi_bab_1_hal_16_18 = r"""
diminta untuk menemukan (i) panjang busur lingkaran besar AB, (ii) sudut PAB, P menjadi kutub utara, dan (iii) titik paling utara pada lingkaran besar AB.
PAHQ adalah meridian yang melalui A dan memotong ekuator di H. HA mengukur lintang dari A, yaitu $HA = 24^\circ 18'$. PA adalah kolintang dari A;

$$
\therefore PA = 90^\circ - 24^\circ 18' = 65^\circ 42'.
$$

Demikian pula $PB = 53^\circ 13'$. Misalkan meridian Greenwich berpotongan dengan ekuator di G. Maka, mengikuti tanda panah,

$$
\begin{aligned}
GH &= \text{bujur (E) dari } A = 133^\circ 39', \\
\text{dan} \quad GK &= \text{bujur (W) dari } B = 125^\circ 24'.
\end{aligned}
$$

Oleh karena itu busur $HGK = 259^\circ 3'$,
dan karenanya $HK$ (yang lebih pendek dari dua busur lingkaran besar yang menghubungkan H dan K) adalah $100^\circ 57'$; yaitu $A\hat{P}B = 100^\circ 57'$. Di dalam segitiga APB kita sekarang diberikan dua sisi PA dan PB serta sudut yang diapit APB.

(i) *Perhitungan dari AB.* Melalui rumus **A**, kita peroleh

$$
\cos AB = \cos PA \cos PB + \sin PA \sin PB \cos APB,
$$

yang mana menjadi, dengan memasukkan data,

$$
\begin{aligned}
\cos AB &= \cos 65^\circ 42' \cos 53^\circ 13' - \sin 65^\circ 42' \sin 53^\circ 13' \cos 79^\circ 3' \\
&\equiv M - N.
\end{aligned}
$$

Kita akan menggunakan logaritma lima-angka.

$$
\begin{aligned}
\log \cos 65^\circ 42' \cdot 0 &\equiv \bar{1}.61438 \\
\log \cos 53^\circ 13' \cdot 0 &\equiv \bar{1}.77728 \\
\therefore \log M &= \bar{1}.39166 \\
\therefore M &= 0.24641; \\
\\
\log \sin 65^\circ 42' \cdot 0 &\equiv \bar{1}.95971 \\
\log \sin 53^\circ 13' \cdot 0 &\equiv \bar{1}.90358 \\
\log \cos 79^\circ 3' \cdot 0 &\equiv \bar{1}.27864 \\
\therefore \log N &= \bar{1}.14193 \\
\therefore N &= 0.13865.
\end{aligned}
$$

Oleh karena itu, 

$$
\begin{aligned}
\cos AB &\equiv M - N = 0.10776; \\
\therefore AB &= 83^\circ 48'.8 \equiv 5028'.8.
\end{aligned}
$$

Jadi jarak lingkaran besar di antara A dan B adalah $83^\circ 48'.8$ atau $5028.8$ mil laut. Ke nilai menit busur terdekat, $AB = 83^\circ 49'$.
"""
st.markdown(materi_bab_1_hal_16_18, unsafe_allow_html=True)

with st.expander("Syarah: Notasi Logaritma Bar/Garis Atas pada Perhitungan Klasik"):
    st.markdown(r"""
    Dalam buku-buku era klasik, nilai logaritma yang negatif ditulis menggunakan notasi "Bar" (garis di atas angka).
    Contoh: $\bar{1}.61438$ berarti $-1 + 0.61438$. 
    Angka di depan koma (karakteristik) bernilai negatif, sedangkan angka di belakang koma (mantissa) tetap positif. Ini mempermudah perhitungan penjumlahan logaritma manual menggunakan tabel sebelum adanya kalkulator elektronik.
    Selain itu, sudut $\cos 100^\circ 57'$ diubah menjadi $-\cos 79^\circ 3'$ (menggunakan sifat sudut suplemen di kuadran II), sehingga tanda minus ditarik ke depan persamaan menjadi $M - N$.
    """)

materi_bab_1_hal_17_19 = r"""
(ii) *Perhitungan dari PAB.* Melalui rumus **A**,

$$
\cos PB = \cos AB \cos PA + \sin AB \sin PA \cos PAB.
$$

Di dalam persamaan ini, seluruh ketiga sisi PB, AB, PA kini telah diketahui dan oleh karenanya kita dapat menurunkan $P\hat{A}B$. Di dalam contoh ini, pertimbangan geometri sederhana menunjukkan bahwa $P\hat{A}B$ kurang dari $90^\circ$ dan akibatnya rumus sinus **B** dapat digunakan tanpa ada ambiguitas; persamaan yang tepat adalah:

$$
\sin PAB = \frac{\sin APB \cdot \sin PB}{\sin AB},
$$

semua besaran pada sisi kanan kini telah diketahui. Namun demikian, untuk tujuan ilustrasi, kita akan menghitung $P\hat{A}B$ menggunakan rumus (11). Nyatakan AB sebagai p, PB sebagai a dan PA sebagai b; maka

$$
2s = p + a + b = 83^\circ 49' + 53^\circ 13' + 65^\circ 42' = 202^\circ 44'.
$$

Oleh karena itu 

$$
s = 101^\circ 22'; \quad s - p = 17^\circ 33'; \quad s - b = 35^\circ 40'.
$$

Di dalam contoh ini, rumus (11) ditulis sebagai:

$$
\sin \frac{A}{2} = \sqrt{\frac{\sin(s-b)\sin(s-p)}{\sin b \sin p}}.
$$

$$
\begin{aligned}
\log \sin (s - b) &\equiv \log \sin 35^\circ 40' \equiv \bar{1}.76572 \\
\log \sin (s - p) &\equiv \log \sin 17^\circ 33' \equiv \bar{1}.47934 \\
\log \text{cosec } b &\equiv \log \text{cosec } 65^\circ 42' \equiv 0.04029 \\
\log \text{cosec } p &\equiv \log \text{cosec } 83^\circ 49' \equiv 0.00253 \\
\therefore \log \sin^2 \frac{A}{2} &= \bar{1}.28788 \\
\therefore \log \sin \frac{A}{2} &= \bar{1}.64394 \\
\therefore \frac{A}{2} &= 26^\circ 8' \\
\therefore A &= 52^\circ 16'.
\end{aligned}
$$

(iii) *Perhitungan lintang paling utara yang dicapai oleh lingkaran besar AB.* Misalkan C adalah titik paling utara pada AB (Gbr. 9). Maka jelas bahwa paralel lintang yang melalui C akan menyinggung lingkaran besar di C dan bahwa meridian PC akan tegak lurus terhadap lingkaran besar AB di C. Maka $P\hat{C}A$ dan $P\hat{C}B$ masing-masing adalah $90^\circ$. Di dalam segitiga PAC, kita kini mengetahui PA, $P\hat{A}C$ dan $P\hat{C}A$ dan kita diminta menemukan PC. Jelas, rumus **B** dapat digunakan; yakni

$$
\frac{\sin PC}{\sin PAC} = \frac{\sin PA}{\sin PCA},
$$

dan, karena $P\hat{C}A = 90^\circ$, kita memperoleh

$$
\sin PC = \sin PA \sin PAC.
$$

$$
\begin{aligned}
\log \sin PA &\equiv \log \sin 65^\circ 42' \equiv \bar{1}.95971 \\
\log \sin PAC &\equiv \log \sin 52^\circ 16' \equiv \bar{1}.89810 \\
\therefore \log \sin PC &= \bar{1}.85781 \\
\therefore PC &= 46^\circ 7'.
\end{aligned}
$$

Jadi lintang dari C adalah $43^\circ 53'$.
Perhitungan untuk bujur dari C ditinggalkan sebagai latihan bagi pembaca.

### 13. Rumus haversine.
Banyak perhitungan diperpendek secara nyata dengan menggunakan "haversines". Haversine dari suatu sudut $\theta$ (ditulis $\text{hav } \theta$) didefinisikan oleh:

$$
\text{hav } \theta = \frac{1}{2}(1 - \cos \theta) = \sin^2 \frac{\theta}{2} \dots\dots(21).
$$

Karena $\cos \theta = 1 - 2 \sin^2 \frac{\theta}{2}$, kita peroleh:

$$
\cos \theta = 1 - 2 \text{ hav } \theta \dots\dots(22).
$$
"""
st.markdown(materi_bab_1_hal_17_19, unsafe_allow_html=True)

materi_bab_1_hal_19_20 = r"""
Kita kini dapat memodifikasi rumus **A**, yang mana adalah:

$$
\cos a = \cos b \cos c + \sin b \sin c \cos A.
$$

Berdasarkan (22) tuliskan $(1 - 2 \text{ hav } a)$ untuk $\cos a$, dan $(1 - 2 \text{ hav } A)$ untuk $\cos A$. Maka

$$
1 - 2 \text{ hav } a = \cos (b - c) - 2 \sin b \sin c \text{ hav } A.
$$

Tuliskan $1 - 2 \text{ hav } (b - c)$ untuk $\cos (b - c)$. Maka kita peroleh

$$
\text{hav } a = \text{hav } (b - c) + \sin b \sin c \text{ hav } A \dots\dots(23),
$$

yang mana adalah bentuk dari rumus fundamental yang dinyatakan dalam persamaan-persamaan haversine.
Dari definisi di (21), $\text{hav } \theta$ *selalu bernilai positif* dan $\text{hav } (-\theta) = \text{hav } \theta$.

Nilai-nilai haversine dan logaritma haversine dari sudut-sudut mulai dari $0^\circ$ hingga $180^\circ$ dapat ditemukan pada beberapa koleksi tabel-tabel matematika yang di antaranya dapat disebutkan *Inman's Nautical Tables* (J. D. Potter, 156 Minories, London, E. 1), yang mana, sebagai tambahan atas tabel-tabel logaritma dan trigonometri yang lazim digunakan (hingga lima angka), berisikan beberapa tabel bernilai astronomi lainnya.

Perhitungan dari sisi AB (Gbr. 9) menggunakan sarana haversine sekarang akan diberikan demi menunjukkan kenyamanan dari metode ini.
Kita menulis (23) sebagai berikut untuk segitiga PAB:

$$
\begin{aligned}
\text{hav } AB &= \text{hav } (PA - PB) + \sin PA \sin PB \text{ hav } APB \\
&\equiv \text{hav } (PA - PB) + X
\end{aligned}
$$

$$
\begin{aligned}
\log \text{hav } APB &\equiv \log \text{hav } 100^\circ 57' \equiv \bar{1}.77450 \\
\log \sin PA &\equiv \log \sin 65^\circ 42' \equiv \bar{1}.95971 \\
\log \sin PB &\equiv \log \sin 53^\circ 13' \equiv \bar{1}.90358 \\
\therefore \log X &= \bar{1}.63779 \\
\therefore X &= 0.43430
\end{aligned}
$$

$$
\begin{aligned}
\text{hav } (PA - PB) &\equiv \text{hav } 12^\circ 29' = 0.01182 \\
\therefore \text{hav } AB &= 0.44612 \\
\therefore AB &= 83^\circ 49',
\end{aligned}
$$

yang mana sejalan dengan hasil kita di hal. 17.

### 14. Metode lain (Another method).
Ketika dua buah sisi dan sudut yang diapitnya dari sebuah segitiga diketahui, metode berikut ini terkadang digunakan ketika dibutuhkan untuk mencari sisi ketiga dan salah satu dari sudut yang tersisa.

Untuk mengilustrasikan metode ini kita akan mencari $AB$ dan $P\hat{A}B$ (Gbr. 9). Nyatakan AB dengan p, PB dengan a, PA dengan b dan $A\hat{P}B$ dengan P. Maka $a = 53^\circ 13'$, $b = 65^\circ 42'$ dan $P = 100^\circ 57'$.
Melalui rumus-rumus **A**, **C** dan **B**, kita memperoleh:

$$
\begin{aligned}
\cos p &= \cos a \cos b + \sin a \sin b \cos P \dots\dots(24), \\
\sin p \cos A &= \cos a \sin b - \sin a \cos b \cos P \dots\dots(25), \\
\sin p \sin A &= \sin a \sin P \dots\dots(26).
\end{aligned}
$$

Definisikan d (suatu besaran positif) dan D dengan

$$
\begin{aligned}
\cos a &= d \cos D \dots\dots(27), \\
\sin a \cos P &= d \sin D \dots\dots(28).
\end{aligned}
$$

Karenanya kita dapat menulis (24)-(26) sebagai berikut:

$$
\begin{aligned}
\cos p &= d \cos (b - D) \dots\dots(29), \\
\sin p \cos A &= d \sin (b - D) \dots\dots(30), \\
\sin p \sin A &= \sin a \sin P \dots\dots(31).
\end{aligned}
$$

(i) Dari (27) dan (28), melalui pembagian,

$$
\tan D = \tan a \cos P \dots\dots(32),
$$

dari mana D dapat dihitung.

(ii) Dari (30) dan (31),

$$
\tan A = \frac{\sin a \sin P}{d \sin (b - D)},
$$

yang mana, dengan memasukkan nilai d yang diberikan oleh (28), menjadi

$$
\tan A = \tan P \sin D \text{ cosec } (b - D) \dots\dots(33),
$$

dari mana A dapat dihitung.

(iii) Dari (29) dan (30),

$$
\tan p = \tan (b - D) \sec A \dots\dots(34),
$$

dari mana p dapat dihitung.

*Perhitungan-perhitungannya.*
(i)

$$
\begin{aligned}
\log \tan a &\equiv \log \tan 53^\circ 13' \equiv 0.12631 \\
\log \cos P &\equiv \log \cos 100^\circ 57' \equiv \bar{1}.27864\ n \\
\therefore \log \tan D &= \bar{1}.40495\ n
\end{aligned}
$$

$\cos P$ bernilai negatif dan kita menempelkan huruf *n* di sebelah logaritmanya untuk mengingatkan kita pada fakta ini. Karena itu mengikut bahwa $\tan D$ bernilai negatif. Kita telah mengasumsikan pada rumus-rumus (27) dan (28) bahwa d adalah besaran positif. Kemudian, dari nilai-nilai a dan P yang diberikan, mengikut bahwa...
"""
st.markdown(materi_bab_1_hal_19_20, unsafe_allow_html=True)

# ==========================================
# HALAMAN 21 - 24 (Kelanjutan Materi & Latihan)
# ==========================================
materi_bab_1_hal_21_22 = r"""
$\cos D$ bernilai positif dan $\sin D$ bernilai negatif; dengan demikian $D$ berada di kuadran keempat, dan dari nilai $\log \tan D$ yang telah kita temukan kita memperoleh

$$
D = 360^\circ - 14^\circ 15'.6 = 345^\circ 44'.4.
$$

Oleh karena itu

$$
b - D \equiv 65^\circ 42' - 345^\circ 44'.4 = -280^\circ 2'.4 = 79^\circ 57'.6.
$$

(ii)

$$
\begin{aligned}
\log \tan P &\equiv \log \tan 100^\circ 57' \equiv 0.71338\ n \\
\log \sin D &\equiv \log \sin 345^\circ 44'.4 \equiv \bar{1}.39151\ n \\
\log \text{cosec } (b - D) &\equiv \log \text{cosec } 79^\circ 57'.6 \equiv 0.00670 \\
\therefore \log \tan A &= 0.11159
\end{aligned}
$$

dan, karena $A$ kurang dari $180^\circ$, kita memperoleh

$$
P\hat{A}B = A = 52^\circ 16'.9.
$$

(iii)

$$
\begin{aligned}
\log \tan (b - D) &\equiv \log \tan 79^\circ 57'.6 \equiv 0.75192 \\
\log \sec A &\equiv \log \sec 52^\circ 16'.9 \equiv 0.21340 \\
\therefore \log \tan p &= 0.96532 \\
\therefore AB \equiv p &= 83^\circ 49',
\end{aligned}
$$

sejalan dengan perhitungan-perhitungan sebelumnya dari $AB$.

### 15. Rasio-rasio trigonometri untuk sudut-sudut kecil.
Jika $\theta$ adalah sebuah sudut kecil dan dinyatakan dalam ukuran melingkar (*circular measure*/radian), kita memiliki rumus-rumus perkiraan yang sangat dikenal:

$$
\sin \theta = \theta \text{ radian}; \quad \cos \theta = 1; \quad \tan \theta = \theta \text{ radian} \dots\dots(35).
$$

Sekarang

$$
1 \text{ radian} = 57^\circ 17' 45'' = 3437\frac{3}{4}' = 206265'',
$$

sehingga

$$
1'' = \frac{1}{206265} \text{ radian},
$$

dan

$$
1' = \frac{1}{3438} \text{ radian, kira-kira}.
$$

Oleh karena itu, berdasarkan persamaan pertama dari (35), ketika $\theta$ secara berturut-turut adalah $1''$ dan $1'$,

$$
\begin{aligned}
\sin 1'' &= \frac{1}{206265} \dots\dots(36), \\
\text{dan} \quad \sin 1' &= \frac{1}{3438} \dots\dots(37).
\end{aligned}
$$

Jika $\theta''$ melambangkan jumlah detik busur dalam $\theta$ radian, maka
$\theta = \frac{\theta''}{206265}$ dan akibatnya

$$
\sin \theta = \frac{\theta''}{206265},
$$

yang mana dapat dituliskan

$$
\sin \theta'' = \theta'' \sin 1'' \dots\dots(38).
$$

Secara serupa,

$$
\sin \theta' = \theta' \sin 1' \dots\dots(39),
$$

di mana $\theta'$ dinyatakan dalam menit busur.
Melalui cara yang serupa, kita mendapati

$$
\tan \theta'' = \theta'' \sin 1''.
$$
"""
st.markdown(materi_bab_1_hal_21_22, unsafe_allow_html=True)

with st.expander("Syarah: Pendekatan Tangen Sudut Kecil"):
    st.markdown(r"""
    Perhatikan pada baris terakhir di atas, buku menuliskan $\tan \theta'' = \theta'' \sin 1''$. Secara matematis, untuk sudut yang sangat kecil, nilai tangen hampir persis sama dengan nilai sinusnya, sehingga $\tan \theta \approx \sin \theta \approx \theta \text{ (dalam radian)}$. Inilah sebabnya buku menyamakan bentuk tangen ke pengali $\sin 1''$.
    """)

materi_bab_1_hal_22_23 = r"""
Dalam astronomi bola, sudut-sudut tertentu kerap kali dinyatakan dalam satuan jam, menit dan detik waktu, berdasarkan relasi-relasi berikut:

$$
24 \text{ jam} = 360^\circ; \quad 1^\text{h} = 15^\circ; \quad 1^\text{m} = 15' \quad \text{dan} \quad 1^\text{s} = 15'' \dots\dots(40).
$$

Oleh karenanya kita memperoleh rumus-rumus perkiraan:

$$
\begin{aligned}
\sin 1^\text{m} &= \sin 15' = 15 \sin 1' \dots\dots(41), \\
\sin 1^\text{s} &= \sin 15'' = 15 \sin 1'' \dots\dots(42).
\end{aligned}
$$

Jika $H$ adalah suatu sudut kecil, yang mana, ketika dinyatakan dalam menit waktu, akan dilambangkan dengan $H^\text{m}$, maka

$$
\sin H = H^\text{m} \sin 1^\text{m} = 15 H^\text{m} \sin 1' \dots\dots(43).
$$

Secara serupa, jika kita menyatakan $H$ dalam detik waktu, kita peroleh

$$
\sin H = H^\text{s} \sin 1^\text{s} = 15 H^\text{s} \sin 1'' \dots\dots(44).
$$

Hasil-hasil ini akan berguna di bab-bab selanjutnya.

### 16. Analogi-analogi Delambre dan Napier.
Untuk referensi, kita memberikan rumus-rumus berikut, yang aslinya berasal dari Delambre, dan dikenal sebagai analogi-analogi Delambre:

$$
\begin{aligned}
\sin \frac{1}{2}c \sin \frac{1}{2}(A - B) &= \cos \frac{1}{2}C \sin \frac{1}{2}(a - b) \dots\dots(45), \\
\sin \frac{1}{2}c \cos \frac{1}{2}(A - B) &= \sin \frac{1}{2}C \sin \frac{1}{2}(a + b) \dots\dots(46), \\
\cos \frac{1}{2}c \sin \frac{1}{2}(A + B) &= \cos \frac{1}{2}C \cos \frac{1}{2}(a - b) \dots\dots(47), \\
\cos \frac{1}{2}c \cos \frac{1}{2}(A + B) &= \sin \frac{1}{2}C \cos \frac{1}{2}(a + b) \dots\dots(48).
\end{aligned}
$$

Rumus-rumus ini mudah untuk diturunkan dari rumus-rumus utama yang telah didiskusikan di halaman-halaman sebelumnya.

Dengan mengambil persamaan-persamaan ini secara berpasangan, kita memperoleh analogi-analogi Napier:

$$
\begin{aligned}
\tan \frac{1}{2}(a + b) &= \frac{\cos \frac{1}{2}(A - B)}{\cos \frac{1}{2}(A + B)} \tan \frac{1}{2}c \dots\dots(49), \\
\tan \frac{1}{2}(a - b) &= \frac{\sin \frac{1}{2}(A - B)}{\sin \frac{1}{2}(A + B)} \tan \frac{1}{2}c \dots\dots(50), \\
\tan \frac{1}{2}(A + B) &= \frac{\cos \frac{1}{2}(a - b)}{\cos \frac{1}{2}(a + b)} \cot \frac{1}{2}C \dots\dots(51), \\
\tan \frac{1}{2}(A - B) &= \frac{\sin \frac{1}{2}(a - b)}{\sin \frac{1}{2}(a + b)} \cot \frac{1}{2}C \dots\dots(52).
\end{aligned}
$$
"""
st.markdown(materi_bab_1_hal_22_23, unsafe_allow_html=True)

with st.expander("Syarah: Penurunan Analogi Napier"):
    st.markdown(r"""
    Buku menyatakan bahwa Analogi Napier didapatkan dengan "mengambil persamaan-persamaan secara berpasangan". Secara aljabar, proses ini adalah murni proses **pembagian** antar persamaan Delambre.
    - Persamaan (49) didapat dari membagi persamaan (46) dengan persamaan (48). Ruas kiri: $(\sin \frac{1}{2}c \cos \frac{1}{2}(A-B)) / (\cos \frac{1}{2}c \cos \frac{1}{2}(A+B))$, di mana $\sin/\cos$ dari sudut $\frac{1}{2}c$ berubah menjadi $\tan \frac{1}{2}c$. 
    - Persamaan (50) didapat dari membagi persamaan (45) dengan (47).
    - Persamaan (51) didapat dari membagi persamaan (47) dengan (48), lalu memindah-ruaskan komponen.
    - Persamaan (52) didapat dari membagi persamaan (45) dengan (46).
    """)

materi_bab_1_latihan = r"""
---
### LATIHAN SOAL (EXERCISES)

1. Di dalam segitiga bola $ABC$, $C = 90^\circ$, $a = 119^\circ 46' 36''$ dan $B = 52^\circ 25' 38''$. Hitunglah nilai-nilai dari $b, c$ dan $A$.
*[Ans. $48^\circ 26' 49'', 109^\circ 14' 0'' \text{ dan } 113^\circ 10' 46''$.]*

2. Di dalam segitiga $ABC$, $a = 57^\circ 22' 11'', b = 72^\circ 12' 19'' \text{ dan } C = 94^\circ 1' 49''$. Hitunglah nilai-nilai dari $c, A$ dan $B$.
*[Ans. $83^\circ 46' 32'', 57^\circ 40' 45'' \text{ dan } 72^\circ 49' 50''$.]*

3. Di dalam segitiga $ABC$, $c = 90^\circ, B = 62^\circ 20' 42'' \text{ dan } a = 136^\circ 19' 0''$. Hitunglah nilai-nilai dari $A, C$ dan $b$.
*[Ans. $139^\circ 46' 13'', 69^\circ 14' 45'' \text{ dan } 71^\circ 18' 9''$.]*

4. Dua buah kapal layar $X$ dan $Y$ berlayar di sepanjang paralel-paralel lintang $48^\circ \text{N}$ dan $15^\circ \text{S}$ secara berurutan, dalam cara sedemikian rupa sehingga pada setiap momen yang diberikan kedua kapal tersebut berada pada meridian bujur yang sama. Jika kecepatan $X$ adalah 15 knot, carilah kecepatan dari $Y$.
*(Catatan: Knot adalah satuan kecepatan yang digunakan di laut; besarnya adalah 1 mil laut per jam).*

5. $A$ dan $B$ adalah dua buah tempat pada permukaan bumi dengan lintang yang sama $\phi$; selisih bujur di antara $A$ dan $B$ adalah $2l$. Buktikan bahwa (i) lintang tertinggi yang dicapai oleh lingkaran besar $AB$ adalah $\tan^{-1}(\tan \phi \sec l)$, dan (ii) jarak yang diukur di sepanjang paralel lintang di antara $A$ dan $B$ melebihi jarak lingkaran besar $AB$ sebesar

$$
2 \text{cosec } 1' [l \cos \phi - \sin^{-1}(\sin l \cos \phi)] \text{ mil laut}.
$$

6. Lintang paling selatan yang dicapai oleh lingkaran besar yang menghubungkan sebuah tempat $A$ di ekuator ke sebuah tempat $B$ di lintang selatan $\phi$ adalah $\phi_1$. Buktikan bahwa selisih bujur di antara $A$ dan $B$ adalah $90^\circ + \cos^{-1}(\tan \phi \cot \phi_1)$.

7. Posisi dari $A$ dan $B$ secara berurutan adalah: Lat. $39^\circ 20'\text{ S}$, Long. $110^\circ 10'\text{ E}$ dan Lat. $44^\circ 30'\text{ S}$, Long. $46^\circ 20'\text{ W}$. Tunjukkan bahwa, jika sebuah kapal berlayar dari $A$ ke $B$ melewati rute sependek mungkin tanpa memotong paralel $62^\circ \text{ S}$, jarak yang dilayari adalah $5847.6$ mil laut.

8. Jika elemen-elemen $a, b, c, A, B, C$ dari suatu segitiga bola menerima inkremen (kenaikan nilai) $da, \dots dC$, tunjukkan bahwa, jika

$$
K = \frac{\sin A}{\sin a} = \frac{\sin B}{\sin b} = \frac{\sin C}{\sin c},
$$

maka:

$$
\begin{aligned}
da &= \cos C \cdot db + \cos B \cdot dc + K \sin b \sin c \cdot dA, \\
db &= \cos A \cdot dc + \cos C \cdot da + K \sin c \sin a \cdot dB, \\
dc &= \cos B \cdot da + \cos A \cdot db + K \sin a \sin b \cdot dC, \\
dA &= -\cos c \cdot dB - \cos b \cdot dC + \frac{1}{K} \sin B \sin C \cdot da, \\
dB &= -\cos a \cdot dC - \cos c \cdot dA + \frac{1}{K} \sin C \sin A \cdot db, \\
dC &= -\cos b \cdot dA - \cos a \cdot dB + \frac{1}{K} \sin A \sin B \cdot dc.
\end{aligned}
$$

9. Buktikan bahwa dua sisi dari sebuah segitiga bola bernilai sama jika dan hanya jika sudut-sudut yang berhadapan dengannya bernilai sama.
$ABC$ adalah sebuah segitiga bola sama sisi di mana pergeseran (displacement) kecil dilakukan, pada sisi-sisi dan sudut-sudutnya, sedemikian rupa sehingga segitiga tersebut tetap sama sisi. Buktikan bahwa

$$
\frac{da}{dA} = \cos \frac{A}{2} \cot \frac{a}{2}.
$$
*[Glas. 1967.]*

"""
st.markdown(materi_bab_1_latihan, unsafe_allow_html=True)
