import csv
from dataclasses import dataclass


@dataclass
class Person:
    no_ktp: str
    nama: str
    tgl_lahir: str
    tmp_lahir: str


orang1 = dict(Person(no_ktp='4567', nama='joao felix', tgl_lahir='24/03/2000', tmp_lahir='Mojokerto'))
#orang2 = Person(no_ktp='8910', nama='marcos lorente', tgl_lahir='24/03/2001', tmp_lahir='Situbondo')

fields = ['no_ktp','nama','tgl_lahir','tmp_lahir']

f = open('person1.csv','w')
writer = csv.DictWriter(f,fields)
writer.writeheader()
writer.writerow(dict(orang1))

