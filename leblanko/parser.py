import re
import glob
import os


class TableFinder(object):
    REGEX_BLOCK_COMMENT = re.compile(r"/\*[^*]*\*+(?:[^*/][^*]*\*+)*/")
    REGEX_WHOLE_LINE_COMMENT = re.compile(r"^\s*(--|#)")
    REGEX_TRAILING_LINE_COMMENT = re.compile(r"--|#")
    REGEX_TOKENS = re.compile(r"[\s)(;]+")
    TABLE_PREDECESSOR = ["from", "join", "with", "table", "view", "partitions"]

    @classmethod
    def _scan_tokens(cls, tokens):
        """ Scan tokens to return table names. """
        tables = set()
        get_next = False
        for token in tokens:
            if get_next:
                if token.lower() not in ["select", ""]:
                    tables.add(token.lower())
                get_next = False
            get_next = token.lower() in cls.TABLE_PREDECESSOR
        return list(tables)

    @classmethod
    def _remove_block_comments(cls, sql_query):
        """ Remove block comments like '/* */'. """
        return cls.REGEX_BLOCK_COMMENT.sub("", sql_query)

    @classmethod
    def _remove_inline_comments(cls, sql_query):
        """ Remove inline comments like '#' or '--'. """
        return [
            line
            for line in sql_query.splitlines()
            if not cls.REGEX_WHOLE_LINE_COMMENT.match(line)
        ]

    @classmethod
    def _remove_trailing_characters(cls, sql_lines):
        """ Remove trailing characters like '--' or '#'. """
        return " ".join(
            [cls.REGEX_TRAILING_LINE_COMMENT.split(line)[0] for line in sql_lines]
        )

    @classmethod
    def _split_query_terms_into_tokens(cls, sql_query):
        """ Split query terms into tokens.
            e.g.: 
                SELECT *    
                FROM mytable
            -> ['SELECT', '*', 'FROM', 'mytable']
        """
        return cls.REGEX_TOKENS.split(sql_query)

    @classmethod
    def get_tables_in_query(cls, sql_query):
        """ Apply basic query formatting and then search
            for potential table names.
        """
        assert isinstance(sql_query, str)

        # Remove the /* */ comments
        sql_query = cls._remove_block_comments(sql_query)

        # Remove whole line -- and # comments
        lines = cls._remove_inline_comments(sql_query)

        # Remove trailing -- and # comments
        sql_query = cls._remove_trailing_characters(lines)

        # Split on blanks, parens and semicolons
        tokens = cls._split_query_terms_into_tokens(sql_query)

        # Find tables into tokens
        tables = cls._scan_tokens(tokens)

        return list(sorted(tables))

    @staticmethod
    def _read_query(filepath):
        """ Retrieve query file content. """
        assert os.path.exists(filepath)
        with open(filepath, "r") as f:
            return f.read()

    @classmethod
    def inspect(cls, pattern):
        """ Get all files matching pattern and extract SQL tables. """
        result = dict()

        if os.path.isdir(pattern):
            pattern = os.path.join(pattern, "**")

        for filepath in sorted(glob.glob(pattern, recursive=True)):
            if os.path.isdir(filepath):
                continue
            sql_query = cls._read_query(filepath)
            parsed_tables = cls.get_tables_in_query(sql_query)
            result[filepath] = parsed_tables
        return result

    @classmethod
    def parse_files(cls, filepaths):
        """ Inspect each filepath iteratively.  """
        parsed_tables = dict()
        for filepath in sorted(filepaths):
            parsed_file = cls.inspect(filepath)
            parsed_tables.update(parsed_file)
        return parsed_tables
