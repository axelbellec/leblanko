CREATE TABLE page_view
(
    viewTime INT,
    userid BIGINT,
    page_url STRING,
    referrer_url STRING,
    ip STRING
    COMMENT 'IP Address of the User'
)
PARTITIONED BY (dt STRING, country STRING)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY '\001'
STORED AS SEQUENCEFILE;