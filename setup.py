from flask import Flask, request
from db import *

app = Flask(__name__)

token = 'tok.qwerty123-456'


@app.route('/token/', methods=['POST'])
def send_token():
    json_string = request.json
    if validate_token(json_string['id'][:-2]):
        # create_db()
        pg_db_connect('insert', json_string['id'][-1:], json_string['id'])
        return json_string
    else:
        print('SMTH WRNG')


@app.route('/token/', methods=['GET'])
def get_token():
    json_string = request.json
    if validate_token(json_string['id'][:-2]):
        pg_db_connect('check', json_string['id'][-1:])
        print(pg_db_connect('check', json_string['id'][-1:]))
        return json_string
    else:
        print('SMTH WRNG')


def validate_token(json_token):
    if json_token == token:
        return True
    else:
        return False


if __name__ == '__main__':
    app.run()
