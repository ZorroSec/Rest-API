from flask import Flask, render_template
import requests
from json import loads

app = Flask(__name__)

@app.route('/api/cep/<cep>')
def cep(cep):
    url = requests.get(f'https://viacep.com.br/ws/{cep}/json/')
    url = loads(url.text)
    return url

if __name__ == '__main__':
    app.run(
        debug=True
    )
