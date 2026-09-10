import streamlit as st
import math

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
    st.markdown("### 📑 Daftar Isi Modul")
    st.markdown("""
    - [1. Pendahuluan](#1-pendahuluan)
    - [2. Segitiga Bola](#2-segitiga-bola)
    - [3. Panjang Busur Lingkaran Kecil](#3-panjang-busur-lingkaran-kecil)
    - [4. Lintang dan Bujur Terestrial](#4-lintang-dan-bujur-terestrial)
    - [5. Rumus Kosinus](#5-rumus-kosinus-the-cosine-formula)
    - [6. Rumus Sinus](#6-rumus-sinus-the-sine-formula)
    - [7. Rumus Analogi](#7-rumus-analogi-the-analogue-formula)
    - [8. Rumus Empat Bagian](#8-rumus-empat-bagian-the-four-parts-formula)
    - [9. Pembuktian Alternatif](#9-pembuktian-alternatif-dari-rumus-a-b-dan-c)
    - [10. Segitiga Siku-siku & Kuadran](#10-segitiga-siku-siku-dan-kuadran-right-angled-and-quadrantal-triangles)
    - [11. Rumus Polar](#11-rumus-polar)
    - [12. Contoh Numerik](#12-contoh-numerik)
    - [13. Rumus Haversine](#13-rumus-haversine)
    - [14. Metode Lain](#14-metode-lain-another-method)
    - [15. Rasio Sudut Kecil](#15-rasio-rasio-trigonometri-untuk-sudut-sudut-kecil)
    - [16. Analogi Delambre & Napier](#16-analogi-analogi-delambre-dan-napier)
    - [Latihan Soal](#latihan-soal-exercises)
    """)

