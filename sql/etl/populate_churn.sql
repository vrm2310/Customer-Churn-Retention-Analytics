-- ==========================================================
-- Populate Churn Table
-- ==========================================================

TRUNCATE TABLE churn;

INSERT INTO churn (
    customer_id,
    churn_label,
    churn_reason
)

SELECT

    customer_id,

    (churn_label = 'Yes'),

    churn_reason

FROM staging_telco_churn;

SELECT
    column_name,
    data_type
FROM information_schema.columns
WHERE table_name = 'churn'
ORDER BY ordinal_position;

SELECT COUNT(*)
FROM churn;

SELECT *
FROM churn
LIMIT 10;

SELECT
    churn_label,
    COUNT(*)
FROM churn
GROUP BY churn_label;