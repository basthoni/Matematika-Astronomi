import streamlit as st

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

materi_bab_1_awal = r"""
### 1. Pendahuluan
Ketika kita memandang bintang-bintang di malam yang cerah, kita mendapatkan kesan yang lazim bahwa mereka semua adalah titik-titik cahaya yang berkilauan, yang seolah-olah terletak di permukaan sebuah bola raksasa di mana masing-masing pengamat menjadi pusatnya. Mata telanjang tentu saja gagal memberikan indikasi apa pun mengenai jarak bintang-bintang tersebut dari kita; namun, hal ini memungkinkan kita untuk membuat perkiraan tentang sudut yang dibentuk di titik pengamat oleh setiap pasang bintang, dan dengan instrumen yang tepat, sudut-sudut ini dapat diukur dengan presisi yang sangat tinggi. Astronomi Bola pada dasarnya berkaitan dengan **arah** di mana bintang-bintang tersebut dilihat, dan sangatlah mudah untuk mendefinisikan arah-arah ini dalam bentuk posisi di permukaan sebuah bola—yakni **bola langit** (*celestial sphere*)—di mana garis lurus yang menghubungkan pengamat ke bintang-bintang berpotongan dengan permukaan ini. Dalam pengertian inilah ungkapan umum "posisi sebuah bintang di bola langit" harus ditafsirkan. Jari-jari bola langit ini sepenuhnya bersifat sembarang. Fondasi dari Astronomi Bola adalah geometri bola.

### 2. Segitiga bola
Setiap bidang yang melewati pusat sebuah bola akan memotong permukaan bola tersebut membentuk sebuah lingkaran yang disebut sebagai **lingkaran besar** (*great circle*). Bidang lain mana pun yang memotong bola tetapi tidak melewati titik pusat juga akan memotong permukaan membentuk sebuah lingkaran, yang dalam hal ini disebut sebagai **lingkaran kecil** (*small circle*). 

Pada Gambar 1, EAB adalah sebuah lingkaran besar, karena bidangnya melewati O, yaitu pusat bola. Misalkan QOP adalah diameter bola yang tegak lurus terhadap bidang lingkaran besar EAB. Misalkan R adalah titik mana pun pada OP dan asumsikan sebuah bidang ditarik melalui R sejajar dengan bidang EAB; permukaan bola tersebut kemudian dipotong membentuk lingkaran kecil FCD. Berdasarkan konstruksinya, OP juga tegak lurus terhadap bidang FCD. Titik-titik ujung P dan Q dari diameter tegak lurus QOP ini disebut sebagai **kutub** (*poles*) dari lingkaran besar dan dari lingkaran kecil yang sejajar tersebut. 
"""
st.markdown(materi_bab_1_awal, unsafe_allow_html=True)

# Memanggil Gambar 1
st.image("Gambar_1.png", caption="Gambar 1 - Segitiga Bola", use_container_width=True)