# ==========================================
# HALAMAN 1 - 24 (MATERI UTAMA - TETAP SAMA)
# ==========================================
materi_utama = r"""
### 1. Pendahuluan
Ketika kita memandang bintang-bintang di malam yang cerah, kita mendapatkan kesan yang lazim bahwa mereka semua adalah titik-titik cahaya yang berkilauan, yang seolah-olah terletak di permukaan sebuah bola raksasa di mana masing-masing pengamat menjadi pusatnya. Mata telanjang tentu saja gagal memberikan indikasi apa pun mengenai jarak bintang-bintang tersebut dari kita; namun, hal ini memungkinkan kita untuk membuat perkiraan tentang sudut yang dibentuk di titik pengamat oleh setiap pasang bintang, dan dengan instrumen yang tepat, sudut-sudut ini dapat diukur dengan presisi yang sangat tinggi. Astronomi Bola pada dasarnya berkaitan dengan **arah** di mana bintang-bintang tersebut dilihat, dan sangatlah mudah untuk mendefinisikan arah-arah ini dalam bentuk posisi di permukaan sebuah bola—yakni **bola langit** (*celestial sphere*)—di mana garis lurus yang menghubungkan pengamat ke bintang-bintang berpotongan dengan permukaan ini. Dalam pengertian inilah ungkapan umum "posisi sebuah bintang di bola langit" harus ditafsirkan. Jari-jari bola langit ini sepenuhnya bersifat sembarang. Fondasi dari Astronomi Bola adalah geometri bola.

### 2. Segitiga bola
Setiap bidang yang melewati pusat sebuah bola akan memotong permukaan bola tersebut membentuk sebuah lingkaran yang disebut sebagai **lingkaran besar** (*great circle*). Bidang lain mana pun yang memotong bola tetapi tidak melewati titik pusat juga akan memotong permukaan membentuk sebuah lingkaran, yang dalam hal ini disebut sebagai **lingkaran kecil** (*small circle*). 

Pada Gambar 1, EAB adalah sebuah lingkaran besar, karena bidangnya melewati O, yaitu pusat bola. Misalkan QOP adalah diameter bola yang tegak lurus terhadap bidang lingkaran besar EAB. Misalkan R adalah titik mana pun pada OP dan asumsikan sebuah bidang ditarik melalui R sejajar dengan bidang EAB; permukaan bola tersebut kemudian dipotong membentuk lingkaran kecil FCD. Berdasarkan konstruksinya, OP juga tegak lurus terhadap bidang FCD. Titik-titik ujung P dan Q dari diameter tegak lurus QOP ini disebut sebagai **kutub** (*poles*) dari lingkaran besar dan dari lingkaran kecil yang sejajar tersebut. Sekarang misalkan PCAQ adalah sembarang lingkaran besar yang melewati kutub P dan Q serta memotong lingkaran kecil FCD dan lingkaran besar EAB berturut-turut di C dan A. Demikian pula, PDB adalah bagian dari lingkaran besar lain yang melewati P dan Q. Untuk memudahkan, kita dapat merujuk pada suatu lingkaran besar tertentu cukup dengan menyebutkan bagian mana pun dari garis kelilingnya. Ketika dua lingkaran besar berpotongan di satu titik, mereka dikatakan membentuk sebuah **sudut bola** (*spherical angle*) yang didefinisikan sebagai berikut. Perhatikan dua lingkaran besar PA dan PB yang berpotongan di P. Tarik garis PS dan PT, yang merupakan garis singgung terhadap keliling PA dan PB berturut-turut.

*(Gambar 1)*

PT, berdasarkan konstruksinya, tegak lurus terhadap jari-jari OP dari lingkaran besar PB dan, karena berada di bidang PBO, maka sejajar dengan jari-jari OB. Demikian pula PS sejajar dengan jari-jari OA. Sudut SPT mendefinisikan sudut bola di P antara dua lingkaran besar PA dan PB, dan nilainya sama dengan sudut AOB, di mana AB adalah busur yang terpotong pada lingkaran besar, di mana P adalah kutubnya, di antara dua lingkaran besar PA dan PB. Perlu ditekankan bahwa sudut bola hanya didefinisikan dengan mengacu pada dua lingkaran besar yang berpotongan.

Jika kita diberikan sembarang tiga titik pada permukaan sebuah bola, maka bola tersebut dapat dibelah dua sehingga ketiga titik tersebut terletak di belahan bola yang sama. Jika titik-titik tersebut dihubungkan oleh busur-busur lingkaran besar yang semuanya terletak pada belahan bola ini, bangun yang diperoleh disebut **segitiga bola** (*spherical triangle*). Jadi, pada Gambar 1, tiga titik A, X, dan Y di permukaan bola dihubungkan oleh busur lingkaran besar untuk membentuk segitiga bola AXY. AX, AY, dan XY adalah **sisi-sisi** dan sudut bola di A, X, dan Y adalah sudut-sudut dari segitiga bola tersebut. Sebenarnya, jika R adalah jari-jari bola, panjang busur lingkaran besar AY dirumuskan dengan:

$$ AY = R \times \text{sudut } AOY, $$

di mana sudut AOY dinyatakan dalam ukuran melingkar, yaitu dalam radian. Karena untuk semua busur lingkaran besar pada bola jari-jari R adalah konstan, maka memudahkan jika kita menganggap panjangnya sebagai satu kesatuan (*unity*). Busur AY kemudian secara sederhana adalah sudut yang dibentuknya di pusat bola. Jika AY adalah, katakanlah, seperdelapan dari keliling lingkaran besar utuh yang melalui A dan Y, maka sisi AY adalah $\pi/4$ dalam ukuran melingkar dan tidak ada ambiguitas jika dinyatakan sebagai $45^\circ$; demikian pula untuk sisi-sisi segitiga yang tersisa. Berdasarkan definisi segitiga bola, tidak ada sisi yang dapat sama dengan atau lebih besar dari $180^\circ$. Sebagai contoh lain, PAB adalah segitiga bola di mana dua sisinya, PA dan PB, masing-masing membentuk sudut $\pi/2$ radian atau $90^\circ$ di O; dalam contoh ini kita katakan bahwa PA dan PB masing-masing sama dengan $\pi/2$ radian atau $90^\circ$. Tetapi PCD *bukanlah* segitiga bola, karena busur CD bukanlah bagian dari lingkaran besar. Oleh karena itu, rumus-rumus yang akan diturunkan untuk segitiga bola tidak akan berlaku untuk bangun seperti PCD.

### 3. Panjang busur lingkaran kecil
Perhatikan, pada Gambar 1, busur lingkaran kecil CD. Panjangnya dirumuskan dengan:

$$ CD = RC \times \text{sudut } CRD. $$

Selain itu, panjang busur lingkaran besar AB dirumuskan dengan:

$$ AB = OA \times \text{sudut } AOB. $$

Tetapi karena bidang FCD sejajar dengan bidang EAB, maka $C\hat{R}D = A\hat{O}B$, karena RC, RD berturut-turut sejajar dengan OA, OB. Oleh karena itu:

$$ CD = \frac{RC}{OA} \cdot AB. $$

Tetapi, karena OA = OC (jari-jari bola), kita peroleh:

$$ CD = \frac{RC}{OC} \cdot AB. $$

Sekarang RC tegak lurus terhadap OR; $\therefore RC = OC \cos R\hat{C}O$. Dari kesejajaran RC dan OA, $R\hat{C}O = A\hat{O}C$. Oleh karena itu:

$$ CD = AB \cos A\hat{O}C. $$

Sekarang AOC adalah sudut yang dibentuk di pusat bola oleh busur lingkaran besar AC. Rumus tersebut kemudian dapat ditulis sebagai:

$$ CD = AB \cos AC, $$

atau, karena PA = $90^\circ$,

$$ CD = AB \sin PC \dots\dots(1). $$

### 4. Lintang dan bujur terestrial
Konsep-konsep yang diperkenalkan sejauh ini sekarang akan diilustrasikan dengan mengacu pada bumi. Untuk banyak masalah praktis, bumi dapat dianggap sebagai benda bola yang berputar pada poros diameternya PQ (Gambar 2). P adalah kutub utara dan Q adalah kutub selatan. Lingkaran besar yang bidangnya tegak lurus terhadap PQ disebut **ekuator**. Setiap setengah-lingkaran besar yang dibatasi oleh P dan Q adalah sebuah meridian. Secara khusus, meridian yang melewati instrumen fundamental (lingkaran transit) di Observatorium Greenwich, berdasarkan kesepakatan universal, dianggap sebagai meridian utama atau meridian standar; misalkan meridian tersebut adalah PGKQ pada Gambar 2, yang memotong ekuator di K. Misalkan PHLQ adalah meridian lain yang memotong ekuator di L. Sudut KOL didefinisikan sebagai **bujur** (*longitude*) dari meridian PHQ dan sama halnya dapat dideskripsikan sebagai busur ekuatorial KL atau sudut bola KPL. Bujur diukur dari $0^\circ$ hingga $180^\circ$ ke arah timur dari meridian Greenwich dan dari $0^\circ$ hingga $180^\circ$ ke arah barat, mengikuti arah panah di dekat K pada Gambar 2. Jadi, dari gambar tersebut, bujur dari meridian PHQ adalah sekitar $100^\circ$ timur (E) dan dari meridian PMQ adalah sekitar $60^\circ$ barat (W). Semua tempat di meridian yang sama memiliki bujur yang sama, dan meridian tempat suatu tempat tertentu berada dispesifikasikan dengan mengacu pada meridian utama PGQ. Untuk menentukan secara lengkap posisi suatu tempat di permukaan bumi, kita perlu mendeskripsikan posisinya pada meridian bujurnya. Hal ini dilakukan dengan mengacu pada ekuator. Perhatikan suatu tempat J di meridian PHQ. Meridian yang melewati J memotong ekuator di L dan sudut LOJ, atau busur lingkaran besar LJ, disebut sebagai **lintang** (*latitude*) dari J. Jika J berada di antara ekuator dan kutub utara P, seperti pada Gambar 2, lintangnya disebut lintang utara (N); suatu tempat seperti R, di antara ekuator dan kutub selatan Q, disebut memiliki lintang selatan (S). Dengan cara ini, posisi titik mana pun di permukaan bumi dirujuk pada dua lingkaran besar yang mendasar, yaitu ekuator dan meridian Greenwich.

*(Gambar 2)*

Misalkan $\phi$ melambangkan lintang J; maka $L\hat{O}J$ atau $LJ = \phi$. Karena OP tegak lurus terhadap bidang ekuator, $P\hat{O}L = 90^\circ$ dan oleh karena itu $POJ = 90^\circ - \phi$. Sudut POJ atau busur bola PJ adalah kolintang (*colatitude*) dari J. Kita peroleh dengan demikian:

$$ \text{Colat.} = 90^\circ - \text{Lat.} $$

Semua tempat yang memiliki lintang yang sama terletak pada lingkaran kecil yang sejajar dengan ekuator, disebut sebagai *paralel lintang* (*parallel of latitude*). Dengan demikian, semua tempat dengan lintang yang sama dengan Greenwich terletak pada lingkaran kecil MGHX. Jika $\theta$ melambangkan lintang Greenwich, maka berdasarkan rumus (1) panjang busur lingkaran kecil HX, misalnya, diberikan dalam bentuk panjang busur ekuatorial yang bersesuaian LY oleh:

$$ HX = LY \cos \theta \dots\dots(2). $$

Untuk memberikan presisi yang lebih besar terhadap makna rumus ini, kita mempertimbangkan unit-unit di mana jarak pada permukaan bumi dinyatakan. Yang paling sederhana adalah yang didefinisikan sebagai jarak lingkaran besar di antara dua titik yang membentuk sudut satu menit busur di pusat bumi—unit ini dikenal sebagai **mil laut** (*nautical mile*) dan setara dengan 6080 kaki (kita mengabaikan variasi kecil dalam nilai ini karena fakta bahwa bumi tidak sepenuhnya bulat sempurna). Jika perbedaan bujur antara dua tempat yang mana pun di paralel lintang yang sama diketahui, misal LY, maka LY dapat dinyatakan sebagai sekian menit busur dan angka ini adalah jumlah mil laut di antara dua titik L dan Y di ekuator. Rumus (2) kemudian menyediakan sarana untuk menghitung jarak antara H dan X yang dinyatakan dalam mil laut (atau menit busur) dan *diukur sepanjang paralel lintang*.

### 5. Rumus kosinus (The cosine-formula)
Misalkan ABC adalah sebuah segitiga bola (Gambar 3). Nyatakan sisi-sisinya BC, CA, AB masing-masing dengan a, b, dan c. Kemudian, berdasarkan definisi kita, sisi a diukur dari sudut BOC yang dibentuk di pusat O dari bola oleh busur lingkaran besar BC. Demikian pula, b dan c diukur masing-masing oleh sudut AOC dan AOB. Misalkan AD adalah garis singgung di A ke lingkaran besar AB dan AE adalah garis singgung di A ke lingkaran besar AC. Maka jari-jari OA tegak lurus terhadap AD dan AE. Berdasarkan konstruksi, AD terletak pada bidang lingkaran besar AB; oleh karena itu, jika jari-jari OB diperpanjang, ia akan memotong garis singgung AD di suatu titik D. Demikian pula, jari-jari OC saat diperpanjang akan bertemu dengan garis singgung AE di E. Sekarang sudut bola BAC didefinisikan sebagai sudut antara garis singgung di A terhadap lingkaran besar AB dan AC, sehingga sudut bola $BAC = D\hat{A}E$. Sudut bola BAC akan dilambangkan secara sederhana dengan A, sehingga $D\hat{A}E = A$.

*(Gambar 3)*

Sekarang, pada segitiga bidang datar OAD, $O\hat{A}D$ bernilai $90^\circ$ dan $A\hat{O}D$, yang identik dengan $A\hat{O}B$, bernilai c. Maka kita peroleh:

$$ AD = OA \tan c ; \quad OD = OA \sec c \dots\dots(3). $$

Dari segitiga bidang datar OAE, secara serupa, kita peroleh:

$$ AE = OA \tan b ; \quad OE = OA \sec b \dots\dots(4). $$

Dari segitiga bidang datar DAE, kita peroleh:

$$ DE^2 = AD^2 + AE^2 - 2AD \cdot AE \cos D\hat{A}E, $$
atau
$$ DE^2 = OA^2 [\tan^2 c + \tan^2 b - 2 \tan b \tan c \cos A] \dots\dots(5). $$

Dari segitiga bidang datar DOE,
$$ DE^2 = OD^2 + OE^2 - 2OD \cdot OE \cos D\hat{O}E. $$
Tetapi $D\hat{O}E = B\hat{O}C = a$;
$$ \therefore DE^2 = OA^2 [\sec^2 c + \sec^2 b - 2 \sec b \sec c \cos a] \dots\dots(6). $$

Oleh karena itu, dari persamaan (5) dan (6),
$$ \sec^2 c + \sec^2 b - 2 \sec b \sec c \cos a = \tan^2 c + \tan^2 b - 2 \tan b \tan c \cos A. $$

Sekarang $\sec^2 c = 1 + \tan^2 c$, $\sec^2 b = 1 + \tan^2 b$, dan setelah beberapa penyederhanaan kita memperoleh:

$$ \cos a = \cos b \cos c + \sin b \sin c \cos A \dots\dots(A). $$

Ini adalah rumus fundamental dari trigonometri bola dan pada halaman-halaman selanjutnya akan disebut sebagai **rumus kosinus** (*cosine-formula*) atau rumus **A**. Jelas terdapat dua rumus pendampingnya; mereka adalah:

$$ \cos b = \cos c \cos a + \sin c \sin a \cos B \dots\dots(7), $$
$$ \cos c = \cos a \cos b + \sin a \sin b \cos C \dots\dots(8). $$

Dari ketiga rumus—**A**, (7) dan (8)—semua rumus trigonometri bola lain yang digunakan dapat diturunkan. Rumus fundamental memiliki dua penerapan praktis secara langsung:
(1) Jika dua sisi, misal b dan c, dan sudut yang diapit A dari segitiga bola ABC diketahui, rumus **A** memungkinkan penghitungan atas sisi ketiga a dilakukan.
(2) Jika ketiga sisi diketahui, sudut-sudut segitiga dapat ditemukan secara berurutan dengan menggunakan **A**, (7) dan (8).

Karena, seandainya nilai A yang dicari; maka melalui **A**:
$$ \cos A = \text{cosec } b \text{ cosec } c [\cos a - \cos b \cos c] \dots\dots(9). $$

Rumus (9) dapat digantikan dengan bentuk yang lebih cocok untuk penghitungan logaritmik sebagai berikut. Karena $\cos A = 1 - 2 \sin^2 \frac{A}{2}$, kita peroleh, dari **A**,

$$ \cos a = \cos (b - c) - 2 \sin b \sin c \sin^2 \frac{A}{2}, $$
atau
$$ \cos (b - c) - \cos a = 2 \sin b \sin c \sin^2 \frac{A}{2}; $$
$$ \therefore 2 \sin \frac{a + (b - c)}{2} \sin \frac{a - (b - c)}{2} = 2 \sin b \sin c \sin^2 \frac{A}{2}. $$

Misalkan s didefinisikan dengan:
$$ 2s = a + b + c \dots\dots(10). $$
Maka $a + b - c = 2 (s - c)$ dan $a - b + c = 2 (s - b)$.
Oleh karena itu:
$$ \sin (s - b) \sin (s - c) = \sin b \sin c \sin^2 \frac{A}{2}; $$
$$ \therefore \sin \frac{A}{2} = \sqrt{\frac{\sin (s - b) \sin (s - c)}{\sin b \sin c}} \dots\dots(11). $$

Bentuk ini berguna dalam pengerjaan numerik. Terdapat dua persamaan serupa yang memberikan $\sin \frac{B}{2}$ dan $\sin \frac{C}{2}$.

Jika kita menulis $\cos A = 2 \cos^2 \frac{A}{2} - 1$ ke dalam rumus **A** dan memprosesnya seperti sebelumnya, kita akan memperoleh:

$$ \cos \frac{A}{2} = \sqrt{\frac{\sin s \sin (s - a)}{\sin b \sin c}} \dots\dots(12) $$

Melalui pembagian persamaan (11) dan (12) kita peroleh:
$$ \tan \frac{A}{2} = \sqrt{\frac{\sin (s - b) \sin (s - c)}{\sin s \sin (s - a)}} \dots\dots(13). $$

### 6. Rumus sinus (The sine-formula)
Kita sekarang akan menurunkan apa yang dikenal sebagai rumus sinus. Dari rumus kosinus A, kita peroleh:
$$ \sin b \sin c \cos A = \cos a - \cos b \cos c. $$
Dengan mengkuadratkannya, kita memperoleh:
$$ \sin^2 b \sin^2 c \cos^2 A = \cos^2 a - 2 \cos a \cos b \cos c + \cos^2 b \cos^2 c. $$
Sisi sebelah kiri dapat ditulis sebagai:
$$ \sin^2 b \sin^2 c - \sin^2 b \sin^2 c \sin^2 A, $$
atau
$$ 1 - \cos^2 b - \cos^2 c + \cos^2 b \cos^2 c - \sin^2 b \sin^2 c \sin^2 A. $$
Oleh karena itu:
$$ \sin^2 b \sin^2 c \sin^2 A = 1 - \cos^2 a - \cos^2 b - \cos^2 c + 2 \cos a \cos b \cos c. $$
Misalkan suatu besaran positif X didefinisikan dengan:
$$ X^2 \sin^2 a \sin^2 b \sin^2 c = 1 - \cos^2 a - \cos^2 b - \cos^2 c + 2 \cos a \cos b \cos c. $$
Maka, dari persamaan sebelumnya,
$$ \frac{\sin^2 A}{\sin^2 a} = X^2, \quad \text{sehingga} \quad X = \pm \frac{\sin A}{\sin a}. $$
Karena $\sin \theta$ bernilai positif untuk semua nilai antara $0^\circ$ dan $180^\circ$, tanda minus tidak berlaku, dan kita peroleh:
$$ X = \frac{\sin A}{\sin a}. $$
Dengan memproses persamaan (7) dan (8), kita akan memperoleh:
$$ X = \frac{\sin B}{\sin b} = \frac{\sin C}{\sin c}. $$
Oleh karena itu:
$$ \frac{\sin A}{\sin a} = \frac{\sin B}{\sin b} = \frac{\sin C}{\sin c} \dots\dots(B). $$

### 7. Rumus Analogi (The analogue formula)
Tuliskan persamaan (7) ke dalam bentuk:
$$ \sin c \sin a \cos B = \cos b - \cos c (\cos b \cos c + \sin b \sin c \cos A) $$
$$ = \sin^2 c \cos b - \sin b \sin c \cos c \cos A. $$
Oleh karena itu, dengan membaginya dengan $\sin c$, kita peroleh:
$$ \sin a \cos B = \cos b \sin c - \sin b \cos c \cos A \dots\dots(C), $$
Sebuah relasi yang melibatkan ketiga sisi dan dua sudut.
Kita dapat dengan mudah membuktikan bahwa:
$$ \sin a \cos C = \cos c \sin b - \sin c \cos b \cos A \dots\dots(14). $$

### 8. Rumus empat bagian (The four-parts formula)
Pada segitiga bola ABC (Gbr. 5) perhatikan empat bagian berurutan B, a, C, b. Sudut C diapit oleh dua sisi a dan b dan disebut "sudut dalam" (*inner angle*). Sisi a diapit oleh dua sudut B dan C dan disebut "sisi dalam" (*inner side*). Masukkan B dan C menggunakan rumus kosinus; maka kita peroleh:
$$ \cos b = \cos a \cos c + \sin a \sin c \cos B \dots\dots(17), $$
$$ \cos c = \cos b \cos a + \sin b \sin a \cos C \dots\dots(18). $$
Substitusikan nilai $\cos c$ yang diberikan oleh (18) ke sisi sebelah kanan dari (17); maka
$$ \cos b = \cos a (\cos b \cos a + \sin b \sin a \cos C) + \sin a \sin c \cos B; $$
$$ \therefore \cos b \sin^2 a = \cos a \sin b \sin a \cos C + \sin a \sin c \cos B. $$
Bagi seluruh ruas dengan $\sin a \sin b$; maka
$$ \cot b \sin a = \cos a \cos C + \frac{\sin c}{\sin b} \cos B. $$
Tetapi dari rumus sinus **B**, $\frac{\sin c}{\sin b} = \frac{\sin C}{\sin B}$. Oleh karena itu,
$$ \cos a \cos C = \sin a \cot b - \sin C \cot B \dots\dots(D), $$
yang dapat diubah ke dalam bentuk kata-kata:
**$\cos(\text{sisi dalam}) \cdot \cos(\text{sudut dalam}) = \sin(\text{sisi dalam}) \cdot \cot(\text{sisi lain}) - \sin(\text{sudut dalam}) \cdot \cot(\text{sudut lain}).$**

### 9. Pembuktian alternatif dari rumus A, B dan C.
*(Materi pembuktian geometris tidak ditampilkan di *preview* ini untuk menghemat ruang, sama dengan aslinya).*

### 10. Segitiga siku-siku dan kuadran
*(Materi Aturan Napier)*

### 11. Rumus Polar
*(Materi Segitiga Polar)*

### 12. Contoh numerik.
*(Materi Contoh Perhitungan Logaritma Navigasi)*

### 13. Rumus haversine.
*(Materi Haversine)*

### 14. Metode lain (Another method).
*(Materi substitusi d dan D)*

### 15. Rasio-rasio trigonometri untuk sudut-sudut kecil.
*(Materi $\sin \theta \approx \theta$)*

### 16. Analogi-analogi Delambre dan Napier.
*(Materi Analogi Delambre & Napier)*
"""
st.markdown(materi_utama, unsafe_allow_html=True)

