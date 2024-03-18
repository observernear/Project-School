from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget, QFileDialog

from operations.qrcodings import qr_code

from options.font import *
from options.color import *


class qrcode_Win(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Initializes the User Interface (UI) for the QR-codes class.
        """
        self.setObjectName("QR-codes")
        self.setFixedSize(600, 400)
        self.setStyleSheet(default_background_color)

        # Create the horizontal layout for the UI
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Create the form layout for the UI
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")

        # Create the vertical layout for the label and input text
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.formLayout.setLayout(
            0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_3)

        # Create the horizontal layout for the input text and create QR button
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Create the vertical layout for the input text label and input text field
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Create the input text label
        self.input_text_label = QtWidgets.QLabel(self)
        self.input_text_label.setObjectName("label_2")
        self.input_text_label.setFont(font_label)
        self.input_text_label.setStyleSheet(invizibility_background_color)
        self.verticalLayout_2.addWidget(self.input_text_label)

        # Create the input text field
        self.textedit_intput = QtWidgets.QTextEdit(self)
        self.textedit_intput.setObjectName("textedit_intput")
        self.textedit_intput.setStyleSheet(plaintext_color + border_radius)
        self.verticalLayout_2.addWidget(self.textedit_intput)

        # Create the create QR button
        self.create_qr_btn = QtWidgets.QPushButton(self)
        self.create_qr_btn.setObjectName("create_qr_btn")
        self.create_qr_btn.setStyleSheet(plaintext_color)
        self.create_qr_btn.setFont(font_btn)
        self.verticalLayout_2.addWidget(self.create_qr_btn)

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        # Create the vertical layout for the output text label and output text field
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # Create the output text label
        self.output_text_label = QtWidgets.QLabel(self)
        self.output_text_label.setObjectName("output_text_label")
        self.output_text_label.setFont(font_label)
        self.output_text_label.setStyleSheet(invizibility_background_color)
        self.verticalLayout.addWidget(self.output_text_label)

        # Create the output text field
        self.textedit_output = QtWidgets.QTextEdit(self)
        self.textedit_output.setObjectName("textedit_output")
        self.textedit_output.setStyleSheet(plaintext_color + border_radius)
        self.verticalLayout.addWidget(self.textedit_output)

        # Create the read QR button
        self.read_qr_btn = QtWidgets.QPushButton(self)
        self.read_qr_btn.setObjectName("read_qr_btn")
        self.read_qr_btn.setStyleSheet(plaintext_color)
        self.read_qr_btn.setFont(font_btn)
        self.verticalLayout.addWidget(self.read_qr_btn)

        self.horizontalLayout.addLayout(self.verticalLayout)
        self.formLayout.setLayout(
            1, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout)

        self.horizontalLayout_2.addLayout(self.formLayout)

        # Connect the read QR button to the qrcode_decrypt method
        self.read_qr_btn.clicked.connect(self.qrcode_decrypt)

        # Connect the create QR button to the qrcode_encrypt method
        self.create_qr_btn.clicked.connect(self.qrcode_encrypt)

        # Call the retranslateUi
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def qrcode_decrypt(self):
        """
        Function to decrypt a QR code image and display the result in a text edit widget.
        """
        options = QFileDialog.Options()
        # Open a file dialog to select a QR code image file
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open QR Code Image", "", "Images (*.png *.jpg *.jpeg *.bmp)", options=options)
        if file_name:
            # Read the QR code from the selected image file
            answer = qr_code.read_qr_code(filename=file_name)
            # Set the decrypted result as the text in the text edit widget
            self.textedit_output.setText(str(answer))

    def qrcode_encrypt(self):
        """
        Encrypts the text and saves it as a QR code image.
        """
        # Prompt the user to select a file to save the QR code image
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Images (*.png *.jpg *.jpeg *.bmp)")

        # Get the text from the input field
        text = self.textedit_intput.toPlainText()

        if filename:
            # Create the QR code image
            answer = qr_code.create_qr_code(text=text)

            if not type(answer) == str:
                # Save the image to the selected file
                answer.save(filename)
            else:
                # Display an error message if the QR code creation fails
                self.textedit_intput.setText(str(answer))

    def retranslateUi(self):
        """
        This function is responsible for retranslating the UI elements.
        """
        _translate = QtCore.QCoreApplication.translate

        # Set the window title
        self.setWindowTitle(_translate("QR-codes", "QR-codes"))

        # Set the input text label
        self.input_text_label.setText(_translate(
            "QR-codes", "input(secret message)"))

        # Set the create QR button text
        self.create_qr_btn.setText(_translate("QR-codes", "Create QR-code"))

        # Set the output text label
        self.output_text_label.setText(_translate(
            "QR-codes", "output(data contained in QR-code)"))

        # Set the read QR button text
        self.read_qr_btn.setText(_translate("QR-codes", "Read QR-code"))
