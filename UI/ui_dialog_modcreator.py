# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_modcreatorYTYfDU.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Dialog_ModFolderCreator(object):
    def setupUi(self, Dialog_ModFolderCreator):
        if not Dialog_ModFolderCreator.objectName():
            Dialog_ModFolderCreator.setObjectName(u"Dialog_ModFolderCreator")
        Dialog_ModFolderCreator.setWindowModality(Qt.WindowModality.NonModal)
        Dialog_ModFolderCreator.resize(386, 228)
        self.formLayout_2 = QFormLayout(Dialog_ModFolderCreator)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setRowWrapPolicy(QFormLayout.RowWrapPolicy.WrapAllRows)
        self.engine_label = QLabel(Dialog_ModFolderCreator)
        self.engine_label.setObjectName(u"engine_label")

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.LabelRole, self.engine_label)

        self.comboBox = QComboBox(Dialog_ModFolderCreator)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setEditable(False)

        self.formLayout_2.setWidget(1, QFormLayout.ItemRole.FieldRole, self.comboBox)

        self.engineFolder_label = QLabel(Dialog_ModFolderCreator)
        self.engineFolder_label.setObjectName(u"engineFolder_label")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.LabelRole, self.engineFolder_label)

        self.enginefolder_button = QPushButton(Dialog_ModFolderCreator)
        self.enginefolder_button.setObjectName(u"enginefolder_button")

        self.formLayout_2.setWidget(2, QFormLayout.ItemRole.FieldRole, self.enginefolder_button)

        self.engineFolderPath_label = QLabel(Dialog_ModFolderCreator)
        self.engineFolderPath_label.setObjectName(u"engineFolderPath_label")

        self.formLayout_2.setWidget(3, QFormLayout.ItemRole.SpanningRole, self.engineFolderPath_label)

        self.name_label = QLabel(Dialog_ModFolderCreator)
        self.name_label.setObjectName(u"name_label")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.LabelRole, self.name_label)

        self.name_line_edit = QLineEdit(Dialog_ModFolderCreator)
        self.name_line_edit.setObjectName(u"name_line_edit")

        self.formLayout_2.setWidget(4, QFormLayout.ItemRole.FieldRole, self.name_line_edit)

        self.create_button = QPushButton(Dialog_ModFolderCreator)
        self.create_button.setObjectName(u"create_button")

        self.formLayout_2.setWidget(5, QFormLayout.ItemRole.SpanningRole, self.create_button)


        self.retranslateUi(Dialog_ModFolderCreator)

        self.comboBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog_ModFolderCreator)
    # setupUi

    def retranslateUi(self, Dialog_ModFolderCreator):
        Dialog_ModFolderCreator.setWindowTitle(QCoreApplication.translate("Dialog_ModFolderCreator", u"ModFolderCreator", None))
        self.engine_label.setText(QCoreApplication.translate("Dialog_ModFolderCreator", u"Engine:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog_ModFolderCreator", u"PSYCH", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog_ModFolderCreator", u"CODENAME", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog_ModFolderCreator", u"VSLICE", None))

        self.engineFolder_label.setText(QCoreApplication.translate("Dialog_ModFolderCreator", u"EngineFolder: ", None))
        self.enginefolder_button.setText(QCoreApplication.translate("Dialog_ModFolderCreator", u"Search Engine Folder", None))
        self.engineFolderPath_label.setText(QCoreApplication.translate("Dialog_ModFolderCreator", u"D://", None))
        self.name_label.setText(QCoreApplication.translate("Dialog_ModFolderCreator", u"Mod Name: ", None))
        self.name_line_edit.setText(QCoreApplication.translate("Dialog_ModFolderCreator", u"Template", None))
        self.create_button.setText(QCoreApplication.translate("Dialog_ModFolderCreator", u"Create", None))
    # retranslateUi

