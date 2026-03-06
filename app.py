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
        'name': '🛡️ DEF',
        'price': '$5 НАВСЕГДА',
        'description': 'Я лично защищаю вас от сватинга, пробива, доксинга. Хожу за вас в КФ.',
        'icon': '🛡️'
    },
    {
        'name': '🔍 OSINT',
        'price': '$3',
        'description': 'Найду полную информацию о человеке/компании.',
        'icon': '🔍'
    },
    {
        'name': '📘 МАНУАЛЫ',
        'price': '$5',
        'description': 'Скину мануалы по OSINT, сносу и другому.',
        'icon': '📘'
    },
    {
        'name': '📦 PRIVATE',
        'price': '$10',
        'description': 'Приглашу в группу со всеми материалами, обучениями, программами.',
        'icon': '📦'
    }
]

# Каналы
channels = [
    {
        'name': '📢 @horinovpr',
        'link': 'https://t.me/horinovpr',
        'description': 'основной канал'
    },
    {
        'name': '🔄 @portalhor',
        'link': 'https://t.me/portalhor',
        'description': 'адаптер'
    },
    {
        'name': '💬 @cgathorinov',
        'link': 'https://t.me/cgathorinov',
        'description': 'чат'
    }
]

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

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)