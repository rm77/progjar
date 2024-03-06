# LAB PEMROGRAMAN JARINGAN

Dalam MK pemrograman jaringan , disediakan 3 buah mesin dengan URL  sebagai berikut.
mesin-mesin tersebut berupa docker container. tiap-tiap mesin dapat diakses dengan mengakses url melalui web browser

- mesin1 : http://<IPaddress>:60001
- mesin2 : http://<IPaddress>:60002
- mesin3 : http://<IPaddress>:60003

dan 1 mesin lagi berupa linux desktop untuk menjalankan wireshark
- mesin4 : http://<IPaddress>:60004, dengan password "progjar666"


untuk mengakses halaman web jupyter, gunakan password
- pada mesin1 (port 60001), gunakan password "mesin1"
- pada mesin2 (port 60002), gunakan password "mesin2"
- pada mesin3 (port 60003), gunakan password "mesin3"

di lingkungan internal antar mesin (diakses dari dalam jupyter/vnc), terdapat 2 buah interface 
- eth0 (terhubung ke interface luar)
- eth1 (terhubung ke interface antar mesin)

untuk lingkungan internal, masing masing mesin mempunyai IP address sebagai berikut:
- mesin1 : 172.16.16.101
- mesin2 : 172.16.16.102
- mesin3 : 172.16.16.103
- mesin4 : 172.16.16.104


# LANGKAH-LANGKAH

- install docker dan docker-compose
- jalankan docker-compose up -d
- cek dengan perintah : docker-compose ps

```
$ docker-compose ps
     Name                    Command                       State                                                    Ports                                          
-------------------------------------------------------------------------------------------------------------------------------------------------------------------
progjar-mesin-1   /bin/sh /tmp/runme.sh            Up (health: starting)   0.0.0.0:20001->20000/tcp,:::20001->20000/tcp, 0.0.0.0:60001->8888/tcp,:::60001->8888/tcp
progjar-mesin-2   /bin/sh /tmp/runme.sh            Up (health: starting)   0.0.0.0:20002->20000/tcp,:::20002->20000/tcp, 0.0.0.0:60002->8888/tcp,:::60002->8888/tcp
progjar-mesin-3   /bin/sh /tmp/runme.sh            Up (healthy)            0.0.0.0:20003->20000/tcp,:::20003->20000/tcp, 0.0.0.0:60003->8888/tcp,:::60003->8888/tcp
progjar-vnc       sh -C /super/run-entrypoint.sh   Up                      5900/tcp, 0.0.0.0:60004->6666/tcp,:::60004->6666/tcp                                    

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
