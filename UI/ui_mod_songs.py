# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mod_songsZoYiTd.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QGridLayout,
    QGroupBox, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_ModSongs(object):
    def setupUi(self, ModSongs):
        if not ModSongs.objectName():
            ModSongs.setObjectName(u"ModSongs")
        ModSongs.resize(782, 579)
        self.gridLayout = QGridLayout(ModSongs)
        self.gridLayout.setObjectName(u"gridLayout")
        self.opponent_label = QLabel(ModSongs)
        self.opponent_label.setObjectName(u"opponent_label")

        self.gridLayout.addWidget(self.opponent_label, 7, 2, 1, 1)

        self.gf_label = QLabel(ModSongs)
        self.gf_label.setObjectName(u"gf_label")

        self.gridLayout.addWidget(self.gf_label, 8, 2, 1, 1)

        self.gf_input = QLineEdit(ModSongs)
        self.gf_input.setObjectName(u"gf_input")

        self.gridLayout.addWidget(self.gf_input, 8, 3, 1, 2)

        self.player_label = QLabel(ModSongs)
        self.player_label.setObjectName(u"player_label")

        self.gridLayout.addWidget(self.player_label, 6, 2, 1, 1)

        self.import_group = QGroupBox(ModSongs)
        self.import_group.setObjectName(u"import_group")
        self.gridLayout_3 = QGridLayout(self.import_group)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.importlocal_button = QPushButton(self.import_group)
        self.importlocal_button.setObjectName(u"importlocal_button")

        self.gridLayout_3.addWidget(self.importlocal_button, 0, 0, 1, 1)

        self.import_button = QPushButton(self.import_group)
        self.import_button.setObjectName(u"import_button")

        self.gridLayout_3.addWidget(self.import_button, 1, 0, 1, 1)

        self.renamedefault_check = QCheckBox(self.import_group)
        self.renamedefault_check.setObjectName(u"renamedefault_check")

        self.gridLayout_3.addWidget(self.renamedefault_check, 3, 0, 1, 1)

        self.open_button = QPushButton(self.import_group)
        self.open_button.setObjectName(u"open_button")

        self.gridLayout_3.addWidget(self.open_button, 2, 0, 1, 1)


        self.gridLayout.addWidget(self.import_group, 1, 0, 6, 2)

        self.notetypes_group = QGroupBox(ModSongs)
        self.notetypes_group.setObjectName(u"notetypes_group")
        self.gridLayout_2 = QGridLayout(self.notetypes_group)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.note_name_combobox = QComboBox(self.notetypes_group)
        self.note_name_combobox.setObjectName(u"note_name_combobox")

        self.gridLayout_2.addWidget(self.note_name_combobox, 1, 0, 1, 1)

        self.note_addconfig_button = QPushButton(self.notetypes_group)
        self.note_addconfig_button.setObjectName(u"note_addconfig_button")

        self.gridLayout_2.addWidget(self.note_addconfig_button, 7, 0, 1, 1)

        self.note_rename_label = QLabel(self.notetypes_group)
        self.note_rename_label.setObjectName(u"note_rename_label")

        self.gridLayout_2.addWidget(self.note_rename_label, 2, 0, 1, 1)

        self.note_rename_input = QLineEdit(self.notetypes_group)
        self.note_rename_input.setObjectName(u"note_rename_input")
        self.note_rename_input.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_2.addWidget(self.note_rename_input, 3, 0, 1, 1)

        self.note_removeconfig_button = QPushButton(self.notetypes_group)
        self.note_removeconfig_button.setObjectName(u"note_removeconfig_button")

        self.gridLayout_2.addWidget(self.note_removeconfig_button, 8, 0, 1, 1)

        self.note_name_label = QLabel(self.notetypes_group)
        self.note_name_label.setObjectName(u"note_name_label")

        self.gridLayout_2.addWidget(self.note_name_label, 0, 0, 1, 1)

        self.note_settings_list = QListWidget(self.notetypes_group)
        QListWidgetItem(self.note_settings_list)
        self.note_settings_list.setObjectName(u"note_settings_list")

        self.gridLayout_2.addWidget(self.note_settings_list, 0, 1, 9, 1)

        self.note_remove_check = QCheckBox(self.notetypes_group)
        self.note_remove_check.setObjectName(u"note_remove_check")

        self.gridLayout_2.addWidget(self.note_remove_check, 6, 0, 1, 1)


        self.gridLayout.addWidget(self.notetypes_group, 10, 2, 1, 3)

        self.opponent_input = QLineEdit(ModSongs)
        self.opponent_input.setObjectName(u"opponent_input")

        self.gridLayout.addWidget(self.opponent_input, 7, 3, 1, 2)

        self.name_input = QLineEdit(ModSongs)
        self.name_input.setObjectName(u"name_input")

        self.gridLayout.addWidget(self.name_input, 4, 3, 1, 2)

        self.exportfnfc_button = QPushButton(ModSongs)
        self.exportfnfc_button.setObjectName(u"exportfnfc_button")

        self.gridLayout.addWidget(self.exportfnfc_button, 8, 0, 1, 1)

        self.translatenotes_check = QCheckBox(ModSongs)
        self.translatenotes_check.setObjectName(u"translatenotes_check")

        self.gridLayout.addWidget(self.translatenotes_check, 7, 1, 1, 1)

        self.addsong_button = QPushButton(ModSongs)
        self.addsong_button.setObjectName(u"addsong_button")

        self.gridLayout.addWidget(self.addsong_button, 7, 0, 1, 1)

        self.name_label = QLabel(ModSongs)
        self.name_label.setObjectName(u"name_label")

        self.gridLayout.addWidget(self.name_label, 4, 2, 1, 1)

        self.translateevents_check = QCheckBox(ModSongs)
        self.translateevents_check.setObjectName(u"translateevents_check")

        self.gridLayout.addWidget(self.translateevents_check, 8, 1, 1, 1)

        self.variant_input = QLineEdit(ModSongs)
        self.variant_input.setObjectName(u"variant_input")

        self.gridLayout.addWidget(self.variant_input, 3, 4, 1, 1)

        self.variants_label = QLabel(ModSongs)
        self.variants_label.setObjectName(u"variants_label")

        self.gridLayout.addWidget(self.variants_label, 3, 3, 1, 1)

        self.isvariant_check = QCheckBox(ModSongs)
        self.isvariant_check.setObjectName(u"isvariant_check")

        self.gridLayout.addWidget(self.isvariant_check, 3, 2, 1, 1)

        self.diff_label = QLabel(ModSongs)
        self.diff_label.setObjectName(u"diff_label")

        self.gridLayout.addWidget(self.diff_label, 2, 2, 1, 1)

        self.internalname_input = QLineEdit(ModSongs)
        self.internalname_input.setObjectName(u"internalname_input")

        self.gridLayout.addWidget(self.internalname_input, 1, 3, 1, 2)

        self.player_input = QLineEdit(ModSongs)
        self.player_input.setObjectName(u"player_input")

        self.gridLayout.addWidget(self.player_input, 6, 3, 1, 2)

        self.stage_input = QLineEdit(ModSongs)
        self.stage_input.setObjectName(u"stage_input")

        self.gridLayout.addWidget(self.stage_input, 5, 3, 1, 2)

        self.events_group = QGroupBox(ModSongs)
        self.events_group.setObjectName(u"events_group")
        self.verticalLayout = QVBoxLayout(self.events_group)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.event_name_label = QLabel(self.events_group)
        self.event_name_label.setObjectName(u"event_name_label")

        self.verticalLayout.addWidget(self.event_name_label)

        self.event_name_combobox = QComboBox(self.events_group)
        self.event_name_combobox.setObjectName(u"event_name_combobox")

        self.verticalLayout.addWidget(self.event_name_combobox)

        self.event_rename_label = QLabel(self.events_group)
        self.event_rename_label.setObjectName(u"event_rename_label")

        self.verticalLayout.addWidget(self.event_rename_label)

        self.event_rename_input = QLineEdit(self.events_group)
        self.event_rename_input.setObjectName(u"event_rename_input")

        self.verticalLayout.addWidget(self.event_rename_input)

        self.event_add_button = QPushButton(self.events_group)
        self.event_add_button.setObjectName(u"event_add_button")

        self.verticalLayout.addWidget(self.event_add_button)

        self.event_remove_button = QPushButton(self.events_group)
        self.event_remove_button.setObjectName(u"event_remove_button")

        self.verticalLayout.addWidget(self.event_remove_button)

        self.event_currentconfig_list = QListWidget(self.events_group)
        self.event_currentconfig_list.setObjectName(u"event_currentconfig_list")

        self.verticalLayout.addWidget(self.event_currentconfig_list)


        self.gridLayout.addWidget(self.events_group, 10, 0, 1, 2)

        self.internalname_label = QLabel(ModSongs)
        self.internalname_label.setObjectName(u"internalname_label")

        self.gridLayout.addWidget(self.internalname_label, 1, 2, 1, 1)

        self.diff_combobox = QComboBox(ModSongs)
        self.diff_combobox.setObjectName(u"diff_combobox")

        self.gridLayout.addWidget(self.diff_combobox, 2, 3, 1, 2)

        self.stage_label = QLabel(ModSongs)
        self.stage_label.setObjectName(u"stage_label")

        self.gridLayout.addWidget(self.stage_label, 5, 2, 1, 1)

