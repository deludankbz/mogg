import os

from utils.fileIO import FileIO

class Tasker:
    def __init__(self, cwd) -> None:

        self.cwd = cwd

        self.taskTokens = ("TODO", "FIX", "NOTE", "ERROR")
        self.foundTasks = list()

        pass

    def getTasks(self, fileBuffers: dict):
        for iDicts in fileBuffers: 
            print(iDicts["buffer"])
            # regex magic here to find comments ...

            if len(self.foundTasks) > 0: 
                relativePath = os.path.relpath(iDicts["filename"], )
                taskAmount = len(self.foundTasks)

                print(f"\x1b[1;90m\n@ {relativePath} :: found {taskAmount} tasks!\x1b[0m\n")

                for i in self.foundTasks: 
                    print(f"\t\x1b[1;96m{i}\x1b[0m")

                self.foundTasks.clear()
        return self.foundTasks

    def showTasks(self):
        pass
