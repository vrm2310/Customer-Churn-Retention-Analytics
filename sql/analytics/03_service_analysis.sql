-- ==========================================================
-- INTERNET SERVICE ANALYSIS
-- ==========================================================

SELECT

    s.internet_service,

    COUNT(*) AS total_customers,

    SUM(CASE WHEN c.churn_label THEN 1 ELSE 0 END) AS churned_customers,

    ROUND(
        100.0 * SUM(CASE WHEN c.churn_label THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percent,

    ROUND(AVG(b.monthly_charges),2) AS avg_monthly_charges,

    ROUND(AVG(b.cltv),2) AS avg_cltv

FROM services s

JOIN churn c
ON s.customer_id = c.customer_id

JOIN billing b
ON s.customer_id = b.customer_id

GROUP BY s.internet_service

ORDER BY churn_rate_percent DESC;

-- ==========================================================
-- TECH SUPPORT ANALYSIS
-- ==========================================================

SELECT

    s.tech_support,

    COUNT(*) AS total_customers,

    SUM(CASE WHEN c.churn_label THEN 1 ELSE 0 END) AS churned_customers,

    ROUND(
        100.0 * SUM(CASE WHEN c.churn_label THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percent

FROM services s

JOIN churn c
ON s.customer_id = c.customer_id

GROUP BY s.tech_support

ORDER BY churn_rate_percent DESC;

-- ==========================================================
-- ONLINE SECURITY ANALYSIS
-- ==========================================================

SELECT

    s.online_security,

    COUNT(*) AS total_customers,

    SUM(CASE WHEN c.churn_label THEN 1 ELSE 0 END) AS churned_customers,

    ROUND(
        100.0 * SUM(CASE WHEN c.churn_label THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percent

FROM services s

JOIN churn c
ON s.customer_id = c.customer_id

GROUP BY s.online_security

ORDER BY churn_rate_percent DESC;