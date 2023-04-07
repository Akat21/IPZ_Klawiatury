from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from components.Navbar import Navbar
from components.RegisterViews import Views
from keyboards.HeadHandChoose import HeadHandChoose
from keyboards.Head import Head
from keyboards.Hand import Hand

class Keyboards(QWidget):
    def __init__(self):
        super(Keyboards, self).__init__()
        print("Kboards")
        self.UIComponents()

    def UIComponents(self):
        self.gridLayout = QGridLayout()

        self.views = Views()
        self.views = self.ViewsRegister(self.views)
        self.SetView(self.views, "HeadHandChoose")

        self.setLayout(self.gridLayout)

    def setHead(self):
        return Head() \
        .register("Eight Pen",lambda: 0) \
        .register("Head Moving Keyboard",lambda: 0) \
        .UIComponents()
    
    def setHand(self):
        return Hand() \
        .register("HandMovingKeyboardSection",lambda: 0) \
        .register("HandMovingStaticKeyboardSection",lambda: 0) \
        .register("EightPenSection",lambda: 0) \
        .UIComponents()

    def ViewsRegister(self, view):
        view.register("HeadHandChoose", lambda:HeadHandChoose(self))
        view.register("Head",self.setHead)
        view.register("Hand",self.setHand)
        return view

    def SetView(self, views, viewName):
        currentView = views.getInstance(viewName)
        
        for i in reversed(range(self.gridLayout.count())): 
            self.gridLayout.itemAt(i).widget().setParent(None)

        self.gridLayout.addWidget(currentView, 3, 0 , 1, 2)
        