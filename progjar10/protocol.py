import logging
import json
import shlex
from logic import PlayerServerInterface

class PlayerServerProtocol:
    def __init__(self):
        self.instance = PlayerServerInterface.Instance()

    def proses_string(self,string_datamasuk=''):
        logging.warning(f"string diproses: {string_datamasuk}")
        c = shlex.split(string_datamasuk.lower())
        try:
            c_request = c[0].strip()
            logging.warning(f"memproses request: {c_request}")
            params = [x for x in c[1:]]
            cl = getattr(self.instance,c_request)(params)
            return json.dumps(cl)
        except Exception:
            return json.dumps(dict(status='ERROR',data='request tidak dikenali'))


if __name__=='__main__':
    #contoh pemakaian
    fp = PlayerServerProtocol()
    print(fp.proses_string("player_register 1"))
    print(fp.proses_string("player_register 2"))
    print(fp.proses_string("set_location 1 mousedown 100 200 1 0 0 "))
    print(fp.proses_string("set_location 2 mousedown 10 20 1 1 0 "))
    print(fp.proses_string("set_location 2 mousemove 10 40 1 1 0 "))
    print(fp.proses_string("set_location 1 mousemove 100 300 1 0 0"))
    print(fp.proses_string("set_location 1 mousedown 150 200 1 0 0"))
    print(fp.proses_string("get_location 1"))
    print(fp.proses_string("get_location 1"))
    print(fp.proses_string("get_location 1"))
    print(fp.proses_string("get_location 1"))
    print(fp.proses_string("get_location 2"))
    print(fp.proses_string("get_location 2"))


