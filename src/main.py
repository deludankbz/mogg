import os
import typer
from utils.fileIO import Utils

app = typer.Typer(name="codeThings")

@app.command()
def main(
        lang: str = typer.Option("", "--lang", help="Choose a language"), 
        inputfolder: str = typer.Option("", "--input", "-i", help="Input folder")): 
    foundFiles = Utils()
   
    foundFiles.pathSelector()
    foundFiles.findFiles('.gitignore')
    foundFiles.fetchBuffer()

    foundFiles.fetchTasks()

    pass

if __name__ == '__main__':
    app()
