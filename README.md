# ECM2429-workshop-3-exercises

## A simple graphical user interface

### Exercises

1. Create a virutal environment and run the program ```mygui.py``` in ```mycode```

2. Install the packages listed in ```requirements.txt```

3. Use ```tox```  to test the program.

4. Generate HTML and PDF docs using Sphinx

5. Look at the test results - can you improve them?

## Resources

### Flake8

To install (venv recommended)
```sh
pip install flake8
```

To check all Python scripts in current directory
```sh
flake8 . --count --exit-zero --max-complexity=5  --statistics
```

### Pytest-cov
To install (venv recommended)

```sh
pip install pytest-cov
```

To get statistics for all tests
```
pytest --cov=. tests
```

### Tox

Example
<https://github.com/PyCQA/flake8/blob/main/tox.ini>

### Docstring generator

<https://marketplace.visualstudio.com/items?itemName=njpwerner.autodocstring>

### Sphinx

To install

```sh
python -m venv .venv
source .venv/bin/activate
python -m pip install sphinx
python -p pip install rinohtype
```

To create docs

```sh
make.bat html
make.bat rinoh
```

<https://www.sphinx-doc.org/en/master/tutorial/getting-started.html>

### Autodoc

<https://eikonomega.medium.com/getting-started-with-sphinx-autodoc-part-1-2cebbbca5365>

<http://www.pythondoc.com/sphinx/ext/autodoc.html>