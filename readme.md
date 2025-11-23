# 📘 number_in_words

Convert integers into readable English words – simple, fast, and dependency-free.

[![PyPI version](https://img.shields.io/pypi/v/number_in_words.svg)](https://pypi.org/project/number_in_words/)
[![Python versions](https://img.shields.io/pypi/pyversions/number_in_words.svg)](https://pypi.org/project/number_in_words/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Overview

**number_in_words** is a lightweight Python package that converts numbers into English words.
It supports values from **0** up to **billions**, formatted just like humans speak.

✔ No dependencies
✔ Fast and accurate
✔ Easy to import and use
✔ Clean modular implementation

---

## Installation

Install using pip:

```bash
pip install number_in_words
```

---

## Usage

### Basic example

```python
import number_in_words as nw

print(nw.num(45))        # forty five
print(nw.num(2024))      # two thousand twenty four
print(nw.num(987654321)) # nine hundred eighty seven million six hundred fifty four thousand three hundred twenty one
```

### Importing the function directly

```python
from number_in_words import num

print(num(123))  # one hundred twenty three
```

---

## Supported Ranges

| Range                 | Example Output                    |
| --------------------- | --------------------------------- |
| 0–13                  | zero → thirteen                   |
| 14–19                 | fourteen → nineteen               |
| 20–99                 | twenty one, ninety nine           |
| 100–999               | one hundred fifty two             |
| 1,000–999,999         | twelve thousand three hundred ten |
| 1,000,000–999,999,999 | ninety eight million ...          |
| 1,000,000,000+        | up to billions                    |

---

## Project Structure

```
number_in_words/
    __init__.py
    main.py
    ds.py
    tens.py
    hundreds.py
    thousands.py
    millions.py
    billions.py
```

Each module handles one specific number range, making the code easy to maintain and extend.

---

## API Reference

### `num(x: int) -> str`

Convert any integer to its English representation.

**Example:**

```python
from number_in_words import num
num(1200305)
```

Output:

```
one million two hundred thousand three hundred five
```

---

## Contributing

Contributions, issues, and pull requests are welcome.

If you find this package useful, please consider giving the repository a ⭐ on  [GitHub!](https://github.com/Saumya-Kanti-Sarma/number_in_words)

---

## Contact

**Author:** Saumya Kanti Sarma
Email: **[work.saumyasarma@gmail.com](mailto:work.saumyasarma@gmail.com)**
Instagram: **[saumya__sarma](https://www.instagram.com/saumya__sarma/)**

Feel free to reach out for collaboration, questions, or feedback.

