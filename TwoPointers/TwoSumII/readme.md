# Two Sum II - Input Array Is Sorted

This repository contains a solution to the LeetCode problem "Two Sum II - Input Array Is Sorted". The problem statement requires finding two numbers in a sorted array that add up to a specific target number. The solution is implemented in Python.

## Problem Description

Given a 1-indexed array of integers `numbers` that is already sorted in non-decreasing order, the goal is to find two numbers such that they add up to a specific target number. Let these two numbers be `numbers[index1]` and `numbers[index2]` where `1 <= index1 < index2 < numbers.length`.

The task is to return the indices of the two numbers, `index1` and `index2`, added by one, as an integer array `[index1, index2]` of length 2. The tests are generated in a way that guarantees a unique solution, and the same element cannot be used twice. The solution should adhere to using only constant extra space.

## Solution Explanation

The provided solution uses a two-pointer approach to solve the problem efficiently. Here's a step-by-step explanation of how the solution works:

1. Initialize two pointers, `l` and `r`, both pointing to the beginning and the end of the `numbers` array, respectively.

2. Enter a loop that continues as long as `l` is less than `r`.

3. Calculate the sum of the elements at indices `l` and `r`, and store it in the variable `curSum`.

4. Compare `curSum` with the `target`:
   - If `curSum` is greater than the `target`, decrement `r` to move towards smaller elements.
   - If `curSum` is less than the `target`, increment `l` to move towards larger elements.
   - If `curSum` is equal to the `target`, the solution is found. Return `[l+1, r+1]` as the indices of the two numbers, adjusted for the 1-indexing.

5. If the loop completes without finding a solution, it means there is no valid pair of numbers that sums up to the target.

The idea behind this solution is that since the array is sorted, the smallest and largest elements are at the two ends. By comparing the sum of these elements with the target, the algorithm narrows down the search space until a valid pair is found or the pointers meet.

## How to Use

1. The solution is implemented as a method named `twoSum` inside the `Solution` class.

2. To use the solution, create an instance of the `Solution` class and call the `twoSum` method, passing the `numbers` array and the `target` as arguments.

3. The method will return an integer array containing the indices of the two numbers that sum up to the target.
