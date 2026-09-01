import streamlit as st

# Konfigurasi Halaman
st.set_page_config(page_title="Modul Matematika Astronomi", page_icon="🔭", layout="wide")

# Header Modul
st.title("Modul Matematika Astronomi")
st.subheader("Program Studi Ilmu Falak - FSH UIN Walisongo")
st.markdown("**Disusun oleh:** M. Basthoni")
st.divider()

# Konten Modul (Menggunakan raw string r""" agar backslash LaTeX aman)
materi_bab_1 = r"""
# BAB I: TRIGONOMETRI SFERIS

### 1. Pendahuluan
Ketika kita memandang bintang-bintang di malam yang cerah, kita mendapatkan kesan yang lazim bahwa mereka semua adalah titik-titik cahaya yang berkilauan, yang seolah-olah terletak di permukaan sebuah bola raksasa di mana masing-masing pengamat menjadi pusatnya. Mata telanjang tentu saja gagal memberikan indikasi apa pun mengenai jarak bintang-bintang tersebut dari kita; namun, hal ini memungkinkan kita untuk membuat perkiraan tentang sudut yang dibentuk di titik pengamat oleh setiap pasang bintang, dan dengan instrumen yang tepat, sudut-sudut ini dapat diukur dengan presisi yang sangat tinggi. Astronomi Sferis pada dasarnya berkaitan dengan **arah** di mana bintang-bintang tersebut dilihat, dan sangatlah mudah untuk mendefinisikan arah-arah ini dalam bentuk posisi di permukaan sebuah bola—yakni **bola langit** (*celestial sphere*)—di mana garis lurus yang menghubungkan pengamat ke bintang-bintang berpotongan dengan permukaan ini. Dalam pengertian inilah ungkapan umum "posisi sebuah bintang di bola langit" harus ditafsirkan. Jari-jari bola langit ini sepenuhnya bersifat sembarang. Fondasi dari Astronomi Sferis adalah geometri bola.

### 2. Segitiga sferis
Setiap bidang yang melewati pusat sebuah bola akan memotong permukaan bola tersebut membentuk sebuah lingkaran yang disebut sebagai **lingkaran besar** (*great circle*). Bidang lain mana pun yang memotong bola tetapi tidak melewati titik pusat juga akan memotong permukaan membentuk sebuah lingkaran, yang dalam hal ini disebut sebagai **lingkaran kecil** (*small circle*). 

Pada Gambar 1, EAB adalah sebuah lingkaran besar, karena bidangnya melewati O, yaitu pusat bola. Misalkan QOP adalah diameter bola yang tegak lurus terhadap bidang lingkaran besar EAB. Misalkan R adalah titik mana pun pada OP dan asumsikan sebuah bidang ditarik melalui R sejajar dengan bidang EAB; permukaan bola tersebut kemudian dipotong membentuk lingkaran kecil FCD. Berdasarkan konstruksinya, OP juga tegak lurus terhadap bidang FCD. Titik-titik ujung P dan Q dari diameter tegak lurus QOP ini disebut sebagai **kutub** (*poles*) dari lingkaran besar dan dari lingkaran kecil yang sejajar tersebut. 

> *(Catatan: Gambar 1 dapat ditambahkan nanti via URL atau folder lokal)*

Ketika dua lingkaran besar berpotongan di satu titik, mereka dikatakan membentuk sebuah **sudut sferis** (*spherical angle*). Perhatikan dua lingkaran besar PA dan PB yang berpotongan di P. Tarik garis PS dan PT, yang merupakan garis singgung terhadap keliling PA dan PB. PT tegak lurus terhadap jari-jari OP dan sejajar dengan jari-jari OB. Demikian pula PS sejajar dengan OA. Sudut SPT mendefinisikan sudut sferis di P, dan nilainya sama dengan sudut AOB, di mana AB adalah busur yang terpotong pada lingkaran besar di antara dua lingkaran besar PA dan PB.

Jika tiga titik pada permukaan sferis dihubungkan oleh busur-busur lingkaran besar, bangun yang diperoleh disebut **segitiga sferis** (*spherical triangle*). Pada Gambar 1, titik A, X, dan Y membentuk segitiga sferis AXY. AX, AY, dan XY adalah **sisi-sisi**, sedangkan sudut di A, X, dan Y adalah sudut-sudutnya. Jika R adalah jari-jari bola, panjang busur lingkaran besar AY dirumuskan dengan:

$$AY = R \times \text{sudut } AOY$$

Karena jari-jari bola konstan, busur AY secara sederhana adalah sudut yang dibentuknya di pusat bola. Pada segitiga sferis, tidak ada sisi yang dapat bernilai sama dengan atau lebih besar dari $180^\circ$.

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
Bumi dapat dianggap sebagai benda sferis yang berputar pada poros diameternya PQ (Gambar 2). P adalah kutub utara dan Q adalah kutub selatan. Lingkaran besar yang bidangnya tegak lurus terhadap PQ disebut **ekuator**. Setiap setengah-lingkaran besar yang dibatasi oleh P dan Q disebut **meridian**.

> *(Catatan: Gambar 2 dapat ditambahkan nanti)*

Meridian yang melewati Observatorium Greenwich (PGKQ) disepakati sebagai meridian utama. Jika PHLQ adalah meridian lain, sudut KOL didefinisikan sebagai **bujur** (*longitude*). Untuk suatu tempat J di meridian PHQ, busur ekuator LJ disebut sebagai **lintang** (*latitude*), dilambangkan dengan $\phi$.

Maka sudut POJ = $90^\circ - \phi$, yang disebut sebagai kolintang (*colatitude*):

$$\text{Colat.} = 90^\circ - \text{Lat.}$$

Semua tempat dengan garis lintang yang sama terletak pada lingkaran kecil yang disebut paralel lintang. Jika $\theta$ adalah lintang Greenwich, maka panjang busur lingkaran kecil HX relatif terhadap busur ekuator LY adalah:

$$HX = LY \cos \theta \dots\dots(2)$$

### 5. Rumus kosinus (The cosine-formula)
Misalkan ABC adalah sebuah segitiga sferis (Gambar 3). Nyatakan sisi-sisinya BC, CA, AB masing-masing sebagai a, b, c.

> *(Catatan: Gambar 3 dapat ditambahkan nanti)*

Dari analisis geometri bidang singgung pada segitiga DAE dan DOE di bawah bola, kita peroleh persamaan:

$$DE^2 = OA^2 [\tan^2 c + \tan^2 b - 2 \tan b \tan c \cos A] \dots\dots(5)$$
$$DE^2 = OA^2 [\sec^2 c + \sec^2 b - 2 \sec b \sec c \cos a] \dots\dots(6)$$

Berdasarkan kedua persamaan di atas, kita akan mendapatkan rumus paling fundamental dalam trigonometri sferis, yang dikenal sebagai **rumus kosinus**:
"""
st.markdown(materi_bab_1, unsafe_allow_html=True)

