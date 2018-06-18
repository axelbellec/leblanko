INSERT OVERWRITE TABLE target_table
SELECT name, id, category FROM source_table_1
UNION ALL
SELECT name, id, "Category159" as category FROM source_table_2
