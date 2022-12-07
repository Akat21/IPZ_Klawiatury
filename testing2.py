import cv2
import mediapipe as mp
import time
import Modules.HandTrackingModule as htm
from Keyboard import Keyboard
from HandMovingKeyboard import HandMovingKeyboard

import PyQt5.QtWidgets as pq
class Menu():

    def __init__(self):
        self.app = pq.QApplication([])
        self.window = pq.QWidget()
        self.window.setWindowTitle("Hand Tracking Program Menu")
        
        self.window.setFixedSize(550,550) 
        self.layout = pq.QVBoxLayout()
        self.grid = pq.QGridLayout()
        self.point = 8


        #label (text)
        self.labelPoint=pq.QLabel("Enter the main point of hand to detect:")
        self.grid.addWidget(self.labelPoint, 0, 0,1,1)
        
        #text line
        self.point_text = pq.QLineEdit()
        self.grid.addWidget(self.point_text, 2, 0,1,1)
        print(self.point_text.text())


        
       


        #button activating the launch function
        self.buttonDetection = pq.QPushButton("Launch detection")
        self.grid.addWidget(self.buttonDetection, 4, 0,1,1)
        self.buttonDetection.clicked.connect( self.launch)

        #Setting the layout
        self.window.setLayout(self.grid)

        #Showing and executing the main window
        self.window.show()
        self.app.exec_()


    def launch(self):

        #Getting the point of hand
        self.point = int(self.point_text.text())   # tu jest punkt do lms

        pTime = 0

        cap = cv2.VideoCapture(0)
        detector = htm.handDetector(maxHands=1)
        classic_keyboard = Keyboard()
        handMovingKeyboard = HandMovingKeyboard(classic_keyboard,self.point)
        print("PUNKT: " + str(self.point))

        while True:
            success, img = cap.read()
            img = cv2.flip(img, 1)
            img = cv2.resize(img, (1080, 768))
            img = detector.findHands(img)
            lmList = detector.findPosition(img)

            handMovingKeyboard.update(lmList)

            img = classic_keyboard.draw_update(img, 10, 100, 30, 30)

            ###FPS###
            cTime = time.time()
            fps = 1/(cTime - pTime)
            pTime = cTime

            ###DRAW RESULT###
            img = handMovingKeyboard.draw_result(img, 600, 600)
            #################
        
            cv2.putText(img, str(int(fps)),(0,15), cv2.FONT_HERSHEY_PLAIN, 1 ,(255,0,255), 2)
            cv2.imshow("Image", img)
            cv2.waitKey(1)
            #########


def main():

    M = Menu()
    #M.launch()

    # launch(8)

if __name__ == '__main__':
    main()