# Syarah 1 menggunakan st.expander agar interaktif seperti pop-up
with st.expander("Klik di sini untuk melihat Catatan Penjelas (Syarah Penurunan Rumus Kosinus Fundamental)"):
    st.markdown(r"""
    Dalam teks asli, penulis menyembunyikan proses aljabar dari penyamaan persamaan $DE^2$ menuju hasil akhir. Berikut penjabaran rincinya:
    1. Samakan kedua persamaan $DE^2$: $\sec^2 c + \sec^2 b - 2 \sec b \sec c \cos a = \tan^2 c + \tan^2 b - 2 \tan b \tan c \cos A$
    2. Gunakan identitas Pythagoras $\sec^2 \theta = 1 + \tan^2 \theta$ pada ruas kiri: $(1 + \tan^2 c) + (1 + \tan^2 b) - 2 \sec b \sec c \cos a = \tan^2 c + \tan^2 b - 2 \tan b \tan c \cos A$
    3. Coret nilai $\tan^2 c$ dan $\tan^2 b$ di kedua ruas, lalu bagi dengan 2: $1 - \sec b \sec c \cos a = - \tan b \tan c \cos A$
    4. Ubah ke bentuk dasar Sinus dan Kosinus: $1 - \left(\frac{\cos a}{\cos b \cos c}\right) = - \left(\frac{\sin b \sin c \cos A}{\cos b \cos c}\right)$
    5. Kalikan seluruh ruas dengan $(\cos b \cos c)$ untuk menghilangkan penyebut, lalu pindah ruaskan sehingga menghasilkan $\cos a = \cos b \cos c + \sin b \sin c \cos A$ (Terbukti).
    """)

materi_bab_1_lanjut_1 = r"""
$$\cos a = \cos b \cos c + \sin b \sin c \cos A \dots\dots(A)$$

Terdapat dua rumus pendampingnya untuk sisi yang lain:
$$\cos b = \cos c \cos a + \sin c \sin a \cos B \dots\dots(7)$$
$$\cos c = \cos a \cos b + \sin a \sin b \cos C \dots\dots(8)$$

Untuk keperluan perhitungan logaritmik guna mencari sudut A, rumus kosinus dapat diubah bentuknya. Melalui pemanfaatan identitas setengah sudut, kita akan mendapati persamaan:
"""
st.markdown(materi_bab_1_lanjut_1, unsafe_allow_html=True)

