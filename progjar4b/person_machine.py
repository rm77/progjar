from person import Person
import json
import logging

'''
PROTOCOL FORMAT

string terbagi menjadi 2 bagian, dipisahkan oleh spasi
COMMAND spasi PARAMETER spasi PARAMETER ...

FITUR

- create : untuk membuat record
  request : create
  parameter : nama spasi notelpon
  response : berhasil -> ok
             gagal -> error

- delete : untuk menghapus record
  request: delete
  parameter : id
  response: berhasil -> OK
            gagal -> ERROR

- list : untuk melihat daftar record
  request: list
  parameter: tidak ada
  response: daftar record person yang ada

- get : untuk mencari record berdasar nama
  request: get 
  parameter: nama yang dicari
  response: record yang dicari dalam bentuk json format

- jika command tidak dikenali akan merespon dengan ERRCMD

'''
p = Person()

class PersonMachine:
    def proses(self,string_to_process):
        s = string_to_process
        cstring = s.split(" ")
        try:
            command = cstring[0].strip()
            if (command=='create'):
                logging.warning("create")
                nama = cstring[1].strip()
                notelpon = cstring[2].strip()
                p.create_data(nama,notelpon)
                return "OK"
            elif (command=='list'):
                logging.warning("list")
                hasil = p.list_data()
                return json.dumps(hasil)
            elif (command=='get'):
                logging.warning("list")
                nama = cstring[1].strip()
                hasil = p.get_data(nama)
                return json.dumps(hasil)
            else:
                return "ERRCMD"
        except:
            return "ERROR"


if __name__=='__main__':
    pm = PersonMachine()
    hasil = pm.proses("list")
    print(hasil)
    hasil = pm.proses("get vanbasten")
    print(hasil)