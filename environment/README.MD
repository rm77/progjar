# LAB PEMROGRAMAN JARINGAN

Dalam MK pemrograman jaringan , disediakan 3 buah mesin dengan URL  sebagai berikut.
mesin-mesin tersebut berupa docker container. tiap-tiap mesin dapat diakses dengan mengakses url melalui web browser
mesin tersebut berupa, jupyter-lab yang didalamnya terdapat utility wireshark

#### PERHATIAN
```
konfigurasi mesin-mesin dalam lab pemrograman jaringan ini dibuat dan telah dicoba dengan baik menggunakan sistem operasi linux
untuk sistem operasi yang lain seperti MACOS bisa jadi tidak berfungsi, untuk memastikan, gunakan WSL (windows subsystem for linux) atau install Virtual Machine dengan HyperV atau virtualbox
(dikarenakan masalah ketidakpastian lisensi, Virtualbox telah diblok dan tidak bisa didownload dalam jaringan ITS, gunakan jaringan internet diluar kampus untuk mendownload Virtualbox)
```

untuk mengakses mesin dengan web based jupyter lab

- mesin1 : http://[IPaddress]:60001
- mesin2 : http://[IPaddress]:60002
- mesin3 : http://[IPaddress]:60003

sedangkan untuk mengakses wireshark

- mesin1 : http://[IPaddress]:50001
- mesin2 : http://[IPaddress]:50002
- mesin3 : http://[IPaddress]:50003


untuk mengakses halaman web jupyter ataupun wireshark (dengan vnc) , gunakan password
- pada mesin1, gunakan password "mesin1"
- pada mesin2, gunakan password "mesin2"
- pada mesin3, gunakan password "mesin3"


untuk lingkungan internal, masing masing mesin mempunyai IP address sebagai berikut:
- mesin1 : 172.16.16.101
- mesin2 : 172.16.16.102
- mesin3 : 172.16.16.103
- mesin4 : 172.16.16.104


masing-masing mesin mempunyai 2 interface yaitu
- eth0 -> menghubungkan dengan dunia luar
- eth1 -> mennghubungkan antar mesin (isolated)

# LANGKAH-LANGKAH

- install docker dan docker-compose
- jalankan docker-compose up -d
- cek dengan perintah : docker-compose ps

```
$ docker-compose ps
     Name                Command             State                                               Ports                                         
-----------------------------------------------------------------------------------------------------------------------------------------------
progjar-mesin-1   /bin/sh /tmp/runme.sh   Up (healthy)   0.0.0.0:50001->6666/tcp,:::50001->6666/tcp, 0.0.0.0:60001->8888/tcp,:::60001->8888/tcp
progjar-mesin-2   /bin/sh /tmp/runme.sh   Up (healthy)   0.0.0.0:50002->6666/tcp,:::50002->6666/tcp, 0.0.0.0:60002->8888/tcp,:::60002->8888/tcp
progjar-mesin-3   /bin/sh /tmp/runme.sh   Up (healthy)   0.0.0.0:50003->6666/tcp,:::50003->6666/tcp, 0.0.0.0:60003->8888/tcp,:::60003->8888/tcp

```

Download/clone materi untuk pemrograman jaringan di https://github.com/rm77/progjar dengan cara
- akses ke salah satu mesin
- buka terminal (di bagian launcher)
- akseslah layar terminal, ketiklah command berikut ini

```
cd work
git clone  https://github.com/rm77/progjar
```  

akan menghasilkan direktori "progjar".
untuk menjalankan gunakan command 

```
python3 <namaprogram.py>
```
