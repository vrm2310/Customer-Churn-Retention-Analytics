-- ==========================================================
-- CHURN DRIVERS
-- Contract × Internet Service
-- ==========================================================

SELECT

    b.contract,

    s.internet_service,

    COUNT(*) AS total_customers,

    SUM(CASE WHEN c.churn_label THEN 1 ELSE 0 END)
        AS churned_customers,

    ROUND(
        100.0 *
        SUM(CASE WHEN c.churn_label THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percent,

    ROUND(AVG(b.monthly_charges),2) AS avg_monthly_charge

FROM billing b

JOIN services s
ON b.customer_id = s.customer_id

JOIN churn c
ON b.customer_id = c.customer_id

GROUP BY

    b.contract,
    s.internet_service

HAVING COUNT(*) >= 50

ORDER BY churn_rate_percent DESC;

-- ==========================================================
-- CONTRACT × TECH SUPPORT
-- ==========================================================

SELECT

    b.contract,

    s.tech_support,

    COUNT(*) AS total_customers,

    SUM(CASE WHEN c.churn_label THEN 1 ELSE 0 END)
        AS churned_customers,

    ROUND(
        100.0 *
        SUM(CASE WHEN c.churn_label THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percent

FROM billing b

JOIN services s
ON b.customer_id = s.customer_id

JOIN churn c
ON b.customer_id = c.customer_id

GROUP BY

    b.contract,
    s.tech_support

HAVING COUNT(*) >= 50

ORDER BY churn_rate_percent DESC;

-- ==========================================================
-- TENURE ANALYSIS
-- ==========================================================

SELECT

CASE

WHEN tenure_months <= 12 THEN '0-12 Months'

WHEN tenure_months <= 24 THEN '13-24 Months'

WHEN tenure_months <= 48 THEN '25-48 Months'

ELSE '49+ Months'

END AS tenure_band,

COUNT(*) AS total_customers,

SUM(CASE WHEN c.churn_label THEN 1 ELSE 0 END)
AS churned_customers,

ROUND(
100.0 *
SUM(CASE WHEN c.churn_label THEN 1 ELSE 0 END)
/ COUNT(*),
2
) AS churn_rate_percent

FROM billing b

JOIN churn c
ON b.customer_id = c.customer_id

GROUP BY tenure_band

ORDER BY churn_rate_percent DESC;