from flask import Flask, render_template
from flask_socketio import SocketIO  
from flask import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'vnkdjnfjknfl1232#'
socketio = SocketIO(app)
messages = []


@app.route('/')
def sessions():
    return render_template('index.html', messages = messages)


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('received my event: ' + str(json))
    socketio.emit('my response', json, callback=messageReceived)
    global messages
    if str(json)[2] == 'u':
    	messages.append(json)
    print(messages)
@app.route('/clear/', methods = ['POST'])
def clean_up():
	print('CALLED HERE')
	global messages
	messages.clear()
	return render_template('index.html', messages = messages)


if __name__ == '__main__':
    socketio.run(app, debug=True)