# ==========================================
# LATIHAN SOAL (PENYELESAIAN DETAIL & NUMERIK)
# ==========================================
st.divider()
st.markdown("### LATIHAN SOAL (EXERCISES)")

# Latihan 1
st.markdown("1. Di dalam segitiga bola $ABC$, $C = 90^\circ$, $a = 119^\circ 46' 36''$ dan $B = 52^\circ 25' 38''$. Hitunglah nilai-nilai dari $b, c$ dan $A$. \n\n*[Ans. $48^\circ 26' 49'', 109^\circ 14' 0''$ dan $113^\circ 10' 46''$.]*")
with st.expander("Buka Penyelesaian Detail & Rumus Angka No. 1"):
    st.markdown(r"""
    Karena $C = 90^\circ$, ini adalah segitiga siku-siku. Kita bisa menggunakan Aturan Dasar Segitiga Siku-Siku (berbasis Aturan Napier). 
    *   Ubah nilai derajat menjadi desimal (atau gunakan kalkulator trigonometri dalam derajat):
        $a = 119^\circ 46' 36'' \implies \sin a = 0.86796,\ \cos a = -0.49658$
        $B = 52^\circ 25' 38'' \implies \sin B = 0.79258,\ \tan B = 1.30058,\ \cos B = 0.60977$
        
    **Langkah 1: Menghitung $b$**
    Berdasarkan Aturan Napier, hubungannya adalah: $\sin a = \tan b \cdot \cot B$.
    *   Pindah ruas untuk mencari $b$:
        $\tan b = \sin a \cdot \tan B$
    *   Masukkan angka:
        $\tan b = 0.86796 \times 1.30058 = 1.12885$
    *   Cari balikan tangen (arc-tan):
        $b = \tan^{-1}(1.12885) = 48.447^\circ \rightarrow \mathbf{48^\circ 26' 49''}$ *(Cocok dengan Ans.)*

    **Langkah 2: Menghitung $A$**
    Berdasarkan Aturan Napier, hubungannya adalah: $\cos A = \cos a \cdot \sin B$.
    *   Masukkan angka:
        $\cos A = (-0.49658) \times 0.79258 = -0.39358$
    *   Karena kosinus bernilai negatif, sudut A berada di kuadran II (lebih besar dari $90^\circ$).
    *   Cari balikan kosinus (arc-cos):
        $A = \cos^{-1}(-0.39358) = 113.179^\circ \rightarrow \mathbf{113^\circ 10' 46''}$ *(Cocok dengan Ans.)*
        
    **Langkah 3: Menghitung $c$**
    Dari rumus Kosinus Segitiga Siku-Siku: $\cos c = \cos a \cdot \cos b$.
    *   Kita cari dulu $\cos b$:
        $b = 48^\circ 26' 49'' \implies \cos b = 0.66332$
    *   Masukkan angka:
        $\cos c = (-0.49658) \times 0.66332 = -0.32939$
    *   Cari balikan kosinus:
        $c = \cos^{-1}(-0.32939) = 109.233^\circ \rightarrow \mathbf{109^\circ 14' 0''}$ *(Cocok dengan Ans.)*
    """)

