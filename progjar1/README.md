# Tugas 1 Pemrograman Jaringan

Nama : Evelyn Tjitrodjojo

NRP : 05111840000099

Kelas : D

# Pembahasan Jawaban

### No 1 Buatlah fork dari https://github.com/rm77/progjar.git ke repo kalian masing-masing (yang sudah disetorkan ke asisten)

Sudah terbentuk pada github di link ini.

### No 2 Jalankan simulator, gunakan 3 buah node alpine , pastikan 3 buah node alpine tersebut tersambung (cek dengan command ping ip address masing-masing)

Berikut adalah gambar topologi yang digunakan. Setelah pengecekan semua ip address telah tersambung.

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/topologi.PNG)

### No 3 Clone lah repository hasil fork tersebut di masing-masing node tersebut di direktori /home/work (jika belum ada dapat dibuat dulu dengan mkdir -p /home/work)

Berikut setelah diclone.

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/soal3.PNG)

### No 4 Dari direktori progjar1 dari repository tersebut:

#### Jalankan program server.py di alpine-1 dan alpine-2, jalankan program client.py di alpine 3

Setelah clone, akan terdapat file server.py dan client.py. Sebelum dijalankan pada alpine 1 dan alpine 2, ubah terlebih dahulu server address menjadi alamat alpine 1 (pada alpine 1) dan alamat alpine 2 (pada alpine 2). Cek alamat masing-masing dengan ifconfig -a. Berikut penggantiannya.

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/nano%20server%201.PNG)
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/nano%20server%202.PNG)

Kemudian ubah file client.py pada alpine 3, sehingga dapat mengirim pada dua alamat yaitu alpine 1 dan 2 sekaligus. Berikut gambarnya, untuk lebih lengkap dapat dilihat pada file client.

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/nano%20client.PNG)

Jalankan kedua server terlebih dahulu. Seperti ini.

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/server1.PNG)
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/server2.PNG)

Kemudian jalankan client. Hasilnya seperti ini.

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/client.PNG)
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/server1-1.PNG)
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/server2-1.PNG)

#### Modifikasilah program client.py tersebut untuk mengirim string sebesar 2 megabytes

Copy file client.py pada folder lain. Buka file client.py yang sudah dicopy, ubah bagian send data seperti ini. Ubah k=100 menjadi k=2000000 untuk mengirim string sebesar 2 mb. Disini menggunakan k=100 untuk keperluan dokumentasi.

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/tugas1a%20code1.PNG)

Sesudah diubah, jalankan kembali server.py pada kedua alpine (alpine 1 dan alpine 2) tanpa mengubah kode server. Baru jalankan kode client yang sudah dimodifikasi. Hasilnya akan seperti ini.

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/tugas1a-client.PNG)
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/tugas1a-alphine1.PNG)
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/tugas1a-alphine2.PNG)

#### Modifikasilah program client.py tersebut untuk mengirim file gambar, dan menulis respon baliknya ke dalam nama file yang berbeda

Copy file client.py yang belum dimodifikasi pada folder lain. Buka file client, ubah kode yang dapat dilihat pada repo ini. Sebelum dijalankan, download gambar terlebih dahulu. Masukkan pada folder yang sama.

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/sebelum%20tugas%201b.PNG)

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/potongankode1b.PNG)

Kemudian jalankan kembali server pada kedua alpine tanpa mengubah kode server. Jalankan kode client yang telah dimodifikasi. Hasilnya akan seperti ini.

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/running%20ab.PNG)

Pada alpine 1 dan 2, akan seperti ini (karena mengirim file berbentuk binary)

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/1b%20alpine1.PNG)
![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/1b%20alpine2.PNG)

Sesudah itu, cek hasilnya pada folder yang sama dengan folder client. Apabila sudah benar, hasilnya seperti ini.

![alt text](https://github.com/marsellaeve/Pemrograman_Jaringan_D/blob/master/progjar1/screenshot%20progjar1/hasil%201b.PNG)

#### Sekian tugas 1 ini. Terima kasih.
