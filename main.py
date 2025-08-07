from parser import QASMParser


def load_qasm_file(path):
    with open(path, 'r') as f:
        return f.read()


if __name__ == "__main__":
    code = load_qasm_file("examples/bell.qasm")
    parser = QASMParser(code)
    parser.parse()
    parser.printable_format()

