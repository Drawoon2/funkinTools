# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dialog_import_song_modhEPoLW.ui'
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
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_songImportMod(object):
    def setupUi(self, songImportMod):
        if not songImportMod.objectName():
            songImportMod.setObjectName(u"songImportMod")
        songImportMod.resize(357, 149)
        self.formLayout = QFormLayout(songImportMod)
        self.formLayout.setObjectName(u"formLayout")
        self.modfolder_label = QLabel(songImportMod)
        self.modfolder_label.setObjectName(u"modfolder_label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.modfolder_label)

        self.select_button = QPushButton(songImportMod)
        self.select_button.setObjectName(u"select_button")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.select_button)

        self.song_label = QLabel(songImportMod)
        self.song_label.setObjectName(u"song_label")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.song_label)

        self.song_combobox = QComboBox(songImportMod)
        self.song_combobox.setObjectName(u"song_combobox")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.song_combobox)

        self.import_button = QPushButton(songImportMod)
        self.import_button.setObjectName(u"import_button")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.SpanningRole, self.import_button)

        self.engine_label = QLabel(songImportMod)
        self.engine_label.setObjectName(u"engine_label")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.engine_label)

        self.showengine_label = QLabel(songImportMod)
        self.showengine_label.setObjectName(u"showengine_label")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.showengine_label)

        self.path_label = QLabel(songImportMod)
        self.path_label.setObjectName(u"path_label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.path_label)

        self.showpath_label = QLabel(songImportMod)
        self.showpath_label.setObjectName(u"showpath_label")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.showpath_label)


        self.retranslateUi(songImportMod)

        QMetaObject.connectSlotsByName(songImportMod)
    # setupUi

    def retranslateUi(self, songImportMod):
        songImportMod.setWindowTitle(QCoreApplication.translate("songImportMod", u"Song Importer", None))
        self.modfolder_label.setText(QCoreApplication.translate("songImportMod", u"Mod Folder:", None))
        self.select_button.setText(QCoreApplication.translate("songImportMod", u"Select Mod Folder", None))
        self.song_label.setText(QCoreApplication.translate("songImportMod", u"Song:", None))
        self.import_button.setText(QCoreApplication.translate("songImportMod", u"Import", None))
        self.engine_label.setText(QCoreApplication.translate("songImportMod", u"Mod Folder Engine: ", None))
        self.showengine_label.setText(QCoreApplication.translate("songImportMod", u"PSYCH", None))
        self.path_label.setText(QCoreApplication.translate("songImportMod", u"Mod Folder Path: ", None))
        self.showpath_label.setText(QCoreApplication.translate("songImportMod", u"/to/the/modFolder", None))
    # retranslateUi

