from converter import Converter

def main():
    converter = Converter({"foo": "bar"})
    print(converter.convert())

if __name__ == "__main__":
    main()
