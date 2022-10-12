'''
    Rachel N. Biesiedzinski 2022

    In this code, client sends a basic math operation using sockets, and the
    server receives it and then respond with the calculation of that operation.
    This code uses TCP protocol to send packets.

    References: https://docs.python.org/2/library/exceptions.html

    To Run via command prompt:
        python server.py portNumber

    Ex:
        python server.py 50027
'''

# These import the socket module needed for the program.
import socket
import sys

# Creates a socket object called s.
s = socket.socket()

# This gets the local machine name.
host = socket.gethostname()

# Takes from the command line, the desired port number.
port = int(sys.argv[1])

# Binds to the port.
s.bind((host, port))

# This will wait for the client connection to be made.
s.listen(5)

print("Server is up and running")

# This will continuosly run until the user exits (exits with
# q/Q/quit/Quit/quit()).
while True:

    # This establishes the connection with the client.
    c, addr = s.accept()
    print('Got connection from', addr)

    while True:
        try:
            #
            equation=c.recv(1024).decode()
                if equation == "Q" or equation == "q" or equation == "Quit" or equation == "quit" or equation == "quit()":
                    c.send("Quit".encode())
                    break

                else:
                    print("You gave me the equation:", equation)
                    result = eval(equation)
                    c.send(str(result).encode())
                    
          # Error testings.
          except (ZeroDivisionError):
               c.send("ZeroDiv".encode())

          except (ArithmeticError):
               c.send("MathError".encode())

          except (SyntaxError):
               c.send("SyntaxError".encode())

          except (NameError):
               c.send("NameError".encode())

    # Closes the connection with the server.
    c.close()


#     ______
#    /  ___ \
#   |  / ,.\ |O    O
#   | |  \_/ | \__/
#   |__\_____/-(..)
# _/_____________/
