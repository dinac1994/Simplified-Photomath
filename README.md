# Simplified-Photomath

This repository includes a simplified version of a popular educational app called Photomath. A user uploads a picture containing a handwritten mathematical expression and the program returns the solution of the given expression.

Expression can contain following mathematical characters: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `+`, `-`, `×`, `(` and `)`.

### There are four parts of this code:

1.  **A handwritten character detector function** - receives an image of expression and returns cropped images of characters

2.  **A classification function** - recieves cropped image of a character and returns a character

3.  **An evaluation function** - recieves a string of characters that represent an expression and returns the evaluation of the expression

4.  **A Photomath Function** - this function includes all of the previous functions. It takes an image of a handwritten expression and outputs a solution of the given expression.

## Part One - Handwritten Character Detector Function

### Input:

