-- ==========================================================
-- Populate Billing Table
-- ==========================================================

TRUNCATE TABLE billing;

INSERT INTO billing (
    customer_id,
    tenure_months,
    contract,
    paperless_billing,
    payment_method,
    monthly_charges,
    total_charges,
    cltv
)

SELECT

    customer_id,

    tenure_months,

    contract,

    (paperless_billing = 'Yes'),

    payment_method,

    monthly_charges,

    -- Convert blank or whitespace-only total_charges values to NULL
	CAST(NULLIF(TRIM(total_charges), '') AS DECIMAL(10,2)),

    cltv

FROM staging_telco_churn;

SELECT COUNT(*)
FROM billing;

SELECT *
FROM billing
LIMIT 10;

SELECT
    COUNT(*) AS null_total_charges
FROM billing
WHERE total_charges IS NULL;