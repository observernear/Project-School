from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QWidget

from operations.codings import morse_code_coder, base64_coder, ascii_coder, bacon_coder

from options.font import *
from options.color import *


class coder_Win(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Initializes the user interface.
        """
        self.setObjectName("Codings")
        self.setFixedSize(600, 400)
        self.setStyleSheet(default_background_color)

        # Create a vertical layout
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        # Create a combo box for selecting the language
        self.set_language = QtWidgets.QComboBox(self)
        self.set_language.setObjectName("set_language")
        self.set_language.setStyleSheet(white_black_color)
        self.set_language.addItem("")
        self.set_language.addItem("")
        self.set_language.addItem("")
        self.set_language.addItem("")
        self.set_language.setFont(font_label)
        self.verticalLayout_4.addWidget(self.set_language)

        # Create a horizontal layout
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Create a vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")

        # Create a label for the input text
        self.input_text_label = QtWidgets.QLabel(self)
        self.input_text_label.setTextFormat(QtCore.Qt.PlainText)
        self.input_text_label.setObjectName("input_text_label")
        self.input_text_label.setFont(font_label)
        self.input_text_label.setStyleSheet(invizibility_background_color)
        self.verticalLayout.addWidget(self.input_text_label)

        # Create a plain text input widget
        self.plainText_input = QtWidgets.QPlainTextEdit(self)
        self.plainText_input.setObjectName("plainText_input")
        self.plainText_input.setStyleSheet(plaintext_color + border_radius)
        self.verticalLayout.addWidget(self.plainText_input)

        # Add a spacer item
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)

        # Add the vertical layout to the horizontal layout
        self.horizontalLayout.addLayout(self.verticalLayout)

        # Create a label for the arrow text
        self.arrow_text_label = QtWidgets.QLabel(self)
        self.arrow_text_label.setObjectName("arrow_text_label")
        self.arrow_text_label.setFont(font_label)
        self.arrow_text_label.setStyleSheet(invizibility_background_color)
        self.horizontalLayout.addWidget(self.arrow_text_label)

        # Create a vertical layout
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        # Create a label for the output text
        self.output_text_label = QtWidgets.QLabel(self)
        self.output_text_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.output_text_label.setTextFormat(QtCore.Qt.AutoText)
        self.output_text_label.setObjectName("output_text_label")
        self.output_text_label.setFont(font_label)
        self.output_text_label.setStyleSheet(invizibility_background_color)
        self.verticalLayout_2.addWidget(self.output_text_label)

        # Create a plain text output widget
        self.plainText_output = QtWidgets.QPlainTextEdit(self)
        self.plainText_output.setObjectName("plainText_output")
        self.plainText_output.setStyleSheet(plaintext_color + border_radius)
        self.verticalLayout_2.addWidget(self.plainText_output)

        # Add a spacer item
        spacerItem1 = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)

        # Add vertical layout to horizontal layout
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        # Add horizontal layout to vertical layout
        self.verticalLayout_4.addLayout(self.horizontalLayout)

        # Create a new horizontal layout
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")

        # Create a new vertical layout
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # Create a radio button for encoding
        self.encode_radio = QtWidgets.QRadioButton(self)
        self.encode_radio.setObjectName("encode_radio")
        self.encode_radio.setFont(font_label)
        self.encode_radio.setStyleSheet(invizibility_background_color)

        # Create a button group for the radio buttons
        self.crypt_btn = QtWidgets.QButtonGroup(self)
        self.crypt_btn.setObjectName("crypt_btn")
        self.crypt_btn.addButton(self.encode_radio)

        # Add the encoding radio button to the vertical layout
        self.verticalLayout_3.addWidget(self.encode_radio)

        # Create a radio button for decoding
        self.decode_radio = QtWidgets.QRadioButton(self)
        self.decode_radio.setObjectName("decode_radio")
        self.decode_radio.setFont(font_label)
        self.decode_radio.setStyleSheet(invizibility_background_color)
        self.crypt_btn.addButton(self.decode_radio)

        # Add the decoding radio button to the vertical layout
        self.verticalLayout_3.addWidget(self.decode_radio)

        # Add the vertical layout to the horizontal layout
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)

        # Create a new horizontal layout
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        # Add a spacer item to the horizontal layout
        spacerItem2 = QtWidgets.QSpacerItem(
            40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)

        # Create a save button
        self.save_btn = QtWidgets.QPushButton(self)
        self.save_btn.setObjectName("save_btn")
        self.save_btn.setStyleSheet(plaintext_color)
        self.save_btn.setFont(font_btn)

        # Add the save button to the horizontal layout
        self.horizontalLayout_2.addWidget(self.save_btn)

        # Create an answer button
        self.answer_btn = QtWidgets.QPushButton(self)
        self.answer_btn.setObjectName("answer_btn")
        self.answer_btn.setStyleSheet(plaintext_color)
        self.answer_btn.setFont(font_btn)

        # Add the answer button to the horizontal layout
        self.horizontalLayout_2.addWidget(self.answer_btn)

        # Add the horizontal layout to the horizontal layout 3
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        # Add the horizontal layout 3 to the vertical layout 4
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        # Set the encoding radio button as the default selection
        self.encode_radio.click()

        # Connect the buttonClicked signal of the button group to the set_btn_answer_text slot
        self.crypt_btn.buttonClicked.connect(self.set_btn_answer_text)

        # Connect the clicked signal of the answer button to the calculate slot
        self.answer_btn.clicked.connect(self.calculate)

        # Connect the clicked signal of the save button to the save_in_file slot
        self.save_btn.clicked.connect(self.save_in_file)

        # Perform retranslation
        self.retranslateUi()

        # Connect slots by object name
        QtCore.QMetaObject.connectSlotsByName(self)

    def save_in_file(self):
        """
        Saves the contents of the plain text input and output fields to a file.

        Prompts the user to choose a file to save, and then writes the contents of the
        plain text input and output fields to the file.
        """
        filename, _ = QFileDialog.getSaveFileName(
            self, "Save File", "", "Text files (*.txt)")

        if filename:
            with open(filename, "w") as f:
                # Write the language and answer to the file
                f.write('Coding: ' + self.set_language.currentText() +
                        ' ' + self.answer_btn.text() + '\n\n')

                # Write the input text to the file
                f.write(self.plainText_input.toPlainText() + '\n')

                # Write a separator line
                f.write('---------------------------------------\n')

                # Write the output text to the file
                f.write(self.plainText_output.toPlainText())

    def set_btn_answer_text(self):
        if self.decode_radio.isChecked():
            self.answer_btn.setText(self.decode_radio.text())
        else:
            self.answer_btn.setText(self.encode_radio.text())

    def calculate(self):
        """
        Calculate the encoded or decoded text based on the selected coder type.
        """
        # Get the input text and coder type
        text = self.plainText_input.toPlainText()
        coder_type = self.set_language.currentText()

        if self.encode_radio.isChecked():
            # Encode the text based on the selected coder type
            match coder_type:
                case "base64":
                    answer = base64_coder.encode_base64(text=text)
                case 'ASCII':
                    answer = ascii_coder.encoder_ascii(text=text)
                case 'MORCE_CODE':
                    answer = morse_code_coder.encoder_morse_code(text=text)
                case 'Bacon':
                    answer = bacon_coder.encoder_bacon(text=text)

        elif self.decode_radio.isChecked():
            # Decode the text based on the selected coder type
            match coder_type:
                case "base64":
                    answer = base64_coder.decode_base64(encoded_text=text)
                case 'ASCII':
                    answer = ascii_coder.decoder_ascii(encoded_text=text)
                case 'MORCE_CODE':
                    answer = morse_code_coder.decoder_morse_code(
                        encoded_text=text)
                case 'Bacon':
                    answer = bacon_coder.decoder_bacon(encoded_text=text)

        # Set the output text
        self.plainText_output.setPlainText(str(answer))

    def retranslateUi(self):
        """
        Translates the user interface elements to the appropriate language.

        This function sets the text for various elements in the user interface,
        such as window title, dropdown items, labels, radio buttons, and buttons.
        """
        _translate = QtCore.QCoreApplication.translate

        # Set the window title
        self.setWindowTitle(_translate("Codings", "Codings"))

        # Set the text for the dropdown items
        self.set_language.setItemText(0, _translate("Codings", "base64"))
        self.set_language.setItemText(1, _translate("Codings", "MORCE_CODE"))
        self.set_language.setItemText(2, _translate("Codings", "ASCII"))
        self.set_language.setItemText(3, _translate("Codings", "Bacon"))

        # Set the text for the labels
        self.input_text_label.setText(_translate("Codings", "Input"))
        self.arrow_text_label.setText(_translate("Codings", "->"))
        self.output_text_label.setText(_translate("Codings", "Output"))

        # Set the text for the radio buttons
        self.encode_radio.setText(_translate("Codings", "Encode"))
        self.decode_radio.setText(_translate("Codings", "Decode"))

        # Set the text for the buttons
        self.save_btn.setText(_translate("Codings", "Save to file"))
        self.answer_btn.setText(_translate("Codings", "Encode"))
