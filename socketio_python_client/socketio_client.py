import socketio

sio = socketio.Client()


def send_presentation():
    sio.emit('chat', {'handle': 'Cliente Python',
                      'message': 'Hola gente de Nodejs.'})


@sio.on('connect')
def on_connect():
    print('connected to the server.')
    send_presentation()


@sio.on('chat')
def on_chat(data):
    print('%s: %s' % (data['handle'], data['message']))


@sio.on('disconnect')
def on_disconnect():
    print("I'm disconnected!")


if __name__ == '__main__':
    sio.connect('http://localhost:4000')