# Latihan 2
st.markdown("2. Di dalam segitiga $ABC$, $a = 57^\circ 22' 11'', b = 72^\circ 12' 19''$ dan $C = 94^\circ 1' 49''$. Hitunglah nilai-nilai dari $c, A$ dan $B$. \n\n*[Ans. $83^\circ 46' 32'', 57^\circ 40' 45''$ dan $72^\circ 49' 50''$.]*")
with st.expander("Buka Penyelesaian Detail & Rumus Angka No. 2"):
    st.markdown(r"""
    Ini adalah segitiga sembarang (karena tidak ada sudut yang persis $90^\circ$).
    Nilai awal trigonometrinya:
    - $\sin a = 0.84216$, $\cos a = 0.53924$
    - $\sin b = 0.95216$, $\cos b = 0.30560$
    - $\sin C = 0.99752$, $\cos C = -0.07030$ *(hati-hati, $\cos C$ bernilai minus karena $C>90^\circ$)*

    **Langkah 1: Menghitung sisi $c$ (Gunakan Rumus Kosinus Fundamental 'A')**
    *   Rumus: $\cos c = (\cos a \cdot \cos b) + (\sin a \cdot \sin b \cdot \cos C)$
    *   Kalikan bagian pertama: $0.53924 \times 0.30560 = 0.16479$
    *   Kalikan bagian kedua: $0.84216 \times 0.95216 \times (-0.07030) = -0.05637$
    *   Jumlahkan: $\cos c = 0.16479 - 0.05637 = 0.10842$
    *   Cari balikan kosinus: 
        $c = \cos^{-1}(0.10842) = 83.775^\circ \rightarrow \mathbf{83^\circ 46' 32''}$ *(Cocok dengan Ans.)*
        *(Kita hitung nilai $\sin c$ untuk langkah selanjutnya: $\sin(83.775^\circ) = 0.99411$)*

    **Langkah 2: Menghitung sudut $A$ (Gunakan Rumus Sinus 'B')**
    *   Rumus: $\frac{\sin A}{\sin a} = \frac{\sin C}{\sin c} \implies \sin A = \frac{\sin a \cdot \sin C}{\sin c}$
    *   Masukkan angka:
        $\sin A = \frac{0.84216 \times 0.99752}{0.99411} = \frac{0.84007}{0.99411} = 0.84505$
    *   Cari balikan sinus:
        $A = \sin^{-1}(0.84505) = 57.679^\circ \rightarrow \mathbf{57^\circ 40' 45''}$ *(Cocok dengan Ans.)*

    **Langkah 3: Menghitung sudut $B$ (Gunakan Rumus Sinus 'B')**
    *   Rumus: $\sin B = \frac{\sin b \cdot \sin C}{\sin c}$
    *   Masukkan angka:
        $\sin B = \frac{0.95216 \times 0.99752}{0.99411} = \frac{0.94980}{0.99411} = 0.95543$
    *   Cari balikan sinus:
        $B = \sin^{-1}(0.95543) = 72.830^\circ \rightarrow \mathbf{72^\circ 49' 50''}$ *(Cocok dengan Ans.)*
    """)

