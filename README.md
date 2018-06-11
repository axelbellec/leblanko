## Le Blanko

> Simple CLI tool to extract table names from query files.

![leblanko](docs/leblanko.gif)

## Installation

*TODO*: publish package to PYPI

## Dependencies

No external dependencies: __`leblanko`__ only use python internal libraries like [`os`](https://docs.python.org/3.5/library/os.html), [`re`](https://docs.python.org/3.5/library/re.html) and [`argparse`](https://docs.python.org/3.5/library/argparse.html).

## Usage

Extract SQL table names inside `query.sql`. 

```python
leblanko query.sql
```

__`leblanko`__ supports pathnames so you can use it to inspect recursively an entire folder, e.g.:

```python
leblanko queries/
```