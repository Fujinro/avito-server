from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Сервер работает!'

@app.route('/avito/callback')
def avito_callback():
    code = request.args.get('code')
    state = request.args.get('state')
    return f'Получен код: {code}, Telegram ID (state): {state}'
