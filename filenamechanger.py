import os
from os import listdir

# Config
path = 'C:\\Users\\yonie\\Music'

#############################################################################################
#############################################################################################
#############################################################################################
#############################################################################################

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

            # Quitar estas palabras
            wordsToQuit =  [
                'ytmp3free.cc_',
                '-youtubemp3free.org',
                '-video',
                '-official',
                '-oficial',
                '-music',
                '-version-original',
                '-audio'
            ]
            for word in wordsToQuit:
                self.tmpName = self.tmpName.replace(word, '')
            
            # Reemplazar guiones por espacios
            self.tmpName = self.tmpName.replace('-', ' ')

            self.saveNewFilename()

    def saveNewFilename(self):
        fullpath1 = path + '\\' + self.originalName
        fullpath2 = path + '\\' + self.tmpName
        os.rename(fullpath1, fullpath2)

# Por cada archivo de la lista crear un objeto SongFile y cambiar su nombre
filesNameList = listdir(path)
for fileName in filesNameList:
    file = SongFile(fileName)
    file.changeName()