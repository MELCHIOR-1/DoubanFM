#!/usr/bin/env python
# -*- coding:utf-8 -*-
from PyQt4.QtWebKit import *
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.Qt import *
import time
class Window(QMainWindow):
     def __init__(self):
         super(Window, self).__init__()
         self.setWindowTitle(u"豆瓣 FM")
         self.setGeometry(450,350,420,180)
         #self.resize(420,180)
         self.setWindowFlags(Qt.WindowCloseButtonHint)
         icon = QIcon("./douban.png")
         self.setWindowIcon(icon)
         self.isTopLevel()
         self.trayIcon = QSystemTrayIcon(self)
         self.trayIcon.setIcon(icon)
         self.trayIcon.show()
         self.trayIcon.activated.connect(self.trayClick) #点击托盘 
         self.trayIcon.setToolTip(u"豆瓣 FM") #托盘信息
         self.Menu() #右键菜单
         self.flag = False
         
         self.web = QWebView(self)
         webSettings = self.web.settings()
         webSettings.setAttribute(QWebSettings.PluginsEnabled,True) #使Pyqt4.QtWebkit支持flash
         self.web.load(QUrl("http://douban.fm/radio"))

         self.web.resize(420,180)
         self.web.show()         
         
     def Menu(self):
         self.restoreAction = QAction(u"还原", self,triggered=self.showNormal)
         self.quitAction = QAction(u"退出", self,triggered=qApp.quit)
         self.trayIconMenu = QMenu(self)
         self.trayIconMenu.addAction(self.restoreAction)
         self.trayIconMenu.addSeparator() #间隔线
         self.trayIconMenu.addAction(self.quitAction)
         self.trayIcon.setContextMenu(self.trayIconMenu) #右击托盘 
     def closeEvent(self, event):
         if self.trayIcon.isVisible():
              self.hide()
              event.ignore()
     def trayClick(self,reason):
         if reason==QSystemTrayIcon.Trigger:
             if(self.flag):
                 self.showNormal()
             else:
                 self.hide()
             self.flag = ~ self.flag
              
         elif reason==QSystemTrayIcon.MiddleClick: #中击
              self.showMessage()
         else:
              pass
     def showMessage(self):
        icon=QSystemTrayIcon.Information
        self.trayIcon.showMessage(u"提示信息",u"点我干嘛？",icon)
if __name__ == '__main__':
     import sys
     app = QApplication(sys.argv)
     frm = Window()
     frm.show()
     sys.exit(app.exec_())

