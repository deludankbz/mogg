import json
import os
from utils.fileIO import Utils

cwd = os.path.join(os.getcwd(), "src", "utils", "config.json")

def printConfig():
    with open(cwd, 'r') as f:
        data = json.load(f)

    extList = list()
    ignList = list()
    for lang, details in data['languages'].items():
        for iExt in details['ext']: extList.append(iExt)
        for iIgn in details['ign']: ignList.append(iIgn)

    new_FIO = Utils()
    new_FIO.pathSelector()
    foundFiles = new_FIO.findFiles(tuple(extList), ignList)
    print(foundFiles)


