-- ==========================================================
-- CONTRACT RETENTION ANALYSIS
-- ==========================================================

SELECT
    b.contract,

    COUNT(*) AS total_customers,

    SUM(CASE WHEN c.churn_label THEN 1 ELSE 0 END) AS churned_customers,

    ROUND(
        100.0 * SUM(CASE WHEN c.churn_label THEN 1 ELSE 0 END) / COUNT(*),
        2
    ) AS churn_rate_percent,

    ROUND(AVG(b.monthly_charges), 2) AS avg_monthly_charges,

    ROUND(AVG(b.cltv), 2) AS avg_cltv

FROM billing b
JOIN churn c
ON b.customer_id = c.customer_id

GROUP BY b.contract

ORDER BY churn_rate_percent DESC;