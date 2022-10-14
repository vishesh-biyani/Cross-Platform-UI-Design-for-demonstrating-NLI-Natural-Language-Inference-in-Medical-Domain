# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 822)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("iitkgp logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777212))
        self.centralwidget.setStyleSheet("#centralwidget\n"
"{\n"
"    \n"
"    border-image: url(C:/Users/Vishesh Biyani/Desktop/whiteback.jpg);\n"
"    background-color: qlineargradient(spread:reflect, x1:0.783773, y1:0.21, x2:1, y2:0, stop:0 rgba(187, 218, 216, 255), stop:1 rgba(255, 255, 255, 255));\n"
"   \n"
"}\n"
"")
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(9, 9, 1141, 450))
        self.frame_2.setMinimumSize(QtCore.QSize(750, 250))
        self.frame_2.setMaximumSize(QtCore.QSize(3000, 5000))
        self.frame_2.setSizeIncrement(QtCore.QSize(0, 100))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.mainLab = QtWidgets.QLabel(self.frame_2)
        self.mainLab.setGeometry(QtCore.QRect(300, 110, 447, 40))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.mainLab.setFont(font)
        self.mainLab.setStyleSheet("color: rgb(255, 170, 0);")
        self.mainLab.setAlignment(QtCore.Qt.AlignCenter)
        self.mainLab.setObjectName("mainLab")
        self.Title = QtWidgets.QLabel(self.frame_2)
        self.Title.setGeometry(QtCore.QRect(-10, 240, 201, 91))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.Title.setFont(font)
        self.Title.setAlignment(QtCore.Qt.AlignCenter)
        self.Title.setObjectName("Title")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(40, 20, 181, 171))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("iitkgp logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setGeometry(QtCore.QRect(9, 265, 1141, 750))
        self.frame_4.setMinimumSize(QtCore.QSize(750, 150))
        self.frame_4.setMaximumSize(QtCore.QSize(3000, 1000))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.GO = QtWidgets.QPushButton(self.frame_4)
        self.GO.setGeometry(QtCore.QRect(1000, 90, 75, 50))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(16)
        self.GO.setFont(font)
        self.GO.setStyleSheet("color: rgb(255, 255, 255);\n"
"border-color: rgb(0, 255, 127);\n"
"background-color: rgb(0, 212, 0);\n"
"border-radius: 5px;\n"
"border-style: solid;\n"
"border-width: 1px;")
        self.GO.setAutoDefault(True)
        self.GO.setDefault(False)
        self.GO.setFlat(False)
        self.GO.setObjectName("GO")
        self.layoutWidget = QtWidgets.QWidget(self.frame_4)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 100, 1001, 202))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(143)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Embeddings = QtWidgets.QComboBox(self.layoutWidget)
        self.Embeddings.setMouseTracking(False)
        self.Embeddings.setAcceptDrops(True)
        self.Embeddings.setStyleSheet("")
        self.Embeddings.setEditable(False)
        self.Embeddings.setObjectName("Embeddings")
        self.Embeddings.addItem("")
        self.Embeddings.addItem("")
        self.Embeddings.addItem("")
        self.Embeddings.addItem("")
        self.Embeddings.addItem("")
        self.horizontalLayout_2.addWidget(self.Embeddings)
        self.DistMult = QtWidgets.QComboBox(self.layoutWidget)
        self.DistMult.setObjectName("DistMult")
        self.DistMult.addItem("")
        self.DistMult.addItem("")
        self.DistMult.addItem("")
        self.horizontalLayout_2.addWidget(self.DistMult)
        self.Sentiment = QtWidgets.QComboBox(self.layoutWidget)
        self.Sentiment.setEditable(False)
        self.Sentiment.setObjectName("Sentiment")
        self.Sentiment.addItem("")
        self.Sentiment.addItem("")
        self.Sentiment.addItem("")
        self.horizontalLayout_2.addWidget(self.Sentiment)
        self.premise = QtWidgets.QComboBox(self.frame_4)
        self.premise.setGeometry(QtCore.QRect(70, 90, 521, 51))
        self.premise.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-width: 1px;\n"
