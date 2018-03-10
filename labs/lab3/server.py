import zmq
import time

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5678")

pub = context.socket(zmq.PUB)
pub.bind("tcp://127.0.0.1:5680")

# Run a simple "Echo" server
while True:
    data = sock.recv()
    data = data.decode()
    topic, message = data.split('-')
   
    if message == '1':
        sock.send_string(topic)
    else:
        sock.send_string(message)
        pub.send_string("%s-%s" % (topic, message))