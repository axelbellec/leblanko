SELECT col1 
--just keep col1 
FROM (
    SELECT col1, SUM(col2) AS col2sum
    FROM t1
    GROUP BY col1
) t2
# Filter on col2sum
WHERE t2.col2sum > 10
