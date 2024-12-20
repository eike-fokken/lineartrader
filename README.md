# lineartrader

This app is used to solve the following problem:


We are given a number of different items, an initial stockpile we have for each item and
a number of possible (linear) trades, each removing a number of items and adding
a number of (different) items. Each trade can be done a number of times.
Naturally, these numbers must be a non-negative integers.

In addition we have goal: Maximize the number of one item.

# Installation

This package is managed with poetry. To install the package, please install
poetry, `pip install poetry`, and afterwards run inside the git repository:

```
poetry install
```


To run the realistic example, change into your virtual environment:

```
poetry shell
```

and run

```
pytest -s tests
```

