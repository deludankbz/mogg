import typer, re
from utils import tasker
from utils.fileIO import FileIO
from utils.config import Config
from utils.tasker import Tasker

app = typer.Typer(name="codeThings")

# TODO: progress bar to indicate where processing is happening

@app.command()
def run( showComments: bool = typer.Option(False, "--showComments", help="Show all comments" )):
    newIO, conf = FileIO(), Config()
    tasker = Tasker(newIO.getPath())

    conf.getConfig()
    seleted = conf.makeSelection()

    newIO.getPath()
    newIO.findFiles(seleted, conf.ignoreme)

    newIO.fetchBuffer()
    tasker.getTasks(newIO.fileBuffers, showComments)
    pass

# @app.command()
# def main( lang: str = typer.Option(None, "--lang", help="Select a specific language" )): 
#
#     foundFiles = Utils()
#     conf = Config()
#     conf.getConfig()
#
#     if lang == None: pass
#
#     elif lang ==  "help":
#         print(f"Available languages:", )
#         for namelang, confDict in conf.configFile["languages"].items():
#             print(f"\t {namelang} :: {confDict["aliases"]}") 
#             return
#
#     elif lang not in conf.aliases:
#         print(f"{lang} not supported!")
#         return
#
#     else:
#         for namelang, confDict in conf.configFile["languages"].items():
#
#             if lang in confDict["aliases"]:
#                 print(f"{lang} is {namelang.title()}")
#
#     foundFiles.pathSelector()
#     foundFiles.findFiles(tuple(conf.allowedExt), conf.ignoreme)
#     foundFiles.fetchBuffer()
#
#     foundFiles.getTasks()
#     foundFiles.showTasks
#
#     pass

if __name__ == '__main__':
    app()
