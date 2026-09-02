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

materi_bab_1_hal_1_2 = r"""
### 1. Pendahuluan
Ketika kita memandang bintang-bintang di malam yang cerah, kita mendapatkan kesan yang lazim bahwa mereka semua adalah titik-titik cahaya yang berkilauan, yang seolah-olah terletak di permukaan sebuah bola raksasa di mana masing-masing pengamat menjadi pusatnya. Mata telanjang tentu saja gagal memberikan indikasi apa pun mengenai jarak bintang-bintang tersebut dari kita; namun, hal ini memungkinkan kita untuk membuat perkiraan tentang sudut yang dibentuk di titik pengamat oleh setiap pasang bintang, dan dengan instrumen yang tepat, sudut-sudut ini dapat diukur dengan presisi yang sangat tinggi. Astronomi Bola pada dasarnya berkaitan dengan **arah** di mana bintang-bintang tersebut dilihat, dan sangatlah mudah untuk mendefinisikan arah-arah ini dalam bentuk posisi di permukaan sebuah bola—yakni **bola langit** (*celestial sphere*)—di mana garis lurus yang menghubungkan pengamat ke bintang-bintang berpotongan dengan permukaan ini. Dalam pengertian inilah ungkapan umum "posisi sebuah bintang di bola langit" harus ditafsirkan. Jari-jari bola langit ini sepenuhnya bersifat sembarang. Fondasi dari Astronomi Bola adalah geometri bola.

### 2. Segitiga bola
Setiap bidang yang melewati pusat sebuah bola akan memotong permukaan bola tersebut membentuk sebuah lingkaran yang disebut sebagai **lingkaran besar** (*great circle*). Bidang lain mana pun yang memotong bola tetapi tidak melewati titik pusat juga akan memotong permukaan membentuk sebuah lingkaran, yang dalam hal ini disebut sebagai **lingkaran kecil** (*small circle*). 

Pada Gambar 1, EAB adalah sebuah lingkaran besar, karena bidangnya melewati O, yaitu pusat bola. Misalkan QOP adalah diameter bola yang tegak lurus terhadap bidang lingkaran besar EAB. Misalkan R adalah titik mana pun pada OP dan asumsikan sebuah bidang ditarik melalui R sejajar dengan bidang EAB; permukaan bola tersebut kemudian dipotong membentuk lingkaran kecil FCD. Berdasarkan konstruksinya, OP juga tegak lurus terhadap bidang FCD. Titik-titik ujung P dan Q dari diameter tegak lurus QOP ini disebut sebagai **kutub** (*poles*) dari lingkaran besar dan dari lingkaran kecil yang sejajar tersebut. Sekarang misalkan PCAQ adalah sembarang lingkaran besar yang melewati kutub P dan Q serta memotong lingkaran kecil FCD dan lingkaran besar EAB berturut-turut di C dan A. Demikian pula, PDB adalah bagian dari lingkaran besar lain yang melewati P dan Q. Untuk memudahkan, kita dapat merujuk pada suatu lingkaran besar tertentu cukup dengan menyebutkan bagian mana pun dari garis kelilingnya. Ketika dua lingkaran besar berpotongan di satu titik, mereka dikatakan membentuk sebuah **sudut bola** (*spherical angle*) yang didefinisikan sebagai berikut. Perhatikan dua lingkaran besar PA dan PB yang berpotongan di P. Tarik garis PS dan PT, yang merupakan garis singgung terhadap keliling PA dan PB berturut-turut.
"""
st.markdown(materi_bab_1_hal_1_2, unsafe_allow_html=True)

# Memanggil Gambar 1
st.image("Gambar_1.png", caption="Gambar 1", use_container_width=True)

