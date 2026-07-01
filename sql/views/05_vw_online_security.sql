CREATE OR REPLACE VIEW vw_online_security AS

SELECT
    s.online_security,

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
        AVG(b.monthly_charges),
        2
    ) AS avg_monthly_charges,

    ROUND(
        AVG(b.cltv),
        2
    ) AS avg_cltv

FROM services s

JOIN billing b
    ON s.customer_id = b.customer_id

JOIN churn ch
    ON s.customer_id = ch.customer_id

GROUP BY
    s.online_security

ORDER BY
    churn_rate_percent DESC;

SELECT *
FROM vw_online_security;