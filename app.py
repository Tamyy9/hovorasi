from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Zobrazí stránku s videohovorom
@app.route('/')
def index():
    return render_template('index.html')

# WebSocketové správy pre signaling WebRTC
@socketio.on('signal')
def handle_signal(data):
    emit('signal', data, broadcast=True)

if __name__ == '__main__':
    socketio.run(app)