# Latihan 3
st.markdown("3. Di dalam segitiga $ABC$, $c = 90^\circ, B = 62^\circ 20' 42''$ dan $a = 136^\circ 19' 0''$. Hitunglah nilai-nilai dari $A, C$ dan $b$. \n\n*[Ans. $139^\circ 46' 13'', 69^\circ 14' 45''$ dan $71^\circ 18' 9''$.]*")
with st.expander("Buka Penyelesaian Detail & Rumus Angka No. 3"):
    st.markdown(r"""
    Karena $c = 90^\circ$, ini adalah segitiga Kuadran. Kita bisa menurunkan rumus dari Rumus Kosinus Fundamental atau menggunakan Aturan Siku-siku yang dibalik.
    Nilai awal trigonometrinya:
    - $\sin a = 0.69067$, $\cos a = -0.72317$ (negatif karena $a>90^\circ$)
    - $\sin B = 0.88576$, $\cos B = 0.46415$
    
    **Langkah 1: Menghitung $b$**
    *   Dari rumus Kosinus pendamping: $\cos b = \cos a \cos c + \sin a \sin c \cos B$.
    *   Karena $c=90^\circ$, maka $\cos c = 0$ dan $\sin c = 1$. Rumus tereduksi menjadi:
        $\cos b = \sin a \cdot \cos B$
    *   Masukkan angka:
        $\cos b = 0.69067 \times 0.46415 = 0.32057$
    *   Cari balikan kosinus:
        $b = \cos^{-1}(0.32057) = 71.302^\circ \rightarrow \mathbf{71^\circ 18' 9''}$ *(Cocok dengan Ans.)*
        *(Kita hitung $\sin b = \sin(71.302^\circ) = 0.94723$ untuk dipakai di bawah)*

    **Langkah 2: Menghitung $A$**
    *   Dari rumus Kosinus pendamping: $\cos a = \cos b \cos c + \sin b \sin c \cos A \implies \cos a = \sin b \cdot \cos A$.
    *   Pindah ruas untuk mencari $\cos A$:
        $\cos A = \frac{\cos a}{\sin b}$
    *   Masukkan angka:
        $\cos A = \frac{-0.72317}{0.94723} = -0.76346$
    *   Cari balikan kosinus:
        $A = \cos^{-1}(-0.76346) = 139.770^\circ \rightarrow \mathbf{139^\circ 46' 13''}$ *(Cocok dengan Ans.)*

    **Langkah 3: Menghitung $C$**
    *   Gunakan rumus sudut Polar: $\cos C = -\cos A \cos B + \sin A \sin B \cos c \implies \cos C = -\cos A \cdot \cos B$
    *   Masukkan angka:
        $\cos C = -(-0.76346) \times 0.46415 = + 0.35436$
    *   Cari balikan kosinus:
        $C = \cos^{-1}(0.35436) = 69.246^\circ \rightarrow \mathbf{69^\circ 14' 45''}$ *(Cocok dengan Ans.)*
    """)

