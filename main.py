import os
from sys import platform, argv
from PyQt6.QtWidgets import QApplication
import explorer

if platform == "linux" or platform == "linux2" or platform == "darwin":
    path = "/"
elif platform == "win32":
    path = "C:/"
else:
    raise OSError("Unknown OS, please try on linux, linux2, macos, or windows")

entries = os.listdir(path)

app = QApplication(argv)
Explorer = explorer.Explorer(path, app)
Explorer.show()
app.exec()