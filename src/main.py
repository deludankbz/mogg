import os
import typer
from utils.fileIO import Utils

app = typer.Typer(name="codeThings")

@app.command()
def main(inputfolder: str = typer.Option("", "--input", "-i", help="Input folder")): 
    foundFiles = Utils()
   
    foundFiles.pathSelector()
    foundFiles.findFiles('.gitignore')
    foundFiles.fetchBuffer()
    foundFiles.fetchTasks()


    # exPath = os.path.join(os.getcwd(), "src", "ex.py")
    
    pass

if __name__ == '__main__':
    app()
