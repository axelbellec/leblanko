import re
import glob
import os


class SQLParser(object):
    REGEX_BLOCK_COMMENT = re.compile(r"/\*[^*]*\*+(?:[^*/][^*]*\*+)*/")
    REGEX_WHOLE_LINE_COMMENT = re.compile(r"^\s*(--|#)")
    REGEX_TRAILING_LINE_COMMENT = re.compile(r"--|#")
    REGEX_TOKENS = re.compile(r"[\s)(;]+")

    @staticmethod
    def _scan_tokens(tokens):
        """ Scan tokens to return table names. """
        tables = set()
        get_next = False
        for token in tokens:
            if get_next:
                if token.lower() not in ["select", ""]:
                    tables.add(token)
                get_next = False
            get_next = token.lower() in ["from", "join", "with"]
        return list(tables)

    @classmethod
    def get_tables_in_query(cls, sql_query):
        """ Apply basic query formatting and then search 
            for potential table names. 
        """
        assert isinstance(sql_query, str)

        # Remove the /* */ comments
        sql_query = cls.REGEX_BLOCK_COMMENT.sub("", sql_query)

        # Remove whole line -- and # comments
        lines = [
            line
            for line in sql_query.splitlines()
            if not cls.REGEX_WHOLE_LINE_COMMENT.match(line)
        ]

        # Remove trailing -- and # comments
        sql_query = " ".join(
            [cls.REGEX_TRAILING_LINE_COMMENT.split(line)[0] for line in lines]
        )

        # Split on blanks, parens and semicolons
        tokens = cls.REGEX_TOKENS.split(sql_query)

        return cls._scan_tokens(tokens)

    @staticmethod
    def _read_query(filepath):
        """ Retrieve file content. """
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