materi_bab_1_lanjut_1 = r"""
Ketika dua lingkaran besar berpotongan di satu titik, mereka dikatakan membentuk sebuah **sudut bola** (*spherical angle*). Perhatikan dua lingkaran besar PA dan PB yang berpotongan di P. Tarik garis PS dan PT, yang merupakan garis singgung terhadap keliling PA dan PB. PT tegak lurus terhadap jari-jari OP dan sejajar dengan jari-jari OB. Demikian pula PS sejajar dengan OA. Sudut SPT mendefinisikan sudut bola di P, dan nilainya sama dengan sudut AOB, di mana AB adalah busur yang terpotong pada lingkaran besar di antara dua lingkaran besar PA dan PB.

Jika tiga titik pada permukaan bola dihubungkan oleh busur-busur lingkaran besar, bangun yang diperoleh disebut **segitiga bola** (*spherical triangle*). Pada Gambar 1, titik A, X, dan Y membentuk segitiga bola AXY. AX, AY, dan XY adalah **sisi-sisi**, sedangkan sudut di A, X, dan Y adalah sudut-sudutnya. Jika R adalah jari-jari bola, panjang busur lingkaran besar AY dirumuskan dengan:

$$AY = R \times \text{sudut } AOY$$

Karena jari-jari bola konstan, busur AY secara sederhana adalah sudut yang dibentuknya di pusat bola. Pada segitiga bola, tidak ada sisi yang dapat bernilai sama dengan atau lebih besar dari $180^\circ$.

### 3. Panjang busur lingkaran kecil
Perhatikan Gambar 1 untuk busur lingkaran kecil CD. Panjangnya dirumuskan dengan:

$$CD = RC \times \text{sudut } CRD$$

Selain itu, panjang busur lingkaran besar AB adalah:

$$AB = OA \times \text{sudut } AOB$$

Karena bidang FCD sejajar dengan bidang EAB, maka sudut CRD = sudut AOB. Oleh karena itu,

$$CD = \frac{RC}{OA} \cdot AB$$

Karena OA = OC (jari-jari bola), dan RC tegak lurus OR, maka RC = OC $\cos(RCO)$. Dari kesejajaran, sudut RCO = sudut AOC. Dengan demikian:

$$CD = AB \cos(AOC)$$

Karena sudut AOC adalah sudut pusat busur AC, rumus dapat ditulis:

$$CD = AB \cos(AC)$$

Atau, karena PA = $90^\circ$:

$$CD = AB \sin(PC) \dots\dots(1)$$

### 4. Lintang dan bujur terestrial
Bumi dapat dianggap sebagai benda bola yang berputar pada poros diameternya PQ. P adalah kutub utara dan Q adalah kutub selatan. Lingkaran besar yang bidangnya tegak lurus terhadap PQ disebut **ekuator**. Setiap setengah-lingkaran besar yang dibatasi oleh P dan Q disebut **meridian**.

Meridian yang melewati Observatorium Greenwich (PGKQ) disepakati sebagai meridian utama. Jika PHLQ adalah meridian lain, sudut KOL didefinisikan sebagai **bujur** (*longitude*). Untuk suatu tempat J di meridian PHQ, busur ekuator LJ disebut sebagai **lintang** (*latitude*), dilambangkan dengan $\phi$.

Maka sudut POJ = $90^\circ - \phi$, yang disebut sebagai kolintang (*colatitude*):

$$\text{Colat.} = 90^\circ - \text{Lat.}$$

Semua tempat dengan garis lintang yang sama terletak pada lingkaran kecil yang disebut paralel lintang. Jika $\theta$ adalah lintang Greenwich, maka panjang busur lingkaran kecil HX relatif terhadap busur ekuator LY adalah:

$$HX = LY \cos \theta \dots\dots(2)$$

### 5. Rumus kosinus (The cosine-formula)
Misalkan ABC adalah sebuah segitiga bola. Nyatakan sisi-sisinya BC, CA, AB masing-masing sebagai a, b, c.

Dari analisis geometri bidang singgung pada segitiga DAE dan DOE di bawah bola, kita peroleh persamaan:

$$DE^2 = OA^2 [\tan^2 c + \tan^2 b - 2 \tan b \tan c \cos A] \dots\dots(5)$$

$$DE^2 = OA^2 [\sec^2 c + \sec^2 b - 2 \sec b \sec c \cos a] \dots\dots(6)$$

Berdasarkan kedua persamaan di atas, kita akan mendapatkan rumus paling fundamental dalam trigonometri bola, yang dikenal sebagai **rumus kosinus**:
"""
st.markdown(materi_bab_1_lanjut_1, unsafe_allow_html=True)

with st.expander("Syarah: Penurunan Rumus Kosinus Fundamental"):
    st.markdown(r"""
    1. Samakan kedua persamaan $DE^2$: $\sec^2 c + \sec^2 b - 2 \sec b \sec c \cos a = \tan^2 c + \tan^2 b - 2 \tan b \tan c \cos A$
    2. Gunakan identitas Pythagoras $\sec^2 \theta = 1 + \tan^2 \theta$ pada ruas kiri: $(1 + \tan^2 c) + (1 + \tan^2 b) - 2 \sec b \sec c \cos a = \tan^2 c + \tan^2 b - 2 \tan b \tan c \cos A$
    3. Coret nilai $\tan^2 c$ dan $\tan^2 b$ di kedua ruas, lalu kurangi 1, dan bagi dengan 2.
    4. Ubah ke bentuk dasar Sinus dan Kosinus, kalikan ruas dengan $(\cos b \cos c)$ sehingga penyebutnya hilang.
    5. Pindah ruaskan persamaan sehingga membuktikan $\cos a = \cos b \cos c + \sin b \sin c \cos A$.
    """)

