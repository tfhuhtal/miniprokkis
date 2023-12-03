from servicehandler import ServiceHandler
from services.console_io import ConsoleIO


def main():
    io = ConsoleIO()
    app = ServiceHandler(io)
    app.run()


if __name__ == "__main__":
    main()
