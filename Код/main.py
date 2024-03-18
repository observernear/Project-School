from PyQt5.QtWidgets import QApplication
import sys
from windows.qmainwindow import mainWin

if __name__ == "__main__":
    # Create a new application
    app = QApplication(sys.argv)

    # Create an instance of the main window
    ex = mainWin()

    # Show the main window
    ex.show()

    # Execute the application event loop
    sys.exit(app.exec())
