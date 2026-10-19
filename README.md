# ST211 - Automated Software Testing

Repository containing quizzes, assignments, and weekly lab exercises for **192-211 Automated Software Testing**.

**Author:** Sai Wanna Htoo (6705140028)

---

## Repository Structure

```text
.
├── README.md
├── Roman_Numeral_Converter/              # Group exercise: Roman numeral converter with unit tests
│   ├── source/
│   │   ├── __init__.py
│   │   └── roman.py
│   └── tests/
│       └── test_roman.py
├── quiz-01/                              # Practical Quiz 01 template
│   ├── README.md
│   ├── solution.py
│   └── test_solution.py
├── quiz-02/                              # Practical Quiz 02 template
│   ├── README.md
│   ├── solution.py
│   └── test_solution.py
├── week_01/                              # Introduction to pytest
│   └── test_first.py
├── week_02/                              # Core testing principles & patterns
│   ├── aaa_pattern/                      # Arrange-Act-Assert testing pattern
│   │   ├── bank.py
│   │   └── test_bank.py
│   ├── boundary_testing/                 # Boundary value analysis
│   │   ├── grades.py
│   │   └── test_grades.py
│   ├── positive_negative/                # Positive & negative test cases
│   │   ├── test_negative.py
│   │   ├── test_positive.py
│   │   └── validators.py
│   ├── test_independence/                # Test isolation and independence
│   │   ├── test_dependent.py
│   │   └── test_independent.py
│   └── test_naming/                      # Descriptive test naming conventions
│       └── test_named.py
├── week_03/                              # Assertions & test organization
│   ├── assertions/                       # Float approx and collection assertions
│   │   ├── test_collections.py
│   │   └── test_floats.py
│   └── test_classes/                     # Grouping tests using test classes
│       ├── shopping.py
│       └── test_shopping.py
├── week_04/                              # Markers, skips, and fixtures
│   ├── Skipping_and_expected_failures/   # Skip conditions, xfail, strict mode
│   │   ├── conditional_skip.py
│   │   ├── pytest.ini
│   │   ├── test_skips.py
│   │   ├── test_strict.py
│   │   └── test_xfail.py
│   ├── Using_Markers/                    # Custom markers (smoke, slow, regression)
│   │   ├── pytest.ini
│   │   └── test_markers.py
│   └── fixture_lab/                      # Pytest fixtures and teardown
│       ├── bank.py
│       └── test_after.py
└── week_05_06/                           # Parameterized & data-driven testing
    ├── README.md
    └── param_lab/
        ├── discount_testing/             # Discount calculator parameterization & IDs
        │   ├── discount.py
        │   ├── test_custom_ids.py
        │   ├── test_default_ids.py
        │   ├── test_discount.py
        │   ├── test_discount_errors.py
        │   ├── test_param_ids.py
        │   └── test_param_marks.py
        ├── logins.csv                    # CSV test dataset
        ├── mathutils.py                  # Math utility functions
        ├── test_browsers.py              # Multi-parameter test matrix
        ├── test_cases.json               # JSON test dataset
        ├── test_csv_driven.py            # Data-driven tests from CSV
        ├── test_data_driven.py           # Data-driven tests from JSON
        ├── test_factorial.py             # Parameterized factorial testing
        ├── test_multi.py                 # Multiple parameters
        ├── test_param.py                 # Basic @pytest.mark.parametrize
        ├── test_param_fixture.py         # Parameterized fixtures
        └── validate.py                   # Validation functions
```

---

## Overview of Contents

### Weekly Labs

- **`week_01` — Getting Started with Pytest**
  - First pytest test functions, assertion basics, and test discovery.

- **`week_02` — Test Design Principles**
  - **AAA Pattern (`aaa_pattern/`):** Structuring tests cleanly into Arrange, Act, and Assert phases.
  - **Boundary Testing (`boundary_testing/`):** Testing edge and boundary conditions (e.g., score thresholds for grading).
  - **Positive & Negative Testing (`positive_negative/`):** Verifying valid inputs and asserting expected exceptions on invalid inputs.
  - **Test Independence (`test_independence/`):** Ensuring tests run in isolation without depending on shared mutable state.
  - **Test Naming (`test_naming/`):** Using clear, descriptive naming conventions to document expected test outcomes.

- **`week_03` — Assertions and Test Classes**
  - **Assertions (`assertions/`):** Floating-point assertions using `pytest.approx()` and verifying collections (lists, dicts, sets).
  - **Test Classes (`test_classes/`):** Organizing related test cases inside test classes for cleaner suite architecture.

- **`week_04` — Advanced Pytest Controls & Fixtures**
  - **Skipping & Expected Failures (`Skipping_and_expected_failures/`):** Skipping tests with `@pytest.mark.skip` / `@pytest.mark.skipif`, and handling expected failures with `@pytest.mark.xfail(strict=True)`.
  - **Custom Markers (`Using_Markers/`):** Registering and applying custom test markers (`smoke`, `slow`, `regression`) via `pytest.ini`.
  - **Fixtures (`fixture_lab/`):** Reusable test setup and teardown management using pytest fixtures and `yield`.

- **`week_05_06` — Parameterized & Data-Driven Testing**
  - **Parameterized Tests (`param_lab/`):** Running identical test logic across diverse input/output combinations using `@pytest.mark.parametrize`.
  - **Custom Identifiers & Parameter Marks (`discount_testing/`):** Customizing test IDs (`ids=...`), dynamic ID functions, and tagging individual parameter sets with `pytest.param(..., marks=...)`.
  - **Parameterized Fixtures (`test_param_fixture.py`):** Supplying multiple parameter configurations to fixtures using `params=[...]`.
  - **Data-Driven Testing (`test_data_driven.py`, `test_csv_driven.py`):** Loading test cases from external files (`test_cases.json` and `logins.csv`).

### Quizzes & Group Projects

- **`quiz-01` & `quiz-02`:** Templates
- **`Roman_Numeral_Converter`:** Group project implementing Roman numeral conversion with unit test coverage.

---

## Running Tests

You can run tests using `pytest` (or `python3 -m pytest`).

### Run Specific Exercises

Because some exercises use relative paths for data files or module imports, execute them from their respective directory or specify their path:

```bash
pytest
```