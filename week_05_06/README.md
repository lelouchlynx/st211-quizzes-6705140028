# Week 5 & 6: Parameterized & Data-Driven Testing

This folder contains lab exercises and practical tasks for Weeks 5 and 6 of **ST211 Automated Software Testing**, focusing on parameterized testing, custom test IDs, parameterized fixtures, and data-driven testing using pytest.

---

## 📁 Folder Structure

```text
week_05_06/
├── README.md
└── param_lab/
    ├── discount_testing/             # Discount calculator parameterization & IDs
    │   ├── discount.py               # Discount calculation logic
    │   ├── test_custom_ids.py        # Custom test IDs with ids=[...]
    │   ├── test_default_ids.py       # Default pytest parameter IDs
    │   ├── test_discount.py          # Parameterized discount tests
    │   ├── test_discount_errors.py   # Exception testing with pytest.raises
    │   ├── test_param_ids.py         # Dynamic test ID generation using functions
    │   └── test_param_marks.py       # Applying marks to parameters via pytest.param
    ├── logins.csv                    # CSV test dataset
    ├── mathutils.py                  # Math utility functions (factorial, etc.)
    ├── test_browsers.py              # Multi-variable parameterization (browser matrix)
    ├── test_cases.json               # JSON test dataset
    ├── test_csv_driven.py            # Data-driven tests reading from logins.csv
    ├── test_data_driven.py           # Data-driven tests reading from test_cases.json
    ├── test_factorial.py             # Parameterized factorial calculations
    ├── test_multi.py                 # Multiple parameter sets (Cartesian product)
    ├── test_param.py                 # Basic @pytest.mark.parametrize usage
    ├── test_param_fixture.py         # Parameterized fixtures using params=[...]
    └── validate.py                   # Input validation helpers
```

---

## 🧪 Key Topics Covered

1. **Basic Parameterization (`test_param.py`, `test_factorial.py`)**
   - Running identical test functions against multiple input/output pairs using `@pytest.mark.parametrize`.

2. **Multiple Parameter Combinations (`test_multi.py`, `test_browsers.py`)**
   - Stacking multiple `@pytest.mark.parametrize` decorators to test matrix combinations (Cartesian products).

3. **Custom Test IDs and Parameter Marking (`discount_testing/`)**
   - Customizing test failure readability using custom IDs (`ids=[...]` or callable formatting functions).
   - Marking individual parameter tuples with `pytest.param(..., marks=...)`.

4. **Parameterized Fixtures (`test_param_fixture.py`)**
   - Defining `@pytest.fixture(params=[...])` to automatically repeat dependent tests across fixture configurations.

5. **Data-Driven Testing (`test_data_driven.py`, `test_csv_driven.py`)**
   - Decoupling test data from test code by dynamically loading test cases from `test_cases.json` and `logins.csv`.

---

## 🚀 Running Tests

Run pytest inside the `param_lab/` directory so relative data files (`logins.csv`, `test_cases.json`) resolve correctly:

```bash
cd param_lab
pytest -v
```