import os, re

from utils.config import Config

class Tasker:
    def __init__(self, cwd) -> None:

        self.cwd = cwd

        self.taskTokens = ("TODO", "FIX", "NOTE", "ERROR")
        self.foundTasks = list()

        pass

    def getTasks(self, fileBuffers: list[dict], allComments: bool):

        conf = Config()

        # FIX check for empty buffer
        # FIX choose patterns correc.

        for iDicts in fileBuffers: 
            # print(iDicts["ext"])
            # print(patterns)

            ext_match = re.search(r"\.[^./]+$", iDicts["filename"])
            if ext_match: 
                patterns = conf.getLangByExtension(ext_match[0])
                for i in patterns["cmtPattern"]:
                    ml_Matches = re.findall(i, ''.join(iDicts["buffer"]))
                    for matches in ml_Matches: self.foundTasks.append(matches)

            if len(self.foundTasks) > 0: 
                relPath = os.path.relpath(iDicts["filename"], self.cwd)
                taskAmount = len(self.foundTasks)

                print(f"\x1b[1;90m\n@ {relPath} :: found {taskAmount} tasks!\x1b[0m\n")

                for i in self.foundTasks: 
                    if allComments: print(f"\t\x1b[1;96m{i}\x1b[0m")
                    else: 
                        if any(temp in i for temp in self.taskTokens): print(f"\t\x1b[1;96m{i}\x1b[0m")

                self.foundTasks.clear()

        return self.foundTasks
