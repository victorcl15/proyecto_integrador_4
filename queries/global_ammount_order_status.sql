-- TODO: Esta consulta devolverá una tabla con dos columnas: estado_pedido y
-- Cantidad. La primera contendrá las diferentes clases de estado de los pedidos,
-- y la segunda mostrará el total de cada uno.
SELECT 
    order_status AS estado_pedido,
    COUNT(*) AS Cantidad
FROM 
    orders
GROUP BY 
    order_status;