materi_bab_1_hal_2_4 = r"""
PT, berdasarkan konstruksinya, tegak lurus terhadap jari-jari OP dari lingkaran besar PB dan, karena berada di bidang PBO, maka sejajar dengan jari-jari OB. Demikian pula PS sejajar dengan jari-jari OA. Sudut SPT mendefinisikan sudut bola di P antara dua lingkaran besar PA dan PB, dan nilainya sama dengan sudut AOB, di mana AB adalah busur yang terpotong pada lingkaran besar, di mana P adalah kutubnya, di antara dua lingkaran besar PA dan PB. Perlu ditekankan bahwa sudut bola hanya didefinisikan dengan mengacu pada dua lingkaran besar yang berpotongan.

Jika kita diberikan sembarang tiga titik pada permukaan sebuah bola, maka bola tersebut dapat dibelah dua sehingga ketiga titik tersebut terletak di belahan bola yang sama. Jika titik-titik tersebut dihubungkan oleh busur-busur lingkaran besar yang semuanya terletak pada belahan bola ini, bangun yang diperoleh disebut **segitiga bola** (*spherical triangle*). Jadi, pada Gambar 1, tiga titik A, X, dan Y di permukaan bola dihubungkan oleh busur lingkaran besar untuk membentuk segitiga bola AXY. AX, AY, dan XY adalah **sisi-sisi** dan sudut bola di A, X, dan Y adalah sudut-sudut dari segitiga bola tersebut. Sebenarnya, jika R adalah jari-jari bola, panjang busur lingkaran besar AY dirumuskan dengan:

$$AY = R \times \text{sudut } AOY,$$

di mana sudut AOY dinyatakan dalam ukuran melingkar, yaitu dalam radian. Karena untuk semua busur lingkaran besar pada bola jari-jari R adalah konstan, maka memudahkan jika kita menganggap panjangnya sebagai satu kesatuan (*unity*). Busur AY kemudian secara sederhana adalah sudut yang dibentuknya di pusat bola. Jika AY adalah, katakanlah, seperdelapan dari keliling lingkaran besar utuh yang melalui A dan Y, maka sisi AY adalah $\pi/4$ dalam ukuran melingkar dan tidak ada ambiguitas jika dinyatakan sebagai $45^\circ$; demikian pula untuk sisi-sisi segitiga yang tersisa. Berdasarkan definisi segitiga bola, tidak ada sisi yang dapat sama dengan atau lebih besar dari $180^\circ$. Sebagai contoh lain, PAB adalah segitiga bola di mana dua sisinya, PA dan PB, masing-masing membentuk sudut $\pi/2$ radian atau $90^\circ$ di O; dalam contoh ini kita katakan bahwa PA dan PB masing-masing sama dengan $\pi/2$ radian atau $90^\circ$. Tetapi PCD *bukanlah* segitiga bola, karena busur CD bukanlah bagian dari lingkaran besar. Oleh karena itu, rumus-rumus yang akan diturunkan untuk segitiga bola tidak akan berlaku untuk bangun seperti PCD.

### 3. Panjang busur lingkaran kecil
Perhatikan, pada Gambar 1, busur lingkaran kecil CD. Panjangnya dirumuskan dengan:

$$CD = RC \times \text{sudut } CRD.$$

Selain itu, panjang busur lingkaran besar AB dirumuskan dengan:

$$AB = OA \times \text{sudut } AOB.$$

Tetapi karena bidang FCD sejajar dengan bidang EAB, maka $C\hat{R}D = A\hat{O}B$, karena RC, RD berturut-turut sejajar dengan OA, OB. Oleh karena itu:

$$CD = \frac{RC}{OA} \cdot AB.$$

Tetapi, karena OA = OC (jari-jari bola), kita peroleh:

$$CD = \frac{RC}{OC} \cdot AB.$$

Sekarang RC tegak lurus terhadap OR; $\therefore RC = OC \cos R\hat{C}O$. Dari kesejajaran RC dan OA, $R\hat{C}O = A\hat{O}C$. Oleh karena itu:

$$CD = AB \cos A\hat{O}C.$$

Sekarang AOC adalah sudut yang dibentuk di pusat bola oleh busur lingkaran besar AC. Rumus tersebut kemudian dapat ditulis sebagai:

$$CD = AB \cos AC,$$

atau, karena PA = $90^\circ$,

$$CD = AB \sin PC \dots\dots(1).$$

### 4. Lintang dan bujur terestrial
Konsep-konsep yang diperkenalkan sejauh ini sekarang akan diilustrasikan dengan mengacu pada bumi. Untuk banyak masalah praktis, bumi dapat dianggap sebagai benda bola yang berputar pada poros diameternya PQ (Gambar 2). P adalah kutub utara dan Q adalah kutub selatan. Lingkaran besar yang bidangnya tegak lurus terhadap PQ disebut **ekuator**. Setiap setengah-lingkaran besar yang dibatasi oleh P dan Q adalah sebuah
"""
st.markdown(materi_bab_1_hal_2_4, unsafe_allow_html=True)

