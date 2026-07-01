CREATE OR REPLACE VIEW vw_partner AS

SELECT
    c.partner,

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

    ROUND(AVG(b.monthly_charges),2) AS avg_monthly_charges,

    ROUND(AVG(b.cltv),2) AS avg_cltv

FROM customers c

JOIN billing b
ON c.customer_id = b.customer_id

JOIN churn ch
ON c.customer_id = ch.customer_id

GROUP BY c.partner

ORDER BY churn_rate_percent DESC;

SELECT * FROM vw_partner;