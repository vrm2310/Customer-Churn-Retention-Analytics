-- ==========================================================
-- Populate Services Table
-- ==========================================================

TRUNCATE TABLE services;

INSERT INTO services (
    customer_id,
    phone_service,
    multiple_lines,
    internet_service,
    online_security,
    online_backup,
    device_protection,
    tech_support,
    streaming_tv,
    streaming_movies
)

SELECT

    customer_id,

    (phone_service = 'Yes'),

    multiple_lines,

    internet_service,

    online_security,

    online_backup,

    device_protection,

    tech_support,

    streaming_tv,

    streaming_movies

FROM staging_telco_churn;

SELECT COUNT(*)
FROM services;

SELECT *
FROM services
LIMIT 10;