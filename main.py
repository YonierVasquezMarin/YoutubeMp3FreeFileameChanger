import os
from os import listdir

# Config
path = 'C:\\Users\\yonie\\Music'

#############################################################################################
#############################################################################################
#############################################################################################

# Variables
songFiles = []

# Clase para cada archivo
class SongFile:
    tmpName: str
    originalName: str

    def __init__(self, name: str):
        self.tmpName = name
        self.originalName = name

    def _isMp3(self):
        return self.tmpName.endswith('.mp3')

    def changeName(self):
        if self._isMp3():
            self.tmpName = self.tmpName.replace('ytmp3free.cc_', '')
            self.tmpName = self.tmpName.replace('-youtubemp3free.org', '')
            self.tmpName = self.tmpName.replace('-video', '')
            self.tmpName = self.tmpName.replace('-official', '')
            self.tmpName = self.tmpName.replace('-oficial', '')
            self.tmpName = self.tmpName.replace('-music', '')
            self.tmpName = self.tmpName.replace('-', ' ')
            self.saveNewFilename()

    def saveNewFilename(self):
        fullpath1 = path + '\\' + self.originalName
        fullpath2 = path + '\\' + self.tmpName
        os.rename(fullpath1, fullpath2)

# Por cada archivo de la lista crear un objeto SongFile y agregarlo a una lista
filesNameList = listdir(path)
for fileName in filesNameList:
    songFiles.append(SongFile(fileName))

# Cambiar el nombre de cada archivo de audio de la lista
for songFile in songFiles:
    songFile.changeName()