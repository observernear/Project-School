import smtplib
import socket
from email.mime.text import MIMEText
import sqlite3
from datetime import datetime


def create_db():
    """
    Creates a SQLite database and a table to store emails.
    """
    # Connect to the database
    conn = sqlite3.connect("emails.db")

    # Create a cursor object to execute SQL commands
    cur = conn.cursor()

    # Create the 'emails' table if it doesn't exist
    cur.execute(
        """CREATE TABLE IF NOT EXISTS emails 
        (id INTEGER PRIMARY KEY, 
        email STRING, 
        message TEXT, 
        date STRING )"""
    )

    # Commit the changes to the database
    conn.commit()

    # Close the connection
    conn.close()


def add_items_db(email: str, message: str):
    """
    Add items to the database.

    Args:
        email (str): The email address.
        message (str): The message.

    Returns:
        None
    """
    # Create the database
    create_db()

    # Get the current date and time
    date = str(datetime.now())[:-7]

    # Create a tuple with the data
    data_tuple = (email, message, date)

    # Connect to the database
    conn = sqlite3.connect("emails.db")
    cur = conn.cursor()

    # Insert the data into the database
    sqlite_insert = """INSERT INTO emails
                        (email, message, date)
                        VALUES
                        (?, ?, ?);"""
    cur.execute(sqlite_insert, data_tuple)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()


EMAIL_SENDER = "dashaerevanlogican@gmail.com"
EMAIL_RECEIVER = "tanya123456789225@gmail.com"
EMAIL_PASSWORD = "wmjf oejo terx zywe"

TCP_IP = "192.168.31.212"
TCP_PORT = 22222
EMAIL_BUFFER_SIZE = 50
MESSAGE_BUFFER_SIZE = 10000

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Allow reuse of the same address
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind the socket to a specific IP address and port
s.bind((TCP_IP, TCP_PORT))

# Listen for incoming connections with a backlog of 10
s.listen(10)


while True:
    # Accept a connection from a client
    conn, addr = s.accept()
    print("Connection address:", addr)

    # Receive the email subject and message from the client
    subject_data = conn.recv(EMAIL_BUFFER_SIZE)
    message_data = conn.recv(MESSAGE_BUFFER_SIZE)

    # Check if both the subject and message are non-empty
    if subject_data.decode("UTF-8").strip() and message_data.decode("UTF-8").strip():
        # Connect to the SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()

        # Login to the email sender's account
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)

        # Create an email message with the subject and message
        msg = MIMEText(message_data.decode("UTF-8"))
        msg["Subject"] = f"{subject_data.decode('UTF-8')} IP: {addr}"

        # Send the email
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())

    # Add the email and message to the database
    add_items_db(email=subject_data.decode('UTF-8'),
                 message=message_data.decode("UTF-8"))

    # Close the connection
    conn.close()

conn.close
