SELECT a.val1, a.val2, b.val, c.val
FROM a JOIN b ON (a.key = b.key) -- compute join
    LEFT OUTER JOIN c ON (a.key = c.key)