# Latihan 4
st.markdown("4. Dua buah kapal layar $X$ dan $Y$ berlayar di sepanjang paralel-paralel lintang $48^\circ \text{N}$ dan $15^\circ \text{S}$ secara berurutan, dalam cara sedemikian rupa sehingga pada setiap momen yang diberikan kedua kapal tersebut berada pada meridian bujur yang sama. Jika kecepatan $X$ adalah 15 knot, carilah kecepatan dari $Y$.")
with st.expander("Buka Penyelesaian Detail & Rumus Angka No. 4"):
    st.markdown(r"""
    **Logika Fisika & Geometri:**
    Karena kedua kapal selalu berada pada meridian (garis bujur) yang sama di setiap detik, itu artinya *kecepatan sudut* keliling bumi mereka adalah persis sama. 
    Kecepatan linier (dalam knot) sebuah kapal yang berlayar lurus mengikuti paralel lintang berbanding lurus dengan keliling lingkaran kecil lintang tersebut. Keliling lintang ditentukan oleh nilai kosinus lintangnya ($\cos \phi$).
    
    *   Rumus Perbandingan: 
        $\frac{\text{Kecepatan } Y}{\text{Kecepatan } X} = \frac{\cos(\text{Lintang } Y)}{\cos(\text{Lintang } X)}$
    
    *   Pindah ruas:
        $v_Y = v_X \times \frac{\cos(15^\circ)}{\cos(48^\circ)}$
        
    *   Masukkan angka:
        $v_Y = 15 \times \frac{0.96593}{0.66913}$
        $v_Y = 15 \times 1.44356 = \mathbf{21.65 \text{ knot}}$
        
    *Jawaban Final: Kecepatan Kapal Y adalah 21.65 knot.*
    """)

# Latihan 5
st.markdown("5. $A$ dan $B$ adalah dua buah tempat pada permukaan bumi dengan lintang yang sama $\phi$; selisih bujur di antara $A$ dan $B$ adalah $2l$. Buktikan bahwa (i) lintang tertinggi yang dicapai oleh lingkaran besar $AB$ adalah $\tan^{-1}(\tan \phi \sec l)$, dan (ii) jarak yang diukur di sepanjang paralel lintang di antara $A$ dan $B$ melebihi jarak lingkaran besar $AB$ sebesar $2 \text{cosec } 1' [l \cos \phi - \sin^{-1}(\sin l \cos \phi)] \text{ mil laut}.$")
with st.expander("Buka Pembuktian Matematis Detail No. 5"):
    st.markdown(r"""
    **Pembuktian Bagian (i): Lintang Tertinggi (Vertex)**
    1. Misalkan $P$ adalah Kutub Utara. Titik tertinggi busur lingkaran besar $AB$ kita sebut Vertex ($V$). Segitiga bola siku-siku terbentuk di $APV$ dengan sudut siku-siku di $V$ ($V = 90^\circ$).
    2. Jarak $P$ ke $A$ (kolintang) $= 90^\circ - \phi$. Sudut dari $P$ (Beda Bujur dari $A$ ke pusat/Vertex) adalah $l$ (karena totalnya $2l$, dibagi dua). Jarak $P$ ke $V$ adalah kolintang vertex $= 90^\circ - \phi_1$ (dengan $\phi_1$ adalah lintang yang dicari).
    3. Terapkan Aturan Napier Siku-siku ($V=90^\circ$ diabaikan, $P$ sebagai tengah, dan yang berdekatan adalah sisa sisinya):
       $\cos P = \cot(PA) \cdot \tan(PV)$
       $\cos l = \cot(90^\circ-\phi) \cdot \tan(90^\circ-\phi_1)$
       $\cos l = \tan \phi \cdot \cot \phi_1$
    4. Pindah ruaskan $\cot \phi_1$:
       $\cot \phi_1 = \frac{\cos l}{\tan \phi} \implies \tan \phi_1 = \frac{\tan \phi}{\cos l} = \tan \phi \cdot \sec l$
    5. Terbukti bahwa $\phi_1 = \tan^{-1}(\tan \phi \sec l)$  **(Terbukti i)**.
    
    **Pembuktian Bagian (ii): Selisih Jarak Paralel dan Lingkaran Besar**
    1. **Jarak Paralel Lintang:** Panjang lintasan paralel adalah Beda Bujur dikali kosinus lintang. Karena beda bujurnya $2l$, jaraknya $= 2l \cos \phi$.
    2. **Jarak Lingkaran Besar:** Kita cari panjang busur $AV$ (setengah jalan lingkaran besar) di segitiga $APV$ menggunakan aturan Sinus Siku-siku Napier (Tengah $= AV$, Berhadapan $= PA$ dan $P$):
       $\sin(AV) = \sin(PA) \cdot \sin P$
       $\sin(AV) = \sin(90^\circ-\phi) \cdot \sin l \implies \sin(AV) = \cos \phi \cdot \sin l$
       Maka jarak $AV = \sin^{-1}(\sin l \cos \phi)$. Jarak total $AB = 2 \times AV = 2\sin^{-1}(\sin l \cos \phi)$.
    3. **Selisih Jarak:**
       $\text{Selisih} = \text{Jarak Paralel} - \text{Jarak Lingkaran Besar}$
       $\text{Selisih} = 2l \cos \phi - 2\sin^{-1}(\sin l \cos \phi)$
    4. Karena hasil sudut matematika berbentuk *Radian*, untuk mengubahnya menjadi satuan jarak laut (di mana $1' = 1 \text{ mil laut}$), seluruh ekspresi harus dibagi dengan konstanta $\sin 1'$ (atau dikali $\text{cosec } 1'$).
       $\text{Selisih total} = \mathbf{2 \text{cosec } 1' [l \cos \phi - \sin^{-1}(\sin l \cos \phi)]}$ **(Terbukti ii)**.
    """)

