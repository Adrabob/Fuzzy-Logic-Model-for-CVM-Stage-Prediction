
# Fuzzy Logic Model for CVM Stage Prediction




## Overview
This project implements a fuzzy logic model to predict the CVM (Cervical Vertebral Maturation) stage based on two input variables: concavity and shape. Fuzzy logic is a powerful tool for handling uncertainty and imprecision, making it well-suited for modeling complex systems with linguistic variables and expert knowledge.
## Fuzzification
Input variables (concavity and shape) are mapped to fuzzy sets using membership functions (e.g., Flat, Concave, Trapezoidal, Horizontal, Square, Vertical).

This allows for partial membership in multiple categories, representing gradual transitions between states.
## Rule Base
A set of IF-THEN rules captures the relationships between input variables and the output CVM stage.

These rules encode expert knowledge and linguistic reasoning.
## Inference
The rules are applied to the fuzzified input values to determine the degree of activation for each output fuzzy set.

This involves combining the fuzzy sets using logical operators (AND, OR) and applying implication methods.
## Defuzzification
The fuzzy output is converted into a crisp numerical value representing the predicted CVM stage.

This often involves methods like centroid calculation or weighted average.
## Translation of Concavity and Shape Information
The model uses specific membership functions and rules to translate concavity and shape information into CVM stage predictions.

For example:

If concavity is "Flat" and shape is "Trapezoidal", the model infers a CVM stage of 1.

If concavity is "Concave" and shape is "Square", the model infers a CVM stage of 5.
# Dependencies
Python 3.x: Ensure you have Python 3.x installed on your system. You can check by running python --version in your terminal. If it's not installed, download it from https://www.python.org/downloads/.

NumPy: A fundamental library for numerical computing in Python.

scikit-fuzzy: A library specifically designed for fuzzy logic applications.

Matplotlib: A powerful library for creating visualizations and plots.
# Running the Code
It is recommended that you use a code editor such as Visual Studio Code to run the code, because in the Windows operating system, dependencies may not be accessible directly through the terminal.
### Install Dependencies:

Open a terminal in VS Code.

Run the following command to install the required dependencies:
```Bash
pip install numpy scikit-fuzzy matplotlib
```

### Run the Code:
Open your code with VS Code.

Navigate to the directory where you saved the `name.py` file using the terminal.
```
You can press Ctrl+F5 for run your code in VS Code
```
This will run the fuzzy logic model and print the predicted CVM stage.
