-- ==========================================================
-- TOP CITIES BY CUSTOMER COUNT
-- ==========================================================

SELECT

    g.city,

    COUNT(*) AS total_customers,

    SUM(CASE WHEN c.churn_label THEN 1 ELSE 0 END)
        AS churned_customers,

    ROUND(
        100.0 *
        SUM(CASE WHEN c.churn_label THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percent,

    ROUND(SUM(b.monthly_charges),2)
        AS monthly_revenue

FROM geography g

JOIN churn c
ON g.customer_id = c.customer_id

JOIN billing b
ON g.customer_id = b.customer_id

GROUP BY g.city

HAVING COUNT(*) >= 20

ORDER BY churn_rate_percent DESC,
         total_customers DESC;

-- ==========================================================
-- TOP REVENUE CITIES
-- ==========================================================

SELECT

    city,

    COUNT(*) AS customers,

    ROUND(SUM(monthly_charges),2)
        AS monthly_revenue,

    ROUND(AVG(monthly_charges),2)
        AS avg_monthly_charge,

    ROUND(AVG(cltv),2)
        AS avg_cltv

FROM geography g

JOIN billing b
ON g.customer_id = b.customer_id

GROUP BY city

HAVING COUNT(*) >= 20

ORDER BY monthly_revenue DESC;