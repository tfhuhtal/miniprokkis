from converter import Converter


def main():
    converter = Converter("example.json")
    print(converter.convert())


if __name__ == "__main__":
    main()
