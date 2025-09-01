# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainDEEZcS.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QToolBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1020, 801)
        self.file_openMod = QAction(MainWindow)
        self.file_openMod.setObjectName(u"file_openMod")
        self.file_recentMod = QAction(MainWindow)
        self.file_recentMod.setObjectName(u"file_recentMod")
        self.file_newMod = QAction(MainWindow)
        self.file_newMod.setObjectName(u"file_newMod")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1020, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        MainWindow.setMenuBar(self.menubar)
        self.tool_bar = QToolBar(MainWindow)
        self.tool_bar.setObjectName(u"tool_bar")
        MainWindow.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.tool_bar)
        self.global_info = QStatusBar(MainWindow)
        self.global_info.setObjectName(u"global_info")
        MainWindow.setStatusBar(self.global_info)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menuFile.addAction(self.file_openMod)
        self.menuFile.addAction(self.file_recentMod)
        self.menuFile.addAction(self.file_newMod)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.file_openMod.setText(QCoreApplication.translate("MainWindow", u"Open a Mod Folder", None))
        self.file_recentMod.setText(QCoreApplication.translate("MainWindow", u"Recents Mods", None))
        self.file_newMod.setText(QCoreApplication.translate("MainWindow", u"New Mod Folder", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.tool_bar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

