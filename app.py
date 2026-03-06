from flask import Flask, render_template, jsonify, request
import datetime
import random
import string
import os

app = Flask(__name__)
app.secret_key = 'horinovex_secret_key_2024'

# Услуги
services = [
    {
        'name': '🛡️ DEF (ЗАЩИТА)',
        'price': '$5 НАВСЕГДА',
        'description': 'Я лично защищаю вас. Полная анонимность в сети, анти-доксинг, удаление личных данных.',
        'icon': '🛡️'
    },
    {
        'name': '🔍 OSINT (ПОИСК)',
        'price': '$5',
        'description': 'Полная информация о человеке/компании. Сливы, базы, соцсети, контакты, пробив.',
        'icon': '🔍'
    }
]

# Каналы
channels = [
    {
        'name': '📢 @horinovpr',
        'link': 'https://t.me/horinovpr',
        'description': 'основной канал',
        'icon': '📡'
    }
]

# Сообщения чата (если понадобятся)
chat_messages = []

@app.route('/')
def index():
    return render_template('index.html', 
                         username='horinovex',
                         services=services,
                         channels=channels)

@app.route('/api/chat/send', methods=['POST'])
def send_message():
    data = request.json
    message = {
        'username': 'horinovex',
        'text': data.get('text', ''),
        'time': datetime.datetime.now().strftime('%H:%M'),
        'id': ''.join(random.choices(string.ascii_letters + string.digits, k=8))
    }
    chat_messages.append(message)
    if len(chat_messages) > 50:
        chat_messages.pop(0)
    return jsonify(message)

@app.route('/api/chat/messages')
def get_messages():
    return jsonify(chat_messages[-20:])

@app.route('/api/track', methods=['POST'])
def track():
    return jsonify({'status': 'ok'})

@app.route('/order', methods=['POST'])
def order():
    data = request.json
    # Здесь можно добавить сохранение заказов
    return jsonify({'status': 'order received'})

if __name__ == '__main__':
    # Эта строчка важна для Render!
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)