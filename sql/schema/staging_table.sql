-- ==========================================================
-- Staging Table
-- Raw import from Excel
-- ==========================================================

DROP TABLE IF EXISTS staging_telco_churn;

CREATE TABLE staging_telco_churn (

    customer_id VARCHAR(20),

    count INTEGER,

    country VARCHAR(100),

    state VARCHAR(100),

    city VARCHAR(100),

    zip_code INTEGER,

    lat_long VARCHAR(100),

    latitude DECIMAL(10,6),

    longitude DECIMAL(10,6),

    gender VARCHAR(20),

    senior_citizen VARCHAR(10),

    partner VARCHAR(10),

    dependents VARCHAR(10),

    tenure_months INTEGER,

    phone_service VARCHAR(10),

    multiple_lines VARCHAR(30),

    internet_service VARCHAR(30),

    online_security VARCHAR(30),

    online_backup VARCHAR(30),

    device_protection VARCHAR(30),

    tech_support VARCHAR(30),

    streaming_tv VARCHAR(30),

    streaming_movies VARCHAR(30),

    contract VARCHAR(50),

    paperless_billing VARCHAR(10),

    payment_method VARCHAR(50),

    monthly_charges DECIMAL(10,2),

    total_charges VARCHAR(30),

    churn_label VARCHAR(10),

    churn_value INTEGER,

    churn_score INTEGER,

    cltv INTEGER,

    churn_reason TEXT

);

TRUNCATE TABLE staging_telco_churn;