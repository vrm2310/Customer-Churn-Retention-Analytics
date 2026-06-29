-- ==========================================================
-- Customer Churn & Retention Analytics
-- Database Schema
-- ==========================================================

DROP TABLE IF EXISTS churn CASCADE;
DROP TABLE IF EXISTS billing CASCADE;
DROP TABLE IF EXISTS services CASCADE;
DROP TABLE IF EXISTS geography CASCADE;
DROP TABLE IF EXISTS customers CASCADE;

-- ==========================================================
-- Customers
-- ==========================================================

CREATE TABLE customers (
    customer_id VARCHAR(20) PRIMARY KEY,
    gender VARCHAR(10),
    senior_citizen BOOLEAN,
    partner BOOLEAN,
    dependents BOOLEAN
);

-- ==========================================================
-- Geography
-- ==========================================================

CREATE TABLE geography (
    customer_id VARCHAR(20) PRIMARY KEY,
    country VARCHAR(100),
    state VARCHAR(100),
    city VARCHAR(100),
    zip_code INTEGER,
    latitude DECIMAL(10,6),
    longitude DECIMAL(10,6),
    CONSTRAINT fk_geography_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

-- ==========================================================
-- Services
-- ==========================================================

CREATE TABLE services (
    customer_id VARCHAR(20) PRIMARY KEY,
    phone_service BOOLEAN,
    multiple_lines VARCHAR(30),
    internet_service VARCHAR(30),
    online_security VARCHAR(30),
    online_backup VARCHAR(30),
    device_protection VARCHAR(30),
    tech_support VARCHAR(30),
    streaming_tv VARCHAR(30),
    streaming_movies VARCHAR(30),
    CONSTRAINT fk_services_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

-- ==========================================================
-- Billing
-- ==========================================================

CREATE TABLE billing (
    customer_id VARCHAR(20) PRIMARY KEY,
    tenure_months INTEGER,
    contract VARCHAR(50),
    paperless_billing BOOLEAN,
    payment_method VARCHAR(50),
    monthly_charges DECIMAL(10,2),
    total_charges DECIMAL(10,2),
    cltv INTEGER,
    CONSTRAINT fk_billing_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

-- ==========================================================
-- Churn
-- ==========================================================

CREATE TABLE churn (
    customer_id VARCHAR(20) PRIMARY KEY,
    churn_label BOOLEAN,
    churn_reason TEXT,
    CONSTRAINT fk_churn_customer
        FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);