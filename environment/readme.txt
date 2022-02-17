#LAB PEMROGRAMAN JARINGAN

Dalam MK pemrograman jaringan , disediakan 4 buah mesin dengan IP address sebagai berikut.
mesin-mesin tersebut berupa docker container. tiap-tiap mesin dapat diakses dengan mengakses url melalui web browser

- mesin1 : 172.16.16.101 http://172.16.16.101:8888
- mesin2 : 172.16.16.102 http://172.16.16.102:8888
- mesin3 : 172.16.16.103 http://172.16.16.103:8888
- mesin4 : 172.16.16.104 http://172.16.16.104:8888

#LANGKAH-LANGKAH

** untuk windows, gunakan wsl2

- install docker dan docker-compose
- jalankan docker-compose up -d
- cek dengan perintah : docker-compose ps

     Name                   Command              State    Ports  
-----------------------------------------------------------------
progjar-mesin-1   tini -g -- sh /script/run.sh   Up      8888/tcp
progjar-mesin-2   tini -g -- sh /script/run.sh   Up      8888/tcp
progjar-mesin-3   tini -g -- sh /script/run.sh   Up      8888/tcp
progjar-mesin-4   tini -g -- sh /script/run.sh   Up      8888/tcp


Download/clone materi untuk pemrograman jaringan di https://github.com/rm77/progjar dengan cara
- akses ke salah satu mesin
- buka terminal (di bagian launcher)
- akseslah layar terminal, ketiklah command berikut ini
  * cd work
  * git clone  https://github.com/rm77/progjar
  * akan menghasilkan direktori "progjar", untuk menjalankan gunakan command python3 <namaprogram.py>
  