#if QT_CONFIG(shortcut)
        self.opponent_label.setBuddy(self.opponent_input)
        self.gf_label.setBuddy(self.gf_input)
        self.player_label.setBuddy(self.player_input)
        self.note_rename_label.setBuddy(self.note_rename_input)
        self.note_name_label.setBuddy(self.note_name_combobox)
        self.name_label.setBuddy(self.name_input)
        self.variants_label.setBuddy(self.variant_input)
        self.diff_label.setBuddy(self.diff_combobox)
        self.event_name_label.setBuddy(self.event_name_combobox)
        self.event_rename_label.setBuddy(self.event_rename_input)
        self.internalname_label.setBuddy(self.internalname_input)
        self.stage_label.setBuddy(self.stage_input)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(ModSongs)

        QMetaObject.connectSlotsByName(ModSongs)
    # setupUi

    def retranslateUi(self, ModSongs):
        ModSongs.setWindowTitle(QCoreApplication.translate("ModSongs", u"Songs / Chart Tool", None))
        self.opponent_label.setText(QCoreApplication.translate("ModSongs", u"Opponent:", None))
        self.gf_label.setText(QCoreApplication.translate("ModSongs", u"Girlfriend:", None))
        self.player_label.setText(QCoreApplication.translate("ModSongs", u"Player:", None))
        self.import_group.setTitle(QCoreApplication.translate("ModSongs", u"Importation Settings", None))
        self.importlocal_button.setText(QCoreApplication.translate("ModSongs", u"Import from local Files (Not added yet)", None))
        self.import_button.setText(QCoreApplication.translate("ModSongs", u"Import from Mod", None))
