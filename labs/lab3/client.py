import sys
import zmq
import threading
import time
from multiprocessing import Process

# ZeroMQ Context
context = zmq.Context()

# TODO: change this to PUB pattern.
# Define the socket using the "Context"
sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5678")

sub = context.socket(zmq.SUB)
sub.connect("tcp://127.0.0.1:5680")
sub.setsockopt_string(zmq.SUBSCRIBE, '')


# Send a "message" using the socket
name = " ".join(sys.argv[1:])
sock.send_string(name + '-1')
name = sock.recv()
name = name.decode()
print("User[{}] Connected to the chat server.".format(name))



def SendMessage():
    global sock
    while True:
        message = input("[{}] >".format(name))
        sock.send_string(name + "-" + message)
        junk = sock.recv()

def getText():
    while True:    
        data = sub.recv()
        data = data.decode()
        title, message = data.split('-')
        if (title != name):
            print("[{}]: {}".format(title,message))


threading.Thread(target=getText).start()
threading.Thread(target=SendMessage).start()