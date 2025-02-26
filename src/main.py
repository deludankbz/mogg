import typer

from utils.fileIO import Utils
from utils.config import printConfig

app = typer.Typer(name="codeThings")

# TODO: progress bar to indicate where processing is happening

@app.command()
def main(
        lang: str = typer.Option("", "--lang", help="choose a language")): 
    # foundFiles = Utils()
    #
    # foundFiles.pathSelector()
    # foundFiles.findFiles('.gitignore')
    # foundFiles.fetchBuffer()
    #
    # foundFiles.fetchTasks()

    printConfig() 

    pass

if __name__ == '__main__':
    app()
