import re
from PyQt4 import QtCore
def prepLinkURL(unformattedURLString):
    return QtCore.QString("http://www.reddit.com/r/" + unformattedURLString)