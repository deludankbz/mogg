import os, re

class Tasker:
    def __init__(self, cwd) -> None:

        self.cwd = cwd

        self.taskTokens = ("TODO", "FIX", "NOTE", "ERROR")
        self.foundTasks = list()

        pass

    def getTasks(self, fileBuffers: list[dict], patterns: list):

        # FIX check for empty buffer
        # FIX choose patterns correc.

        for iDicts in fileBuffers: 
            # print(iDicts["ext"])
            # print(patterns)

            for i in patterns:
                # print(i)
                ml_Matches = re.findall(i, ''.join(iDicts["buffer"]))
                for matches in ml_Matches: self.foundTasks.append(matches)

            if len(self.foundTasks) > 0: 
                relPath = os.path.relpath(iDicts["filename"], self.cwd)
                taskAmount = len(self.foundTasks)

                print(f"\x1b[1;90m\n@ {relPath} :: found {taskAmount} tasks!\x1b[0m\n")

                for i in self.foundTasks: 
                    print(f"\t\x1b[1;96m{i}\x1b[0m")

                self.foundTasks.clear()
            else: print("no tasks!")

        return self.foundTasks
