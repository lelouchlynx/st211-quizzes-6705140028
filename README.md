# 192-211 Automated Software Testing

## Student Information
- **Name:** Sai Wanna Htoo
- **Student ID:** 6705140028
- **Course:** 192-211 Automated Software Testing

---

## Overview
This repository contains weekly lab exercises, quizzes, and practical assignments for the **192-211 Automated Software Testing** course. It covers core unit testing principles, test design patterns, and test automation practices using Python and `pytest`.

## Repository Structure
- **`quiz-01/` & `quiz-02/`**: Course quizzes and solutions covering unit testing concepts.
- **`week_01/`**: Introduction to automated testing with `pytest`.
- **`week_02/`**: Core testing practices including:
  - AAA (Arrange-Act-Assert) pattern
  - Boundary value testing
  - Positive and negative testing
  - Test naming conventions
  - Test independence
- **`week_03/`**: Advanced testing concepts:
  - Custom assertions and error handling
  - Structuring tests using test classes
- **`Roman_Numeral_Converter/`**: Hands-on group activity and exercise on Roman numeral conversion and automated test suites.

## How to Run Tests
Ensure you have Python and `pytest` installed:
```bash
pip install pytest
```

Run all tests across the repository:
```bash
pytest
```

Run tests for a specific folder:
```bash
pytest week_02/
pytest quiz-01/
```