import os

import pytest

from leblanko.parser import TableFinder
from tests.utils import normalize_query
from tests.config import QUERIES_PATH
from tests.fixtures import (
    query_block_comments,
    query_without_block_comments,
    query_whole_line_comments,
    query_without_whole_line_comments,
    query_inline_comments,
    query_without_inline_comments,
    simple_query,
    simple_query_tokens,
)


def test_read_query(simple_query):
    assert normalize_query(simple_query) == "SELECT * FROM mytable"


def test_block_comments(query_block_comments, query_without_block_comments):
    table_finder = TableFinder()
    cleaned_query = table_finder._remove_block_comments(query_block_comments)
    assert normalize_query(cleaned_query) == query_without_block_comments


def test_whole_line_comments(
    query_whole_line_comments, query_without_whole_line_comments
):
    table_finder = TableFinder()
    cleaned_query = table_finder._remove_inline_comments(query_whole_line_comments)
    cleaned_query_str = normalize_query(" ".join(cleaned_query))
    assert cleaned_query_str == query_without_whole_line_comments


def test_inline_comments(query_inline_comments, query_without_inline_comments):
    table_finder = TableFinder()
    cleaned_query = table_finder._remove_trailing_characters(query_inline_comments)
    cleaned_query_str = normalize_query(cleaned_query)
    assert cleaned_query_str == query_without_inline_comments


def test_split_query_terms_into_tokens(simple_query, simple_query_tokens):
    table_finder = TableFinder()
    query_tokens = table_finder._split_query_terms_into_tokens(simple_query)
    assert query_tokens == simple_query_tokens


@pytest.mark.parametrize(
    "query_file, table_names",
    [
        ("query_alter_table.hql", ["table_name"]),
        ("query_block_comments.sql", ["customers"]),
        ("query_create_table.hql", ["page_view"]),
        ("query_inline_comments.sql", ["a", "b", "c"]),
        ("query_insert.hql", ["source_table_1", "source_table_2", "target_table"]),
        ("query_join.hql", ["a", "b", "c"]),
        ("query_select.hql", ["t1"]),
        ("query_simple.sql", ["mytable"]),
        ("query_union.hql", ["action_comment", "action_video", "users"]),
        ("query_whole_line_comments.hql", ["t1"]),
    ],
)
def test_tables_names(query_file, table_names):
    query_path = os.path.join(QUERIES_PATH, query_file)
    table_finder = TableFinder()
    sql_query = table_finder._read_query(query_path)
    parsed_tables = table_finder.get_tables_in_query(sql_query)
    assert parsed_tables == table_names
