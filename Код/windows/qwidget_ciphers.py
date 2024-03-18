from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget

from operations.ciphers import xor_cipher, caesar_cipher, atbash_cipher

from options.font import *
from options.color import *


class cipher_Win(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Initialize the user interface.
        """
        self.setObjectName("Ciphers")
        self.setFixedSize(600, 400)
        self.setStyleSheet(default_background_color)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # Set language combo box
        self.set_language = QtWidgets.QComboBox(self)
        self.set_language.setObjectName("set_language")
        self.set_language.setStyleSheet(white_black_color)
        self.set_language.addItem("")
        self.set_language.addItem("")
        self.set_language.addItem("")
        self.set_language.setFont(font_label)
        self.verticalLayout_4.addWidget(self.set_language)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # Input text label
        self.input_text_label = QtWidgets.QLabel(self)
        self.input_text_label.setObjectName("input_text_label")
        self.input_text_label.setFont(font_label)
        self.input_text_label.setStyleSheet(invizibility_background_color)
        self.verticalLayout.addWidget(self.input_text_label)

        # Plain text input field
        self.plainText_input = QtWidgets.QPlainTextEdit(self)
        self.plainText_input.setObjectName("plainText_input")
        self.plainText_input.setStyleSheet(plaintext_color + border_radius)
        self.verticalLayout.addWidget(self.plainText_input)

        # Key text label
        self.key_text_label = QtWidgets.QLabel(self)
        self.key_text_label.setObjectName("key_text_label")
        self.key_text_label.setFont(font_label)
        self.key_text_label.setStyleSheet(invizibility_background_color)
        self.verticalLayout.addWidget(self.key_text_label)

        # Key line edit field
        self.key_line = QtWidgets.QLineEdit(self)
        self.key_line.setObjectName("key_line")
        self.key_line.setStyleSheet(plaintext_color + border_radius)
        self.verticalLayout.addWidget(self.key_line)

        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout)

        # Arrow text label
        self.arrow_text_label = QtWidgets.QLabel(self)
        self.arrow_text_label.setObjectName("arrow_text_label")
        self.arrow_text_label.setFont(font_label)
        self.arrow_text_label.setStyleSheet(invizibility_background_color)
        self.horizontalLayout.addWidget(self.arrow_text_label)

        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Output text label
        self.output_text_label = QtWidgets.QLabel(self)
        self.output_text_label.setObjectName("output_text_label")
        self.output_text_label.setFont(font_label)
        self.output_text_label.setStyleSheet(invizibility_background_color)
        self.verticalLayout_2.addWidget(self.output_text_label)

        # Plain text output field
        self.plainText_output = QtWidgets.QPlainTextEdit(self)
        self.plainText_output.setObjectName("plainText_output")
        self.verticalLayout_2.addWidget(self.plainText_output)
        self.plainText_output.setStyleSheet(plaintext_color + border_radius)
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)

        # Add spacer item for vertical layout

        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # Create vertical layout

        self.encrypt_rad = QtWidgets.QRadioButton(self)
        self.encrypt_rad.setObjectName("encrypt_rad")
        self.encrypt_rad.setFont(font_label)
        self.encrypt_rad.setStyleSheet(invizibility_background_color)
        self.group_rad = QtWidgets.QButtonGroup(self)
        self.group_rad.setObjectName("group_rad")
        self.group_rad.addButton(self.encrypt_rad)
        self.verticalLayout_3.addWidget(self.encrypt_rad)

        # Create encrypt radio button and add it to the vertical layout

        self.decrypt_rad = QtWidgets.QRadioButton(self)
        self.decrypt_rad.setObjectName("decrypt_rad")
        self.decrypt_rad.setFont(font_label)
        self.decrypt_rad.setStyleSheet(invizibility_background_color)
        self.group_rad.addButton(self.decrypt_rad)
        self.verticalLayout_3.addWidget(self.decrypt_rad)

        # Create decrypt radio button and add it to the vertical layout

        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)

        # Add spacer item for horizontal layout

        self.save_btn = QtWidgets.QPushButton(self)
        self.save_btn.setObjectName("save_btn")
        self.save_btn.setStyleSheet(plaintext_color)
        self.save_btn.setFont(font_btn)
        self.horizontalLayout_2.addWidget(self.save_btn)

        # Create save button and add it to the horizontal layout

        self.answer_btn = QtWidgets.QPushButton(self)
        self.answer_btn.setObjectName("answer_btn")
        self.answer_btn.setStyleSheet(plaintext_color)
        self.answer_btn.setFont(font_btn)
        self.horizontalLayout_2.addWidget(self.answer_btn)

        # Create answer button and add it to the horizontal layout

        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.encrypt_rad.click()

        # Set the encrypt radio button as the default selected option

        self.set_language.activated.connect(self.clear_key_line)

        # Connect the activated signal of set_language to the clear_key_line method

        self.save_btn.clicked.connect(self.save_in_file)

        # Connect the clicked signal of save_btn to the save_in_file method

        self.answer_btn.clicked.connect(self.calculate)

        # Connect the clicked signal of answer_btn to the calculate method

        self.group_rad.buttonClicked.connect(self.set_btn_answer_text)

        # Connect the buttonClicked signal of group_rad to the set_btn_answer_text method

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def clear_key_line(self):
        """
        Clears the key line based on the selected language.
        If the language is 'Atbash', sets the key line text to 'None' and disables it.
        Otherwise, clears the key line and enables it.
        """
        language = self.set_language.currentText()

        if language == 'Atbash':
            # Set the key line text to 'None' and disable it
            self.key_line.setText('None')
            self.key_line.setDisabled(True)
        else:
            # Clear the key line and enable it
            self.key_line.clear()
            self.key_line.setDisabled(False)

    def save_in_file(self):
        """
        Save the contents of the application to a file.
        """
        # Get the filename from the user
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Text files (*.txt)")

        if filename:
            # Open the file for writing
            with open(filename, "w") as f:
                # Write the cipher information to the file
                f.write('Cipher: ' + self.set_language.currentText() +
                        ' ' + self.answer_btn.text() + '\n\n')

                # Write the plain text input to the file
                f.write(self.plainText_input.toPlainText() + '\n')

                # Write a separator to the file
                f.write('---------------------------------------\n')

                # Write the plain text output to the file
                f.write(self.plainText_output.toPlainText() + '\n\n')

                # Write the secret key to the file
                f.write('Secret key: ' + self.key_line.text())

    def set_btn_answer_text(self):
        """
        Sets the text of the answer button based on the selected radio button.
        """
        if self.decrypt_rad.isChecked():
            # If the decrypt radio button is checked, set the answer button text to the decrypt radio button text
            self.answer_btn.setText(self.decrypt_rad.text())
        else:
            # Otherwise, set the answer button text to the encrypt radio button text
            self.answer_btn.setText(self.encrypt_rad.text())

    def calculate(self):
        """
        Performs the encryption or decryption based on the selected cipher type.
        """
        text = self.plainText_input.toPlainText()
        key = self.key_line.text()
        coder_type = self.set_language.currentText()

        if self.encrypt_rad.isChecked():
            # Encryption
            match coder_type:
                case "Caezar":
                    try:
                        answer = caesar_cipher.encrypt_caesar(
                            text=str(text), key=int(key))
                    except ValueError:
                        answer = 'In the "Key" field you need to enter an integer!'
                case 'Xor':
                    try:
                        answer = xor_cipher.encrypt_xor(
                            text=str(text), key=int(key))
                    except ValueError:
                        answer = 'In the "Key" field you need to enter a secret integer!'
                case 'Atbash':
                    answer = atbash_cipher.encrypt_atbash(text=str(text))

        elif self.decrypt_rad.isChecked():
            # Decryption
            match coder_type:
                case "Caezar":
                    try:
                        answer = caesar_cipher.decrypt_caesar(
                            encrypted_text=str(text), key=int(key))
                    except ValueError:
                        answer = 'In the "Key" field you need to enter an integer!'
                case 'Xor':
                    try:
                        answer = xor_cipher.decrypt_xor(
                            encrypted_text=str(text), key=int(key))
                    except ValueError:
                        answer = 'In the "Key" field you need to enter a secret integer!'
                case 'Atbash':
                    answer = atbash_cipher.decrypt_atbash(
                        encrypted_text=str(text))

        self.plainText_output.setPlainText(str(answer))

    def retranslateUi(self):
        """
        This function is responsible for translating the UI elements to the desired language.
        """
        _translate = QtCore.QCoreApplication.translate

        # Set the window title
        self.setWindowTitle(_translate("Ciphers", "Ciphers"))

        # Set the options in the language selection dropdown
        self.set_language.setItemText(0, _translate("Ciphers", "Caezar"))
        self.set_language.setItemText(1, _translate("Ciphers", "Xor"))
        self.set_language.setItemText(2, _translate("Ciphers", "Atbash"))

        # Set labels for input, key, arrow, and output fields
        self.input_text_label.setText(_translate("Ciphers", "Input"))
        self.key_text_label.setText(_translate("Ciphers", "Key:"))
        self.arrow_text_label.setText(_translate("Ciphers", "->"))
        self.output_text_label.setText(_translate("Ciphers", "Output"))

        # Set text for encrypt and decrypt radio buttons, save button, and answer button
        self.encrypt_rad.setText(_translate("Ciphers", "Encrypt"))
        self.decrypt_rad.setText(_translate("Ciphers", "Decrypt"))
        self.save_btn.setText(_translate("Ciphers", "Save in file"))
        self.answer_btn.setText(_translate("Ciphers", "Encrypt"))
