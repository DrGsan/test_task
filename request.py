import requests

# res = requests.post('http://127.0.0.1:5000/token/', json={"id": "tok.qwerty123-456.A"})
# res = requests.post('http://127.0.0.1:5000/token/', json={"id": "tok.qwerty123-456.B"})
# res = requests.post('http://127.0.0.1:5000/token/', json={"id": "tok.qwerty123-456.C"})


# res = requests.get('http://127.0.0.1:5000/token/', json={"id": "tok.qwerty123-456.A"})
res = requests.get('http://127.0.0.1:5000/token/', json={"id": "tok.qwerty123-456.B"})
# res = requests.get('http://127.0.0.1:5000/token/', json={"id": "tok.qwerty123-456.C"})

if res.ok:
    print(res.json())
