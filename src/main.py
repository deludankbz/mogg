import os
import sys


taskTuple = ("TODO", "FIX", "NOTE", "ERROR")

def getFile(filename: str) -> list[str]:
    with open(filename, 'r') as fBuffer:
        return fBuffer.readlines()

def readTask(fBuffer: list[str], filename: str):
    taskList = list()
    for i in fBuffer: 
        # FIX startswith(commSufix) <- based on languge; only work with python
        if i.startswith('#') & any(temp in i for temp in taskTuple): 
            taskList.append(i.replace('\n', ''))

    print(f"@ {filename} :: found {len(taskList)} tasks! (ln: {len(fBuffer)})")

    # NOTE we print todo's here
    for i in taskList: print("    ", i)
    pass

def main():
    args = sys.argv[1:]
    print(f"count of args :: {len(args)}")

    for iArg in args:
        tempExPath = os.path.join(os.getcwd(), "src", iArg)
        if os.path.isfile(tempExPath): readTask(getFile(tempExPath), iArg)

        # print(f"count of args :: {args[iArg]}")
    
    # exPath = os.path.join(os.getcwd(), "src", "ex.py")
    
    pass

if __name__ == '__main__':
    main()
