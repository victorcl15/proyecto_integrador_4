-- TODO: Esta consulta devolverá una tabla con los ingresos por mes y año.
-- Tendrá varias columnas: month_no, con los números de mes del 01 al 12;
-- month, con las primeras 3 letras de cada mes (ej. Ene, Feb);
-- Year2016, con los ingresos por mes de 2016 (0.00 si no existe);
-- Year2017, con los ingresos por mes de 2017 (0.00 si no existe); y
-- Year2018, con los ingresos por mes de 2018 (0.00 si no existe).
WITH OrderRevenue AS (
    SELECT 
        order_id, 
        MAX(payment_value) AS total_amount 
    FROM 
        olist_order_payments 
    WHERE 
        payment_sequential = 1 
    GROUP BY 
        order_id
), 
MonthlyRevenue AS (
    SELECT 
        strftime('%m', o.order_delivered_customer_date) AS month_no, 
        strftime('%Y', o.order_delivered_customer_date) AS year, 
        SUM(orv.total_amount) AS monthly_total 
    FROM 
        olist_orders o 
    JOIN 
        OrderRevenue orv 
        ON o.order_id = orv.order_id 
    WHERE 
        o.order_status = 'delivered' 
        AND o.order_delivered_customer_date IS NOT NULL 
        AND strftime('%Y', o.order_delivered_customer_date) IN ('2016','2017','2018') 
    GROUP BY 
        month_no, year
) 
SELECT 
    month_no, 
    CASE month_no 
        WHEN '01' THEN 'Jan' 
        WHEN '02' THEN 'Feb' 
        WHEN '03' THEN 'Mar' 
        WHEN '04' THEN 'Apr' 
        WHEN '05' THEN 'May' 
        WHEN '06' THEN 'Jun' 
        WHEN '07' THEN 'Jul' 
        WHEN '08' THEN 'Aug' 
        WHEN '09' THEN 'Sep' 
        WHEN '10' THEN 'Oct' 
        WHEN '11' THEN 'Nov' 
        WHEN '12' THEN 'Dec' 
    END AS month, 
    COALESCE(ROUND(MAX(CASE WHEN year = '2016' THEN monthly_total END), 2), 0.00) AS "Year2016", 
    COALESCE(ROUND(MAX(CASE WHEN year = '2017' THEN monthly_total END), 2), 0.00) AS "Year2017", 
    COALESCE(ROUND(MAX(CASE WHEN year = '2018' THEN monthly_total END), 2), 0.00) AS "Year2018" 
FROM 
    MonthlyRevenue 
GROUP BY 
    month_no 
ORDER BY 
    month_no;