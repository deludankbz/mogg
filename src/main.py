import typer

from utils.fileIO import Utils
from utils.config import Config

app = typer.Typer(name="codeThings")

# TODO: progress bar to indicate where processing is happening

@app.command()
def run( showComments: bool = typer.Option(False, "--showComments", help="Show all comments" )):
    print(showComments)
    pass

@app.command()
def main( lang: str = typer.Option(None, "--lang", help="Select a specific language" )): 

    foundFiles = Utils()
    conf = Config()
    conf.getConfig()

    if lang == None: pass

    elif lang ==  "help":
        print(f"Available languages:", )
        for namelang, confDict in conf.configFile["languages"].items():
            print(f"\t {namelang} :: {confDict["aliases"]}") 
            return

    elif lang not in conf.aliases:
        print(f"{lang} not supported!")
        return

    else:
        for namelang, confDict in conf.configFile["languages"].items():

            if lang in confDict["aliases"]:
                print(f"{lang} is {namelang.title()}")

    foundFiles.pathSelector()
    foundFiles.findFiles(tuple(conf.allowedExt), conf.ignoreme)
    foundFiles.fetchBuffer()

    foundFiles.fetchTasks()

    pass

if __name__ == '__main__':
    app()