materi_bab_1_lanjut_2 = r"""
$$\cos a = \cos b \cos c + \sin b \sin c \cos A \dots\dots(A)$$

Terdapat dua rumus pendampingnya untuk sisi yang lain:

$$\cos b = \cos c \cos a + \sin c \sin a \cos B \dots\dots(7)$$

$$\cos c = \cos a \cos b + \sin a \sin b \cos C \dots\dots(8)$$

Melalui pemanfaatan identitas setengah sudut, kita akan mendapati persamaan **Sinus Setengah Sudut** (di mana $2s = a + b + c$):

$$\sin \frac{A}{2} = \sqrt{\frac{\sin (s - b) \sin (s - c)}{\sin b \sin c}} \dots\dots(11)$$

Jika kita menggunakan pendekatan yang sama dan mensubstitusikan identitas $\cos A = 2 \cos^2 \frac{A}{2} - 1$ ke dalam rumus kosinus, kita akan mendapatkan persamaan untuk **Kosinus Setengah Sudut**:
"""
st.markdown(materi_bab_1_lanjut_2, unsafe_allow_html=True)

materi_bab_1_lanjut_3 = r"""
$$\cos \frac{A}{2} = \sqrt{\frac{\sin s \sin (s - a)}{\sin b \sin c}} \dots\dots(12)$$

Melalui pembagian persamaan (11) dan (12), kita peroleh rumus **Tangen Setengah Sudut**:

$$\tan \frac{A}{2} = \sqrt{\frac{\sin (s - b) \sin (s - c)}{\sin s \sin (s - a)}} \dots\dots(13)$$

### 6. Rumus sinus (The sine-formula)
Kita sekarang akan menurunkan pembuktian atas rumus sinus. Bertolak dari rumus kosinus sisi a, kita pindah ruaskan sehingga $\sin b \sin c \cos A = \cos a - \cos b \cos c$. Dengan mengkuadratkan kedua ruas, kita memperoleh:

$$\sin^2 b \sin^2 c \cos^2 A = \cos^2 a - 2 \cos a \cos b \cos c + \cos^2 b \cos^2 c$$

Substitusikan $\cos^2 A = 1 - \sin^2 A$. Melalui penjabaran aljabar kita dapat mendefinisikan sebuah perbandingan $X$. Karena nilai sisi dan sudut pada segitiga bola berada di antara $0^\circ$ hingga $180^\circ$ (sehingga nilai sinusnya selalu positif dan tanda minus diabaikan), kita mendapatkan kesebandingan fundamental yang disebut sebagai **Rumus B**:

$$\frac{\sin A}{\sin a} = \frac{\sin B}{\sin b} = \frac{\sin C}{\sin c} \dots\dots(B)$$
"""
st.markdown(materi_bab_1_lanjut_3, unsafe_allow_html=True)

with st.expander("Syarah: Proses Aljabar Menuju Rumus Sinus"):
    st.markdown(r"""
    Setelah kuadrat ruas dikembangkan, kita ganti $\cos^2 A$ dengan $(1 - \sin^2 A)$.
    1. $\sin^2 b \sin^2 c - \sin^2 b \sin^2 c \sin^2 A = \cos^2 a - 2\cos a\cos b\cos c + \cos^2 b\cos^2 c$
    2. Susun ulang untuk mencari nilai $\sin^2 A$:
       $\sin^2 b \sin^2 c \sin^2 A = \sin^2 b \sin^2 c - \cos^2 a + 2\cos a\cos b\cos c - \cos^2 b\cos^2 c$
    3. Ganti $\sin^2$ di ruas kanan dengan $(1 - \cos^2)$:
       $= (1-\cos^2 b)(1-\cos^2 c) - \cos^2 a + 2\cos a\cos b\cos c - \cos^2 b\cos^2 c$
    4. Setelah disederhanakan, kita dapati ruas kanan bernilai identik tanpa memandang sudut apa yang diuji:
       $\frac{\sin^2 A}{\sin^2 a} = \frac{1 - \cos^2 a - \cos^2 b - \cos^2 c + 2\cos a\cos b\cos c}{\sin^2 a \sin^2 b \sin^2 c}$
    5. Menarik akar dari rumusan di atas menghasilkan Rumus Sinus.
    """)

