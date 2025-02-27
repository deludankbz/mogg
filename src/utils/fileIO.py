import os, glob, re

class FileIO:
    def __init__(self) -> None:

        self.fileBuffers = list()

        self.cwd = os.getcwd()
        self.foundFiles = list()

        pass

    def getPath(self, chosenFolder=None) -> str:
        if chosenFolder != None: return os.path.join(self.cwd, chosenFolder)
        else: return self.cwd

    def findFiles(self, extensions: tuple, ignore: list):

            fmtGlobPath = os.path.join(self.getPath(), "**")

            for name in glob.glob(fmtGlobPath, recursive=True):
                matchedRef = re.search(r'^.+\.[a-zA-Z0-9]+$', name)

                if matchedRef: 
                    
                    if not any(i in name for i in ignore) and name.endswith(extensions):
                        self.foundFiles.append(name)

            return self.foundFiles

    def fetchBuffer(self) -> list[dict]:

        for file in self.foundFiles:
            if os.path.isfile(file):

                with open(file,'r') as fopen_buffer:
                    newBuffer = {"filename": file, "buffer": fopen_buffer.readlines()}
                    self.fileBuffers.append(newBuffer)

        return self.fileBuffers