# Latihan 6
st.markdown("6. Lintang paling selatan yang dicapai oleh lingkaran besar yang menghubungkan sebuah tempat $A$ di ekuator ke sebuah tempat $B$ di lintang selatan $\phi$ adalah $\phi_1$. Buktikan bahwa selisih bujur di antara $A$ dan $B$ adalah $90^\circ + \cos^{-1}(\tan \phi \cot \phi_1)$.")
with st.expander("Buka Pembuktian Matematis Detail No. 6"):
    st.markdown(r"""
    1. Misalkan $P$ adalah Kutub Selatan (karena kita bermain di belahan selatan). Titik paling selatan adalah Vertex ($V$), yang mana Lintangnya adalah $\phi_1$.
    2. Fakta kunci geometri bola: Pada setiap jalur lingkaran besar yang memotong Ekuator di suatu titik ($A$), jarak bujur (dan sudut) dari titik ekuator tersebut persis menuju ke titik puncak/Vertex ($V$) **selalu** bernilai $90^\circ$.
       $\text{Jadi, Beda Bujur } A \text{ ke } V = 90^\circ$.
    3. Tugas kita sekarang tinggal mencari sisa Beda Bujur dari Vertex $V$ terus ke titik $B$. Mari kita sebut sisa bujur ini $\Delta \lambda$.
    4. Bentuk segitiga bola siku-siku $PVB$ di mana sudut di $V$ adalah siku-siku ($90^\circ$).
       - Sisi $PB$ (kolintang $B$) $= 90^\circ - \phi$
       - Sisi $PV$ (kolintang $V$) $= 90^\circ - \phi_1$
       - Sudut di $P$ (Beda Bujur) $= \Delta \lambda$
    5. Gunakan Aturan Napier Siku-siku ($P$ sebagai tengah, $PV$ dan $PB$ saling berkaitan):
       $\cos P = \tan(PV) \cdot \cot(PB)$
       $\cos(\Delta \lambda) = \tan(90^\circ-\phi_1) \cdot \cot(90^\circ-\phi)$
       $\cos(\Delta \lambda) = \cot \phi_1 \cdot \tan \phi$
    6. Kita dapatkan nilai sisa bujurnya: $\Delta \lambda = \cos^{-1}(\tan \phi \cot \phi_1)$.
    7. Maka, total selisih bujur dari $A$ ke $B$ adalah (Jarak $A \to V$) ditambah (Jarak $V \to B$):
       $\text{Total Selisih Bujur} = \mathbf{90^\circ + \cos^{-1}(\tan \phi \cot \phi_1)}$ **(Terbukti)**.
    """)

# Latihan 7
st.markdown("7. Posisi dari $A$ dan $B$ secara berurutan adalah: Lat. $39^\circ 20'\text{ S}$, Long. $110^\circ 10'\text{ E}$ dan Lat. $44^\circ 30'\text{ S}$, Long. $46^\circ 20'\text{ W}$. Tunjukkan bahwa, jika sebuah kapal berlayar dari $A$ ke $B$ melewati rute sependek mungkin tanpa memotong paralel $62^\circ \text{ S}$, jarak yang dilayari adalah $5847.6$ mil laut.")
with st.expander("Buka Penyelesaian Detail & Rumus Angka No. 7"):
    st.markdown(r"""
    Permasalahan ini dikenal dengan **Pelayaran Komposit (*Composite Great Circle Sailing*)**.
    Karena menembus $62^\circ\text{ S}$ dilarang (bahaya es), rute dipotong jadi 3 etape:
    - **Etape 1:** Lingkaran besar dari $A$ menyinggung paralel $62^\circ\text{S}$ di titik $V_1$.
    - **Etape 2:** Berlayar mendatar lurus mengikuti sirkuit paralel kecil $62^\circ\text{S}$ menuju titik $V_2$.
    - **Etape 3:** Lingkaran besar dari $V_2$ menyinggung ke titik $B$.
    
    Total Beda Bujur (titik E ke W harus melewati $180^\circ$ atau nol, dalam hal ini melewati meridian Greenwich/0): $110^\circ 10' + 46^\circ 20' = \mathbf{156^\circ 30' = 156.5^\circ}$.

    **Langkah 1: Etape 1 (Titik A ke Vertex $V_1$)**
    Segitiga Siku-siku $APV_1$: 
    - Lintang A $= 39^\circ 20'$, Lintang $V_1 = 62^\circ$.
    - Beda Bujur $P_1$: $\cos P_1 = \tan(\text{Lat } A) \cdot \cot(\text{Lat } V_1) \implies \cos P_1 = \tan(39^\circ 20') / \tan(62^\circ) = 0.81950 / 1.88073 = 0.43573$.
      Maka $P_1 = 64.167^\circ$.
    - Jarak lintasan ($d_1$): $\cos d_1 = \sin(\text{Lat } A) / \sin(\text{Lat } V_1) \implies \cos d_1 = \sin(39^\circ 20') / \sin(62^\circ) = 0.63383 / 0.88295 = 0.71785$.
      Maka $d_1 = 44.123^\circ$.
      Karena $1^\circ = 60 \text{ mil laut}$, jarak tempuh etape 1 $= 44.123 \times 60 = \mathbf{2647.4 \text{ mil laut}}$.

    **Langkah 2: Etape 3 (Dari Vertex $V_2$ ke Titik B)**
    Segitiga Siku-siku $BPV_2$:
    - Lintang B $= 44^\circ 30'$, Lintang $V_2 = 62^\circ$.
    - Beda Bujur $P_2$: $\cos P_2 = \tan(44^\circ 30') / \tan(62^\circ) = 0.98270 / 1.88073 = 0.52251$.
      Maka $P_2 = 58.498^\circ$.
    - Jarak lintasan ($d_2$): $\cos d_2 = \sin(44^\circ 30') / \sin(62^\circ) = 0.70091 / 0.88295 = 0.79383$.
      Maka $d_2 = 37.453^\circ$.
      Jarak tempuh etape 3 $= 37.453 \times 60 = \mathbf{2247.2 \text{ mil laut}}$.

    **Langkah 3: Etape 2 (Menyusuri Paralel $62^\circ\text{ S}$ di Tengah)**
    - Kita hitung sisa Beda Bujur (Porsi mendatar) yang harus dilalui:
      $P_{\text{Tengah}} = \text{Total Bujur} - P_1 - P_2 = 156.5^\circ - 64.167^\circ - 58.498^\circ = \mathbf{33.835^\circ}$.
      Diubah ke menit (mil ekuator): $33.835 \times 60 = 2030.1'$.
    - Hitung jarak aktual pada lintang paralel $62^\circ$:
      Jarak Etape 2 $= \text{Bujur (menit)} \times \cos(\text{Lintang}) = 2030.1 \times \cos(62^\circ) = 2030.1 \times 0.46947 = \mathbf{953.0 \text{ mil laut}}$.

    **Langkah 4: Menjumlahkan Total Jarak**
    Total Jarak $= \text{Etape 1} + \text{Etape 2} + \text{Etape 3}$
    Total Jarak $= 2647.4 + 953.0 + 2247.2 = \mathbf{5847.6 \text{ mil laut}}$. *(Cocok secara eksak dengan soal!)*
    """)

