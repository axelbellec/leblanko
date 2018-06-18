import os

import pytest

from tests.config import QUERIES_PATH
from tests.utils import normalize_query
from leblanko.parser import TableFinder


@pytest.fixture
def query_block_comments():
    table_finder = TableFinder()
    query_path = os.path.join(QUERIES_PATH, "query_block_comments.sql")
    return table_finder._read_query(query_path)


@pytest.fixture
def query_without_block_comments():
    query = """
        SELECT *
        FROM Customers;
    """
    return normalize_query(query)


@pytest.fixture
def query_whole_line_comments():
    table_finder = TableFinder()
    query_path = os.path.join(QUERIES_PATH, "query_whole_line_comments.hql")
    return table_finder._read_query(query_path)


@pytest.fixture
def query_without_whole_line_comments():
    query = """
        SELECT col1
        FROM (
            SELECT col1, SUM(col2) AS col2sum
            FROM t1
            GROUP BY col1
        ) t2
        WHERE t2.col2sum > 10
    """
    return normalize_query(query)


@pytest.fixture
def query_inline_comments():
    table_finder = TableFinder()
    query_path = os.path.join(QUERIES_PATH, "query_inline_comments.sql")
    return table_finder._read_query(query_path).splitlines()


@pytest.fixture
def query_without_inline_comments():
    query = """
        SELECT a.val1, a.val2, b.val, c.val
        FROM a JOIN b ON (a.key = b.key)
            LEFT OUTER JOIN c ON (a.key = c.key)
    """
    return normalize_query(query)


@pytest.fixture
def simple_query():
    table_finder = TableFinder()
    query_path = os.path.join(QUERIES_PATH, "query_simple.sql")
    return table_finder._read_query(query_path)


@pytest.fixture
def simple_query_tokens():
    return ["SELECT", "*", "FROM", "mytable"]