#if QT_CONFIG(whatsthis)
        self.renamedefault_check.setWhatsThis(QCoreApplication.translate("ModSongs", u"<html><head/><body><p>If true change the name to a managable format for the tool to try to make the event compatible with the rest of engines</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.renamedefault_check.setText(QCoreApplication.translate("ModSongs", u"Rename Default Events", None))
        self.open_button.setText(QCoreApplication.translate("ModSongs", u"Open Song", None))
        self.notetypes_group.setTitle(QCoreApplication.translate("ModSongs", u"NoteTypes Translation Settings", None))
        self.note_addconfig_button.setText(QCoreApplication.translate("ModSongs", u"Add Note Config", None))
        self.note_rename_label.setText(QCoreApplication.translate("ModSongs", u"Rename to:", None))
        self.note_removeconfig_button.setText(QCoreApplication.translate("ModSongs", u"Remove Note Config", None))
        self.note_name_label.setText(QCoreApplication.translate("ModSongs", u"Notetype:", None))

        __sortingEnabled = self.note_settings_list.isSortingEnabled()
        self.note_settings_list.setSortingEnabled(False)
        ___qlistwidgetitem = self.note_settings_list.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("ModSongs", u"Default / Rename To \"customNameLOL\" / Remove it", None));
        self.note_settings_list.setSortingEnabled(__sortingEnabled)

        self.note_remove_check.setText(QCoreApplication.translate("ModSongs", u"Remove it", None))
        self.exportfnfc_button.setText(QCoreApplication.translate("ModSongs", u"Export as .FNFC", None))
        self.translatenotes_check.setText(QCoreApplication.translate("ModSongs", u"Translate NoteTypes", None))
        self.addsong_button.setText(QCoreApplication.translate("ModSongs", u"Add Song", None))
        self.name_label.setText(QCoreApplication.translate("ModSongs", u"Visible Name:", None))
        self.translateevents_check.setText(QCoreApplication.translate("ModSongs", u"Translate Events", None))
#if QT_CONFIG(whatsthis)
        self.variants_label.setWhatsThis(QCoreApplication.translate("ModSongs", u"<html><head/><body><p>This more for Vslice</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.variants_label.setText(QCoreApplication.translate("ModSongs", u"Variant Tag: ", None))
#if QT_CONFIG(whatsthis)
        self.isvariant_check.setWhatsThis(QCoreApplication.translate("ModSongs", u"<html><head/><body><p>If CHECKED</p><p>-In vslice will have separate his data  (Something like the erect variants)</p><p>-In Codename will have separate voices files</p><p>-In Psych will separate the chart in other folder</p></body></html>", None))
#endif // QT_CONFIG(whatsthis)
        self.isvariant_check.setText(QCoreApplication.translate("ModSongs", u"Is a Variant", None))
        self.diff_label.setText(QCoreApplication.translate("ModSongs", u"Difficult Selected: ", None))
        self.events_group.setTitle(QCoreApplication.translate("ModSongs", u"Events Translation Settings", None))
        self.event_name_label.setText(QCoreApplication.translate("ModSongs", u"Event Name:", None))
        self.event_rename_label.setText(QCoreApplication.translate("ModSongs", u"Rename To:", None))
        self.event_add_button.setText(QCoreApplication.translate("ModSongs", u"Add Event Config", None))
        self.event_remove_button.setText(QCoreApplication.translate("ModSongs", u"Remove Event Config", None))
        self.internalname_label.setText(QCoreApplication.translate("ModSongs", u"Internal Name:", None))
        self.stage_label.setText(QCoreApplication.translate("ModSongs", u"Stage:", None))
    # retranslateUi

