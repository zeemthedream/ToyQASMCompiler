# TODO: implement instructions (AST) class and optimize parser to abstracted/validated qasm instructions

class Instruction:
    def __init__(self, type: str):
        self.type = type
