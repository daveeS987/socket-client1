import socketio

sio = socketio.Client()


# ------------------- Event Listeners -----------------


@sio.event
def connect():
    print("We're Connected!")


@sio.event
def receive(data):
    print(data)


@sio.event
def connect_error(data):
    print("Connection Failed")
    print("Error Data: ", data)


@sio.event
def disconnect():
    print("We Disconnected!")



# ------------------- Connect to Server -----------------

# Use this to Test Locally
# sio.connect("http://localhost:8000")

# Use this to connect with Remote Server
sio.connect("https://basic-socket-io-server.herokuapp.com/")




# --------------------- Your Code ---------------------


running = True

name = input("Enter Name >> ")
print("Type a message and hit enter")

while running:
    your_answer = input(">> ")
    if your_answer == "q":
        running = False
    sio.emit("message", f"{name}: {your_answer}")

sio.wait()
