# 3-SAT Solver utilizando Independent Set 🧠

## Descripción
Implementación de un algoritmo para resolver instancias del problema **3-SAT** mediante su conversión a un grafo para tratarlo como un problema **independent set**, el cual se resulenve con un enfoque **greedy**.

El problema **3-SAT** es una variante del problema de satisfacibilidad booleana (SAT), donde cada cláusula contiene exactamente tres literales.**.

## Algoritmo
### Paso 1: Conversión a grafo
- Se crea un **grafo** donde cada nodo representa una **literal** de la entrada.
- Al ser entradas del tipo 3-SAT cada cláusula forma un **triángulo**.
- Los triángulos de las cláusulas se conectan entre sí mediante las literales compartidas, formando una estructura compleja de restricciones.

### Paso 2: Algoritmo Greedy para Independent Set
- Se utiliza un enfoque **greedy** para seleccionar nodos. 
- El algoritmo selecciona un conjunto de nodos independientes.
