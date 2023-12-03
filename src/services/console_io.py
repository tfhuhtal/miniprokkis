class ConsoleIO:
    def __init__(self, inputs=None):
        self.inputs = inputs or []
        self.outputs = []

    def write(self, value):
        self.outputs.append(value)
        print(value)

    def read(self):
        if len(self.inputs) > 0:
            return self.inputs.pop(0)
        return ""

    def add_input(self, value, val=False):
        if not val:
            self.inputs.append(input(value))
        else:
            self.inputs.append(value)
