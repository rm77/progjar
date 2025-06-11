import logging
import json
import shlex
#from logic import PlayerServerInterface
from logic_v2 import PlayerServerInterface

class PlayerServerProtocol:
    def __init__(self):
        self.file = PlayerServerInterface()

    def proses_string(self,string_datamasuk=''):
        logging.warning(f"string diproses: {string_datamasuk}")
        c = shlex.split(string_datamasuk.lower())
        try:
            c_request = c[0].strip()
            logging.warning(f"memproses request: {c_request}")
            params = [x for x in c[1:]]
            cl = getattr(self.file,c_request)(params)
            return json.dumps(cl)
        except Exception:
            return json.dumps(dict(status='ERROR',data='request tidak dikenali'))


if __name__=='__main__':
    #contoh pemakaian
    fp = PlayerServerProtocol()
    print(fp.proses_string("set_location 1 100 200"))
    print(fp.proses_string("get_location 1"))
    print(fp.proses_string("get_all_players 0"))