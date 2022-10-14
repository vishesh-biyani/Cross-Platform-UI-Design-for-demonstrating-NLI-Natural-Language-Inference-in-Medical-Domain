from PyQt5 import QtWidgets, QtCore, QtGui

from new2 import Ui_MainWindow
from new_results import Ui_windmain
import pandas as pd


#string1 = ""

class FirstWindow(QtWidgets.QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(FirstWindow,self).__init__(parent)
        self.setupUi(self)
        self.msg = QtWidgets.QMessageBox()
      #  self.msg1 = QtWidgets.QMessageBox()
     #   self.msg2 = QtWidgets.QMessageBox()
     #   self.msg3 = QtWidgets.QMessageBox()
     #   self.msg4 = QtWidgets.QMessageBox()
     #   self.msg5 = QtWidgets.QMessageBox()
        
        

class SecondWindow(QtWidgets.QMainWindow, Ui_windmain):
    def __init__(self,parent=None):
        super(SecondWindow,self).__init__(parent)
        self.setupUi(self)
        self.BACK.clicked.connect(self.hide)

class Manager:
    def __init__(self):
        
        self.first = FirstWindow()
        self.second = SecondWindow()
        self.options = {}
        self.first.GO.clicked.connect(lambda: self.setOptions())
        self.first.GO.clicked.connect(lambda: self.copa())
        self.first.GO.clicked.connect(lambda: self.finRes())
        self.second.BACK.clicked.connect(self.first.show)

        self.first.show()
    

    def setOptions(self):
        ctc = 1
        j = []
        if(self.first.premise.currentIndex() == 0):
           j.append("Premise")
           # self.first.msg1.setIcon(QtWidgets.QMessageBox.Warning)
           # self.first.msg1.setWindowIcon(QtGui.QIcon("C:/Users/Vishesh Biyani/Desktop/iitkgp logo.png"))
           # self.first.msg1.setText("Please select valid Sentiment input.")
           # self.first.msg1.setWindowTitle("Improper Sentiment Input")
           # self.first.msg1.setStandardButtons(QtWidgets.QMessageBox.Ok)
           ctc=0
           # self.first.setEnabled(False)
           # self.ret1 = self.first.msg1.exec_()
           # if(self.ret1 == QtWidgets.QMessageBox.Ok):
            #    del j[-1]
        if(self.first.hypothesis.currentIndex() == 0):
            j.append("Hypothesis")   
         #   self.first.msg2.setIcon(QtWidgets.QMessageBox.Warning)
          #  self.first.msg2.setWindowIcon(QtGui.QIcon("C:/Users/Vishesh Biyani/Desktop/iitkgp logo.png"))
          #  self.first.msg2.setText("Please select valid Embedding input.")
          #  self.first.msg2.setWindowTitle("Improper Embedding Input")
         #   self.first.msg2.setStandardButtons(QtWidgets.QMessageBox.Ok)
            ctc=0
          #  self.first.setEnabled(False)
          #  self.ret2 = self.first.msg2.exec_()
           # if(self.ret2 == QtWidgets.QMessageBox.Ok):
           #     del j[-1]

        if(self.first.Embeddings.currentIndex()==0):
            j.append("Embedding")
            #self.first.msg3.setIcon(QtWidgets.QMessageBox.Warning)
            #self.first.msg3.setWindowIcon(QtGui.QIcon("C:/Users/Vishesh Biyani/Desktop/iitkgp logo.png"))
            #self.first.msg3.setText("Please select valid DistMult input.")
            #self.first.msg3.setWindowTitle("Improper DistMult Input")
            #self.first.msg3.setStandardButtons(QtWidgets.QMessageBox.Ok)
            ctc=0
            #self.first.setEnabled(False)
            #self.ret3 = self.first.msg3.exec_()
            #if(self.ret3 == QtWidgets.QMessageBox.Ok):
             #   del j[-1]

        if(self.first.DistMult.currentIndex()==0):
            j.append("DistMult")
          #  self.first.msg4.setIcon(QtWidgets.QMessageBox.Warning)
          #  self.first.msg4.setWindowIcon(QtGui.QIcon("C:/Users/Vishesh Biyani/Desktop/iitkgp logo.png"))
          #  self.first.msg4.setText("Please give valid Premise input.")
           # self.first.msg4.setWindowTitle("Improper Premise Input")
          #  self.first.msg4.setStandardButtons(QtWidgets.QMessageBox.Ok)
            ctc=0
           # self.first.setEnabled(False)
           # self.ret4 = self.first.msg4.exec_()
          #  if(self.ret4 == QtWidgets.QMessageBox.Ok):
           #     del j[-1]
        
        if(self.first.Sentiment.currentIndex()==0):
            j.append("Sentiment")
          #  self.first.msg5.setIcon(QtWidgets.QMessageBox.Warning)
           # self.first.msg5.setWindowIcon(QtGui.QIcon("C:/Users/Vishesh Biyani/Desktop/iitkgp logo.png"))
          #  self.first.msg5.setText("Please give valid Hypothesis input.")
          #  self.first.msg5.setWindowTitle("Improper Hypothesis Input")
          #  self.first.msg5.setStandardButtons(QtWidgets.QMessageBox.Ok)
            ctc=0
           # self.first.setEnabled(False)
          #  self.ret5 = self.first.msg5.exec_()
         #   if(self.ret5 == QtWidgets.QMessageBox.Ok):
          #      del j[-1]
        
        if(ctc==1):
            self.options.update([('dataset',self.first.Embeddings.currentText()),('distmult',bool(int(self.first.DistMult.currentText()))),('sentiment',bool(int(self.first.Sentiment.currentText())))])
        else:
            if(len(j)!=0): 
                print(j[0])
                self.first.msg.setIcon(QtWidgets.QMessageBox.Warning)
                self.first.msg.setWindowIcon(QtGui.QIcon("C:/Users/Vishesh Biyani/Desktop/iitkgp logo.png"))
                if(len(j)==1):
                    self.first.msg.setText("Not all inputs are correct. Please verify the following inputs:\n\n"
                        "1.%s\n" % (str(j[0])))
                if(len(j)==2):
                    self.first.msg.setText("Not all inputs are correct. Please verify the following inputs:\n\n"
                        "1.%s\n2.%s\n" % (str(j[0]),str(j[1])))
                if(len(j)==3):
                    self.first.msg.setText("Not all inputs are correct. Please verify the following inputs:\n\n"
                        "1.%s\n2.%s\n3.%s\n" % (str(j[0]),str(j[1]),str(j[2])))
                if(len(j)==4):
                    self.first.msg.setText("Not all inputs are correct. Please verify the following inputs:\n\n"
                        "1.%s\n2.%s\n3.%s\n4.%s\n" % (str(j[0]),str(j[1]),str(j[2]),str(j[3])))                
                if(len(j)==5):
                    self.first.msg.setText("Not all inputs are correct. Please verify the following inputs:\n\n"
                        "1.%s\n2.%s\n3.%s\n4.%s\n5.%s\n" % (str(j[0]),str(j[1]),str(j[2]),str(j[3]),str(j[4])))  

                self.first.msg.setWindowTitle("Improper input")
                self.first.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
                ret = self.first.msg.exec_()
                if(ret==QtWidgets.QMessageBox.Ok):
                        j = []
            else:    
                self.first.setEnabled(True)

    

    def finRes(self):
    #    global string1
        self.second.PremiseOUT.setText(self.first.premise.currentText())
        self.second.HypothesisOUT.setText(self.first.hypothesis.currentText())
    #    if(self.first.num is not 0):
    #        self.second.SentimentOUT.setText(self.first.Sentiment.currentText())
     #   else:
      #      self.second.SentimentOUT.clear()
        if(self.first.Sentiment.currentIndex() is not 0 and self.first.Embeddings.currentIndex() is not 0 and self.first.DistMult.currentIndex() is not 0):
         #   lbl1 = self.GO(self.first.premise.currentText(),self.first.hypothesis.currentText(),self.first.Embeddings.currentText(),bool(int(self.first.Sentiment.currentText())))
          #  self.second.GoldLabelOUT.setText(string1)
            self.second.show()

 #   def GO(self,str_Premise,str_Hypothesis,str_Embeddings,senti):
   #     lbl = self.Test(self.options)
   #     return lbl

  #  def Test(self,options):
   #     label = "Entailment"
    #    return label

    def copa(self):
      #  global string1
        self.fil = pd.read_csv('Samples for demo.csv', error_bad_lines=False)
        q = -1
        for i in range(len(self.fil.index)):
            if(self.first.premise.currentText() == self.fil.values[i,0] and self.first.hypothesis.currentText() == self.fil.values[i,1]):
                q = self.fil.index[i] 
 
            
        for m in range(len(self.fil.columns)):
            if(self.fil.columns.values[m] == "gold_label"):
                self.second.SentimentOUT.setText(str(self.fil.values[q,m]))
            if(str(self.first.Embeddings.currentText()+'+'+self.first.DistMult.currentText()+'+'+self.first.Sentiment.currentText()) ==  self.fil.columns.values[m]):
                self.second.GoldLabelOUT.setText(str(self.fil.values[q,m]))
                


if __name__ =='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    manager = Manager()
    sys.exit(app.exec_())