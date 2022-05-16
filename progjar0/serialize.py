import csv
import json
import shelve
import yaml
import dicttoxml
import xmltodict

from dataclasses import dataclass, asdict


@dataclass
class Person:
    no_ktp: str
    nama: str
    tgl_lahir: str
    tmp_lahir: str

fields = ['no_ktp','nama','tgl_lahir','tmp_lahir']
orang1 = Person(no_ktp='4567', nama='joao felix', tgl_lahir='24/03/2000', tmp_lahir='Mojokerto')


def serialize_to_csv():
    f = open('person1.csv','w')
    writer = csv.DictWriter(f,fields)
    writer.writeheader()
    writer.writerow(asdict(orang1))

def deserialize_from_csv():
    f = open('person1.csv','r')
    reader = csv.DictReader(f,fields)
    for row in reader:
        print(row)

def serialize_to_json():
    f = open('person1.json','w')
    json.dump(asdict(orang1),f,indent=True)

def serialize_from_json():
    f=open('person1.json','r')
    hasil = json.load(f)
    print(hasil)


def serialize_to_shelve():
    p = shelve.open('person1.simpan')
    p['orang1']=asdict(orang1)
    p.close()

def deserialize_from_shelve():
    p = shelve.open('person1.simpan')
    print(p['orang1'])
    p.close()

def serialize_to_xml():
    x = dicttoxml.dicttoxml(asdict(orang1),attr_type=False)
    f = open('orang.xml','wb')
    f.write(x)
    f.close()

def serialize_from_xml():
    f = open('orang.xml','rb')
    x= f.read()
    ##OrderedDict([('root', OrderedDict([('no_ktp', '4567'), ('nama', 'joao felix'), ('tgl_lahir', '24/03/2000'), ('tmp_lahir', 'Mojokerto')]))])
    d = dict(xmltodict.parse(x))['root']
    d = dict(d)
    print(d)
    f.close()

def serialize_to_yaml():
    f = open('orang.yaml','w')
    yaml.dump(asdict(orang1),f,default_flow_style=False)

def serialize_from_yaml():
    f = open('orang.yaml','r')
    hasil = yaml.safe_load(f)
    print(hasil)


if __name__=='__main__':
    serialize_to_csv()
    deserialize_from_csv()

    serialize_to_json()
    serialize_from_json()

    serialize_to_shelve()
    deserialize_from_shelve()

    serialize_to_xml()
    serialize_from_xml()

    serialize_to_yaml()
    serialize_from_yaml()