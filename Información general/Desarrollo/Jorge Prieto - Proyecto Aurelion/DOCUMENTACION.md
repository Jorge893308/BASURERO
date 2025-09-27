# Me gustaría analizar cual es el cliente que más compra en dinero.

## Tabla Clientes
id_cliente	int ordinal
nombre_cliente	str nominal
email	str nominal
ciudad	str nominal
fecha_alta str intervalo

## Tabla Detalle_ventas
id_venta	int ordinal
id_producto	int ordinal
nombre_producto	str nominal
cantidad int ordinal
precio_unitario	int ordinal
importe int ordinal

## Tabla Productos
id_producto	int ordinal
nombre_producto	str nominal
categoria	str nominal
precio_unitario int ordinal

## Tabla Ventas
id_venta	int ordinal
fecha	str intervalo
id_cliente	int ordinal
nombre_cliente	str nominal
email	str nominal
medio_pago str nominal