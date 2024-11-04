
LeetCode Solutions
Welcome to my LeetCode Solutions repository! This repository contains solutions to LeetCode problems across various categories and difficulty levels. I’ve documented my thought process, solution approach, and relevant time and space complexities for each problem to make it easier for others to understand my methodology.

Table of Contents
Categories
Array
String
Linked List
Tree
Graph
Dynamic Programming
Backtracking
Others
Languages Used
Solution Structure
How to Use This Repository
Acknowledgments
Categories
Each category contains links to specific LeetCode problems and my corresponding solution files. Problems are further classified by difficulty level: Easy, Medium, and Hard.

Array
Easy
Two Sum - Python
Remove Duplicates from Sorted Array - Python
Medium
3Sum - Python
Subarray Sum Equals K - Python
Hard
First Missing Positive - Python
String
Easy
Valid Palindrome - Python
Medium
Longest Substring Without Repeating Characters - Python
Hard
Edit Distance - Python
...

(Repeat similar structure for other categories like Linked List, Tree, Graph, Dynamic Programming, Backtracking, and Others)

Languages Used
This repository primarily contains solutions in:

Python - Most solutions are implemented in Python for simplicity and readability.
JavaScript - A few solutions are available in JavaScript, especially for problems suited to web-based applications.
Java - Solutions to select problems implemented in Java.
Feel free to reach out if you'd like solutions in other languages!

Solution Structure
Each solution file follows this format:

Problem Description: Brief summary of the problem to provide context.
Approach: Outline of the approach, including reasoning and key observations.
Complexity Analysis: Time and space complexity for the solution.
Code: The actual code for the solution.
Test Cases: Sample test cases with expected outputs.
Example:

python
Copy code
# Problem: Two Sum
# Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.
# 
# Approach:
# - Use a hash map to store the complement of each element.
# - Check if the complement exists in the hash map to identify the pair.
#
# Complexity: Time O(n), Space O(n)

class Solution:
    def twoSum(self, nums, target):
        complement_map = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in complement_map:
                return [complement_map[complement], i]
            complement_map[num] = i
How to Use This Repository
Clone this repository:

bash
Copy code
git clone https://gitlab.com/username/leetcode-solutions.git
cd leetcode-solutions
Navigate to the category folder and open the solution file of the problem you are interested in.

Read through the problem description, approach, and code. Try running the code in your preferred coding environment to understand how it works.
