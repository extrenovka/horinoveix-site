from flask import Flask, render_template, jsonify, request, session
import datetime
import json
import random
import string

app = Flask(__name__)
app.secret_key = 'horinovex_secret_key_2024'

# Ваши услуги
services = [
    {
        'name': '🛡️ Защита в интернете (Деф)',
        'price': '$5 НАВСЕГДА',
        'description': 'Полная анонимность, защита от слежки, VPN + Proxy',
        'icon': '🛡️'
    },
    {
        'name': '🔍 Поиск информации (OSINT)',
        'price': '$5',
        'description': 'Найду любую информацию о человеке/компании',
        'icon': '🔍'
    },
    {
        'name': '📁 Архив данных',
        'price': '$10',
        'description': 'Доступ к закрытым архивам и базам',
        'icon': '📁'
    }
]

# Каналы (вы заполняете сами)
channels = [
    {
        'name': '📢 HORINOVEX NEWS',
        'link': 'https://t.me/your_channel_1',
        'description': 'Главные новости и обновления',
        'icon': '📡'
    },
    {
        'name': '💬 Чат horinovex',
        'link': 'https://t.me/your_chat',
        'description': 'Общение с единомышленниками',
        'icon': '💭'
    },
    {
        'name': '📦 Архив horinovex',
        'link': 'https://t.me/your_archive',
        'description': 'Базы, сливы, инструменты',
        'icon': '📦'
    }
]

# Сообщения чата
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
    # Храним только последние 50 сообщений
    if len(chat_messages) > 50:
        chat_messages.pop(0)
    return jsonify(message)

@app.route('/api/chat/messages')
def get_messages():
    return jsonify(chat_messages[-20:])  # Последние 20 сообщений

@app.route('/api/track', methods=['POST'])
def track():
    return jsonify({'status': 'ok'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)