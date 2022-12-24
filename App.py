import logging
from flask import Flask, request, render_template
from flask_socketio import SocketIO
from AI.ChatBot import ChatBot

app = Flask(__name__)
app.config['SECRET_KEY'] = 'top-secret!'
socketio = SocketIO(app, manage_session=False, cors_allowed_origins='*', logger=False)
logging.getLogger('werkzeug').setLevel(logging.ERROR)

clients = {}

@socketio.on('connect')
def addClient():
    print(f"New Client Connect: {request.sid}")
    clientInfo = {}
    clientInfo['socketIO'] = socketio
    clientInfo['room'] = request.sid
    clients[request.sid] = ChatBot(clientInfo)

@socketio.on('message')
def handleMessage(msg):
    print(f"Client {request.sid}: {msg}")
    clients[request.sid].ProcessMessage(msg)

@socketio.on('disconnect')
def handleDisconnect():
    clients.pop(request.sid)

@app.route("/")
def hello():
    message = "Hello, World"
    return message

if __name__ == "__main__":
    print('\n\nAccess http://localhost:5001\n\n', )
    socketio.run(app, port=5001)