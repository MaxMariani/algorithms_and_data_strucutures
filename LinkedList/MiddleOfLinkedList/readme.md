# Middle of Linked List

## Description

This problem involves finding the middle node of a singly linked list. If the linked list has an odd number of nodes, the middle node is returned. If the linked list has an even number of nodes, the second middle node is returned.

## Problem Statement

Given the head of a singly linked list, implement a function `middleNode` that returns the middle node of the linked list.

### Example

Given the linked list: `1 -> 2 -> 3 -> 4 -> 5 -> 6`, the middle node is `4`.

Given the linked list: `1 -> 2 -> 3 -> 4 -> 5`, the middle node is `3`.

## Approach

The solution involves using two pointers to traverse the linked list. One pointer moves one step at a time, while the other pointer moves two steps at a time. When the faster pointer reaches the end of the list, the slower pointer will be at the middle node.

## Complexity Analysis

- Time Complexity: O(n), where n is the number of nodes in the linked list.
- Space Complexity: O(1), as no additional data structures are used.
