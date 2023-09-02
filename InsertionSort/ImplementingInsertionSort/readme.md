# Insertion Sort Algorithm

This repository contains a JavaScript implementation of the Insertion Sort algorithm. The insertion sort algorithm is a simple sorting algorithm that builds the final sorted array one item at a time. It is much less efficient on large lists than more advanced algorithms such as quicksort, heapsort, or merge sort. However, it can be quite efficient for small lists or lists that are nearly sorted.

## Algorithm Description

The `insertionSort` function in this repository implements the insertion sort algorithm. Here's how it works:

1. It starts by iterating through the input array, starting from the second element (`i = 1`) to the last element.

2. For each element at index `i`, it compares it to the elements to its left (at indices `j = i` to `0`).

3. If the current element is smaller than the element to its left, it swaps them. This process continues until the current element is in its correct sorted position within the subarray.

4. The algorithm repeats this process for all elements in the array, resulting in a sorted array when finished.

## Usage

You can use this implementation to sort an array of numbers by calling the `insertionSort` function and passing your array as an argument. For example:

```javascript
const unsortedArray = [1, 4, 2, 8, 345, 123, 43, 32, 5643, 63, 123, 43, 2, 55, 1, 234, 92];
const sortedArray = insertionSort(unsortedArray);
console.log(sortedArray);
