FILE SERVER
TUJUAN: melayani client dalam request file server

ATURAN PROTOKOL:
- client harus mengirimkan request dalam bentuk string
- string harus dalam format
  REQUEST spasi PARAMETER
- PARAMETER dapat berkembang menjadi PARAMETER1 spasi PARAMETER2 dan seterusnya

REQUEST YANG DILAYANI:
- informasi umum:
  * Jika request tidak dikenali akan menghasilkan pesan
    - status: ERROR
    - data: request tidak dikenali
  * Semua result akan diberikan dalam bentuk JSON dan diakhiri
    dengan character ascii code #13#10#13#10 atau "\r\n\r\n"

LIST
* TUJUAN: untuk mendapatkan daftar seluruh file yang dilayani oleh file server
* PARAMETER: tidak ada
* RESULT:
- BERHASIL:
  - status: OK
  - data: list file
- GAGAL:
  - status: ERROR
  - data: pesan kesalahan

GET
* TUJUAN: untuk mendapatkan isi file dengan menyebutkan nama file dalam parameter
* PARAMETER:
  - PARAMETER1 : nama file
* RESULT:
- BERHASIL:
  - status: OK
  - data_namafile : nama file yang diminta
  - data_file : isi file yang diminta (dalam bentuk base64)
- GAGAL:
  - status: ERROR
  - data: pesan kesalahan

