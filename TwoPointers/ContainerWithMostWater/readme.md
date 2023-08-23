# Container With Most Water - LeetCode Problem

This repository contains a Python solution for the "Container With Most Water" problem on LeetCode. The problem statement and solution explanation are provided below.

## Problem Description

You are given an integer array `height` of length n. There are n vertical lines drawn such that the two endpoints of the ith line are `(i, 0)` and `(i, height[i])`.

Your task is to find two lines that, together with the x-axis, form a container such that the container contains the most water. In other words, you need to find the maximum amount of water that can be stored within this container.

It's important to note that you are not allowed to slant the container.

## Solution Explanation

The provided solution is implemented in Python using the `maxArea` function within the `Solution` class. The solution employs a two-pointer approach to efficiently find the maximum area. The steps of the solution are as follows:

1. Initialize two pointers, `l` and `r`, pointing to the leftmost and rightmost elements of the `height` array, respectively. Also, initialize a variable `max_area` to keep track of the maximum area found.

2. Use a `while` loop to iterate while the `l` pointer is less than the `r` pointer. This loop is used to explore all possible container configurations.

3. Calculate the area of the container formed by the lines at indices `l` and `r`. The area is calculated as the minimum height between the two lines (i.e., `min(height[l], height[r])`) multiplied by the width between the two lines (i.e., `r - l`).

4. Compare the calculated area with the current maximum area (`max_area`). If the calculated area is greater, update `max_area` with the new value.

5. Since the goal is to maximize the area, we need to consider the possibility of finding a greater area by moving the pointers. If `height[l]` is less than `height[r]`, it means that moving the left pointer one step to the right (`l += 1`) could potentially result in a higher container height, and thus a higher area. Similarly, if `height[l]` is greater than or equal to `height[r]`, move the right pointer one step to the left (`r -= 1`).

6. Repeat steps 3 to 5 until the `l` pointer is no longer less than the `r` pointer. At this point, the loop will terminate, and the maximum area will be stored in the `max_area` variable.

7. Return the value of `max_area` as the final result.

## How to Use

1. Clone this repository to your local machine.
2. Open the Python file containing the solution (`container_with_most_water.py`).
3. Implement the `maxArea` function in your preferred programming environment.
4. Test the solution with various input cases to verify its correctness.

Feel free to use, modify, and distribute this solution according to the terms of the license.

Happy coding!
