from ClaseNodo import ClaseNodo  

class ArbolBinario:
    """
    Árbol Binario de Búsqueda (BST):
    - Inserta: menores a la izquierda; mayores o iguales a la derecha.
    - Contar nodos: recursivo (DFS).
    - isVacio: True si no hay raíz.
    """

    def __init__(self):
        self.raiz = None

    # ---------- Inserción (API pública) ----------
    def insertar(self, valor):
        """Inserta un valor en el árbol."""
        self.raiz = self._insertarRecursivo(self.raiz, valor)

    # ---------- Inserción (recursiva) ----------
    def _insertarRecursivo(self, nodo, valor):
        """
        Caso base: nodo vacío -> crear y retornar ClaseNodo(valor).
        Caso recursivo: comparar y bajar por izquierda o derecha.
        Duplicados van a la derecha para replicar tu comportamiento.
        """
        if nodo is None:
            return ClaseNodo(valor)

        if valor < nodo.getValor():
            nodo.setHijoIzquierdo(self._insertarRecursivo(nodo.getHijoIzquierdo(), valor))
        else:
            nodo.setHijoDerecho(self._insertarRecursivo(nodo.getHijoDerecho(), valor))
        return nodo  # devolver la raíz del subárbol

    # ---------- Contar nodos (API pública) ----------
    def contarNodos(self):
        """Devuelve la cantidad total de nodos del árbol."""
        return self._contarNodosRecursivo(self.raiz)

    # ---------- Contar nodos (recursivo) ----------
    def _contarNodosRecursivo(self, nodo):
        """
        Caso base: subárbol vacío -> 0.
        Caso recursivo: 1 (nodo actual) + contar(izq) + contar(der).
        """
        if nodo is None:
            return 0
        return 1 + self._contarNodosRecursivo(nodo.getHijoIzquierdo()) + \
                   self._contarNodosRecursivo(nodo.getHijoDerecho())

    # ---------- Utilidades ----------
    def isVacio(self):
        """True si el árbol está vacío."""
        return self.raiz is None

    def inorden(self):
        """Devuelve los valores en orden ascendente (útil para probar)."""
        res = []
        self._inordenRec(self.raiz, res)
        return res

    def _inordenRec(self, nodo, res):
        if nodo is None:
            return
        self._inordenRec(nodo.getHijoIzquierdo(), res)
        res.append(nodo.getValor())
        self._inordenRec(nodo.getHijoDerecho(), res)


# -------------------------
# Ejemplo de uso 
# -------------------------
if __name__ == "__main__":
    arbol1 = ArbolBinario()
    for v in [75, 90, 100, 50, 55, 30, 300]:
        arbol1.insertar(v)

    print("Cantidad de nodos:", arbol1.contarNodos())
    print("En orden:", arbol1.inorden())