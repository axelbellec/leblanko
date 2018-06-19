import json
from collections import OrderedDict


class Exporter(object):
    def export(self, data):
        raise NotImplementedError

    def _get_distinct_tables(self, data):
        list_of_tables = sum([tables_names for _, tables_names in data.items()], [])
        return list(OrderedDict.fromkeys(list_of_tables))


class DefaultExporter(Exporter):
    def export(self, data):
        return "\n".join(
            [
                "--- {:>15}\n\t{}".format(filepath, tables)
                for filepath, tables in data.items()
            ]
        )


class JsonExporter(Exporter):
    def export(self, data):
        json_data = {
            "distinct_tables": self._get_distinct_tables(data),
            "summary": data,
        }
        return json.dumps(json_data, indent=2, sort_keys=True, ensure_ascii=True)


class MarkdownExporter(Exporter):
    TEMPLATE = "__Tables dependencies__: \n{}\n" + "\n*__Distinct tables used__*: {}"

    def export(self, data):
        return self._render_template(data)

    @staticmethod
    def _format_tables_names(tables_names):
        return ", ".join(["`{}`".format(table_name) for table_name in tables_names])

    def _add_line_entry(self, filepath, tables_used):
        return "- *{filepath}*: {tables_fmt}".format(
            filepath=filepath, tables_fmt=self._format_tables_names(tables_used)
        )

    def _render_template(self, data):
        list_of_tables = "\n".join(
            [
                self._add_line_entry(filepath, tables_used)
                for filepath, tables_used in data.items()
            ]
        )
        distinct_tables_used = self._format_tables_names(
            self._get_distinct_tables(data)
        )
        return self.TEMPLATE.format(list_of_tables, distinct_tables_used)
