#!/usr/bin/env python
# server.py

import socket
import select
from random import randint
import sys

def main():
    s = socket.socket()         # Create a socket object
    host = socket.gethostname() # Get local machine name
    port = 5000                 # Reserve a port for your service.
    s.bind((host, port))        # Bind to the port
    print "Listening on  %s port %s..." % (host, port)

    s.listen(5)                 # Now wait for client connection.
    while True:
        try:
            client, addr = s.accept()
            ready = select.select([client,],[], [],2)
            if ready[0]:
                data = client.recv(1)
                client.send(str(randint(1,9)))
        except KeyboardInterrupt:
            print
            print "Stop."
            break
        except socket.error, msg:
            print "Socket error! %s" % msg
            break

if __name__ == "__main__":
    main()
