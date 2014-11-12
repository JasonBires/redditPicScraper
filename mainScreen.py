from PyQt4 import QtGui, QtCore
import sys
from IScraper import ScraperInterface as iScraper

class ScraperInterfaceGUI(QtGui.QWidget):
    def __init__(self):
        super(ScraperInterfaceGUI, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        self.scraper = iScraper() #create scraper interface object
        
        run = QtGui.QLabel('Run')
        
        self.urlListDownloader = QtGui.QPushButton('Download', self)
        self.toURLButton = QtGui.QPushButton('toURL', self)
        self.startDLButton = QtGui.QPushButton("DL Images", self)
        
        self.urlEdit = QtGui.QTextEdit()
        
        self.urlList = QtGui.QListWidget()
        
        self.urlListDownloader.clicked.connect(self.startListDL)
        self.toURLButton.clicked.connect(self.textToList)
        self.startDLButton.clicked.connect(self.startDL)
        
        self.urlEdit.textChanged.connect(self.saveURL)
        
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(run, 1, 0)
        grid.addWidget(self.startDLButton, 1, 1)

        grid.addWidget(self.toURLButton, 2, 0)
        grid.addWidget(self.urlEdit, 2, 1)
        
        grid.addWidget(self.urlListDownloader, 3, 0)
        grid.addWidget(self.urlList, 3, 1,)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')    
        self.show()

    def textToList(self):
        stringList = str(self.url).splitlines()
        for string in stringList:
            self.urlList.addItem(QtCore.QString("http://www.reddit.com/r/" + string))
        #self.urlList.addItem(self.url)
    
    def startDL(self):
        self.scraper.downloadPage(str(self.url), 2)
    
    def startListDL(self):
        count = self.urlList.count()
        urlList = []
        for x in range(0, count):
            urlList.append(str(self.urlList.item(x).text()))
        self.scraper.downloadFromSubreddits(urlList, 1)
    
    def saveURL(self):
        sender = self.sender()
        self.url = sender.toPlainText()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = ScraperInterfaceGUI()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()