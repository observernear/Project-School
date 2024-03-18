import socket
import time


def request_server(subject, message):
    """
    Sends a request to the server with the given subject and message.

    Args:
        subject (str): The subject of the request.
        message (str): The message of the request.
    """

    TCP_IP = "94.228.165.150"
    TCP_PORT = 22222

    # Create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    s.connect((TCP_IP, TCP_PORT))

    # Send the subject
    s.send(subject)
    time.sleep(1)

    # Send the message
    s.send(message)

    # Close the socket
    s.close()
