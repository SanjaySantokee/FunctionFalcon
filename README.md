# FunctionFalcon
FunctionFalcon is a Python program that allows users to enter mathematical expressions and get the solutions using an API. The program also features a history list where past calculations can be viewed and copied to the clipboard.

## Installation

1. Clone the repository or download the source code.
2. Install the required dependencies by running `pip install -r requirements.txt`.
3. Run `python main.py` to launch the program.

## Usage

1. Enter a mathematical expression in the input field and click the "Solve" button or press the Enter key to get the solution.
2. The solution will be displayed in the output field.
3. To copy the solution to the clipboard, click the "Copy" button next to the output field.
4. To view past calculations, scroll down to the history list at the bottom of the window.
5. To copy a past calculation to the clipboard, click the "Copy" button next to the calculation in the history list.

## Supported Operations

Math Solver supports the following mathematical operations:

- Basic arithmetic (addition, subtraction, multiplication, division)
- Exponents
- Square roots
- Trigonometric functions (sin, cos, tan, arcsin, arccos, arctan)
- Logarithmic functions (log, ln)

## API

FunctionFalcon uses the [Wolfram Alpha API](https://www.wolframalpha.com/) to solve mathematical expressions. To use the program, you will need to sign up for a Wolfram Alpha API key and enter it in the `config.py` file.

## License

This program is licensed under the MIT License. See the `LICENSE` file for more information.
