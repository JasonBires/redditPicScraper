from PyQt4 import QtGui
import sys
import mainDL as scraper

class Example(QtGui.QWidget):
    url = ""
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        run = QtGui.QLabel('Run')
        urlButton = QtGui.QPushButton('URL')

        runButton = QtGui.QPushButton("RUNME", self)
        urlEdit = QtGui.QTextEdit()
        
        runButton.clicked.connect(self.buttonClicked)
        urlEdit.textChanged.connect(self.saveURL)
        
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(run, 1, 0)
        grid.addWidget(runButton, 1, 1)

        grid.addWidget(urlButton, 2, 0)
        grid.addWidget(urlEdit, 2, 1)

        #grid.addWidget(review, 3, 0)
        #grid.addWidget(reviewEdit, 3, 1, 5, 1)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')    
        self.show()
    
    def buttonClicked(self):
        scraper.pullXPages(2, self.url)
        
    def saveURL(self):
        sender = self.sender()
        self.url = str(sender.toPlainText())
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()