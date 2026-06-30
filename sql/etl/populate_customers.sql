-- ==========================================================
-- Populate Customers Table
-- ==========================================================

TRUNCATE TABLE customers CASCADE;

INSERT INTO customers (
    customer_id,
    gender,
    senior_citizen,
    partner,
    dependents
)

SELECT
    customer_id,

    gender,

    CASE
        WHEN senior_citizen = 'Yes' THEN TRUE
        ELSE FALSE
    END,

    CASE
        WHEN partner = 'Yes' THEN TRUE
        ELSE FALSE
    END,

    CASE
        WHEN dependents = 'Yes' THEN TRUE
        ELSE FALSE
    END

FROM staging_telco_churn;