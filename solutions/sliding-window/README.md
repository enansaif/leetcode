# Sliding window algorithm

## When applicable

- Find a contiguous sequence of elements that satisfy a certain condition

## Types

1. Fixed window ([438] Find All Anagrams in a String)

2. Dynamic window ([1838] Frequency of the Most Frequent Element)

3. Dynamic window with auxiliary data structures ([904] Fruit Into Baskets)

## General pattern

- set left, right pointers

- iterate while right pointer is valid

- on each iteration

	-  add the right element

	- while the condition is invalid, we shrink the window i.e. remove left element and update left pointer

	- now that we are sure the condition is valid, we do some calculations

	- update right pointer
