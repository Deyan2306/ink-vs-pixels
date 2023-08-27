# Project Naming Conventions and Structure
This document outlines the coding conventions and project structure to be followed when contributing to this repository.

### Naming Conventions
#### Variable and Function Naming

* Use **snake_case** for variable and function names.
* Choose **descriptive** and **meaningful** names that reflect the purpose of the variable or function.

Example:
```python
# Good
sample_rate = 44100
process_data(input_data)

# Awful
sr = 44100
proc = input_data
```

### Class Naming
* Use **CamelCase** for class names.
* Keep class names **concise** and **indicative** of their purpose.

Example:
```python
class Manga:
    # class implementation...
```

### Static Constants
* Place static constants in a file named `dspconst.py` at the `/utils` directory.

Example:
```python
PAGES_COUNT = 198  # INT 
PRICE_PER_BOOK = 9.99 # FLOAT
```

### Methods
* Place the custom made functions in a file named `dspfunctions.py` and separate the topic sections with comments and explanations.

Example:
```python
### Price based functions
# --------------------------

# This method calculates the average page price based on the price of the book and the number of pages 
def average_page_price(book_price, pages_count):
    # function implementation...
```

### Project Structure
```
project_root/
│
├── classes/
│   ├── manga.py
│   ├── comic_book.py
│   └── ...
│
├── project.ipynb
├── utils/
│   ├── dspconst.py
│   ├── dspfunctions.py
│   └── ...
│
├── tests/
│   ├── function_tests.py
│   └── ...
│
├── .git/
│   └── ...
│
├── images/
│   └── ...
│
├── datasets/
│   └── ...
│
│── notes
│   ├── project_notes.ipynb
│   └── ...
│
├── .gitignore
├── README.md
├── CONVENTIONS.md
└── LICENSE
```

* Place class files in the `/classes` directory.
* `dspconst.py` contains static constants.
* DSP-related functions should be in the `dspfunctions.py` file.s
* Utilize the `/utils` directory for utility functions.
* Keep test files in the `/tests` directory.

### Images
* All of the images should be in the `/images` directory.

### Datasets
* All of the datasets should stay in the `/datasets` directory.
* Separated by topic in different folders.

### Conclusion
Adhering to these naming conventions and project structure will ensure consistent and maintainable code across the repository. All contributors are expected to follow these guidelines for a cohesive and collaborative development experience.

> Author: Deyan Sirakov