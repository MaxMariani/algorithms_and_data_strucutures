# Baseball Game Score Calculator

This repository contains a Python script designed to calculate scores for a baseball game with specific rules. The script takes a list of operations as input and calculates the sum of scores based on the provided rules.

## Game Rules

1. At the start of the game, the record is empty.
2. The script takes a list of strings `operations` as input, where each string represents an operation to be applied to the record.
3. The possible operations are:
   - An integer `x`: Record a new score of `x`.
   - `'+'`: Record a new score that is the sum of the previous two scores.
   - `'D'`: Record a new score that is double the previous score.
   - `'C'`: Invalidate the previous score, removing it from the record.
4. The script processes each operation in the order they appear in the input list.
5. The final result should be the sum of all the scores in the record after applying all operations.

## Constraints

- 1 <= operations.length <= 1000
- operations[i] is "C", "D", "+", or a string representing an integer in the range [-3 * 10^4, 3 * 10^4].
- For operation "+", there will always be at least two previous scores on the record.
- For operations "C" and "D", there will always be at least one previous score on the record.



## Getting Started

To use the script, follow these steps:

1. Clone this repository to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the repository's directory.
4. Run the script using the command: `python baseballgame.py`

Make sure you have Python installed on your machine.

## Example

For example, given the input operations:
```python
ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]
```

The output should be:
```python
27
```

