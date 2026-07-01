CREATE OR REPLACE VIEW vw_revenue_analysis AS

SELECT
    b.contract,

    COUNT(*) AS total_customers,

    ROUND(SUM(b.monthly_charges),2) AS total_monthly_revenue,

    ROUND(AVG(b.monthly_charges),2) AS avg_monthly_revenue,

    ROUND(SUM(b.cltv),2) AS total_cltv,

    ROUND(AVG(b.cltv),2) AS avg_cltv

FROM billing b

GROUP BY
    b.contract

ORDER BY
    total_cltv DESC;

SELECT * FROM vw_revenue_analysis;