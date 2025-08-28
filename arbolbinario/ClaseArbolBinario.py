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
# Ejemplo de uso
# ============================================================
if __name__ == "__main__":
    arbol = ArbolBinario()

    print("=== Construcción del Árbol Binario ===")
    print("Ingrese hasta 7 valores enteros para el árbol:")

    # ---------------------------------------
    # Insertar valores por usuario (máx 7)
    # ---------------------------------------
    for i in range(7):
        try:
            valor = int(input(f"Ingrese valor {i+1}: "))
            arbol.insertar_nodo_iterativo(valor)  # usando inserción iterativa
        except ValueError:
            print("Debe ingresar un número entero válido.")
            break

    # ---------------------------------------
    # Mostrar si el árbol está vacío
    # ---------------------------------------
    print("\n¿El árbol está vacío? (rec):", arbol.es_vacio_recursivo())
    print("¿El árbol está vacío? (it):", arbol.es_vacio_iterativo())

    # ---------------------------------------
    # Recorridos
    # ---------------------------------------
    inorden = arbol.inorden_iterativo()
    preorden = arbol.preorden_iterativo()
    postorden = arbol.postorden_iterativo()

    print("\nRecorridos del árbol:")
    print("Inorden :", inorden)
    print("Preorden:", preorden)
    print("Postorden:", postorden)

    # ---------------------------------------
    # Búsqueda de un valor
    # ---------------------------------------
    try:
        valor_buscar = int(input("\nIngrese un valor a buscar en el árbol: "))
        nodo = arbol.buscar_x_iterativo(valor_buscar)

        print(f"\nBuscar {valor_buscar} (rec):",
              arbol.buscar_x_recursivo(valor_buscar) is not None)
        print(f"Buscar {valor_buscar} (it):", nodo is not None)

        if nodo:
            # ¿Es hoja?
            print(f"¿El nodo {valor_buscar} es hoja? (rec):",
                  arbol.es_hoja_recursivo(nodo))
            print(f"¿El nodo {valor_buscar} es hoja? (it):",
                  arbol.es_hoja_iterativo(nodo))

            # Revisar en qué recorrido(s) aparece
            print(f"\nEl valor {valor_buscar} aparece en:")
            if valor_buscar in inorden:
                print(" - Inorden ✅")
            if valor_buscar in preorden:
                print(" - Preorden ✅")
            if valor_buscar in postorden:
                print(" - Postorden ✅")
        else:
            print(f"El valor {valor_buscar} no se encuentra en el árbol.")
    except ValueError:
        print("Debe ingresar un número entero válido.")