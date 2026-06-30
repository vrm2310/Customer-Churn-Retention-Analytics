-- ==========================================================
-- Populate Geography Table
-- ==========================================================

TRUNCATE TABLE geography;

INSERT INTO geography (
    customer_id,
    country,
    state,
    city,
    zip_code,
    latitude,
    longitude
)

SELECT

    customer_id,

    country,

    state,

    city,

    zip_code,

    latitude,

    longitude

FROM staging_telco_churn;

SELECT COUNT(*)
FROM geography;

SELECT *
FROM geography
LIMIT 10;