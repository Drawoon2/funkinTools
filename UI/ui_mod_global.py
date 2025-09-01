# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mod_globalqpTnCo.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_ModGlobal(object):
    def setupUi(self, ModGlobal):
        if not ModGlobal.objectName():
            ModGlobal.setObjectName(u"ModGlobal")
        ModGlobal.resize(433, 228)
        self.gridLayout = QGridLayout(ModGlobal)
        self.gridLayout.setObjectName(u"gridLayout")
        self.desc_input = QLineEdit(ModGlobal)
        self.desc_input.setObjectName(u"desc_input")

        self.gridLayout.addWidget(self.desc_input, 2, 1, 1, 2)

        self.version_input = QLineEdit(ModGlobal)
        self.version_input.setObjectName(u"version_input")

        self.gridLayout.addWidget(self.version_input, 3, 1, 1, 2)

        self.desc_label = QLabel(ModGlobal)
        self.desc_label.setObjectName(u"desc_label")

        self.gridLayout.addWidget(self.desc_label, 2, 0, 1, 1)

        self.name_input = QLineEdit(ModGlobal)
        self.name_input.setObjectName(u"name_input")

        self.gridLayout.addWidget(self.name_input, 0, 1, 1, 2)

        self.api_label = QLabel(ModGlobal)
        self.api_label.setObjectName(u"api_label")

        self.gridLayout.addWidget(self.api_label, 4, 0, 1, 1)

        self.save_button = QPushButton(ModGlobal)
        self.save_button.setObjectName(u"save_button")

        self.gridLayout.addWidget(self.save_button, 6, 0, 1, 1)

        self.version_label = QLabel(ModGlobal)
        self.version_label.setObjectName(u"version_label")

        self.gridLayout.addWidget(self.version_label, 3, 0, 1, 1)

        self.icon_label = QLabel(ModGlobal)
        self.icon_label.setObjectName(u"icon_label")

        self.gridLayout.addWidget(self.icon_label, 0, 3, 1, 1)

        self.discord_input = QLineEdit(ModGlobal)
        self.discord_input.setObjectName(u"discord_input")

        self.gridLayout.addWidget(self.discord_input, 5, 1, 1, 2)

        self.api_input = QLineEdit(ModGlobal)
        self.api_input.setObjectName(u"api_input")

        self.gridLayout.addWidget(self.api_input, 4, 1, 1, 2)

        self.name_label = QLabel(ModGlobal)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout.addWidget(self.name_label, 0, 0, 1, 1)

        self.discord_label = QLabel(ModGlobal)
        self.discord_label.setObjectName(u"discord_label")

        self.gridLayout.addWidget(self.discord_label, 5, 0, 1, 1)

        self.selecticon_button = QPushButton(ModGlobal)
        self.selecticon_button.setObjectName(u"selecticon_button")

        self.gridLayout.addWidget(self.selecticon_button, 0, 4, 1, 1)

        self.icon_preview = QLabel(ModGlobal)
        self.icon_preview.setObjectName(u"icon_preview")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.icon_preview.sizePolicy().hasHeightForWidth())
        self.icon_preview.setSizePolicy(sizePolicy)
        self.icon_preview.setPixmap(QPixmap(u"../assets/defaultIcon.png"))
        self.icon_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.icon_preview, 2, 3, 4, 2)

        self.clear_button = QPushButton(ModGlobal)
        self.clear_button.setObjectName(u"clear_button")

        self.gridLayout.addWidget(self.clear_button, 6, 1, 1, 1)


        self.retranslateUi(ModGlobal)

        QMetaObject.connectSlotsByName(ModGlobal)
    # setupUi

    def retranslateUi(self, ModGlobal):
        ModGlobal.setWindowTitle(QCoreApplication.translate("ModGlobal", u"Global Settings", None))
        self.desc_label.setText(QCoreApplication.translate("ModGlobal", u"Description:", None))
        self.api_label.setText(QCoreApplication.translate("ModGlobal", u"Api Version:", None))
        self.save_button.setText(QCoreApplication.translate("ModGlobal", u"Save Changes", None))
        self.version_label.setText(QCoreApplication.translate("ModGlobal", u"Mod Version:", None))
        self.icon_label.setText(QCoreApplication.translate("ModGlobal", u"Current Icon:", None))
        self.name_label.setText(QCoreApplication.translate("ModGlobal", u"Mod Name:", None))
        self.discord_label.setText(QCoreApplication.translate("ModGlobal", u"Discord RPC ID:", None))
        self.selecticon_button.setText(QCoreApplication.translate("ModGlobal", u"Set other Icon", None))
        self.icon_preview.setText("")
        self.clear_button.setText(QCoreApplication.translate("ModGlobal", u"Clear Changes", None))
    # retranslateUi

