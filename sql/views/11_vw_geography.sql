CREATE OR REPLACE VIEW vw_geography AS

SELECT
    g.city,

    COUNT(*) AS total_customers,

    SUM(
        CASE
            WHEN ch.churn_label = TRUE THEN 1
            ELSE 0
        END
    ) AS churned_customers,

    ROUND(
        100.0 *
        SUM(CASE WHEN ch.churn_label THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percent,

    ROUND(
        SUM(b.monthly_charges),
        2
    ) AS monthly_revenue,

    ROUND(
        AVG(b.cltv),
        2
    ) AS avg_cltv

FROM geography g

JOIN billing b
    ON g.customer_id = b.customer_id

JOIN churn ch
    ON g.customer_id = ch.customer_id

GROUP BY
    g.city

HAVING COUNT(*) >= 20

ORDER BY
    monthly_revenue DESC;

SELECT * FROM vw_geography;

SELECT *
FROM geography
LIMIT 5;