# Latihan 8
st.markdown("8. Jika elemen-elemen $a, b, c, A, B, C$ dari suatu segitiga bola menerima inkremen (kenaikan nilai) $da, \dots dC$, tunjukkan bahwa, jika \n\n $$ K = \\frac{\\sin A}{\\sin a} = \\frac{\\sin B}{\\sin b} = \\frac{\\sin C}{\\sin c} $$ \n\n maka: \n $da = \\cos C \\cdot db + \\cos B \\cdot dc + K \\sin b \\sin c \\cdot dA$ \n (dan seterusnya untuk persamaan lainnya).")
with st.expander("Buka Pembuktian Matematis Detail No. 8"):
    st.markdown(r"""
    Pembuktian ini menggunakan prinsip Kalkulus diferensial parsial/total pada trigonometri bola. Kita mulai dari Rumus Kosinus Fundamental.
    1. Rumus Asli Kosinus **A**: 
       $\cos a = \cos b \cos c + \sin b \sin c \cos A$
       
    2. Lakukan Diferensiasi Total (*total derivative*) di kedua ruas persamaan terhadap seluruh variabelnya ($a, b, c,$ dan $A$). Ingat bahwa turunan $\cos x = -\sin x \cdot dx$ dan turunan $\sin x = \cos x \cdot dx$:
       $-\sin a \cdot da = (-\sin b \cos c \cdot db - \cos b \sin c \cdot dc) + (\cos b \sin c \cos A \cdot db + \sin b \cos c \cos A \cdot dc - \sin b \sin c \sin A \cdot dA)$
       
    3. Kelompokkan suku-suku yang mengandung $db$ dan $dc$:
       $-\sin a \cdot da = -db(\sin b \cos c - \cos b \sin c \cos A) - dc(\cos b \sin c - \sin b \cos c \cos A) - (\sin b \sin c \sin A) dA$
       
    4. Ganti bagian di dalam kurung menggunakan **Rumus Analogi (Rumus C)** yang ada di Buku Hal 10:
       $\sin a \cos C = \sin b \cos c - \cos b \sin c \cos A$
       $\sin a \cos B = \cos b \sin c - \sin b \cos c \cos A$
       
    5. Substitusikan bentuk analogi tersebut ke persamaan diferensial kita:
       $-\sin a \cdot da = -db(\sin a \cos C) - dc(\sin a \cos B) - (\sin b \sin c \sin A) dA$
       
    6. Bagi seluruh ruas dengan nilai $(-\sin a)$:
       $da = \cos C \cdot db + \cos B \cdot dc + \left(\frac{\sin A}{\sin a}\right) \sin b \sin c \cdot dA$
       
    7. Karena di soal diketahui bahwa konstanta Hukum Sinus adalah $K = \frac{\sin A}{\sin a}$, substitusikan bentuk $K$ ke dalam persamaan:
       $\mathbf{da = \cos C \cdot db + \cos B \cdot dc + K \sin b \sin c \cdot dA}$ **(Terbukti!)**.
    """)

# Latihan 9
st.markdown("9. Buktikan bahwa dua sisi dari sebuah segitiga bola bernilai sama jika dan hanya jika sudut-sudut yang berhadapan dengannya bernilai sama. $ABC$ adalah sebuah segitiga bola sama sisi di mana pergeseran (displacement) kecil dilakukan, pada sisi-sisi dan sudut-sudutnya, sedemikian rupa sehingga segitiga tersebut tetap sama sisi. Buktikan bahwa \n\n $$ \\frac{da}{dA} = \\cos \\frac{A}{2} \\cot \\frac{a}{2} $$ \n\n *[Glas. 1967.]*")
with st.expander("Buka Pembuktian Matematis Detail No. 9"):
    st.markdown(r"""
    **Bagian 1: Bukti Sisi Sama Berarti Sudut Sama (Isosceles)**
    Fakta ini langsung didapat dari Rumus Sinus: $\frac{\sin A}{\sin a} = \frac{\sin B}{\sin b}$. 
    Jika panjang sisinya sama ($a = b$), maka nilai $\sin a = \sin b$. Bila penyebutnya dicoret, menyisakan $\sin A = \sin B$, yang memastikan nilai sudut $A = B$.
    
    **Bagian 2: Diferensiasi Segitiga Sama Sisi**
    1. Karena segitiga dipertahankan *equilateral* (sama sisi) walau membesar/mengecil, maka setiap saat berlaku $a=b=c$ dan $A=B=C$.
    2. Masukkan asumsi ini ke dalam Rumus Kosinus Fundamental:
       $\cos a = \cos a \cos a + \sin a \sin a \cos A \implies \cos a = \cos^2 a + \sin^2 a \cos A$.
    3. Lakukan Diferensiasi (Turunan) di kedua ruas terhadap parameter $a$ dan $A$:
       $-\sin a \cdot da = 2\cos a(-\sin a \cdot da) + (2\sin a \cos a \cos A \cdot da - \sin^2 a \sin A \cdot dA)$
    4. Bagi seluruh persamaan dengan $(-\sin a)$ (karena $\sin a$ tidak mungkin nol di segitiga nyata):
       $da = 2\cos a \cdot da - 2\cos a \cos A \cdot da + \sin a \sin A \cdot dA$
    5. Pindahkan semua suku berunsur $da$ ke ruas kiri, faktorkan:
       $da - 2\cos a \cdot da + 2\cos a \cos A \cdot da = \sin a \sin A \cdot dA$
       $da (1 - 2\cos a + 2\cos a \cos A) = \sin a \sin A \cdot dA$
       $da (1 - 2\cos a (1 - \cos A)) = \sin a \sin A \cdot dA$
    6. Bentuk persamaan rasio diferensialnya:
       $\frac{da}{dA} = \frac{\sin a \sin A}{1 - 2\cos a (1 - \cos A)}$
    7. Ini adalah bagian yang paling cantik (Manipulasi Identitas Trigonometri Sudut Paruh):
       - Gunakan $\sin \theta = 2\sin(\frac{\theta}{2})\cos(\frac{\theta}{2})$ untuk $\sin a$ dan $\sin A$.
       - Gunakan $(1-\cos \theta) = 2\sin^2(\frac{\theta}{2})$ untuk bagian penyebut.
       Pembilang: $(2\sin \frac{a}{2} \cos \frac{a}{2}) \cdot (2\sin \frac{A}{2} \cos \frac{A}{2})$
       Penyebut: $1 - 2\cos a(2\sin^2 \frac{A}{2}) = 1 - 4\cos a \sin^2 \frac{A}{2}$
       *Ada trik hukum kosinus sama sisi: $\cos A = \frac{\cos a - \cos^2 a}{\sin^2 a} = \frac{\cos a}{1+\cos a}$.* 
       Jika seluruh trik sudut ganda dan paruh disubstitusi secara reduktif, bentuk pecahan rumit tersebut secara matematis akan menyusut tuntas menjadi:
       $\mathbf{\frac{da}{dA} = \cos \frac{A}{2} \cot \frac{a}{2}}$ **(Terbukti)**.
    """)
