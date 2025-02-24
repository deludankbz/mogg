import typer
from utils.fileIO import Utils

app = typer.Typer(name="codeThings")

@app.command()
def test(): print("TEST")


def main():
    foundFiles = Utils()
    
    args = sys.argv[1:]
    print(f"count of args :: {len(args)}")

    foundFiles.findFiles(args)
    foundFiles.fetchBuffer()
    foundFiles.fetchTasks()


    # exPath = os.path.join(os.getcwd(), "src", "ex.py")
    
    pass

if __name__ == '__main__':
    main()
