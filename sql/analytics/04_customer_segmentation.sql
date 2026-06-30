-- ==========================================================
-- GENDER ANALYSIS
-- ==========================================================

SELECT

    c.gender,

    COUNT(*) AS total_customers,

    SUM(CASE WHEN ch.churn_label THEN 1 ELSE 0 END)
        AS churned_customers,

    ROUND(
        100.0 *
        SUM(CASE WHEN ch.churn_label THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percent,

    ROUND(AVG(b.cltv),2) AS avg_cltv

FROM customers c

JOIN churn ch
ON c.customer_id = ch.customer_id

JOIN billing b
ON c.customer_id = b.customer_id

GROUP BY c.gender

ORDER BY churn_rate_percent DESC;

-- ==========================================================
-- SENIOR CITIZEN ANALYSIS
-- ==========================================================

SELECT

    senior_citizen,

    COUNT(*) AS total_customers,

    SUM(CASE WHEN ch.churn_label THEN 1 ELSE 0 END)
        AS churned_customers,

    ROUND(
        100.0 *
        SUM(CASE WHEN ch.churn_label THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percent,

    ROUND(AVG(b.cltv),2) AS avg_cltv

FROM customers c

JOIN churn ch
ON c.customer_id = ch.customer_id

JOIN billing b
ON c.customer_id = b.customer_id

GROUP BY senior_citizen

ORDER BY churn_rate_percent DESC;

-- ==========================================================
-- PARTNER ANALYSIS
-- ==========================================================

SELECT

    partner,

    COUNT(*) AS total_customers,

    SUM(CASE WHEN ch.churn_label THEN 1 ELSE 0 END)
        AS churned_customers,

    ROUND(
        100.0 *
        SUM(CASE WHEN ch.churn_label THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percent,

    ROUND(AVG(b.cltv),2) AS avg_cltv

FROM customers c

JOIN churn ch
ON c.customer_id = ch.customer_id

JOIN billing b
ON c.customer_id = b.customer_id

GROUP BY partner

ORDER BY churn_rate_percent DESC;

-- ==========================================================
-- DEPENDENTS ANALYSIS
-- ==========================================================

SELECT

    dependents,

    COUNT(*) AS total_customers,

    SUM(CASE WHEN ch.churn_label THEN 1 ELSE 0 END)
        AS churned_customers,

    ROUND(
        100.0 *
        SUM(CASE WHEN ch.churn_label THEN 1 ELSE 0 END)
        / COUNT(*),
        2
    ) AS churn_rate_percent,

    ROUND(AVG(b.cltv),2) AS avg_cltv

FROM customers c

JOIN churn ch
ON c.customer_id = ch.customer_id

JOIN billing b
ON c.customer_id = b.customer_id

GROUP BY dependents

ORDER BY churn_rate_percent DESC;