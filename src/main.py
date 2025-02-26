import typer

from utils.fileIO import Utils
from utils.config import Config

app = typer.Typer(name="codeThings")

# TODO: progress bar to indicate where processing is happening

@app.command()
def main(
        lang: str = typer.Option("", "--lang", help="choose a language")): 

    foundFiles = Utils()
    conf = Config()

    conf.getConfig()

    foundFiles.pathSelector()
    foundFiles.findFiles(tuple(conf.allowedExt), conf.ignoreme)
    foundFiles.fetchBuffer()

    foundFiles.fetchTasks()

    pass

if __name__ == '__main__':
    app()
