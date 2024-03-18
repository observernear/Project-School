from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget

from client.client import *

from options.font import *
from options.color import *


class support_Win(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Initializes the user interface of the support window.
        """
        self.setObjectName("SUPPORT")
        self.setFixedSize(240, 365)
        self.setStyleSheet(default_background_color)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # Label
        self.label = QtWidgets.QLabel(self)
        self.label.setFont(font_big)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label.setStyleSheet(invizibility_background_color)
        self.verticalLayout_3.addWidget(self.label)

        # Email Text Label and Line Edit
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.email_text_label = QtWidgets.QLabel(self)
        self.email_text_label.setFont(font_label)
        self.email_text_label.setObjectName("email_text_label")
        self.email_text_label.setStyleSheet(invizibility_background_color)
        self.verticalLayout.addWidget(self.email_text_label)
        self.line_email = QtWidgets.QLineEdit(self)
        self.line_email.setStyleSheet(plaintext_color + border_radius)
        self.line_email.setObjectName("line_email")
        self.verticalLayout.addWidget(self.line_email)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        # Appeal Text Label and Plain Text Edit
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.appeal_text_label = QtWidgets.QLabel(self)
        self.appeal_text_label.setFont(font_label)
        self.appeal_text_label.setObjectName("appeal_text_label")
        self.appeal_text_label.setStyleSheet(invizibility_background_color)
        self.verticalLayout_2.addWidget(self.appeal_text_label)
        self.text_request = QtWidgets.QPlainTextEdit(self)
        self.text_request.setStyleSheet(plaintext_color + border_radius)
        self.text_request.setObjectName("text_request")
        self.verticalLayout_2.addWidget(self.text_request)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        # Exit and Send Buttons
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exit_btn = QtWidgets.QPushButton(self)
        self.exit_btn.setFont(font_btn)
        self.exit_btn.setStyleSheet(plaintext_color)
        self.exit_btn.setObjectName("cancel_btn")
        self.horizontalLayout.addWidget(self.exit_btn)
        self.send_btn = QtWidgets.QPushButton(self)
        self.send_btn.setFont(font_btn)
        self.send_btn.setStyleSheet(plaintext_color)
        self.send_btn.setObjectName("send_btn")
        self.horizontalLayout.addWidget(self.send_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)

        # Connect button signals to slots
        self.send_btn.clicked.connect(self.send_message)
        self.exit_btn.clicked.connect(self.shut_down)

        # Set text and translations
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def shut_down(self):
        """
        Shuts down the support window.
        """
        self.close()

    def send_message(self):
        """
        Sends a support message.
        """
        # Get the email from the input field
        email = self.line_email.text()

        # Check if the email is valid
        if '@' in email:
            try:
                # Get the message text from the input field and encode it to UTF-8
                text = self.text_request.toPlainText().encode('utf-8')
                email = email.encode('utf-8')

                # Send the support request to the server
                request_server(email, text)

                # Clear the email input field and set the success message
                self.line_email.clear()
                self.text_request.setPlainText("Successfully!")

                # Reset the label styles
                self.email_text_label.setStyleSheet(
                    invizibility_background_color)
                self.appeal_text_label.setStyleSheet(
                    invizibility_background_color)
            except Exception:
                # Handle any exceptions and reset the input fields
                self.line_email.clear()
                self.text_request.clear()

                # Set the error label styles
                self.email_text_label.setStyleSheet(
                    "color: rgb(255, 0, 0);" + invizibility_background_color)
                self.appeal_text_label.setStyleSheet(
                    "color: rgb(255, 0, 0);" + invizibility_background_color)
        else:
            # Reset the input fields and set the error label styles
            self.line_email.clear()
            self.text_request.clear()
            self.appeal_text_label.setStyleSheet(invizibility_background_color)
            self.email_text_label.setStyleSheet(
                "color: rgb(255, 0, 0);" + invizibility_background_color)

    def retranslateUi(self):
        """
        This function is responsible for translating the UI elements.

        It uses the QtCore.QCoreApplication.translate method to retrieve the translated text
        based on the given context and source text.

        It then sets the translated text as the new text for each UI element.
        """
        _translate = QtCore.QCoreApplication.translate

        # Set the window title
        self.setWindowTitle(_translate("SUPPORT", "SUPPORT"))

        # Set the label text
        self.label.setText(_translate("SUPPORT", "SUPPORT"))

        # Set the email text label text
        self.email_text_label.setText(_translate("SUPPORT", "email:"))

        # Set the appeal text label text
        self.appeal_text_label.setText(_translate("SUPPORT", "appeal:"))

        # Set the exit button text
        self.exit_btn.setText(_translate("SUPPORT", "Exit"))

        # Set the send button text
        self.send_btn.setText(_translate("SUPPORT", "Send"))
