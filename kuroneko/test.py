from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

num = 0

@socketio.on("connect", namespace="/test")
def connect():
    num += 1
    print("Clinet connected")
    render_template("index.html", num=num)

if __name__ == "__main__":
    main()