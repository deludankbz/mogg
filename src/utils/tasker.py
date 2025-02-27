import os

from utils.fileIO import FileIO

class Tasker:
    def __init__(self) -> None:
        self.file_io = FileIO()
        self.config = FileIO()

        self.taskTokens = ("TODO", "FIX", "NOTE", "ERROR")
        self.foundTasks = list()

        pass

    def getTasks(self):
        for iDicts in self.file_io.fileBuffers: 
            for line in iDicts["buffer"]: 
                print()
                # regex magic here to find comments ...

            if len(self.foundTasks) > 0: 
                relativePath = os.path.relpath(iDicts["filename"], self.file_io.cwd)
                taskAmount = len(self.foundTasks)

                print(f"\x1b[1;90m\n@ {relativePath} :: found {taskAmount} tasks!\x1b[0m\n")

                for i in self.foundTasks: 
                    print(f"\t\x1b[1;96m{i}\x1b[0m")

                self.foundTasks.clear()
        pass

    def showTasks(self):


        pass
