import streamlit as st

st.set_page_config(page_title="Modul Matematika Astronomi", page_icon="🔭", layout="wide")

st.title("Modul Matematika Astronomi")
st.subheader("Program Studi Ilmu Falak - FSH UIN Walisongo")
st.markdown("**Disusun oleh:** Mochammad Basthoni")
st.divider()

# BAGIAN 1: Teks sebelum gambar
materi_bab_1_awal = r"""
# BAB I
# TRIGONOMETRI BOLA

### 1. Pendahuluan
Ketika kita memandang bintang-bintang di malam yang cerah, kita mendapatkan kesan yang lazim bahwa mereka semua adalah titik-titik cahaya yang berkilauan, yang seolah-olah terletak di permukaan sebuah bola raksasa di mana masing-masing pengamat menjadi pusatnya. Mata telanjang tentu saja gagal memberikan indikasi apa pun mengenai jarak bintang-bintang tersebut dari kita; namun, hal ini memungkinkan kita untuk membuat perkiraan tentang sudut yang dibentuk di titik pengamat oleh setiap pasang bintang, dan dengan instrumen yang tepat, sudut-sudut ini dapat diukur dengan presisi yang sangat tinggi. Astronomi Bola pada dasarnya berkaitan dengan **arah** di mana bintang-bintang tersebut dilihat, dan sangatlah mudah untuk mendefinisikan arah-arah ini dalam bentuk posisi di permukaan sebuah bola—yakni **bola langit** (*celestial sphere*)—di mana garis lurus yang menghubungkan pengamat ke bintang-bintang berpotongan dengan permukaan ini. Dalam pengertian inilah ungkapan umum "posisi sebuah bintang di bola langit" harus ditafsirkan. Jari-jari bola langit ini sepenuhnya bersifat sembarang. Fondasi dari Astronomi Bola adalah geometri bola.

### 2. Segitiga bola
Setiap bidang yang melewati pusat sebuah bola akan memotong permukaan bola tersebut membentuk sebuah lingkaran yang disebut sebagai **lingkaran besar** (*great circle*). Bidang lain mana pun yang memotong bola tetapi tidak melewati titik pusat juga akan memotong permukaan membentuk sebuah lingkaran, yang dalam hal ini disebut sebagai **lingkaran kecil** (*small circle*). 

Pada Gambar 1, EAB adalah sebuah lingkaran besar, karena bidangnya melewati O, yaitu pusat bola. Misalkan QOP adalah diameter bola yang tegak lurus terhadap bidang lingkaran besar EAB. Misalkan R adalah titik mana pun pada OP dan asumsikan sebuah bidang ditarik melalui R sejajar dengan bidang EAB; permukaan bola tersebut kemudian dipotong membentuk lingkaran kecil FCD. Berdasarkan konstruksinya, OP juga tegak lurus terhadap bidang FCD. Titik-titik ujung P dan Q dari diameter tegak lurus QOP ini disebut sebagai **kutub** (*poles*) dari lingkaran besar dan dari lingkaran kecil yang sejajar tersebut. 
"""
st.markdown(materi_bab_1_awal, unsafe_allow_html=True)

# BAGIAN GAMBAR: Dimasukkan sebagai perintah Python
st.image("Gambar_1.png", caption="Gambar 1 - Segitiga Bola", use_container_width=True)

# BAGIAN 2: Teks setelah gambar
materi_bab_1_lanjut = r"""
Ketika dua lingkaran besar berpotongan di satu titik, mereka dikatakan membentuk sebuah **sudut bola** (*spherical angle*). Perhatikan dua lingkaran besar PA dan PB yang berpotongan di P. Tarik garis PS dan PT, yang merupakan garis singgung terhadap keliling PA dan PB. PT tegak lurus terhadap jari-jari OP dan sejajar dengan jari-jari OB. Demikian pula PS sejajar dengan OA. Sudut SPT mendefinisikan sudut bola di P, dan nilainya sama dengan sudut AOB, di mana AB adalah busur yang terpotong pada lingkaran besar di antara dua lingkaran besar PA dan PB.

Jika tiga titik pada permukaan sferis dihubungkan oleh busur-busur lingkaran besar, bangun yang diperoleh disebut **segitiga bola** (*spherical triangle*). Pada Gambar 1, titik A, X, dan Y membentuk segitiga bola AXY. AX, AY, dan XY adalah **sisi-sisi**, sedangkan sudut di A, X, dan Y adalah sudut-sudutnya. Jika R adalah jari-jari bola, panjang busur lingkaran besar AY dirumuskan dengan:

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
"""
st.markdown(materi_bab_1_lanjut, unsafe_allow_html=True)

# LANJUTAN MATERI...
materi_bab_1_akhir = r"""
### 5. Rumus kosinus (The cosine-formula)
Misalkan ABC adalah sebuah segitiga bola (Gambar 3). Nyatakan sisi-sisinya BC, CA, AB masing-masing sebagai a, b, c.

Dari analisis geometri bidang singgung pada segitiga DAE dan DOE di bawah bola, kita peroleh persamaan:

$$DE^2 = OA^2 [\tan^2 c + \tan^2 b - 2 \tan b \tan c \cos A] \dots\dots(5)$$
$$DE^2 = OA^2 [\sec^2 c + \sec^2 b - 2 \sec b \sec c \cos a] \dots\dots(6)$$

Berdasarkan kedua persamaan di atas, kita akan mendapatkan rumus paling fundamental dalam trigonometri bola, yang dikenal sebagai **rumus kosinus**:
"""
st.markdown(materi_bab_1_akhir, unsafe_allow_html=True)

with st.expander("Catatan Penjelas: Syarah Penurunan Rumus Kosinus Fundamental"):
    st.markdown(r"""
    1. Samakan kedua persamaan $DE^2$: $\sec^2 c + \sec^2 b - 2 \sec b \sec c \cos a = \tan^2 c + \tan^2 b - 2 \tan b \tan c \cos A$
    2. Gunakan identitas Pythagoras $\sec^2 \theta = 1 + \tan^2 \theta$ pada ruas kiri: $(1 + \tan^2 c) + (1 + \tan^2 b) - 2 \sec b \sec c \cos a = \tan^2 c + \tan^2 b - 2 \tan b \tan c \cos A$
    3. Coret nilai $\tan^2 c$ dan $\tan^2 b$ di kedua ruas, lalu bagi dengan 2: $1 - \sec b \sec c \cos a = - \tan b \tan c \cos A$
    4. Ubah ke bentuk dasar Sinus dan Kosinus: $1 - \left(\frac{\cos a}{\cos b \cos c}\right) = - \left(\frac{\sin b \sin c \cos A}{\cos b \cos c}\right)$
    5. Kalikan seluruh ruas dengan $(\cos b \cos c)$ untuk menghilangkan penyebut, lalu pindah ruaskan sehingga menghasilkan $\cos a = \cos b \cos c + \sin b \sin c \cos A$ (Terbukti).
    """)

# Penutup
materi_penutup = r"""
$$\cos a = \cos b \cos c + \sin b \sin c \cos A \dots\dots(A)$$
"""
st.markdown(materi_penutup, unsafe_allow_html=True)
