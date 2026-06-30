-- ==========================================================
-- REVENUE BY CONTRACT
-- ==========================================================

SELECT

    contract,

    COUNT(*) AS customers,

    ROUND(SUM(monthly_charges),2) AS total_monthly_revenue,

    ROUND(AVG(monthly_charges),2) AS avg_monthly_revenue,

    ROUND(SUM(total_charges),2) AS lifetime_revenue,

    ROUND(AVG(cltv),2) AS avg_cltv

FROM billing

GROUP BY contract

ORDER BY total_monthly_revenue DESC;

-- ==========================================================
-- PAYMENT METHOD ANALYSIS
-- ==========================================================

SELECT

    payment_method,

    COUNT(*) AS customers,

    ROUND(SUM(monthly_charges),2) AS total_monthly_revenue,

    ROUND(AVG(monthly_charges),2) AS avg_monthly_revenue,

    ROUND(AVG(cltv),2) AS avg_cltv

FROM billing

GROUP BY payment_method

ORDER BY total_monthly_revenue DESC;

-- ==========================================================
-- MONTHLY REVENUE AT RISK
-- ==========================================================

SELECT

    COUNT(*) AS churned_customers,

    ROUND(SUM(b.monthly_charges),2) AS monthly_revenue_lost,

    ROUND(AVG(b.monthly_charges),2) AS avg_monthly_revenue_per_customer,

    ROUND(SUM(b.cltv),2) AS cltv_at_risk

FROM billing b

JOIN churn c
ON b.customer_id = c.customer_id

WHERE c.churn_label = TRUE;

-- ==========================================================
-- ACTIVE VS CHURNED REVENUE
-- ==========================================================

SELECT

    c.churn_label,

    COUNT(*) AS customers,

    ROUND(SUM(b.monthly_charges),2) AS monthly_revenue,

    ROUND(AVG(b.monthly_charges),2) AS avg_monthly_revenue,

    ROUND(AVG(b.cltv),2) AS avg_cltv

FROM billing b

JOIN churn c
ON b.customer_id = c.customer_id

GROUP BY c.churn_label;