from PyQt4 import QtGui, QtCore
import sys
import mainDL as scraper

class ScraperInterface(QtGui.QWidget):
    url = ""
    def __init__(self):
        super(ScraperInterface, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        run = QtGui.QLabel('Run')
        urlListLabel = QtGui.QLabel('URL List')
        
        self.urlButton = QtGui.QPushButton('URL', self)
        self.runButton = QtGui.QPushButton("RUNME", self)
        
        self.urlEdit = QtGui.QTextEdit()
        
        self.urlList = QtGui.QListWidget()
        
        self.urlButton.clicked.connect(self.textToList)
        self.runButton.clicked.connect(self.run)
        
        self.urlEdit.textChanged.connect(self.saveURL)
        
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(run, 1, 0)
        grid.addWidget(self.runButton, 1, 1)

        grid.addWidget(self.urlButton, 2, 0)
        grid.addWidget(self.urlEdit, 2, 1)
        
        grid.addWidget(urlListLabel, 3, 0)
        grid.addWidget(self.urlList, 3, 1,)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')    
        self.show()

    def textToList(self):
        self.urlList.addItem(self.url)
    
    def run(self):
        scraper.pullXPages(2, str(self.url))
        
    def saveURL(self):
        sender = self.sender()
        self.url = sender.toPlainText()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = ScraperInterface()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()