import os
import glob
import re

class Utils:
    def __init__(self) -> None:
        # TODO make this bit into a config file
        self.taskTokens = ("TODO", "FIX", "NOTE", "ERROR")
        self.taskBuffers = list()

        self.cwd = os.getcwd()
        self.foundFiles = list()

        pass

    def pathSelector(self, chosenFolder=None):
        if chosenFolder != None: return os.path.join(self.cwd, chosenFolder)
        else: return self.cwd

    def findFiles(self):
        fmtGlobPath = os.path.join(self.pathSelector(), "**")

        for name in glob.glob(fmtGlobPath, recursive=True):
            matchedRef = re.search(r'^.+\.[a-zA-Z0-9]+$', name)

            if matchedRef: 
                self.foundFiles.append(name)
                print(name)

        return self.foundFiles

    def fetchBuffer(self) -> list[dict]:
        for file in self.foundFiles:
            if os.path.isfile(file):
                with open(file,'r') as fopen_buffer:
                    newBuffer = {"filename": file, "buffer": fopen_buffer.readlines()}
                    self.taskBuffers.append(newBuffer)

        return self.taskBuffers

    def fetchTasks(self):
        for iDicts in self.taskBuffers:
            print(iDicts)
        pass
