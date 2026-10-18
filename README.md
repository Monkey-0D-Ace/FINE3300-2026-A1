# FINE3300-2026-A1
This repository contains FINE 3300 Assignment 1 - Talal Mehmood

# FINE 3300 Assignment 1  
## Python for Finance Professionals

## Project Description

This project was completed for FINE 3300: Python for Finance Professionals. The purpose of the assignment was to create a Python exchange rate calculator that reads annual exchange rate data provided by the Bank of Canada and converts between Canadian dollars (CAD) and U.S. dollars (USD).

The project applies several concepts introduced throughout the first four lectures of the course, including source code management using Git and GitHub, Python variables and data types, lists and indexing, conditional statements, functions, and object-oriented programming using classes and methods (Habib, “Lecture #1”; Habib, “Lecture #2”; Habib, “Lecture #3”; Habib, “Lecture #4”).

Git and GitHub were used to maintain the project and track changes to the code. In the course, Git was introduced as a distributed version-control system, while GitHub was presented as a platform for hosting remote repositories (Habib, “Lecture #1”).

---

## Part 1: Exchange Rate Calculator

For Part 1, I created a Python class called `ExchangeRates`. The class receives the Bank of Canada CSV filename through its constructor and reads the exchange rate information from the file.

The structure of the class follows the object-oriented programming concepts introduced in Lecture 4. A Python class contains data members that represent the state of an object and methods that define its behaviour. The `__init__()` method is used as the class constructor and initializes the object when it is created (Habib, “Lecture #4”).

The program reads the Bank of Canada data into a list and uses:

```python
rows[-1]
```

to obtain the final row of the file. Negative indexing was introduced when working with Python lists, where an index of `-1` refers to the final item in a list (Habib, “Lecture #2”).

The latest USD/CAD rate is then converted to a floating-point number so it can be used in mathematical calculations. Python data types, including integers, floating-point values, strings, and Boolean values, were introduced in Lecture 2 (Habib, “Lecture #2”).

The `convert()` method determines the direction of the conversion using conditional statements. Conditional statements allow the program to execute different instructions depending on whether a condition evaluates to true or false (Habib, “Lecture #3”).

For a USD-to-CAD conversion, the program multiplies the U.S. dollar amount by the USD/CAD exchange rate. For a CAD-to-USD conversion, the program divides the Canadian dollar amount by the same exchange rate.

The program also uses:

```python
if __name__ == "__main__":
```

This follows the structure demonstrated in the class examples from Lecture 4, including the Lottery and Bond examples, where the class definition is separated from the portion of the program that creates and uses an object (Habib, “Lecture #4”).

---

## Part 1: Program Results

The final USD/CAD exchange rate contained in the provided Bank of Canada data file was **1.3978 CAD per USD**.

The program was tested using the two $100,000 conversions required by the assignment.

### USD to CAD

```text
$100,000.00 USD = $139,780.00 CAD
```

### CAD to USD

```text
$100,000.00 CAD = $71,540.99 USD
```

Both calculations were successfully produced by the completed `ExchangeRates.py` program.

---

## Part 2: Vibe Coding

For Part 2 of the assignment, I used an AI model to independently generate another version of the exchange rate calculator.

### AI Model Used

**Claude Opus 5.5 by Anthropic**

The AI-generated program was saved separately as `ExchangeRatesAI.py`.

The AI-generated version reads the Bank of Canada CSV file, obtains the latest USD/CAD exchange rate from the final row, and performs conversions between USD and CAD based on user input.

---

## Prompt Used

The following prompt was provided to Claude:

> For part 2 of this assignement i want you to pbuild a code and a file and that does what faisal asks and wea are allowed to use ai so make it happend build me a file and nmae it waht the prof asks and do eveything is asks and i wasnt then the fasteset most effiecent way possible

This was the only prompt used to generate the Part 2 program.

---

## AI Program Results

The AI-generated version was tested using the same $100,000 conversions as the original program.

### USD to CAD

```text
Enter the amount to convert: 100000
Convert from (USD or CAD): USD
Convert to (USD or CAD): CAD
$100,000.00 USD = $139,780.00 CAD
(Exchange rate used: 1 USD = 1.3978 CAD)
```

### CAD to USD

```text
Enter the amount to convert: 100000
Convert from (USD or CAD): CAD
Convert to (USD or CAD): USD
$100,000.00 CAD = $71,540.99 USD
(Exchange rate used: 1 USD = 1.3978 CAD)
```

The AI-generated program therefore produced the same conversion results as my original program.

---

## Comparison of My Code and the AI-Generated Code

Both my original program and the AI-generated program successfully satisfy the main objective of the assignment. Both programs read the Bank of Canada CSV file, obtain the latest USD/CAD exchange rate, prompt the user for an amount and two currencies, and perform either a USD-to-CAD or CAD-to-USD conversion.

My original program more closely follows the class structure demonstrated in Lecture 4. For example, I stored the filename and USD/CAD exchange rate as private class members using double underscores. Lecture 4 explains that members preceded by two underscores are treated as private through Python's name-mangling behaviour (Habib, “Lecture #4”).

This approach is similar to Faisal Habib's `Bond` class, which stores the bond's face value, coupon rate, and term as private members before using public methods to perform calculations (Habib, “Lecture #4”).

The AI-generated version uses a slightly more modular structure. Instead of reading the entire exchange-rate file directly inside the constructor, it creates a separate `_load_latest_rate()` method. The constructor calls this method and stores the resulting exchange rate.

The AI version also processes the currency inputs using:

```python
.strip().upper()
```

This removes surrounding spaces and converts the input to uppercase before performing the conversion. In addition, the AI version includes a `ValueError` if the user enters a currency other than USD or CAD.

My original program does not include this additional validation because the assignment states that users can be assumed to provide legitimate input values.

Another difference is the way the main program is structured. My program places the user prompts directly under:

```python
if __name__ == "__main__":
```

whereas the AI-generated program places the user interaction inside a separate `main()` function and then calls that function from the `if __name__ == "__main__":` block.

The AI-generated program also displays an additional line showing the exchange rate used:

```text
(Exchange rate used: 1 USD = 1.3978 CAD)
```

This information was not specifically required for the calculation, but it provides additional transparency because the user can see the exact exchange rate used to produce the result.

Overall, both programs produce the same correct results. My original program is simpler and more closely follows the class structure and programming techniques demonstrated in the course lectures. The AI-generated program adds greater modularity, additional input handling, and more information in its output.

Comparing the two versions demonstrated that an AI model can create a functional solution efficiently, but the generated code may also introduce additional programming techniques that go beyond what is necessary for the assignment.

---

## Git and GitHub

The project was maintained using Git and GitHub. Lecture 1 explains that source code management allows programmers to track changes, manage different versions of code, collaborate, and share code through repositories (Habib, “Lecture #1”).

After making changes locally in Visual Studio Code, the files were added to Git, committed, and pushed to the remote GitHub repository. This follows the workflow introduced in Lecture 1, where `git add` is used to stage files, `git commit` records the changes, and `git push` sends the changes from the local repository to the remote repository (Habib, “Lecture #1”).

---

## GitHub Repository

https://github.com/Monkey-0D-Ace/FINE3300-2026-A1

---

## Works Cited

Habib, Faisal. “FINE 3300 Lecture #1.” *Python for Finance Professionals*, Schulich School of Business, York University, 2026. Course lecture slides.

Habib, Faisal. “FINE 3300 Lecture #2.” *Python for Finance Professionals*, Schulich School of Business, York University, 2026. Course lecture slides.

Habib, Faisal. “FINE 3300 Lecture #3.” *Python for Finance Professionals*, Schulich School of Business, York University, 2026. Course lecture slides.

Habib, Faisal. “FINE 3300 Lecture #4.” *Python for Finance Professionals*, Schulich School of Business, York University, 2026. Course lecture slides.

Anthropic. *Claude Opus 5.5*. Response to the prompt beginning “For part 2 of this assignement…,” 2026. Large language model.
