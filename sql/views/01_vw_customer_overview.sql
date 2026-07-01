CREATE OR REPLACE VIEW vw_customer_overview AS

SELECT
    COUNT(*) AS total_customers,

    SUM(
        CASE
            WHEN churn_label = FALSE THEN 1
            ELSE 0
        END
    ) AS active_customers,

    SUM(
        CASE
            WHEN churn_label = TRUE THEN 1
            ELSE 0
        END
    ) AS churned_customers,

    ROUND(
        100.0 *
        SUM(CASE WHEN churn_label THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percent,

    ROUND(
        AVG(b.monthly_charges),
        2
    ) AS average_monthly_charges,

    ROUND(
        AVG(b.cltv),
        2
    ) AS average_cltv

FROM customers c

JOIN billing b
ON c.customer_id = b.customer_id

JOIN churn ch
ON c.customer_id = ch.customer_id;

SELECT *
FROM vw_customer_overview;