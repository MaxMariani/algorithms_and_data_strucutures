# Valid Parentheses Checker

This Python script checks the validity of a given string containing only parentheses characters ('(', ')', '{', '}', '[', ']'). The script determines whether the input string follows the rules of valid parentheses usage as described below:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket must have a corresponding open bracket of the same type.

## Problem Statement

Given a string `s` containing only the characters '(', ')', '{', '}', '[', ']', the script checks whether the input string has a valid arrangement of parentheses.

## Constraints

- 1 <= `s.length` <= 10,000
- `s` consists of only the characters '(', ')', '{', '}', '[', ']'.

## LeetCode Source

This script is based on the [LeetCode problem #20: Valid Parentheses](https://leetcode.com/problems/valid-parentheses/).

## Usage

To use the script, you need to define the `validParenthesis` function and pass a string as an argument to it. The function will return `True` if the input string contains valid parentheses and `False` otherwise. Here's how you can use the function:

```python
print(validParenthesis('({{}})]'))  # Replace this with the string you want to check
```

## Function Explanation
The `validParenthesis` function follows these steps to determine the validity of the input string:

1. Initialize a dictionary `p` that maps closing brackets to their corresponding opening brackets.
2. Create an empty list `stack` to simulate a stack data structure.
3. Iterate through each character `c` in the input string `s`:
   - If `c` is a closing bracket and the stack is not empty and the top element of the stack matches the corresponding opening bracket for `c`, pop the top element from the stack.
   - Otherwise, if `c` is an opening bracket, append it to the stack.
4. After iterating through all characters in `s`, if the stack is empty, return `True` (valid parentheses arrangement), otherwise return `False` (invalid arrangement).

## Example
For the input string `'({{}})]'`, the function will output `False` since the arrangement is not valid according to the rules of valid parentheses.

## Note
This script provides a simple and efficient way to check the validity of parentheses arrangements in strings. It utilizes a stack data structure to keep track of opening brackets and matches them with their corresponding closing brackets.