# Tempat memanggil Gambar 2 (pastikan Bapak sudah mengunggah file Gambar_2.png)
st.image("Gambar_2.png", caption="Gambar 2", use_container_width=True)

materi_bab_1_hal_5_6 = r"""
**meridian**. Secara khusus, meridian yang melewati instrumen fundamental (lingkaran transit) di Observatorium Greenwich, berdasarkan kesepakatan universal, dianggap sebagai meridian utama atau meridian standar; misalkan meridian tersebut adalah PGKQ pada Gambar 2, yang memotong ekuator di K. Misalkan PHLQ adalah meridian lain yang memotong ekuator di L. Sudut KOL didefinisikan sebagai **bujur** (*longitude*) dari meridian PHQ dan sama halnya dapat dideskripsikan sebagai busur ekuatorial KL atau sudut bola KPL. Bujur diukur dari $0^\circ$ hingga $180^\circ$ ke arah timur dari meridian Greenwich dan dari $0^\circ$ hingga $180^\circ$ ke arah barat, mengikuti arah panah di dekat K pada Gambar 2. Jadi, dari gambar tersebut, bujur dari meridian PHQ adalah sekitar $100^\circ$ timur (E) dan dari meridian PMQ adalah sekitar $60^\circ$ barat (W). Semua tempat di meridian yang sama memiliki bujur yang sama, dan meridian tempat suatu tempat tertentu berada dispesifikasikan dengan mengacu pada meridian utama PGQ. Untuk menentukan secara lengkap posisi suatu tempat di permukaan bumi, kita perlu mendeskripsikan posisinya pada meridian bujurnya. Hal ini dilakukan dengan mengacu pada ekuator. Perhatikan suatu tempat J di meridian PHQ. Meridian yang melewati J memotong ekuator di L dan sudut LOJ, atau busur lingkaran besar LJ, disebut sebagai **lintang** (*latitude*) dari J. Jika J berada di antara ekuator dan kutub utara P, seperti pada Gambar 2, lintangnya disebut lintang utara (N); suatu tempat seperti R, di antara ekuator dan kutub selatan Q, disebut memiliki lintang selatan (S). Dengan cara ini, posisi titik mana pun di permukaan bumi dirujuk pada dua lingkaran besar yang mendasar, yaitu ekuator dan meridian Greenwich.

Misalkan $\phi$ melambangkan lintang J; maka $L\hat{O}J$ atau $LJ = \phi$. Karena OP tegak lurus terhadap bidang ekuator, $P\hat{O}L = 90^\circ$ dan oleh karena itu $POJ = 90^\circ - \phi$. Sudut POJ atau busur bola PJ adalah kolintang (*colatitude*) dari J. Kita peroleh dengan demikian:

$$\text{Colat.} = 90^\circ - \text{Lat.}$$

Semua tempat yang memiliki lintang yang sama terletak pada lingkaran kecil yang sejajar dengan ekuator, disebut sebagai *paralel lintang* (*parallel of latitude*). Dengan demikian, semua tempat dengan lintang yang sama dengan Greenwich terletak pada lingkaran kecil MGHX. Jika $\theta$ melambangkan lintang Greenwich, maka berdasarkan rumus (1) panjang busur lingkaran kecil HX, misalnya, diberikan dalam bentuk panjang busur ekuatorial yang bersesuaian LY oleh:

$$HX = LY \cos \theta \dots\dots(2).$$

Untuk memberikan presisi yang lebih besar terhadap makna rumus ini, kita mempertimbangkan unit-unit di mana jarak pada permukaan bumi dinyatakan. Yang paling sederhana adalah yang didefinisikan sebagai jarak lingkaran besar di antara dua titik yang membentuk sudut satu menit busur di pusat bumi—unit ini dikenal sebagai **mil laut** (*nautical mile*) dan setara dengan 6080 kaki (kita mengabaikan variasi kecil dalam nilai ini karena fakta bahwa bumi tidak sepenuhnya bulat sempurna). Jika perbedaan bujur antara dua tempat yang mana pun di paralel lintang yang sama diketahui, misal LY, maka LY dapat dinyatakan sebagai sekian menit busur dan angka ini adalah jumlah mil laut di antara dua titik L dan Y di ekuator. Rumus (2) kemudian menyediakan sarana untuk menghitung jarak antara H dan X yang dinyatakan dalam mil laut (atau menit busur) dan *diukur sepanjang paralel lintang*.

### 5. Rumus kosinus (The cosine-formula)
Misalkan ABC adalah sebuah segitiga bola (Gambar 3). Nyatakan sisi-sisinya BC, CA, AB masing-masing dengan a, b, dan c. Kemudian, berdasarkan definisi kita,
"""
st.markdown(materi_bab_1_hal_5_6, unsafe_allow_html=True)

