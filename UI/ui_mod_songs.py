# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mod_songsXXSMsR.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFormLayout,
    QGridLayout, QGroupBox, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_ModSongs(object):
    def setupUi(self, ModSongs):
        if not ModSongs.objectName():
            ModSongs.setObjectName(u"ModSongs")
        ModSongs.resize(582, 486)
        self.gridLayout = QGridLayout(ModSongs)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_6 = QLabel(ModSongs)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)

        self.lineEdit_6 = QLineEdit(ModSongs)
        self.lineEdit_6.setObjectName(u"lineEdit_6")

        self.gridLayout.addWidget(self.lineEdit_6, 5, 2, 1, 1)

        self.groupBox_2 = QGroupBox(ModSongs)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.gridLayout_2 = QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_7 = QLabel(self.groupBox_2)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 0, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.groupBox_2)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout_2.addWidget(self.pushButton_5, 7, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.groupBox_2)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout_2.addWidget(self.pushButton_6, 8, 0, 1, 1)

        self.checkBox_3 = QCheckBox(self.groupBox_2)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.gridLayout_2.addWidget(self.checkBox_3, 6, 0, 1, 1)

        self.label_8 = QLabel(self.groupBox_2)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout_2.addWidget(self.label_8, 2, 0, 1, 1)

        self.listWidget = QListWidget(self.groupBox_2)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")

        self.gridLayout_2.addWidget(self.listWidget, 0, 1, 9, 1)

        self.comboBox = QComboBox(self.groupBox_2)
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout_2.addWidget(self.comboBox, 1, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.groupBox_2)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_2.addWidget(self.lineEdit_7, 3, 0, 1, 1)


        self.gridLayout.addWidget(self.groupBox_2, 7, 1, 1, 2)

        self.pushButton_4 = QPushButton(ModSongs)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 4, 0, 1, 1)

        self.label = QLabel(ModSongs)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.label_2 = QLabel(ModSongs)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)

        self.pushButton_3 = QPushButton(ModSongs)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 5, 0, 1, 1)

        self.label_3 = QLabel(ModSongs)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)

        self.checkBox = QCheckBox(ModSongs)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 6, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(ModSongs)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout.addWidget(self.lineEdit_3, 2, 2, 1, 1)

        self.checkBox_2 = QCheckBox(ModSongs)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.gridLayout.addWidget(self.checkBox_2, 6, 2, 1, 1)

        self.groupBox = QGroupBox(ModSongs)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_9 = QLabel(self.groupBox)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout.addWidget(self.label_9)

        self.comboBox_2 = QComboBox(self.groupBox)
        self.comboBox_2.setObjectName(u"comboBox_2")

        self.verticalLayout.addWidget(self.comboBox_2)

        self.label_10 = QLabel(self.groupBox)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.lineEdit_8 = QLineEdit(self.groupBox)
        self.lineEdit_8.setObjectName(u"lineEdit_8")

        self.verticalLayout.addWidget(self.lineEdit_8)

        self.pushButton_7 = QPushButton(self.groupBox)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.groupBox)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.listWidget_2 = QListWidget(self.groupBox)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.verticalLayout.addWidget(self.listWidget_2)


        self.gridLayout.addWidget(self.groupBox, 7, 0, 1, 1)

        self.lineEdit_5 = QLineEdit(ModSongs)
        self.lineEdit_5.setObjectName(u"lineEdit_5")

        self.gridLayout.addWidget(self.lineEdit_5, 4, 2, 1, 1)

        self.lineEdit_4 = QLineEdit(ModSongs)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.gridLayout.addWidget(self.lineEdit_4, 3, 2, 1, 1)

        self.lineEdit = QLineEdit(ModSongs)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 0, 2, 1, 1)

        self.label_4 = QLabel(ModSongs)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(ModSongs)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout.addWidget(self.lineEdit_2, 1, 2, 1, 1)

        self.groupBox_3 = QGroupBox(ModSongs)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.formLayout = QFormLayout(self.groupBox_3)
        self.formLayout.setObjectName(u"formLayout")
        self.pushButton_2 = QPushButton(self.groupBox_3)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.pushButton_2)

        self.pushButton = QPushButton(self.groupBox_3)
        self.pushButton.setObjectName(u"pushButton")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.pushButton)

        self.checkBox_4 = QCheckBox(self.groupBox_3)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.checkBox_4)


        self.gridLayout.addWidget(self.groupBox_3, 0, 0, 4, 1)

        self.label_5 = QLabel(ModSongs)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)


        self.retranslateUi(ModSongs)

        QMetaObject.connectSlotsByName(ModSongs)
    # setupUi

    def retranslateUi(self, ModSongs):
        ModSongs.setWindowTitle(QCoreApplication.translate("ModSongs", u"Songs / Chart Tool", None))
        self.label_6.setText(QCoreApplication.translate("ModSongs", u"Girlfriend:", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("ModSongs", u"NoteTypes Translation Settings", None))
        self.label_7.setText(QCoreApplication.translate("ModSongs", u"Notetype:", None))
        self.pushButton_5.setText(QCoreApplication.translate("ModSongs", u"Add Note Config", None))
        self.pushButton_6.setText(QCoreApplication.translate("ModSongs", u"Remove Note Config", None))
        self.checkBox_3.setText(QCoreApplication.translate("ModSongs", u"Remove it", None))
        self.label_8.setText(QCoreApplication.translate("ModSongs", u"Rename to:", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("ModSongs", u"Default / Rename To \"customNameLOL\" / Remove it", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton_4.setText(QCoreApplication.translate("ModSongs", u"Export as .FNFC", None))
        self.label.setText(QCoreApplication.translate("ModSongs", u"Internal Name:", None))
        self.label_2.setText(QCoreApplication.translate("ModSongs", u"Visible Name:", None))
        self.pushButton_3.setText(QCoreApplication.translate("ModSongs", u"Add Song", None))
        self.label_3.setText(QCoreApplication.translate("ModSongs", u"Stage:", None))
        self.checkBox.setText(QCoreApplication.translate("ModSongs", u"Translate Events", None))
        self.checkBox_2.setText(QCoreApplication.translate("ModSongs", u"Translate NoteTypes", None))
        self.groupBox.setTitle(QCoreApplication.translate("ModSongs", u"Events Translation Settings", None))
        self.label_9.setText(QCoreApplication.translate("ModSongs", u"Event Name:", None))
        self.label_10.setText(QCoreApplication.translate("ModSongs", u"Rename To:", None))
        self.pushButton_7.setText(QCoreApplication.translate("ModSongs", u"Add Event Config", None))
        self.pushButton_8.setText(QCoreApplication.translate("ModSongs", u"Remove Event Config", None))
        self.label_4.setText(QCoreApplication.translate("ModSongs", u"Player:", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("ModSongs", u"Importation Settings", None))
        self.pushButton_2.setText(QCoreApplication.translate("ModSongs", u"Import from local Files (Not added yet)", None))
        self.pushButton.setText(QCoreApplication.translate("ModSongs", u"Import from Mod", None))
#if QT_CONFIG(whatsthis)
        self.checkBox_4.setWhatsThis(QCoreApplication.translate("ModSongs", u"<html><head/><body><p>If true change the name to a managable format for the tool to make the event compatible with the rest of engines</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.checkBox_4.setText(QCoreApplication.translate("ModSongs", u"Rename Default Events", None))
        self.label_5.setText(QCoreApplication.translate("ModSongs", u"Opponent:", None))
    # retranslateUi

