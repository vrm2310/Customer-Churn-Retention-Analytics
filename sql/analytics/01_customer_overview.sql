-- ==========================================================
-- CUSTOMER OVERVIEW REPORT
-- ==========================================================

SELECT 'Total Customers' AS metric,
       COUNT(*)::NUMERIC AS value
FROM customers

UNION ALL

SELECT 'Active Customers',
       COUNT(*)::NUMERIC
FROM churn
WHERE churn_label = FALSE

UNION ALL

SELECT 'Churned Customers',
       COUNT(*)::NUMERIC
FROM churn
WHERE churn_label = TRUE

UNION ALL

SELECT 'Churn Rate (%)',
       ROUND(
           100.0 * SUM(CASE WHEN churn_label THEN 1 ELSE 0 END) / COUNT(*),
           2
       )
FROM churn

UNION ALL

SELECT 'Average Tenure (Months)',
       ROUND(AVG(tenure_months), 2)
FROM billing

UNION ALL

SELECT 'Average Monthly Charges ($)',
       ROUND(AVG(monthly_charges), 2)
FROM billing

UNION ALL

SELECT 'Average CLTV ($)',
       ROUND(AVG(cltv), 2)
FROM billing;