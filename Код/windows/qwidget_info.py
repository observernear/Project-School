from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QWidget

from options.color import *
from options.font import *
from options.text import *


class info_Win(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.initUI()

    def initUI(self):
        """
        Initialize the user interface.
        """
        self.setObjectName("info_Win")
        self.setFixedSize(600, 400)
        self.setStyleSheet(grey_background_color)
        self.info_tab = QtWidgets.QTabWidget(self)
        self.info_tab.setGeometry(QtCore.QRect(0, 0, 600, 400))
        self.info_tab.setFont(font_btn)
        self.info_tab.setStyleSheet(tab_color)
        self.info_tab.setObjectName("info_tab")

        # About Us tab
        self.about_us = QtWidgets.QWidget()
        self.about_us.setObjectName("about_us")
        self.text_us = QtWidgets.QTextBrowser(self.about_us)
        self.text_us.setGeometry(QtCore.QRect(0, -1, 600, 371))
        self.text_us.setFont(font_label)
        self.text_us.setStyleSheet(default_background_color)
        self.text_us.setObjectName("text_us")
        self.text_us.setOpenExternalLinks(True)
        self.info_tab.addTab(self.about_us, "")

        # About Codings tab
        self.about_codings = QtWidgets.QWidget()
        self.about_codings.setObjectName("about_codings")
        self.text_codings = QtWidgets.QTextBrowser(self.about_codings)
        self.text_codings.setGeometry(QtCore.QRect(0, -1, 600, 371))
        self.text_codings.setFont(font_label)
        self.text_codings.setStyleSheet(default_background_color)
        self.text_codings.setObjectName("text_codings")
        self.info_tab.addTab(self.about_codings, "")

        # About Ciphers tab
        self.about_ciphers = QtWidgets.QWidget()
        self.about_ciphers.setObjectName("about_ciphers")
        self.text_ciphers = QtWidgets.QTextBrowser(self.about_ciphers)
        self.text_ciphers.setGeometry(QtCore.QRect(0, -1, 600, 371))
        self.text_ciphers.setFont(font_label)
        self.text_ciphers.setStyleSheet(default_background_color)
        self.text_ciphers.setObjectName("text_ciphers")
        self.info_tab.addTab(self.about_ciphers, "")

        # About QR Codes tab
        self.about_qrcodes = QtWidgets.QWidget()
        self.about_qrcodes.setObjectName("about_qrcodes")
        self.text_qrcodes = QtWidgets.QTextBrowser(self.about_qrcodes)
        self.text_qrcodes.setGeometry(QtCore.QRect(0, -1, 600, 371))
        self.text_qrcodes.setFont(font_label)
        self.text_qrcodes.setStyleSheet(default_background_color)
        self.text_qrcodes.setObjectName("text_qrcodes")
        self.info_tab.addTab(self.about_qrcodes, "")

        self.retranslateUi()
        self.info_tab.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        """
        This function is responsible for retranslating the UI elements.
        """
        _translate = QtCore.QCoreApplication.translate

        # Set the window title
        self.setWindowTitle(_translate("info_Win", "info"))

        # Set the HTML content of the text_us widget with translated text
        self.text_us.setHtml(_translate("info_Win", text_about_us))

        # Set the tab text and HTML content of the about_us tab
        self.info_tab.setTabText(self.info_tab.indexOf(
            self.about_us), _translate("info_Win", "About Us"))

        # Set the HTML content of the text_codings widget with translated text
        self.text_codings.setHtml(_translate("info_Win", text_about_codings))

        # Set the tab text and HTML content of the about_codings tab
        self.info_tab.setTabText(self.info_tab.indexOf(
            self.about_codings), _translate("info_Win", "About Codings"))

        # Set the HTML content of the text_ciphers widget with translated text
        self.text_ciphers.setHtml(_translate("info_Win", text_about_ciphers))

        # Set the tab text and HTML content of the about_ciphers tab
        self.info_tab.setTabText(self.info_tab.indexOf(
            self.about_ciphers), _translate("info_Win", "About ciphers"))

        # Set the HTML content of the text_qrcodes widget with translated text
        self.text_qrcodes.setHtml(_translate("info_Win", text_about_qrcodes))

        # Set the tab text and HTML content of the about_qrcodes tab
        self.info_tab.setTabText(self.info_tab.indexOf(
            self.about_qrcodes), _translate("info_Win", "About QR-codes"))
