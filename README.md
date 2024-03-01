 This is a script that allows you to automate your python test suite

## Getting Started

First, install the required dependency:

```bash
pip install pytest
# and
pip install pytest-html
```

## Testing 
To begin the test, you need to run the python common with the name of the script and the location of the test suite, see sample below

```bash
python main.py test_calculator.py
```
Where **main.py** is the name of the script and **test_calculator.py** is the name of the test suite.

you can either run it by specifying the name of the test suite on the terminal or by 
editing the default test path on **line 49** in **main.py**
