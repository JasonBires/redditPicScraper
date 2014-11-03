from PyQt4 import QtGui
import sys
import mainDL as scraper

class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
    def initUI(self):
        
        run = QtGui.QLabel('Run')
        author = QtGui.QLabel('Author')
        review = QtGui.QLabel('Review')

        runButton = QtGui.QPushButton("RUNME", self)
        authorEdit = QtGui.QLineEdit()
        reviewEdit = QtGui.QTextEdit()
        
        runButton.clicked.connect(self.buttonClicked)
        
        grid = QtGui.QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(run, 1, 0)
        grid.addWidget(runButton, 1, 1)

        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)

        grid.addWidget(review, 3, 0)
        grid.addWidget(reviewEdit, 3, 1, 5, 1)
        
        self.setLayout(grid) 
        
        self.setGeometry(300, 300, 350, 300)
        self.setWindowTitle('Review')    
        self.show()
    
    def buttonClicked(self):
        scraper.pullXPages(2, "http://www.reddit.com/r/earthporn")
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()