# PLP Python Week 3 Assignment

## File Descriptions
* **grade_reporter.py**: A script that evaluates a list of student scores, prints their letter grades, counts how many students passed or failed, and outputs the rounded average score.
* **bug_hunt.py**: A debugged program that correctly calculates and prints the sum of integers from 1 to 5.

## Bug Hunt Reflection
The hardest bug to find was the logic error in the loop condition (`count < 5`). Because Python ran the program perfectly fine without throwing an error message, it did not immediately draw attention to itself. I knew something was wrong because the prompt explicitly stated the correct answer should be 15, but the uncorrected logic only added up to 10 because it excluded the number 5 entirely.
