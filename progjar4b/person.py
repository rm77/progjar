import shelve
import uuid


class Person:
    def __init__(self):
        self.data = shelve.open('mydata.dat')
    def create_data(self,nama=None,telpon=None):
        if (nama is None):
            return False
        id=str(uuid.uuid4())
        data = dict(id=id,nama=nama,telpon=telpon)
        self.data[id]=data
        return True
    def get_data(self,nama=None):
        for i in self.data.keys():
            try:
                if (self.data[i]['nama'].lower() ==nama.lower()):
                    return self.data[i]
            except:
                return False
    def delete_data(self,id=None):
        if (id is None):
            return False
        del self.data[id]
    def list_data(self):
        k = [self.data[i] for i in self.data.keys()]
        return k

if __name__=='__main__':
    p = Person()
    p.create_data("vanBasten","621234")
    p.create_data("vanPersie","621235")
    p.create_data("vanNistelroy","621236")
    p.create_data("vanDerVaart","621237")
    print(p.list_data())
    print(p.get_data('vanbasten'))