# Tempat memanggil Gambar 3 (pastikan Bapak sudah mengunggah file Gambar_3.png)
st.image("Gambar_3.png", caption="Gambar 3", use_container_width=True)

materi_bab_1_hal_7_10 = r"""
sisi a diukur dari sudut BOC yang dibentuk di pusat O dari bola oleh busur lingkaran besar BC. Demikian pula, b dan c diukur masing-masing oleh sudut AOC dan AOB. Misalkan AD adalah garis singgung di A ke lingkaran besar AB dan AE adalah garis singgung di A ke lingkaran besar AC. Maka jari-jari OA tegak lurus terhadap AD dan AE. Berdasarkan konstruksi, AD terletak pada bidang lingkaran besar AB; oleh karena itu, jika jari-jari OB diperpanjang, ia akan memotong garis singgung AD di suatu titik D. Demikian pula, jari-jari OC saat diperpanjang akan bertemu dengan garis singgung AE di E. Sekarang sudut bola BAC didefinisikan sebagai sudut antara garis singgung di A terhadap lingkaran besar AB dan AC, sehingga sudut bola $BAC = D\hat{A}E$. Sudut bola BAC akan dilambangkan secara sederhana dengan A, sehingga $D\hat{A}E = A$.

Sekarang, pada segitiga bidang datar OAD, $O\hat{A}D$ bernilai $90^\circ$ dan $A\hat{O}D$, yang identik dengan $A\hat{O}B$, bernilai c. Maka kita peroleh:

$$AD = OA \tan c ; \quad OD = OA \sec c \dots\dots(3).$$

Dari segitiga bidang datar OAE, secara serupa, kita peroleh:

$$AE = OA \tan b ; \quad OE = OA \sec b \dots\dots(4).$$

Dari segitiga bidang datar DAE, kita peroleh:

$$DE^2 = AD^2 + AE^2 - 2AD \cdot AE \cos D\hat{A}E,$$

atau

$$DE^2 = OA^2 [\tan^2 c + \tan^2 b - 2 \tan b \tan c \cos A] \dots\dots(5).$$

Dari segitiga bidang datar DOE,

$$DE^2 = OD^2 + OE^2 - 2OD \cdot OE \cos D\hat{O}E.$$

Tetapi $D\hat{O}E = B\hat{O}C = a$;
$\therefore DE^2 = OA^2 [\sec^2 c + \sec^2 b - 2 \sec b \sec c \cos a] \dots\dots(6).$

Oleh karena itu, dari persamaan (5) dan (6),

$$\sec^2 c + \sec^2 b - 2 \sec b \sec c \cos a = \tan^2 c + \tan^2 b - 2 \tan b \tan c \cos A.$$

Sekarang $\sec^2 c = 1 + \tan^2 c$, $\sec^2 b = 1 + \tan^2 b$, dan setelah beberapa penyederhanaan kita memperoleh:

$$\cos a = \cos b \cos c + \sin b \sin c \cos A \dots\dots(A).$$

Ini adalah rumus fundamental dari trigonometri bola dan pada halaman-halaman selanjutnya akan disebut sebagai **rumus kosinus** (*cosine-formula*) atau rumus **A**. Jelas terdapat dua rumus pendampingnya; mereka adalah:

$$\cos b = \cos c \cos a + \sin c \sin a \cos B \dots\dots(7),$$

$$\cos c = \cos a \cos b + \sin a \sin b \cos C \dots\dots(8).$$

Dari ketiga rumus—**A**, (7) dan (8)—semua rumus trigonometri bola lain yang digunakan dapat diturunkan. Rumus fundamental memiliki dua penerapan praktis secara langsung:
(1) Jika dua sisi, misal b dan c, dan sudut yang diapit A dari segitiga bola ABC diketahui, rumus **A** memungkinkan penghitungan atas sisi ketiga a dilakukan.
(2) Jika ketiga sisi diketahui, sudut-sudut segitiga dapat ditemukan secara berurutan dengan menggunakan **A**, (7) dan (8).

Karena, seandainya nilai A yang dicari; maka melalui **A**:

$$\cos A = \text{cosec } b \text{ cosec } c [\cos a - \cos b \cos c] \dots\dots(9).$$

Rumus (9) dapat digantikan dengan bentuk yang lebih cocok untuk penghitungan logaritmik sebagai berikut. Karena $\cos A = 1 - 2 \sin^2 \frac{A}{2}$, kita peroleh, dari **A**,

$$\cos a = \cos b \cos c + \sin b \sin c \left(1 - 2 \sin^2 \frac{A}{2}\right)$$

$$= \cos (b - c) - 2 \sin b \sin c \sin^2 \frac{A}{2},$$

atau

$$\cos (b - c) - \cos a = 2 \sin b \sin c \sin^2 \frac{A}{2};$$

$$\therefore 2 \sin \frac{a + (b - c)}{2} \sin \frac{a - (b - c)}{2} = 2 \sin b \sin c \sin^2 \frac{A}{2}.$$

Misalkan s didefinisikan dengan:

$$2s = a + b + c \dots\dots(10).$$

Maka $a + b - c = 2 (s - c)$ dan $a - b + c = 2 (s - b)$.
Oleh karena itu:

$$\sin (s - b) \sin (s - c) = \sin b \sin c \sin^2 \frac{A}{2};$$

$$\therefore \sin \frac{A}{2} = \sqrt{\frac{\sin (s - b) \sin (s - c)}{\sin b \sin c}} \dots\dots(11).$$

Bentuk ini berguna dalam pengerjaan numerik. Terdapat dua persamaan serupa yang memberikan $\sin \frac{B}{2}$ dan $\sin \frac{C}{2}$.

Jika kita menulis $\cos A = 2 \cos^2 \frac{A}{2} - 1$ ke dalam rumus **A** dan memprosesnya seperti sebelumnya, kita akan memperoleh:

$$\cos \frac{A}{2} = \sqrt{\frac{\sin s \sin (s - a)}{\sin b \sin c}} \dots\dots(12)$$

dengan dua persamaan serupa yang memberikan $\cos \frac{B}{2}$ dan $\cos \frac{C}{2}$.

Melalui pembagian persamaan (11) dan (12) kita peroleh:

$$\tan \frac{A}{2} = \sqrt{\frac{\sin (s - b) \sin (s - c)}{\sin s \sin (s - a)}} \dots\dots(13).$$

Terdapat dua persamaan serupa, yang memberikan $\tan \frac{B}{2}$ dan $\tan \frac{C}{2}$. 
Persamaan (11), (12) maupun (13) mana pun dapat digunakan untuk menghitung A, jika ketiga sisinya diketahui.

### 6. Rumus sinus (The sine-formula)
Kita sekarang akan menurunkan apa yang dikenal sebagai rumus sinus. Dari rumus kosinus A, kita peroleh:

$$\sin b \sin c \cos A = \cos a - \cos b \cos c.$$

Dengan mengkuadratkannya, kita memperoleh:

$$\sin^2 b \sin^2 c \cos^2 A = \cos^2 a - 2 \cos a \cos b \cos c + \cos^2 b \cos^2 c.$$

Sisi sebelah kiri dapat ditulis sebagai:

$$\sin^2 b \sin^2 c - \sin^2 b \sin^2 c \sin^2 A,$$

atau

$$1 - \cos^2 b - \cos^2 c + \cos^2 b \cos^2 c - \sin^2 b \sin^2 c \sin^2 A.$$

Oleh karena itu:

$$\sin^2 b \sin^2 c \sin^2 A = 1 - \cos^2 a - \cos^2 b - \cos^2 c + 2 \cos a \cos b \cos c.$$

Misalkan suatu besaran positif X didefinisikan dengan:

$$X^2 \sin^2 a \sin^2 b \sin^2 c = 1 - \cos^2 a - \cos^2 b - \cos^2 c + 2 \cos a \cos b \cos c.$$

Maka, dari persamaan sebelumnya,

$$\frac{\sin^2 A}{\sin^2 a} = X^2,$$

sehingga

$$X = \pm \frac{\sin A}{\sin a}.$$

Tetapi dalam segitiga bola, masing-masing sisinya kurang dari $180^\circ$, dan hal ini juga berlaku untuk sudut-sudutnya. Karena $\sin \theta$ bernilai positif untuk semua nilai $\theta$ antara $0^\circ$ dan $180^\circ$, tanda minus pada persamaan di atas tidak dapat diterima (*inadmissible*), dan kita peroleh:

$$X = \frac{\sin A}{\sin a}.$$

Dengan memproses persamaan (7) dan (8) menggunakan cara yang serupa, kita akan memperoleh:

$$X = \frac{\sin B}{\sin b} = \frac{\sin C}{\sin c}.$$

Oleh karena itu:

$$\frac{\sin A}{\sin a} = \frac{\sin B}{\sin b} = \frac{\sin C}{\sin c} \dots\dots(B).$$

Hasil ini akan kita rujuk sebagai **rumus sinus** (*sine-formula*) atau rumus **B**.
Rumus **B** memberikan suatu relasi antara sembarang dua sisi dari sebuah segitiga dan dua sudut yang berhadapan (*opposite*) dengan sisi-sisi tersebut. Namun, ia harus digunakan dengan kehati-hatian (*circumspection*) dalam perhitungan numerik; karena, andaikan kedua sisi a dan b beserta sudut B diketahui, maka melalui **B**:

$$\sin A = \frac{\sin a \sin B}{\sin b},$$

dari mana nilai $\sin A$ dapat dihitung. Tetapi $\sin(180^\circ - A) = \sin A$, dan tanpa informasi tambahan adalah tidak mungkin untuk memutuskan mana di antara dua sudut $A$ atau $180^\circ - A$ yang merepresentasikan solusi yang benar. Ambiguitas analogis pada trigonometri bidang datar dapat diingatkan kembali ke perhatian pembaca.

### 7. Rumus Analogi (The analogue formula)
Tuliskan persamaan (7) ke dalam bentuk:

$$\sin c \sin a \cos B = \cos b - \cos c \cos a$$
$$= \cos b - \cos c (\cos b \cos c + \sin b \sin c \cos A)$$
$$= \sin^2 c \cos b - \sin b \sin c \cos c \cos A.$$

Oleh karena itu, dengan membaginya dengan $\sin c$, kita peroleh:

$$\sin a \cos B = \cos b \sin c - \sin b \cos c \cos A \dots\dots(C),$$

sebuah relasi yang melibatkan ketiga belas sisi dan dua sudut.
Kita dapat dengan mudah membuktikan dengan cara yang serupa, dimulai dari persamaan (8), bahwa:

$$\sin a \cos C = \cos c \sin b - \sin c \cos b \cos A \dots\dots(14).$$

Seperti yang telah kita lihat, rumus kosinus **A** memberikan nilai $\cos a$ dalam bentuk b, c, dan sudut apit A. Rumus-rumus **C** dan (14) adalah, dalam beberapa hal, analog dengan **A** karena rumus tersebut memberikan nilai $\sin a \times \text{kosinus}$ dari salah satu...
"""
st.markdown(materi_bab_1_hal_7_10, unsafe_allow_html=True)
