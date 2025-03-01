-- TODO: Esta consulta devolverá una tabla con dos columnas; customer_state y Revenue.
-- La primera contendrá las abreviaturas que identifican a los 10 estados con mayores ingresos,
-- y la segunda mostrará el ingreso total de cada uno.
-- PISTA: Todos los pedidos deben tener un estado "delivered" y la fecha real de entrega no debe ser nula.
SELECT 
    customer_state,
    SUM(total_amount) AS Revenue
FROM 
    orders
WHERE 
    order_status = 'delivered' AND
    order_delivered_customer_date IS NOT NULL
GROUP BY 
    customer_state
ORDER BY 
    Revenue DESC
LIMIT 10;