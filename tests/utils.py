import re


def remove_extra_spaces(string):
    return re.sub("\s+", " ", string)


def normalize_query(formatted_query):
    return remove_extra_spaces(formatted_query).strip()