# Syarah 2
with st.expander("Klik di sini untuk melihat Catatan Penjelas (Syarah Perubahan Bentuk ke Perkalian Sinus)"):
    st.markdown(r"""
    Perubahan bentuk ekspresi $\cos(b-c) - \cos a$ menjadi bentuk perkalian sinus didapatkan menggunakan **Rumus Selisih Kosinus**:
    $\cos P - \cos Q = -2 \sin \left(\frac{P+Q}{2}\right) \sin \left(\frac{P-Q}{2}\right)$
    
    Dengan memisalkan $P = (b-c)$ dan $Q = a$, diperoleh bentuk $-2 \sin \left(\frac{b-c+a}{2}\right) \sin \left(\frac{b-c-a}{2}\right)$. Mengingat sifat fungsi sinus ganjil $\sin(-x) = -\sin(x)$, tanda minus di luar dapat dimasukkan ke fungsi sinus belakang untuk membalik urutan pembilangnya menjadi $a - (b - c)$.
    """)

materi_bab_1_lanjut_2 = r"""
$$2 \sin \frac{a + (b - c)}{2} \sin \frac{a - (b - c)}{2} = 2 \sin b \sin c \sin^2 \frac{A}{2}$$

Misalkan setengah keliling s didefinisikan dengan $2s = a + b + c \dots\dots(10)$. Maka kita memperoleh rumusan **Sinus Setengah Sudut**:

$$\sin \frac{A}{2} = \sqrt{\frac{\sin (s - b) \sin (s - c)}{\sin b \sin c}} \dots\dots(11)$$

Jika kita menggunakan pendekatan yang sama dan mensubstitusikan identitas $\cos A = 2 \cos^2 \frac{A}{2} - 1$ ke dalam rumus kosinus, kita akan mendapatkan persamaan untuk **Kosinus Setengah Sudut**:
"""
st.markdown(materi_bab_1_lanjut_2, unsafe_allow_html=True)

# Syarah 3
with st.expander("Klik di sini untuk melihat Catatan Penjelas (Syarah Penurunan Rumus Kosinus Setengah Sudut)"):
    st.markdown(r"""
    Buku teks melompati turunan aljabar rumus (12). Berikut uraian lengkapnya:
    1. Mulai dari Rumus Kosinus (A): $\cos a = \cos b \cos c + \sin b \sin c \cos A$
    2. Substitusikan identitas $\cos A = 2 \cos^2 \left(\frac{A}{2}\right) - 1$, lalu kalikan masuk: $\cos a = (\cos b \cos c - \sin b \sin c) + 2 \sin b \sin c \cos^2 \frac{A}{2}$
    3. Gunakan identitas penjumlahan sudut $\cos(b+c) = \cos b \cos c - \sin b \sin c$, lalu pindah ruaskan: $2 \sin b \sin c \cos^2 \frac{A}{2} = \cos a - \cos(b+c)$
    4. Gunakan Rumus Selisih Kosinus: $= 2 \sin \left(\frac{a+b+c}{2}\right) \sin \left(\frac{b+c-a}{2}\right)$
    5. Substitusikan definisi setengah keliling $s = \frac{a+b+c}{2}$ (di mana $\frac{b+c-a}{2} = s - a$), sehingga: $2 \sin b \sin c \cos^2 \frac{A}{2} = 2 \sin s \sin(s-a)$
    6. Bagi kedua ruas dengan $(\sin b \sin c)$ lalu akar-kuadratkan untuk memperoleh $\cos \frac{A}{2} = \sqrt{\frac{\sin s \sin(s-a)}{\sin b \sin c}}$ (Terbukti).
    """)

materi_bab_1_akhir = r"""
$$\cos \frac{A}{2} = \sqrt{\frac{\sin s \sin (s - a)}{\sin b \sin c}} \dots\dots(12)$$

Melalui pembagian persamaan (11) dan (12), kita peroleh rumus **Tangen Setengah Sudut**:

$$\tan \frac{A}{2} = \sqrt{\frac{\sin (s - b) \sin (s - c)}{\sin s \sin (s - a)}} \dots\dots(13)$$

### 6. Rumus sinus (The sine-formula)
Kita sekarang akan menurunkan pembuktian atas rumus sinus. Bertolak dari rumus kosinus sisi a, kita pindah ruaskan sehingga $\sin b \sin c \cos A = \cos a - \cos b \cos c$. Dengan mengkuadratkan kedua ruas, kita memperoleh:

$$\sin^2 b \sin^2 c \cos^2 A = \cos^2 a - 2 \cos a \cos b \cos c + \cos^2 b \cos^2 c$$
"""
st.markdown(materi_bab_1_akhir, unsafe_allow_html=True)
