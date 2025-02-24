import os
import glob
import re
import sys

class Utils:
    def __init__(self) -> None:
        # TODO make this bit into a config file
        self.taskTokens = ("TODO", "FIX", "NOTE", "ERROR")
        self.taskBuffers = list()

        self.cwd = os.getcwd()
        self.foundFiles = list()

        pass

    def findFiles(self, chosenFolder=None):
        print(chosenFolder)
        fmtGlobPath = os.path.join(self.cwd, "*")

        for name in glob.glob(fmtGlobPath, recursive=True): 
            matchedRef = re.search(r'^.+\.[a-zA-Z0-9]+$', name)

            if matchedRef: self.foundFiles.append(name)

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
            for lines in iDicts["buffer"]: 
                if lines.startswith("#"): 
                    print(lines.replace('\n', ''))
        pass

def main():
    foundFiles = Utils()
    
    args = sys.argv[1:]
    print(f"count of args :: {len(args)}")

    foundFiles.findFiles(args)
    foundFiles.fetchBuffer()
    foundFiles.fetchTasks()


    # exPath = os.path.join(os.getcwd(), "src", "ex.py")
    
    pass

if __name__ == '__main__':
    main()
