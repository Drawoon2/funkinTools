from PySide6.QtWidgets import QWidget, QFileDialog
from PySide6.QtCore import QDir
from Funkin import Song, SongHandlers
from Constants import Character, Engine, SearchFormat

from Funkin.ModFolder import VsliceMod, PsychMod, CodenameMod
import UI, Dialogs, Manager, Paths

class ModSong(QWidget):
    def __init__(self, parent:QWidget = None):
        super().__init__(parent)
        self.ui = UI.Ui_ModSongs()
        self.ui.setupUi(self)
        self.song:Song = None
        self.curDiff:str = None
        self.noteSettings:dict[str, dict] = {}
        self.eventSettings:dict[str, str] = {}
        
        self.ui.renamedefault_check.setChecked(True)
        self.ui.open_button.pressed.connect(lambda: self.importFromMod(True))
        self.ui.import_button.pressed.connect(self.importFromMod)

        self.ui.diff_combobox.currentTextChanged.connect(self.updateDiff)
        self.ui.addsong_button.pressed.connect(self.addSong)
        self.ui.exportfnfc_button.pressed.connect(self.exportFNFC)

        self.ui.note_addconfig_button.pressed.connect(self.addNoteConfig)
        self.ui.note_removeconfig_button.pressed.connect(self.removeNoteConfig)
        self.ui.note_name_combobox.currentTextChanged.connect(self.updateNoteConfig)

        self.ui.event_name_combobox.currentTextChanged.connect(self.updateEvent)
        self.ui.event_add_button.pressed.connect(self.addEventConfig)
        self.ui.event_remove_button.pressed.connect(self.removeEventConfig)

        self.ui.translateevents_check.toggled.connect(self.toggleEventConfig)
        self.toggleEventConfig(self.ui.translateevents_check.isChecked())

        self.ui.translatenotes_check.toggled.connect(self.toggleNoteConfig)
        self.toggleNoteConfig(self.ui.translatenotes_check.isChecked())

        Manager.instance.onModFolderUpdate.connect(self.updateModFolder)

        self.updateModFolder()
        self.updateSongUI()

    def updateSongUI(self):
        disabled = self.song is None
        #Global
        self.ui.internalname_label.setDisabled(disabled)
        self.ui.internalname_input.setDisabled(disabled)
        self.ui.diff_label.setDisabled(disabled)
        self.ui.diff_combobox.setDisabled(disabled)
        self.ui.variants_label.setDisabled(disabled)
        self.ui.variant_input.setDisabled(disabled)
        self.ui.isvariant_check.setDisabled(disabled)
        self.ui.name_label.setDisabled(disabled)
        self.ui.name_input.setDisabled(disabled)
        self.ui.stage_label.setDisabled(disabled)
        self.ui.stage_input.setDisabled(disabled)
        self.ui.player_label.setDisabled(disabled)
        self.ui.player_input.setDisabled(disabled)
        self.ui.gf_label.setDisabled(disabled)
        self.ui.gf_input.setDisabled(disabled)
        self.ui.opponent_label.setDisabled(disabled)
        self.ui.opponent_input.setDisabled(disabled)

        self.ui.exportfnfc_button.setDisabled(disabled)
        #Events Notes
        self.ui.translateevents_check.setDisabled(disabled)
        self.ui.translatenotes_check.setDisabled(disabled)
        if disabled:
            self.toggleNoteConfig(not disabled)
            self.toggleEventConfig(not disabled)
        else:
            self.toggleNoteConfig(self.ui.translateevents_check.isChecked())
            self.toggleEventConfig(self.ui.translateevents_check.isChecked())
        
        self.updateModFolder()
    def updateModFolder(self):
        mod = Manager.instance.modFolder
        disabled = mod is None
        self.ui.open_button.setDisabled(disabled)
        if self.song is None:
            disabled = True
        self.ui.addsong_button.setDisabled(disabled)
        
    def importFromMod(self, fromManager:bool = False):
        dialog = Dialogs.ImportSongMod(fromManager, self)
        dialog.renameDefault = self.ui.renamedefault_check.isChecked()
        result = dialog.exec()
        if result == 1:
            self.setSong(dialog.song)

    def toggleNoteConfig(self, value):
        self.ui.notetypes_group.setDisabled(not value)
    def toggleEventConfig(self, value):
        self.ui.events_group.setDisabled(not value)
    def updateNoteConfig(self, noteType = None):
        noteConfig = self.noteSettings.get(noteType, {})
        self.ui.note_rename_input.setText(noteConfig.get("newName", noteType))
        self.ui.note_remove_check.setChecked(noteConfig.get("removeIt", False))

    def updateNotetypeList(self):
        self.ui.note_settings_list.clear()
        for noteType, data in self.noteSettings.items():
            text = noteType
            if data.get("newName") is not None:
                text += f" / Rename to \"{data.get("newName")}\""
            if data.get("removeIt", False):
                text += f" / Remove it"
            self.ui.note_settings_list.addItem(text)
    def addNoteConfig(self):
        noteType = self.ui.note_name_combobox.currentText()
        rename = self.ui.note_rename_input.text()
        removeIt = self.ui.note_remove_check.isChecked()
        keepIt = False
        data = {}
        if rename != noteType:
            data["newName"] = rename
            keepIt = True

        if removeIt:
            data["removeIt"] = removeIt
            keepIt = True

        if keepIt:
            self.noteSettings[noteType] = data
            self.updateNotetypeList()
    def removeNoteConfig(self):
        noteType = self.ui.note_name_combobox.currentText()
        if self.noteSettings.get(noteType) is None:
            return
        self.noteSettings.pop(noteType)
        self.updateNotetypeList()
        self.updateNoteConfig(noteType)
    def addEventConfig(self):
        event = self.ui.event_name_combobox.currentText()
        newName = self.ui.event_rename_input.text()
        if newName != event:
            self.eventSettings[event] = newName
        self.updateEventList()
    def removeEventConfig(self):
        event = self.ui.event_name_combobox.currentText()
        if self.eventSettings.get(event) is None:
            return
        self.eventSettings.pop(event)
        self.updateEventList()
        self.updateEvent(event)
    def updateEventList(self):
        self.ui.event_currentconfig_list.clear()
        for event, newName in self.eventSettings.items():
            text = f"{event} / Rename to \"{newName}\""
            self.ui.event_currentconfig_list.addItem(text)
    def updateEvent(self, event = None):
        self.ui.event_rename_input.setText(self.eventSettings.get(event, event))

    def setSong(self, song:Song):
        self.song = song
        self.updateSongUI()
        self.updateUI()
    def updateUI(self):
        self.noteSettings = {}
        self.eventSettings = {}
        self.ui.internalname_input.setText(self.song.internName)

        self.ui.diff_combobox.currentTextChanged.disconnect(self.updateDiff)
        self.ui.diff_combobox.clear()
        diffs = self.song.getDifficults()
        self.ui.diff_combobox.addItems(diffs)
        self.updateDiff(diffs[0], True)

        self.ui.diff_combobox.currentTextChanged.connect(self.updateDiff)

        self.ui.event_name_combobox.clear()
        self.ui.event_name_combobox.addItems(self.song.getEventsName())

        self.ui.note_name_combobox.clear()
        self.ui.note_name_combobox.addItems(self.song.getNotetypes())

    def updateDiff(self, diff = None, newSong:bool = False):
        print(f"{diff=}")
        if not newSong:
            self.updateChart()
        else:
            self.ui.diff_combobox.setCurrentText(diff)

        self.curDiff = diff
        chart = self.song.getChart(self.curDiff)
        if chart is None:
            print(f"updateDiff: diff {self.curDiff} not Found")
            return
        self.ui.stage_input.setText(chart.stage)
        self.ui.name_input.setText(chart.songName)

        self.ui.opponent_input.setText(chart.getLane(Character.DAD).character)
        self.ui.player_input.setText(chart.getLane(Character.BOYFRIEND).character)
        self.ui.gf_input.setText(chart.getLane(Character.GF).character)
        self.ui.isvariant_check.setChecked(chart.isVariant)
        self.ui.variant_input.setText(chart.variantTag or "")
    def updateChart(self):
        if self.curDiff is None or self.curDiff == "":
            return
        chart = self.song.getChart(self.curDiff)
        if chart is None:
            print(f"updateChart: diff {self.curDiff} not Found")
            return
        chart.stage = self.ui.stage_input.text()
        chart.songName = self.ui.name_input.text()

        chart.getLane(Character.DAD).character = self.ui.opponent_input.text()
        chart.getLane(Character.BOYFRIEND).character = self.ui.player_input.text()
        chart.getLane(Character.GF).character = self.ui.gf_input.text()
        chart.isVariant = self.ui.isvariant_check.isChecked()
        if chart.isVariant:
            chart.variantTag = self.ui.variant_input.text()
        else:
            chart.variantTag = None
    def applySongConfig(self):
        self.updateChart()
        toRemove = []
        toRenameNotetype = {}
        if self.ui.translatenotes_check.isChecked():
            for noteType, data in self.noteSettings.items():
                if data.get("newName") is not None:
                    toRenameNotetype[noteType] = data.get("newName")
                if data.get("removeIt", False):
                    toRemove.append(noteType)
        toRenameEvents = {}
        if self.ui.translateevents_check.isChecked():
            toRenameEvents = self.eventSettings
            
        for diff, chart in self.song.charts.items():
            chart.removeNoteTypes(toRemove)
            chart.renameNoteTypes(toRenameNotetype)
            chart.renameEvents(toRenameEvents)
    def addSong(self):
        self.applySongConfig()
        mod = Manager.instance.modFolder
        if mod.getEngine() == Engine.CODENAME:
            print("Isn't added yet")
            Dialogs.errorDialog(self, "Feature not Added", "Exportation to codename engine isn't added yet")
            return
        SongHandlers.exportSong(mod, self.song, self.song.getDifficults())
        Dialogs.informativeDialog(self, "Song Added!!", f"Song {self.song.internName} has be added in {mod.getModName()}")
    def exportFNFC(self):
        defaultName = Paths.join(QDir.currentPath(), f"{self.song.internName}.fnfc")
        path, filter = QFileDialog.getSaveFileName(self, "Save .fnfc", defaultName, SearchFormat.FNFC_FORMAT)

        if path == "":
            return
        self.applySongConfig()
        SongHandlers.exportFNFC(self.song, self.song.getDifficults(), path)
        Dialogs.informativeDialog(self, "Song Saved!!", f"Song \"{self.song.internName}\" has be saved in Path: {path}")
        