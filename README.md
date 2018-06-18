## Le Blanko


> Simple CLI tool to extract table names from query files.

![leblanko](docs/leblanko.gif)

<div align="center">
	<a href="https://travis-ci.org/axelbellec/leblanko"><img src="https://travis-ci.org/axelbellec/leblanko.svg?branch=master" alt="Build Status" /></a>
	<a href="https://coveralls.io/github/axelbellec/leblanko">
	<img src="https://coveralls.io/repos/github/axelbellec/leblanko/badge.svg" alt="Coverage Status"/>
	</a>
</div>

__`leblanko`__ provides an easy way to put accross a clearer summary of all SQL tables used in your project. 

## Installation

*TODO*: publish package to PYPI

Install the latest version of __`leblanko`__:
```bash
pip install git+https://github.com/axelbellec/leblanko.git
```

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

If you only want to scan a bunch of SQL files you can specify file extension:

```python
leblanko *.sql
```

## Tests

You can clone this repository:
```bash
git clone https://github.com/axelbellec/leblanko.git
```
Install test dependencies:
```bash
pip install -r dev-requirements.txt
``` 
Then, launch test suite:
```bash
./launch_tests.sh
```

