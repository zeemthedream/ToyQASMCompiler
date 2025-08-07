## ToyQASMCompilier 

Personal project to gain experience in quantum circuit representation and the core logic required to translate quantum assembly into an executable format. As well as, learn about core quantum computing concepts.

### Project Goals
1. Create a parser that parses a small subset of OpenQASM 3.0 
2. After parsing, build a smple Abstact Syntax Tree (AST)
3. Converts the AST into a quantum circuit representation.
4. Aditionally, can also simulate circuits or output equivalent pseudocode

### Core Concepts

- `Qubit`: quantum bit that can exist in a superposition of 0 and 1. It's a 2D complex vector that can be manipulated by gates like H (Hadamard), X (quantum NOT), etc.
  - A qubit can be in a linear combination of 0 and 1. Only when measured does it collapse to 0 or 1 based on probabilities.
- Quantum circuits are sequences of gate operations on qubits
  - gates include `X`, `H`, `Z`, `CX`, `Measure`
- `Entanglement`: two or more quibits can be in a joint together state such that their individual states don't tell you the full story
- `Bell State`: maximally entangled 2-quibit state. 
- `AST`: Abstract Syntax tree is a structured, hierarchical representation of a program. Each node represents a meaningful element like a gate, a measurement, or a register declaration.