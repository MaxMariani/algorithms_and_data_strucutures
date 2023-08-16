# Reverse Polish Notation Calculator

This repository contains a Python script for evaluating mathematical expressions using Reverse Polish Notation (RPN). RPN is a mathematical notation in which every operator follows all of its operands.

[![Reverse Polish Notation and The Stack - Computerphile](https://img.shields.io/badge/YouTube-Red?style=flat&logo=youtube)](https://www.youtube.com/watch?v=7ha78yWRDlE)





## Table of Contents

- [Usage](#usage)
- [Script Overview](#script-overview)
  - [How to Use the `calculate_rpn` Function](#how-to-use-the-calculate_rpn-function)
  - [Example](#example)
- [Implementation Details](#implementation-details)
- [Supported Operations](#supported-operations)
- [Error Handling](#error-handling)

## Usage

1. Make sure you have Python installed on your system.
2. Copy and paste the provided Python script into a `.py` file (e.g., `rpn_calculator.py`).
3. Open a terminal or command prompt.
4. Navigate to the directory where the `.py` file is located.
5. Run the script

## Script Overview

The script defines a dictionary `op` containing lambda functions for basic arithmetic operations (`+`, `-`, `*`, and `/`). It also defines a function `calculate_rpn(expression)` that takes an RPN expression as input and returns the result of the calculation.

### How to Use the `calculate_rpn` Function

1. Provide a space-separated RPN expression as a string.
2. Call the `calculate_rpn(expression)` function with the expression as an argument.
3. The function will return the calculated result.

### Example

```python
expression = "4 5 + 3 *"
result = calculate_rpn(expression)
print("Result:", result)
```

This will output:

```python
Result: 27.0
```
## Implementation Details
The implementation follows these steps:

1. Split the input expression into individual tokens (operands and operators).
2. Iterate through the tokens in the expression.
   - If the token is a digit, push it onto the stack.
   - If the token is an operator, pop the required number of operands from the stack, apply the operator, and push the result onto the stack.
   - If the token is neither a digit nor an operator, raise a ValueError.
3. Once all tokens are processed, the final result will be at the top of the stack.

## Supported Operations
The calculator supports the following operations:

- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)

## Error Handling
The script provides basic error handling. If an invalid token is encountered, a ValueError is raised with an appropriate error message.

