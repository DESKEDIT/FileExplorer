from PyQt6.QtGui import QResizeEvent, QAction
from PyQt6.QtWidgets import QVBoxLayout, QTextEdit, QWidget, QTableWidget, QTableWidgetItem, QMainWindow, QStyleFactory
from PyQt6.QtCore import Qt
import os

class Explorer(QMainWindow):
    def __init__(self, startpath, app):
        super().__init__()
        self.app = app
        self.path = startpath
        self.pathdata = os.listdir(self.path)
        self.widget = QWidget()
        self.setCentralWidget(self.widget)
        self.initUi()
    def initUi(self):
        self.menubar = self.menuBar()
        self.styleBar = self.menubar.addMenu("Style") # type: ignore
        for style in QStyleFactory.keys(): # type: ignore
            styleAction = QAction(style, self)
            styleAction.triggered.connect(lambda checked, s=style: self.app.setStyle(s)) # type: ignore
            self.styleBar.addAction(styleAction) # type: ignore
        self.pathText = QTextEdit()
        self.pathText.setText(self.path)
        self.pathText.setFixedHeight(20)
        self.itemTable = QTableWidget()
        self.itemTable.setRowCount(len(self.pathdata))
        self.itemTable.setColumnCount(1)
        self.itemTable.setHorizontalHeaderLabels(["Name"])
        for itempos, item in enumerate(self.pathdata):
            item = QTableWidgetItem(
                item.strip())
            item.setFlags(~Qt.ItemFlag.ItemIsEditable) # type: ignore
            self.itemTable.setItem(itempos, 0, item)
        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.pathText)
        self.vbox.addWidget(self.itemTable)

        self.widget.setLayout(self.vbox)