'''
    Rachel N. Biesiedzinski 2022

    In this code, client sends a basic math operation using sockets, and the
    server receives it and then respond with the calculation of that operation.
    This code uses TCP protocol to send packets.

    References: https://docs.python.org/2/library/exceptions.html
                http://stackoverflow.com/questions/319279/how-to-validate-ip-address-in-python

    To Run via command prompt:
        python client.py hostname portNumber

    Ex:
        python client.py 10.173.204.63 50027
'''

# These import the socket module needed for the program.
import socket
import sys
import ipaddress

# Creates a socket object called s.
s = socket.socket()

try:
    # Reading IP Address.
    host = str(ipaddress.ip_address(sys.argv[1]))

    # Reading port number.
    port = int(sys.argv[2])

    # Connecting to server.
    s.connect((host, port))

    print("The IP address of the server is:", host)
    print("The port number of the server is:", port)

    while(True):
        # Promts user for an calculation they want made.
        equ=input("Please give me your equation (Ex: 2+2) or Q to quit: ")

        # Sends users input to server to be calculated.
        s.send(equ.encode())

        # Where the client receives the servers response.
        result = s.recv(1024).decode()

        if result == "Quit":
            print("Closing client connection, goodbye")
            break

        # Error test response for dividing by zero.
        elif result == "ZeroDiv":
            print("You can't divide by 0, try again")

        # Error test response for a math error.
        elif result == "MathError":
            print("There is an error with your math, try again")

        # Error test response for Syntax mistakes.
        elif result == "SyntaxError":
            print("There is a syntax error, please try again")

        # Error test response for not entering an equation in.
        elif result == "NameError":
            print("You did not enter an equation, try again")

        # No error, result will be printed.
        else:
            print("The answer is:", result)

    # Close the socket when done
    s.close

# Throws an error for incorect use of command prompt format.
except (IndexError, ValueError):
    print("You did not specify an IP address and port number")


#     ______
#    /  ___ \
#   |  / ,.\ |O    O
#   | |  \_/ | \__/
#   |__\_____/-(..)
# _/_____________/
