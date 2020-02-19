from flask import Flask,render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

users = {}

@socketio.on('message')
def handleMessage(msg):
	send(msg, broadcast=True)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connectMSG')
def handle_my_custom_event(json):
    send(json['data'], broadcast=True)

if __name__ == '__main__':
	socketio.run(app)