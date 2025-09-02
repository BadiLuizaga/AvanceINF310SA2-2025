from ClaseNodo import ClaseNodo


class ArbolBinario:
    """
    Árbol Binario de Búsqueda (BST).
    - Inserta: menores a la izquierda; mayores o iguales a la derecha.
    """

    def __init__(self):
        self.raiz = None

    # ============================================================
    # 1. InsertarNodo
    # ============================================================
    def insertar_nodo_recursivo(self, valor):
        """Inserta un nodo de forma recursiva."""
        # Se llama al meotodo auxiliar para insertar desde la raiz
        self.raiz = self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        # Caso base: si el nodo actual es none, intertamos aqui
        if nodo is None:
            return ClaseNodo(valor)
        # si el valor es menor, vamos a la izqueirda
        if valor < nodo.getValor():
            nodo.setHijoIzquierdo(self._insertar_recursivo(nodo.getHijoIzquierdo(), valor))
        # si el valor es mayor o igual, vamos a la derecha
        else:
            nodo.setHijoDerecho(self._insertar_recursivo(nodo.getHijoDerecho(), valor))
        return nodo

    def insertar_nodo_iterativo(self, valor):
        """Inserta un nodo de forma iterativa."""
        nuevo = ClaseNodo(valor) # creamos el nuevo nodo
        if self.raiz is None: # si el arbol esta vacio, el nuevo sera la raiz
            self.raiz = nuevo
            return

        actual = self.raiz
        while True: # recorremos el arbol hasta encontrar el lugar adecuado 
            if valor < actual.getValor(): # vamos a la izquierda 
                if actual.getHijoIzquierdo() is None:
                    actual.setHijoIzquierdo(nuevo) # insertamos aqui 
                    break
                actual = actual.getHijoIzquierdo()
            else: # vamos por la derecha 
                if actual.getHijoDerecho() is None:
                    actual.setHijoDerecho(nuevo) # insertamos aqui
                    break
                actual = actual.getHijoDerecho()

    # ============================================================
    # 2. EsVacio
    # ============================================================
    def es_vacio_recursivo(self):
        """Verifica recursivamente si el árbol está vacío."""
        return self._es_vacio_recursivo(self.raiz)

    def _es_vacio_recursivo(self, nodo):
        # un arbol esta vacio si la raiz es none 
        return nodo is None

    def es_vacio_iterativo(self):
        """Verifica iterativamente si el árbol está vacío."""
        return self.raiz is None # revisa si la raiz existe 

    # ============================================================
    # 3. EsHoja
    # ============================================================
    def es_hoja_recursivo(self, nodo):
        """Verifica recursivamente si un nodo es hoja."""
        if nodo is None:
            return False # un nodo nulo se puede ser hoja
        # un nodo es hoja si no tiene hijos izquierdo ni derecho
        return nodo.getHijoIzquierdo() is None and nodo.getHijoDerecho() is None

    def es_hoja_iterativo(self, nodo):
        """Verifica iterativamente si un nodo es hoja."""
        if nodo is None:
            return False
        # lo mismo que pero aqui sin recursividad 
        return not (nodo.getHijoIzquierdo() or nodo.getHijoDerecho())

    # ============================================================
    # 4. BuscarX
    # ============================================================
    def buscar_x_recursivo(self, valor):
        """Busca un valor en el árbol de forma recursiva."""
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, nodo, valor):
        # Caso base: nodo no existe 
        if nodo is None:
            return None
        # si encontramos un valor, devolvemos el nodo
        if nodo.getValor() == valor:
            return nodo
        # si es menor, buscamos el hijo izquierdo
        if valor < nodo.getValor():
            return self._buscar_recursivo(nodo.getHijoIzquierdo(), valor)
        # si es mayor, buscamos el hijo derecho
        return self._buscar_recursivo(nodo.getHijoDerecho(), valor)

    def buscar_x_iterativo(self, valor):
        """Busca un valor en el árbol de forma iterativa."""
        actual = self.raiz
        while actual: # recorremos el arbol hasta encontrar o llegar al none
            if actual.getValor() == valor:
                return actual
            if valor < actual.getValor():
                actual = actual.getHijoIzquierdo()
            else:
                actual = actual.getHijoDerecho()
        return None

    # ============================================================
    # 5. InOrden
    # ============================================================
    def inorden_recursivo(self):
        """Recorrido inorden (recursivo)."""
        res = []
        self._inorden_rec(self.raiz, res)
        return res

    def _inorden_rec(self, nodo, res):
        if nodo:
            # Primero recorremos el hijo izquierdo
            self._inorden_rec(nodo.getHijoIzquierdo(), res)
            # luego visitamos el nodo 
            res.append(nodo.getValor())
            # Y finalmente recorremos el hijo derecho
            self._inorden_rec(nodo.getHijoDerecho(), res)

    def inorden_iterativo(self):
        """Recorrido inorden (iterativo)."""
        res, stack = [], []
        actual = self.raiz
        # usamos una pila para simular la recursividad
        while stack or actual:
            while actual: # bajamos siempre por la izquierda
                stack.append(actual)
                actual = actual.getHijoIzquierdo()
            actual = stack.pop() # procesamos el nodo 
            res.append(actual.getValor())
            actual = actual.getHijoDerecho() # Movemos a la derecha
        return res

    # ============================================================
    # 6. PreOrden
    # ============================================================
    def preorden_recursivo(self):
        """Recorrido preorden (recursivo)."""
        res = []
        self._preorden_rec(self.raiz, res)
        return res

    def _preorden_rec(self, nodo, res):
        if nodo:
            res.append(nodo.getValor()) # visitamos primero la raiz 
            self._preorden_rec(nodo.getHijoIzquierdo(), res) # izquierda
            self._preorden_rec(nodo.getHijoDerecho(), res) # derecha

    def preorden_iterativo(self):
        """Recorrido preorden (iterativo)."""
        if self.raiz is None:
            return []
        res, stack = [], [self.raiz] # la pila inicia con la raiz
        while stack:
            nodo = stack.pop() # sacamos el ultimo nodo 
            res.append(nodo.getValor()) # visitamos 
            # primero apilamos el derecho, para procesar antes del izquierdo
            if nodo.getHijoDerecho():
                stack.append(nodo.getHijoDerecho())
            if nodo.getHijoIzquierdo():
                stack.append(nodo.getHijoIzquierdo())
        return res

    # ============================================================
    # 7. PostOrden
    # ============================================================
    def postorden_recursivo(self):
        """Recorrido postorden (recursivo)."""
        res = []
        self._postorden_rec(self.raiz, res)
        return res

    def _postorden_rec(self, nodo, res):
        if nodo:
            self._postorden_rec(nodo.getHijoIzquierdo(), res) # izquierda
            self._postorden_rec(nodo.getHijoDerecho(), res) # derecha
            res.append(nodo.getValor()) # raiz

    def postorden_iterativo(self):
        """Recorrido postorden (iterativo)."""
        if self.raiz is None:
            return []
        res, stack = [], [(self.raiz, False)]
        # la pila guarda (nodo, visitado)
        while stack:
            nodo, visitado = stack.pop()
            if nodo is None:
                continue
            if visitado:
                # si ya fue visitado, lo agregamos al resultado 
                res.append(nodo.getValor())
            else:
                # marcamos el nodo como "visitado" y luego aplicamos sus hijos 
                stack.append((nodo, True))
                if nodo.getHijoDerecho():
                    stack.append((nodo.getHijoDerecho(), False))
                if nodo.getHijoIzquierdo():
                    stack.append((nodo.getHijoIzquierdo(), False))
        return res
    # ============================================================
    # 8) Altura
    # ============================================================
    def altura_recursiva(self):
        """
        Altura (en niveles). Árbol vacío -> 0.
        Hoja -> 1. En general: 1 + máx(altura izq, altura der).
        """
        return self._altura_rec(self.raiz)

    def _altura_rec(self, nodo):
        # Caso base: subárbol vacío tiene altura 0.
        if nodo is None:
            return 0
        # Caso recursivo: 1 + máximo entre alturas de los subárboles.
        return 1 + max(
            self._altura_rec(nodo.getHijoIzquierdo()),
            self._altura_rec(nodo.getHijoDerecho()),
        )

    def altura_iterativa(self):
        """Altura por BFS (niveles)."""
        # Recorre nivel por nivel; cada vuelta del while suma 1 nivel.
        if self.raiz is None:
            return 0
        from collections import deque

        cola = deque([self.raiz]) # cola inicial con la raiz
        niveles = 0
        while cola:
             # Procesa todos los nodos del nivel actual.
            for _ in range(len(cola)):
                n = cola.popleft()
                # Encola hijos del siguiente nivel si existen.
                if n.getHijoIzquierdo():
                    cola.append(n.getHijoIzquierdo())
                if n.getHijoDerecho():
                    cola.append(n.getHijoDerecho())
            niveles += 1 # terminó de recorrer un nivel completo
        return niveles

    # ============================================================
    # 9) Cantidad de nodos
    # ============================================================
    def cantidad_recursiva(self):
        """Cantidad total de nodos (recursivo)."""
        # Devuelve el número total de nodos del árbol
        return self._cantidad_rec(self.raiz)

    def _cantidad_rec(self, nodo):
        # Caso base: subárbol vacío aporta 0.
        if nodo is None:
            return 0
        # Caso recursivo: 1 (nodo actual) + nodos(izq) + nodos(der).
        return (
            1
            + self._cantidad_rec(nodo.getHijoIzquierdo())
            + self._cantidad_rec(nodo.getHijoDerecho())
        )

    def cantidad_iterativa(self):
        """Cantidad total de nodos (BFS)."""
        # Cuenta nodos con un BFS usando una cola.
        if self.raiz is None:
            return 0
        from collections import deque

        cola = deque([self.raiz])
        conteo = 0
        while cola:
            n = cola.popleft()
            conteo += 1 # cuenta el nodo desencolado
            # Encola hijos si existen para seguir recorriendo.
            if n.getHijoIzquierdo():
                cola.append(n.getHijoIzquierdo())
            if n.getHijoDerecho():
                cola.append(n.getHijoDerecho())
        return conteo

    # ============================================================
    # 10) Amplitud (BFS)
    # ============================================================
    def amplitud(self):
        """Recorrido por niveles (BFS) como lista plana de valores."""
        if self.raiz is None:
            return []
        from collections import deque

        cola = deque([self.raiz])
        res = []
        while cola:
            n = cola.popleft()
            res.append(n.getValor())
            if n.getHijoIzquierdo():
                cola.append(n.getHijoIzquierdo())
            if n.getHijoDerecho():
                cola.append(n.getHijoDerecho())
        return res

    def amplitud_por_niveles(self):
        """Recorrido por niveles como lista de listas (niveles separados)."""
        if self.raiz is None:
            return []
        from collections import deque

        cola = deque([self.raiz])
        niveles = []
        while cola:
            nivel = []
            for _ in range(len(cola)):
                n = cola.popleft()
                nivel.append(n.getValor())
                if n.getHijoIzquierdo():
                    cola.append(n.getHijoIzquierdo())
                if n.getHijoDerecho():
                    cola.append(n.getHijoDerecho())
            niveles.append(nivel)
        return niveles


# ============================================================
# Ejemplo de uso
# ============================================================
if __name__ == "__main__":
    arbol = ArbolBinario()
    datos = [100, 90, 120, 70, 75, 130, 200, 110, 95]
    for v in datos:
        arbol.insertar_nodo_iterativo(v)

    print("Inorden (it):  ", arbol.inorden_iterativo())
    print("Preorden (it): ", arbol.preorden_iterativo())
    print("Postorden (it):", arbol.postorden_iterativo())

    print("Cantidad (rec):", arbol.cantidad_recursiva())
    print("Cantidad (it): ", arbol.cantidad_iterativa())
    print("Altura (rec):  ", arbol.altura_recursiva())
    print("Altura (it):   ", arbol.altura_iterativa())

    print("Amplitud (BFS):", arbol.amplitud())
    print("Por niveles:   ", arbol.amplitud_por_niveles())

    x = 95
    nodo_x = arbol.buscar_x_iterativo(x)
    print(f"Buscar {x}:    ", nodo_x is not None)
    if nodo_x:
        print(f"¿{x} es hoja? (rec):", arbol.es_hoja_recursivo(nodo_x))
        print(f"¿{x} es hoja? (it): ", arbol.es_hoja_iterativo(nodo_x))