"border-style: solid;")
        self.premise.setObjectName("premise")
        self.premise.addItem("")
        self.premise.addItem("")
        self.premise.addItem("")
        self.premise.addItem("")
        self.premise.addItem("")
        self.premise.addItem("")
        self.premise.addItem("")
        self.premise.addItem("")
        self.hypothesis = QtWidgets.QComboBox(self.frame_4)
        self.hypothesis.setGeometry(QtCore.QRect(610, 90, 361, 51))
        self.hypothesis.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"border-radius: 5px;\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"")
        self.hypothesis.setObjectName("hypothesis")
        self.hypothesis.addItem("")
        self.hypothesis.addItem("")
        self.hypothesis.addItem("")
        self.hypothesis.addItem("")
        self.hypothesis.addItem("")
        self.hypothesis.addItem("")
        self.hypothesis.addItem("")
        if(self.premise.currentIndex() == 0):
                self.hypothesis.setEnabled(False)
        else:
                self.hypothesis.setEnabled(True)
        self.layoutWidget.raise_()
        self.GO.raise_()
        self.premise.raise_()
        self.hypothesis.raise_()
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(9, 421, 1141, 150))
        self.frame.setMinimumSize(QtCore.QSize(750, 150))
        self.frame.setMaximumSize(QtCore.QSize(3000, 200))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setGeometry(QtCore.QRect(9, 577, 1141, 121))
        self.frame_6.setMaximumSize(QtCore.QSize(3000, 16777215))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        
        self.frame_2.raise_()
        self.frame_6.raise_()
        self.frame.raise_()
        self.frame_4.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        self.menuExamples = QtWidgets.QMenu(self.menubar)
        self.menuExamples.setObjectName("menuExamples")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.ClearAll = QtWidgets.QAction(MainWindow)
        self.ClearAll.setObjectName("ClearAll")
        self.menuExamples.addAction(self.ClearAll)
        self.menuExamples.addAction(self.actionClose)
        self.menubar.addAction(self.menuExamples.menuAction())
        self.num = 2
        self.retranslateUi(MainWindow)
        self.Embeddings.setCurrentIndex(0)
        self.Sentiment.setCurrentIndex(0)
        self.actionClose.triggered.connect(MainWindow.close)
        self.premise.currentIndexChanged.connect(lambda: self.me())
        self.ClearAll.triggered.connect(lambda: self.Sentiment.setEnabled(True))
        self.ClearAll.triggered.connect(lambda: self.Embeddings.setEnabled(True))
        self.ClearAll.triggered.connect(lambda: self.DistMult.setEnabled(True))
        self.ClearAll.triggered.connect(lambda: self.premise.setEnabled(True))
        self.ClearAll.triggered.connect(lambda: self.hypothesis.setEnabled(True))
        self.ClearAll.triggered.connect(lambda: self.DistMult.setCurrentIndex(0))
        self.ClearAll.triggered.connect(lambda: self.Embeddings.setCurrentIndex(0))
        self.ClearAll.triggered.connect(lambda: self.Sentiment.setCurrentIndex(0))
        self.ClearAll.triggered.connect(lambda: self.hypothesis.setCurrentIndex(0))
        self.ClearAll.triggered.connect(lambda: self.premise.setCurrentIndex(0))
        self.ClearAll.triggered.connect(lambda: self.premise.setStyleSheet("border-radius: 5px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 1px;\n"
"border-style: solid;"))
        self.ClearAll.triggered.connect(lambda: self.hypothesis.setStyleSheet("border-radius: 5px;\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 1px;\n"
"border-style: solid;"))
        self.ClearAll.triggered.connect(lambda: self.Embeddings.setStyleSheet(""))
        self.ClearAll.triggered.connect(lambda: self.Sentiment.setStyleSheet(""))
        self.ClearAll.triggered.connect(lambda: self.DistMult.setStyleSheet(""))
        self.ClearAll.triggered.connect(self.check)
        self.ClearAll.triggered.connect(lambda: self.reset())
        self.premise.currentIndexChanged.connect(lambda: self.messi())
        self.Embeddings.currentIndexChanged.connect(lambda: self.ronaldo())

        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def reset(self):
            self.DistMult.clear()
            self.DistMult.addItem("  DistMult")
            self.DistMult.addItem("0")
            self.DistMult.addItem("1")
            self.Sentiment.clear()
            self.Sentiment.addItem("  Sentiment")
            self.Sentiment.addItem("0")
            self.Sentiment.addItem("1")
    

    def senti(self):
        if(self.DistMult.currentIndex() == 1):
                self.Sentiment.clear()
                self.Sentiment.addItem("  Sentiment")
                self.Sentiment.addItem("0")
        elif(self.DistMult.currentIndex() == 2):
                self.Sentiment.clear()
                self.Sentiment.addItem("  Sentiment")
                self.Sentiment.addItem("0")
                self.Sentiment.addItem("1")

    def ronaldo(self):
        if (self.Embeddings.currentIndex() == 1): #elmo
                self.DistMult.clear()
                self.DistMult.addItem("  DistMult")
                self.DistMult.addItem("0")  
                self.Sentiment.clear()
                self.Sentiment.addItem("  Sentiment")
                self.Sentiment.addItem("0")
        elif(self.Embeddings.currentIndex() == 2): #bioelmo
                self.DistMult.clear()
                self.DistMult.addItem("  DistMult")
                self.DistMult.addItem("0")
                self.DistMult.addItem("1")
                self.DistMult.currentIndexChanged.connect(lambda: self.senti())
               # self.Sentiment.clear()
               # self.Sentiment.addItem("  Sentiment")
               # self.Sentiment.addItem("0")
               # self.Sentiment.addItem("1")
                      #  if(self.DistMult.currentIndex() == 1):
                      #          self.Sentiment.clear()
                      #          self.Sentiment.addItem("  Sentiment")
                     #           self.Sentiment.addItem("0")
                     #   elif(self.DistMult.currentIndex() == 2):
                      #          self.Sentiment.clear()
                      #          self.Sentiment.addItem("  Sentiment")
                       #         self.Sentiment.addItem("0")
                        #        self.Sentiment.addItem("1")


        elif(self.Embeddings.currentIndex() == 3): #fastText
                self.DistMult.clear()
                self.DistMult.addItem("  DistMult")
                self.DistMult.addItem("1")  
                self.Sentiment.clear()
                self.Sentiment.addItem("  Sentiment")
                self.Sentiment.addItem("0")
        elif(self.Embeddings.currentIndex() == 4): #glove
                self.DistMult.clear()
                self.DistMult.addItem("  DistMult")
                self.DistMult.addItem("1")  
                self.Sentiment.clear()
                self.Sentiment.addItem("  Sentiment")
                self.Sentiment.addItem("0")
        
    def messi(self):
        if(self.premise.currentIndex() == 1):
                self.hypothesis.clear()
                self.hypothesis.addItem("   HYPOTHESIS")
                self.hypothesis.addItem("the patient is hypotensive")
                self.hypothesis.addItem("the patient is hypertensive")
        elif(self.premise.currentIndex() == 2):
                self.hypothesis.clear()
                self.hypothesis.addItem("   HYPOTHESIS")
                self.hypothesis.addItem("His chest pain has been getting worse")
        elif(self.premise.currentIndex() == 3):
                self.hypothesis.clear()
                self.hypothesis.addItem("   HYPOTHESIS")
                self.hypothesis.addItem("The patient required a higher level of care.")
        elif(self.premise.currentIndex() == 4):
                self.hypothesis.clear()
                self.hypothesis.addItem("   HYPOTHESIS")
                self.hypothesis.addItem("Patient has stable blood pressure")
        elif(self.premise.currentIndex() == 5):
                self.hypothesis.clear()
                self.hypothesis.addItem("   HYPOTHESIS")
                self.hypothesis.addItem("The patient was hemodynamically unstable")
        elif(self.premise.currentIndex() == 6):
                self.hypothesis.clear()
                self.hypothesis.addItem("   HYPOTHESIS")
                self.hypothesis.addItem("The patient does not have infectious symptoms.")



    def check(self):
            self.num = 0
            if(self.premise.currentIndex() == 0):
                self.hypothesis.setEnabled(False)
            else:
                self.hypothesis.setEnabled(True)

    def me(self):
            if(self.premise.currentIndex() == 0):
                self.hypothesis.setEnabled(False)
            else:
                self.hypothesis.setEnabled(True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "IIT KGP"))
        self.mainLab.setText(_translate("MainWindow", "IIT KGP"))
        self.Title.setText(_translate("MainWindow", "Title"))
        self.GO.setText(_translate("MainWindow", "GO"))
        self.Embeddings.setCurrentText(_translate("MainWindow", " Embeddings"))
        self.Embeddings.setItemText(0, _translate("MainWindow", " Embeddings"))
        self.Embeddings.setItemText(1, _translate("MainWindow", "Elmo"))
        self.Embeddings.setItemText(2, _translate("MainWindow", "BioElmo"))
        self.Embeddings.setItemText(3, _translate("MainWindow", "FastText"))
        self.Embeddings.setItemText(4, _translate("MainWindow", "Glove"))
        self.DistMult.setItemText(0, _translate("MainWindow", "  DistMult"))
        self.DistMult.setItemText(1, _translate("MainWindow", "0"))
        self.DistMult.setItemText(2, _translate("MainWindow", "1"))
        self.Sentiment.setCurrentText(_translate("MainWindow", "  Sentiment"))
        self.Sentiment.setItemText(0, _translate("MainWindow", "  Sentiment"))
        self.Sentiment.setItemText(1, _translate("MainWindow", "0"))
        self.Sentiment.setItemText(2, _translate("MainWindow", "1"))
        self.premise.setItemText(0, _translate("MainWindow", "   PREMISE"))
        self.premise.setItemText(1, _translate("MainWindow", "Patient also required multiple pressors to maintain her blood pressure."))
        self.premise.setItemText(2, _translate("MainWindow", "He was initially reluctant to undergo surgery but has had increasing amounts of chest pain episodes."))
        self.premise.setItemText(3, _translate("MainWindow", "Patient also required multiple pressors to maintain her blood pressure."))
        self.premise.setItemText(4, _translate("MainWindow", "He was transferred to [**Hospital1 22**] for further management."))
        self.premise.setItemText(5, _translate("MainWindow", "Her BP fell to 97/52, then later rose to 197/92 (very labile)."))
        self.premise.setItemText(6, _translate("MainWindow", "A temporary wire was not necessary at this time due to her narrow complex and hemodynamic stability."))
        self.premise.setItemText(7, _translate("MainWindow", "He denies any fever, diarrhea, chest pain, cough, URI symptoms, or dysuria."))
        self.hypothesis.setItemText(0, _translate("MainWindow", "   HYPOTHESIS"))
        self.hypothesis.setItemText(1, _translate("MainWindow", "the patient is hypotensive"))
        self.hypothesis.setItemText(2, _translate("MainWindow", "His chest pain has been getting worse"))
        self.hypothesis.setItemText(3, _translate("MainWindow", "the patient is hypotensive"))
        self.hypothesis.setItemText(4, _translate("MainWindow", "The patient required a higher level of care."))
        self.hypothesis.setItemText(5, _translate("MainWindow", "Patient has stable blood pressure"))
        self.hypothesis.setItemText(6, _translate("MainWindow", "The patient was hemodynamically unstable"))
        self.hypothesis.setItemText(7, _translate("MainWindow", "The patient does not have infectious symptoms."))
        self.menuExamples.setTitle(_translate("MainWindow", "File"))
        self.actionClose.setText(_translate("MainWindow", "Close"))
        self.ClearAll.setText(_translate("MainWindow", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

