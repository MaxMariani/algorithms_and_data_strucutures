# Valid Palindrome

## Description
This repository contains a solution for the "Valid Palindrome" problem. The goal of this problem is to determine whether a given phrase is a palindrome. A phrase is considered a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

## Problem Statement
Given a string `s`, the task is to implement a function `isPalindrome(s: str) -> bool` that returns `True` if the input string is a palindrome according to the given criteria, and `False` otherwise.

## Thought Process
The solution provided for this problem involves the following steps:

1. Convert the input string `s` to lowercase using the `lower()` method.
2. Create a new string `ns` to store the alphanumeric characters of the converted string. Iterate through each character `l` in the converted string `s`:
    - If `l` is a lowercase letter between 'a' and 'z' or a digit between '0' and '9', add it to the `ns` string.
3. Initialize two pointers `left` and `right` at the beginning and end of the `ns` string, respectively.
4. Using a `while` loop, compare characters at the `left` and `right` positions of `ns`:
    - If they are not equal, return `False`, indicating that the string is not a palindrome.
    - Increment `left` and decrement `right` to move closer towards the center of the string.
5. If the loop completes without finding any unequal characters, return `True`, indicating that the string is a palindrome.

By following these steps, the provided solution effectively determines whether the input string is a valid palindrome according to the specified criteria.
