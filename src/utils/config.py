import re, glob, json, os
from utils.fileIO import FileIO

class Config():
    def __init__(self) -> None:
        self.configFilePath = os.path.join(os.getcwd(), "src", "utils", "config.json")
        self.configFile = dict()
 
        self.languages = list()
        self.aliases = list()
        self.patterns = list()

        self.selected = list()

        self.ignoreme = list()
        self.allowedExt = list()

        self.foundFiles = list()

        pass

    def makeSelection(self) -> tuple:
        "See presented extensions and chose available extensions accordingly."

        if not self.configFile:
            self.getConfig()

        for i in self.foundFiles:
            ext_match = re.search(r"\.[^./]+$", i)
            if ext_match: self.selected.append(ext_match[0])

        return tuple(set(self.selected))

    def getConfig(self) -> dict:

        with open(self.configFilePath, 'r') as f:
            self.configFile = json.load(f)

        for lang, details in self.configFile['languages'].items():
            self.languages.append(lang)
            for iExt in details['ext']: self.allowedExt.append(iExt)
            for iIgn in details['ign']: self.ignoreme.append(iIgn)
            for iAlias in details['aliases']: self.aliases.append(iAlias)
            for iPatterns in details['cmtPattern']: self.patterns.append(iPatterns)

        self.foundFiles = FileIO().findFiles(tuple(self.allowedExt), self.ignoreme)

        return self.configFile 

    def printConfig(self) -> None:
        
        if not self.configFile:
            self.getConfig()

        print(self.foundFiles)
        pass

