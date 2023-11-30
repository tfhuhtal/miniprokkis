import re
from console_io import ConsoleIO
from referencehandler import ReferenceHandler


class AppLibrary:
    def __init__(self):
        self._io = ConsoleIO()

        self._app = ReferenceHandler(self._io)

    def input(self, value):
        self._io.add_input(value, True)

    def output_should_contain(self, value):
        outputs = self._io.outputs
        splitted = []
        for out in outputs:
            splitted.append(re.split(r'\W+', out))
        x = False
        for split in splitted:
            if value in split:
                x = True
        if not x:
            raise AssertionError(
                f"Output \"{value}\" is not in {str(splitted)}")

    def run_application(self):
        self._app.run()
