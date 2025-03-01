-- TODO: Esta consulta devolverá una tabla con las 10 categorías con mayores ingresos
-- (en inglés), el número de pedidos y sus ingresos totales. La primera columna será
-- Category, que contendrá las 10 categorías con mayores ingresos; la segunda será
-- Num_order, con el total de pedidos de cada categoría; y la última será Revenue,
-- con el ingreso total de cada categoría.
-- PISTA: Todos los pedidos deben tener un estado 'delivered' y tanto la categoría
-- como la fecha real de entrega no deben ser nulas.
SELECT
    oi.category AS Category,
    COUNT(DISTINCT o.order_id) AS Num_order,
    SUM(oi.total_amount) AS Revenue
FROM
    orders o
JOIN
    order_items oi ON o.order_id = oi.order_id
WHERE
    o.order_status = 'delivered' AND
    o.order_delivered_customer_date IS NOT NULL AND
    oi.category IS NOT NULL
GROUP BY
    oi.category
ORDER BY
    Revenue DESC
LIMIT 10;