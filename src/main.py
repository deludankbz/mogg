import os
import typer
from utils.fileIO import Utils

app = typer.Typer(name="codeThings")

@app.command()
def main(inputfolder: str = typer.Option("", "--input", "-i", help="Input folder")): 
    foundFiles = Utils()
   
    if os.path.isdir(inputfolder):
        foundFiles.pathSelector()
        foundFiles.findFiles()
        foundFiles.fetchBuffer()
        foundFiles.fetchTasks()
    else: raise Exception(FileNotFoundError)


    # exPath = os.path.join(os.getcwd(), "src", "ex.py")
    
    pass

if __name__ == '__main__':
    app()
