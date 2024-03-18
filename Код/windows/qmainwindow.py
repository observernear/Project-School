from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow

from windows.qwidget_support import support_Win
from windows.qwidget_ciphers import cipher_Win
from windows.qwidget_codings import coder_Win
from windows.qwidget_qrcodes import qrcode_Win
from windows.qwidget_info import info_Win

from options.font import *
from options.color import *
from options.text import main_text


class mainWin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Initialize the user interface.
        """
        # Set object name and fixed size
        self.setObjectName("CryptoMaster")
        self.setFixedSize(715, 475)
        self.setStyleSheet(default_background_color)

        # Create central widget
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")

        # Create main label
        self.main_label = QtWidgets.QTextBrowser(self.centralwidget)
        self.main_label.setGeometry(QtCore.QRect(0, 0, 715, 475))
        self.main_label.setObjectName("label")
        self.main_label.setFont(font_label)

        # Set central widget
        self.setCentralWidget(self.centralwidget)

        # Create menu bar
        self.menubar = QtWidgets.QMenuBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 713, 22))
        self.menubar.setObjectName("menubar")

        # Create menu options
        self.menuoperations = QtWidgets.QMenu(self.menubar)
        self.menuoperations.setObjectName("menuoperations")
        self.menuother = QtWidgets.QMenu(self.menubar)
        self.menuother.setObjectName("menusupport")

        # Set menu bar
        self.setMenuBar(self.menubar)

        # Create menu actions
        self.coding_action = QtWidgets.QAction(self)
        self.coding_action.setObjectName("coding_action")
        self.cipher_action = QtWidgets.QAction(self)
        self.cipher_action.setObjectName("cipher_action")
        self.qrcoding_action = QtWidgets.QAction(self)
        self.qrcoding_action.setObjectName("qrcoding_action")
        self.support_action = QtWidgets.QAction(self)
        self.support_action.setObjectName("support_action")
        self.info_action = QtWidgets.QAction(self)
        self.info_action.setObjectName("support_action")

        # Add separators to menus
        self.menuoperations.addSeparator()
        self.menuother.addSeparator()

        # Add actions to menus
        self.menuoperations.addAction(self.coding_action)
        self.menuoperations.addAction(self.cipher_action)
        self.menuoperations.addAction(self.qrcoding_action)
        self.menuother.addAction(self.support_action)
        self.menuother.addAction(self.info_action)

        # Add menus to menu bar
        self.menubar.addAction(self.menuoperations.menuAction())
        self.menubar.addAction(self.menuother.menuAction())

        # Set menu bar style and font
        self.menubar.setStyleSheet(white_black_color)
        self.menubar.setFont(font_label)

        # Connect action signals to slots
        self.support_action.triggered.connect(self.open_support_win)
        self.coding_action.triggered.connect(self.open_coding_win)
        self.cipher_action.triggered.connect(self.open_cipher_win)
        self.qrcoding_action.triggered.connect(self.open_qrcode_win)
        self.info_action.triggered.connect(self.open_info_win)

        # Perform UI translation and connect slots by name
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def open_support_win(self):
        """
        Opens the support window.
        """
        self.SupportWindow = support_Win(self)
        self.SupportWindow.show()

    def open_cipher_win(self):
        """
        Opens the cipher window.
        """
        self.CiperWindow = cipher_Win(self)
        self.CiperWindow.show()

    def open_coding_win(self):
        """
        Opens the coding window.
        """
        self.CodingWindow = coder_Win(self)
        self.CodingWindow.show()

    def open_qrcode_win(self):
        """
        Opens the QR code window.
        """
        self.QrcodingWindow = qrcode_Win(self)
        self.QrcodingWindow.show()

    def open_info_win(self):
        """
        Opens the info window.
        """
        self.InfoWindow = info_Win(self)
        self.InfoWindow.show()

    def retranslateUi(self):
        """
        Translates the user interface elements.
        """
        _translate = QtCore.QCoreApplication.translate

        # Set the window title
        self.setWindowTitle(_translate("CryptoMaster", "CryptoMaster"))

        # Set the text of the main label
        self.main_label.setText(_translate("CryptoMaster", main_text))

        # Set the text and shortcut for the "OPERATION" menu
        self.menuoperations.setTitle(_translate("CryptoMaster", "OPERATION"))

        # Set the text and shortcut for the "OTHER" menu
        self.menuother.setTitle(_translate("CryptoMaster", "OTHER"))

        # Set the text and shortcut for the "Codings" action
        self.coding_action.setText(_translate("CryptoMaster", "Codings"))
        self.coding_action.setShortcut(_translate("CryptoMaster", "Alt+O"))

        # Set the text and shortcut for the "Ciphers" action
        self.cipher_action.setText(_translate("CryptoMaster", "Ciphers"))
        self.cipher_action.setShortcut(_translate("CryptoMaster", "Alt+I"))

        # Set the text and shortcut for the "QRcodes" action
        self.qrcoding_action.setText(_translate("CryptoMaster", "QRcodes"))
        self.qrcoding_action.setShortcut(_translate("CryptoMaster", "Alt+Q"))

        # Set the text and shortcut for the "Support" action
        self.support_action.setText(_translate("CryptoMaster", "Support"))
        self.support_action.setShortcut(_translate("CryptoMaster", "Alt+S"))

        # Set the text and shortcut for the "Info" action
        self.info_action.setText(_translate("CryptoMaster", "Info"))
        self.info_action.setShortcut(_translate("CryptoMaster", "Alt+N"))
