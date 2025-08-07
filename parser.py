import re


# QASM language assembly parser
class QASMParser:

    def __init__(self, code: str):
        self.code = code.strip().splitlines()
        self.version = 0
        self.qubit_registers = {}
        self.instructions = []

    # parse the qasm code provided on initialization
    def parse(self):
        for line in self.code:
            line = line.strip().strip(';')

            if not line or line.startswith("//"):
                continue

            if line.startswith("OPENQASM"):
                self.version = line.split()[1]
            elif line.startswith("qreg"):
                match = re.match(r"qreg\s+(\w+)\[(\d+)\]", line)
                if match:
                    reg_name = match.group(1)
                    size = int(match.group(2))
                    self.qubit_registers[reg_name] = size
            else:
                self.instructions.append(line)

    # print parsed code in readable format
    def printable_format(self):
        print("QASM Version: ", self.version)
        print("Qubit Registers:")
        for name, size in self.qubit_registers.items():
            print(f"  {name}[{size}]")
        print("Instructions:")
        for instruction in self.instructions:
            print(f"  {instruction}")
