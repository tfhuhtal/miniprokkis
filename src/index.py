from referencehandler import ReferenceHandler
from console_io import ConsoleIO

def main():
    io = ConsoleIO()
    app = ReferenceHandler(io)
    app.run()

if __name__ == "__main__":
    main()