import json
import os
from utils.fileIO import Utils

class Config():
    def __init__(self) -> None:
        self.configFilePath = os.path.join(os.getcwd(), "src", "utils", "config.json")
        self.configFile = dict()
 
        self.ignoreme = list()
        self.allowedExt = list()
        pass

    def makeSelection(self):
        "See presented filepaths and chose extensions accordingly."

        if not self.configFile:
            self.getConfig()

        pass

    def getConfig(self):

        with open(self.configFilePath, 'r') as f:
            self.configFile = json.load(f)

        for lang, details in self.configFile['languages'].items():
            for iExt in details['ext']: self.allowedExt.append(iExt)
            for iIgn in details['ign']: self.ignoreme.append(iIgn)

        return self.configFile 

    def printConfig(self):
        
        if not self.configFile:
            self.getConfig()

        new_FIO = Utils()
        new_FIO.pathSelector()
        foundFiles = new_FIO.findFiles(tuple(self.allowedExt), self.ignoreme)

        print(foundFiles)

