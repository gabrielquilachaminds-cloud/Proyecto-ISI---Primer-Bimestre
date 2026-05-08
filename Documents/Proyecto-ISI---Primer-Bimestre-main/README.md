# TPS QuickShop — Sistema de Punto de Venta

Sistema de Procesamiento de Transacciones (TPS) desarrollado en Python para la gestión de ventas de un minimarket. Permite registrar ventas, controlar el stock en tiempo real y almacenar todas las transacciones en archivos CSV.

---

## Descripción

**QuickShop TPS** es una aplicación de escritorio que simula un punto de venta real. Está desarrollada con Python 3 usando Tkinter para la interfaz gráfica y el módulo `csv` para el almacenamiento de datos. No requiere internet ni base de datos externa — funciona completamente de forma local (stand alone).

---

## Requisitos

- Python 3.8 o superior
- Sistema operativo: Windows, Linux o macOS
- No requiere instalar librerías externas

Para verificar tu versión de Python:
```bash
python --version
```

---

## Cómo ejecutar el sistema

1. Descarga o clona este repositorio:
```bash
git clone https://github.com/[tu-usuario]/tps-quickshop.git
cd tps-quickshop
```

2. Ejecuta el programa:
```bash
python tps_minimarket.py
```

3. Al iniciarse por primera vez, el sistema crea automáticamente los archivos `inventario.csv`, `transacciones.csv` y `detalles_venta.csv` en la misma carpeta.

---

## Interfaz del sistema

La pantalla principal está dividida en **tres paneles**:

| Panel | Nombre | Función |
|-------|--------|---------|
| Izquierdo | Catálogo & Stock | Muestra todos los productos con precio y stock disponible |
| Central | Venta en curso | Carrito de compra, totales y métodos de pago |
| Derecho | Historial del día | Transacciones realizadas, estadísticas y stock crítico |

---

## Manual de usuario

### 1. Registrar una venta

1. En el **panel izquierdo**, busca el producto por nombre o filtra por categoría.
2. Haz clic sobre el producto para seleccionarlo.
3. Define la cantidad en el campo "Cantidad" (por defecto es 1).
4. Presiona **" Agregar al carrito"** o haz doble clic sobre el producto.
5. El producto aparece en el **panel central** con su subtotal calculado.
6. Repite los pasos para agregar más productos.
7. Elige el método de pago: **Efectivo, Tarjeta, Transferencia o QR**.
8. Presiona el botón verde **" COBRAR / PROCESAR VENTA"**.
9. El sistema muestra el recibo con el detalle completo de la venta.

### 2. Eliminar un producto del carrito

- Selecciona el producto en el carrito (panel central).
- Presiona **"Quitar producto seleccionado"**.

### 3. Cancelar una venta

- Presiona **" Cancelar venta"** en el panel central.
- Confirma en la ventana de diálogo.
- El carrito se vacía y **no se registra ninguna transacción**.

### 4. Consultar el historial

- El **panel derecho** muestra automáticamente todas las ventas del día.
- Incluye: ID de transacción, hora, total, método de pago y cantidad de ítems.
- Las estadísticas (total recaudado, ticket promedio) se actualizan tras cada venta.
- Presiona **" Actualizar historial"** para refrescar manualmente.

### 5. Control de stock

- Los productos con **menos de 10 unidades** se muestran en **amarillo**.
- Los productos **agotados** se muestran en **rojo** y no pueden venderse.
- El panel inferior derecho muestra la lista de **productos en stock crítico**.
- Si intentas vender más unidades de las disponibles, el sistema te avisa y no lo permite.

---

## Archivos de datos generados

El sistema genera y actualiza automáticamente tres archivos CSV:

### `transacciones.csv`
Registra cada venta procesada.

| Campo | Descripción |
|-------|-------------|
| id_transaccion | Identificador único (TX-0001, TX-0002...) |
| fecha | Fecha de la venta (YYYY-MM-DD) |
| hora | Hora exacta (HH:MM:SS) |
| cajero | Operador del sistema |
| subtotal | Monto antes del IVA |
| iva | IVA del 12% |
| total | Total cobrado al cliente |
| metodo_pago | Efectivo / Tarjeta / Transferencia / QR |
| estado | COMPLETADA |

### `detalles_venta.csv`
Registra cada producto de cada venta.

| Campo | Descripción |
|-------|-------------|
| id_transaccion | Referencia a la venta principal |
| codigo_producto | Código del producto (ej: B003) |
| nombre_producto | Nombre del artículo |
| precio_unitario | Precio de cada unidad |
| cantidad | Unidades vendidas |
| subtotal_linea | precio × cantidad |

### `inventario.csv`
Catálogo con stock actualizado en tiempo real.

| Campo | Descripción |
|-------|-------------|
| codigo | Código único (B001, S003...) |
| nombre | Nombre del producto |
| precio | Precio de venta |
| stock | Unidades disponibles actuales |
| categoria | Bebidas, Snacks, Lácteos, etc. |

---

## Productos del catálogo

El sistema incluye **55 productos** distribuidos en **7 categorías**:

- **Bebidas** — Aguas, gaseosas, jugos, energizantes, leche
- **Snacks** — Papas, doritos, galletas, chocolates
- **Lácteos** — Yogur, quesos, huevos, mantequilla
- **Panadería** — Pan de molde, tostadas, croissants
- **Abarrotes** — Arroz, aceite, atún, pasta, salsas
- **Limpieza** — Jabón, shampoo, detergente, papel higiénico
- **Personal** — Desodorante, pasta dental, afeitadora

---

## Estructura del proyecto

```
tps-quickshop/
│
├── tps_minimarket.py       # Programa principal
├── inventario.csv          # Catálogo y stock (generado automáticamente)
├── transacciones.csv       # Registro de ventas (generado automáticamente)
├── detalles_venta.csv      # Detalle de productos por venta (generado automáticamente)
└── README.md               # Este archivo
```

---

## Componentes del Sistema de Información (SI)

| Componente | Detalle |
|------------|---------|
| **Personas** | Cajero (operador), Cliente (comprador), Administrador (revisor de datos) |
| **Datos** | 3 archivos CSV: transacciones, detalles y inventario |
| **Software** | Python 3 + Tkinter + módulo csv |
| **Hardware** | Laptop Lenovo L490, 8GB RAM, Windows/Linux |
| **Redes** | Sistema stand alone — sin conexión a internet |
| **Procesos** | Venta, actualización de stock, cancelación, consulta de historial |

---

## Materia

Sistemas de Información  
Desarrollado con Python 3 — sin dependencias externas
