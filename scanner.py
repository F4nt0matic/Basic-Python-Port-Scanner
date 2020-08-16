#!/bin/python3
# Author: Fant0matic Helped by hmaverickadams


import sys  # allows us to enter command line arguments, among other things
import socket
from datetime import datetime


def new_line():
    print("\n")


# Define our target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # Translate an host name to an IPV4
else:
    print("Invalid amount of args")
    print("Syntax: python3 scanner.py <ip>")
    sys.exit()

# Add a pretty banner
print("-" * 50)
print("Author: Fantomatic")
print("Github: https://github.com/F4nt0matic")
print("-" * 50)
print("Scanning Target: " + target)
print("Time started: " + str(datetime.now()))
print("-" * 50)

try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Its a float
        result = s.connect_ex((target, port))  # returns error indicator

        if result == 0:
            print("Port ~ {} ~ is open".format(port))
            s.close()


except KeyboardInterrupt:
    print("\n Exiting Program by Keyboard Interrupt.")
    sys.exit()

except socket.gaierror:
    print("Hostname could not be resolved.")
    sys.exit()



except socket.error:
    print("Couldn't connect to server.")
    sys.exit()

new_line()
print("-------------Ended checking ports--------------")
