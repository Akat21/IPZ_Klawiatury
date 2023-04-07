from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from components.Navbar import Navbar
from components.RegisterViews import Views

class Hand(QWidget):
    def __init__(self, parent = None):
        super(Hand, self).__init__(parent)
        self.parent = parent
        print("Hand")
        self.keyboards = Views()

    def UIComponents(self):
        gridLayout = QGridLayout()

        for i,keyboard in enumerate(self.keyboards.getList()):
            keyboard=str(keyboard)
            print(keyboard)
            keyBoardBtn=QPushButton(keyboard, objectName="Hand"+keyboard+"Btn")
            keyBoardBtn.clicked.connect(lambda aniki, self=self, keyboard=keyboard:self.keyBoardBtnOnClick(keyboard))
            gridLayout.addWidget(keyBoardBtn, self.keyboards.getN(), i, 1, 1)
        
        self.setLayout(gridLayout)
        return self

    def keyBoardBtnOnClick(self,keyBoardName):
        print(keyBoardName)
        self.keyboards.getInstance(keyBoardName)

    def register(self, name, constructor):
        self.keyboards.register(name, constructor)
        return self