materi_bab_1_lanjut_4 = r"""
### 7. Rumus Analogi (The analogue formula)
Jika kita menuliskan kembali persamaan (7) kemudian mensubstitusikan ekspresi $\cos a$ dari rumus dasar (A), kita akan mendapati persamaan aljabar:

$$\sin c \sin a \cos B = \cos b - \cos c (\cos b \cos c + \sin b \sin c \cos A)$$

$$\sin c \sin a \cos B = \cos b (1 - \cos^2 c) - \sin b \sin c \cos c \cos A$$

Dengan membagi kedua ruas menggunakan $\sin c$, kita memperoleh hubungan yang melibatkan ketiga sisi dan dua sudut (Rumus C):

$$\sin a \cos B = \cos b \sin c - \sin b \cos c \cos A \dots\dots(C)$$

$$\sin a \cos C = \cos c \sin b - \sin c \cos b \cos A \dots\dots(14)$$

### 8. Rumus Empat Bagian (The four-parts formula)
Pada segitiga bola $ABC$, perhatikan empat unsur berurutan, misalnya $B, a, C, b$. Sisi di antara dua sudut (sisi a) disebut "sisi dalam" (*inner side*), dan sudut di antara dua sisi (sudut C) disebut "sudut dalam" (*inner angle*). Modifikasi substitusi menghasilkan **Rumus D**:

$$\cos a \cos C = \sin a \cot b - \sin C \cot B \dots\dots(D)$$

Sebagai bantuan memori, rumus ini dapat dibaca:
**$\cos(\text{sisi dlm}) \cdot \cos(\text{sudut dlm}) = \sin(\text{sisi dlm}) \cdot \cot(\text{sisi luar}) - \sin(\text{sudut dlm}) \cdot \cot(\text{sudut luar})$**

### 9. Segitiga Siku-Siku dan Aturan Napier
Jika salah satu sudut segitiga bola bernilai $90^\circ$, segitiga tersebut disebut **segitiga siku-siku** (*right-angled triangle*). Jika salah satu sisinya bernilai $90^\circ$, disebut **segitiga kuadran** (*quadrantal*). 

Aturan klasik yang dicetuskan oleh John Napier menggunakan susunan melingkar dari lima "bagian" (*circular parts*). Jika satu variabel dipilih sebagai "tengah" (*middle*), dua variabel di sebelahnya adalah "yang berdekatan" (*adjacents*) dan dua sisanya adalah "yang berhadapan" (*opposites*). Hukum Napier berbunyi:
* $\sin(\text{tengah}) = \text{hasil kali tangen dari yang berdekatan}$
* $\sin(\text{tengah}) = \text{hasil kali kosinus dari yang berhadapan}$

### 10. Rumus Polar
Konsep segitiga polar $A'B'C'$ dibangun dengan menetapkan kutub-kutub dari sisi segitiga asli $ABC$. Pada geometri ini, sudut dan sisi saling terhubung melalui relasi suplemen: $a' = 180^\circ - A$ dan $A' = 180^\circ - a$. Dengan menerapkan rumus (A) pada segitiga polar, kita memperoleh rumus kosinus untuk sudut:

$$\cos A = -\cos B \cos C + \sin B \sin C \cos a$$
"""
st.markdown(materi_bab_1_lanjut_4, unsafe_allow_html=True)

materi_bab_1_lanjut_5 = r"""
### 11. Rumus Haversine
Dalam astronomi dan navigasi, banyak perhitungan jarak menjadi jauh lebih praktis dan bebas dari ambiguitas kuadran dengan menggunakan fungsi *haversine* (*half-versed-sine*). Haversine dari sudut $\theta$ didefinisikan sebagai:

$$\text{hav } \theta = \frac{1}{2}(1 - \cos \theta) = \sin^2 \frac{\theta}{2} \dots\dots(21)$$

Modifikasi dari rumus kosinus fundamental menghasilkan bentuk persamaan haversine yang selalu bernilai positif:

$$\text{hav } a = \text{hav} (b - c) + \sin b \sin c \text{ hav } A \dots\dots(23)$$

### 12. Analogi Delambre dan Napier
Untuk referensi tingkat lanjut, berikut adalah formula-formula yang diturunkan untuk memecahkan segitiga bola ketika dua sisi dan sudut yang diapitnya diketahui (Analogi Napier):

$$\tan \frac{1}{2}(A+B) = \frac{\cos \frac{1}{2}(a-b)}{\cos \frac{1}{2}(a+b)} \cot \frac{1}{2}C \dots\dots(51)$$

$$\tan \frac{1}{2}(A-B) = \frac{\sin \frac{1}{2}(a-b)}{\sin \frac{1}{2}(a+b)} \cot \frac{1}{2}C \dots\dots(52)$$

*(Akhir Bab 1)*
"""
st.markdown(materi_bab_1_lanjut_5, unsafe_allow_html=True)
