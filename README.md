# Simplified-Photomath

This repository includes a simplified version of a popular educational app called Photomath. A user uploads a picture containing a handwritten mathematical expression and the program returns the solution of the given expression.

Expression can contain following mathematical characters: `0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `+`, `-`, `×`, `(` and `)`.

### There are four parts of this code:

1.  **A handwritten character detector function** - receives an image of expression and returns cropped images of characters

2.  **A Classification Function** - recieves cropped image of a character and returns a character. We will use a CNN for classification that was made and trained in a `NN_model.ipynb` file.

3.  **An Evaluation Function** - recieves a string of characters that represent an expression and returns the evaluation of the expression

4.  **A Photomath Function** - this function includes all of the previous functions. It takes an image of a handwritten expression and outputs a solution of the given expression.

## Part One - Handwritten Character Detector Function

### Input:

![Slika_1](https://user-images.githubusercontent.com/92053362/146676997-29315fb1-bec6-4b97-9b9f-b82b1e50f267.png)

### Output:

![Slika_2](https://user-images.githubusercontent.com/92053362/146677016-a8800588-a364-4246-9d70-48a2b3773ea5.png)

## Part Two - A Classification Function

### Input:
<img width="58" alt="Slika_22" src="https://user-images.githubusercontent.com/92053362/146677096-bf83fc32-61a1-406e-959f-3aa25aba32f8.png">

### Output: "2"

## Part Three - An Evaluation Function

### Input: "2+3"

### Output: "5"

## Part Four - A Photomath Function

This is where everything gets together!

### Input:

![Slika_1](https://user-images.githubusercontent.com/92053362/146677152-6646892f-e52d-41f8-af76-1db314aa196e.png)

From the input image, we get cropped images of the characters using ***Character Detector Function***.

We then iterate through all of the cropped images of characters and we classify each image as a character (using  ***Classification Function*** and we append those characters to one string. That string is going to be a math expression from the image.

The final step is to use ***Evaluation Function*** that takes the expression string and solves it. The final output is the solution of the expression.

### Output: "5".


## Examples from UI of a simple Flask app:
<img width="1226" alt="Slika_11" src="https://user-images.githubusercontent.com/92053362/146677678-8ca81690-81fe-4f9a-b9c4-11edd73036f0.png">
<img width="1254" alt="Slika_9" src="https://user-images.githubusercontent.com/92053362/146677475-c7567126-954f-4585-b154-bc4496c1b42c.png">
<img width="1211" alt="Slika_10" src="https://user-images.githubusercontent.com/92053362/146677481-8fbe3863-9949-4261-ad86-d286fdabe382.png">


