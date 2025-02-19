# Incubyte TDD Assessment

## String Calculator TDD Kata

This repository contains the solution to the Incubyte TDD Kata assessment.



## Objective

The goal of this assessment is to evaluate the ability to write readable and testable code using Test-Driven Development (TDD) practices. The task is to implement a String Calculator with the following requirements:

### Requirements

1. Create a simple String calculator with a method signature like this:

   - Input: a string of comma-separated numbers
   - Output: an integer, sum of the numbers

2. Examples:

   - Input: `""`, Output: `0`
   - Input: `"1"`, Output: `1`
   - Input: `"1,5"`, Output: `6`

3. Allow the `add` method to handle any amount of numbers.

4. Allow the `add` method to handle new lines between numbers (instead of commas). For example, `"1\n2,3"` should return `6`.

5. Support different delimiters:
   - To change the delimiter, the beginning of the string will contain a separate line that looks like this: `"//[delimiter]\n[numbers…]"`. For example, `"//;\n1;2"` where the delimiter is `";"` should return `3`.

6. Calling `add` with a negative number will throw an exception: "negative numbers not allowed <negative_number>". If there are multiple negative numbers, show all of them in the exception message, separated by commas.

7. Extra points for completing all the steps from TDD Kata 1.

### Getting Started

To get started with the project, clone the repository and follow the instructions below.

```sh
git clone <repository_url>
cd <repository_name>
```

### Running Tests

To run the tests, use the following command:

```sh
python -m unittest discover
```

### Project Structure

The project structure is as follows:

```
.
├── src
│   ├── __init__.py
│   └── string_calculator.py
├── tests
│   ├── __init__.py
│   └── test_string_calculator.py
└── README.md
```

### Implementation

The implementation follows the TDD approach by writing tests first and then implementing the corresponding functionality. Each step is committed separately to show the evolution of the code.

### Conclusion

This assessment demonstrates the ability to write clean, readable, and testable code using TDD practices. The String Calculator implementation handles various scenarios, including different delimiters and negative numbers, with appropriate error handling.

### References

- [TDD Kata 1](https://kata-log.rocks/string-calculator-kata)
- [TDD Video](https://www.youtube.com/watch?v=EZ05e7EMOLM)
