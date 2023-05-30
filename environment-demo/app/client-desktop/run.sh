SERVER_IP=127.0.0.1
SERVER_PORT=8889
export SERVER_IP SERVER_PORT
virtualenv venv
. ./venv/bin/activate
pip3 install -r requirements.txt
python3 chat-flet.py
deactivate
