#Importin Files, Packages and Libraries..
from PyQt5.QtWidgets import *
import sys
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *

#Screen (Window) Initialization..
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        #Window Options (Name, Icon, Size, etc.)..
        self.showMaximized()
        self.setWindowTitle('Hat Browser')
        self.setWindowIcon(QIcon('icon.png'))

        #Browser UI Creating And Editing..
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('https://google.com'))
        self.setCentralWidget(self.browser)

        #Navigation Bar For The Browser (Backwards, Forwards, Reload, etc.)..
        nav_Bar = QToolBar()
        self.addToolBar(nav_Bar)
        nav_Bar.setMovable(False)
        nav_Bar.setIconSize(QSize(18, 18))

        #Navigation Bar’s Actions (Backwards, Forwards, Reload, etc.)..
        #Back Button..
        back_button = QAction('Backwards', self)
        back_button.setToolTip('Press to go backwards!')
        back_button.setIcon(QIcon('back.png'))
        back_button.triggered.connect(self.browser.back)
        nav_Bar.addAction(back_button)

        #Forward Button..
        forward_button = QAction('Forward', self)
        forward_button.setToolTip('Press to go forward!')
        forward_button.setIcon(QIcon('forward.png'))
        forward_button.triggered.connect(self.browser.forward)
        nav_Bar.addAction(forward_button)

        # reload Button..
        reload_button = QAction('Reload', self)
        reload_button.setToolTip('Press refresh this page!')
        reload_button.setIcon(QIcon('reload.png'))
        reload_button.triggered.connect(self.browser.reload)
        nav_Bar.addAction(reload_button)

        # home Button..
        home_button = QAction('home', self)
        home_button.setToolTip('Press to go to home page!')
        home_button.setIcon(QIcon('home.png'))
        home_button.triggered.connect(self.navigate_home)
        nav_Bar.addAction(home_button)

        #Url Bar..
        self.url_Bar = QLineEdit()
        self.url_Bar.returnPressed.connect(self.navigate_to_url)
        nav_Bar.addWidget(self.url_Bar)
        self.browser.urlChanged.connect(self.url_changed)
        self.url_Bar.setFont(QFont('Lucida Fax', 11))

        # search Button..
        search_button = QAction('search', self)
        search_button.setToolTip('Search')
        search_button.setIcon(QIcon('search.png'))
        search_button.triggered.connect(self.navigate_to_url)
        search_button.setShortcut("Enter")
        nav_Bar.addAction(search_button)


    #Navigation to home page function..
    def navigate_home(self):
        self.browser.setUrl(QUrl('https://facebook.com'))

    #Follow the url function..
    def navigate_to_url(self):
        url = self.url_Bar.text()
        self.browser.setUrl(QUrl(url))

    #Updating the url function
    def url_changed(self, pr):
        self.url_Bar.setText(pr.toString())












app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.setApplicationName('Hat Browser')
app.exec_()