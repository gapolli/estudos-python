import requests

req = requests.get("http://api.open-notify.org/astros.json")
dados = req.json()
print("People in Space right now: " + str(dados['number']))
n = 1
for name in dados['people']:
    print("People " + str(n) + ": " + name['name'])
    n += 1
