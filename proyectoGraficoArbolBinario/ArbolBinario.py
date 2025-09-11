from ClaseNodo import ClaseNodo

class ArbolBinario:

    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        self.raiz = self._insertarRecursivo(self.raiz, valor)

    def _insertarRecursivo(self, raizAux, valor):
        if raizAux is None:
            return ClaseNodo(valor)
        else:
            if valor < raizAux.getValor():
                raizAux.setHijoIzquierdo(self._insertarRecursivo(raizAux.getHijoIzquierdo(), valor))
            else:
                raizAux.setHijoDerecho(self._insertarRecursivo(raizAux.getHijoDerecho(), valor))
            return raizAux

    def contarNodos(self):
        return self._contarNodosRecursivo(self.raiz)

    def _contarNodosRecursivo(self, raizAux):
        if raizAux is None:
            return 0
        return 1 + self._contarNodosRecursivo(raizAux.getHijoIzquierdo()) + self._contarNodosRecursivo(raizAux.getHijoDerecho())

    def isVacio(self):
        return self.raiz is None

    def eliminar(self, x):
        self.raiz = self.__eliminarRecursivo(self.raiz, x)

    def __eliminarRecursivo(self, nodoRaiz, x):
        if nodoRaiz is None:
            return None
        if x == nodoRaiz.getValor():
            return self.eliminarNodo(nodoRaiz)
        if x < nodoRaiz.getValor():
            nodoRaiz.setHijoIzquierdo(self.__eliminarRecursivo(nodoRaiz.getHijoIzquierdo(), x))
        else:
            nodoRaiz.setHijoDerecho(self.__eliminarRecursivo(nodoRaiz.getHijoDerecho(), x))
        return nodoRaiz

    def eliminarNodo(self, nodo):
        if nodo.verificarRaiz():
            return None
        if nodo.getHijoIzquierdo() is None and nodo.getHijoDerecho() is not None:
            return nodo.getHijoDerecho()
        if nodo.getHijoIzquierdo() is not None and nodo.getHijoDerecho() is None:
            return nodo.getHijoIzquierdo()
        nodoVerdeDato = self.__buscarSiguienteSucesor(nodo.getHijoDerecho())
        nodo.setValor(nodoVerdeDato)
        nodo.setHijoDerecho(self.__eliminarRecursivo(nodo.getHijoDerecho(), nodoVerdeDato))
        return nodo

    def __buscarSiguienteSucesor(self, nodoDerecho):
        while nodoDerecho.getHijoIzquierdo() is not None:
            nodoDerecho = nodoDerecho.getHijoIzquierdo()
        return nodoDerecho.getValor()

    # Nuevos métodos de recorrido
    def recorridoInOrden(self):
        """Recorrido InOrden: Izquierda -> Raíz -> Derecha"""
        resultado = []
        self._inOrdenRecursivo(self.raiz, resultado)
        return resultado

    def _inOrdenRecursivo(self, nodo, resultado):
        if nodo is not None:
            self._inOrdenRecursivo(nodo.getHijoIzquierdo(), resultado)
            resultado.append(nodo.getValor())
            self._inOrdenRecursivo(nodo.getHijoDerecho(), resultado)

    def recorridoPreOrden(self):
        """Recorrido PreOrden: Raíz -> Izquierda -> Derecha"""
        resultado = []
        self._preOrdenRecursivo(self.raiz, resultado)
        return resultado

    def _preOrdenRecursivo(self, nodo, resultado):
        if nodo is not None:
            resultado.append(nodo.getValor())
            self._preOrdenRecursivo(nodo.getHijoIzquierdo(), resultado)
            self._preOrdenRecursivo(nodo.getHijoDerecho(), resultado)

    def recorridoPostOrden(self):
        """Recorrido PostOrden: Izquierda -> Derecha -> Raíz"""
        resultado = []
        self._postOrdenRecursivo(self.raiz, resultado)
        return resultado

    def _postOrdenRecursivo(self, nodo, resultado):
        if nodo is not None:
            self._postOrdenRecursivo(nodo.getHijoIzquierdo(), resultado)
            self._postOrdenRecursivo(nodo.getHijoDerecho(), resultado)
            resultado.append(nodo.getValor())

    def buscar(self, valor):
        """Buscar un valor en el árbol"""
        return self._buscarRecursivo(self.raiz, valor)

    def _buscarRecursivo(self, nodo, valor):
        if nodo is None:
            return False
        if valor == nodo.getValor():
            return True
        elif valor < nodo.getValor():
            return self._buscarRecursivo(nodo.getHijoIzquierdo(), valor)
        else:
            return self._buscarRecursivo(nodo.getHijoDerecho(), valor)

    def obtenerAltura(self):
        """Obtener la altura del árbol"""
        return self._obtenerAlturaRecursiva(self.raiz)

    def _obtenerAlturaRecursiva(self, nodo):
        if nodo is None:
            return 0
        alturaIzq = self._obtenerAlturaRecursiva(nodo.getHijoIzquierdo())
        alturaDer = self._obtenerAlturaRecursiva(nodo.getHijoDerecho())
        return 1 + max(alturaIzq, alturaDer)

    def limpiarArbol(self):
        """Limpiar todo el árbol"""
        self.raiz = None

    def obtenerEstructuraVisual(self):
        """Obtener una representación visual simple del árbol"""
        if self.isVacio():
            return "Árbol vacío"
        return self._estructuraVisualRecursiva(self.raiz, "", True)

    def _estructuraVisualRecursiva(self, nodo, prefijo, esUltimo):
        if nodo is None:
            return ""
        
        resultado = prefijo + ("└── " if esUltimo else "├── ") + str(nodo.getValor()) + "\n"
        
        hijos = []
        if nodo.getHijoIzquierdo() is not None:
            hijos.append(("izq", nodo.getHijoIzquierdo()))
        if nodo.getHijoDerecho() is not None:
            hijos.append(("der", nodo.getHijoDerecho()))
        
        for i, (tipo, hijo) in enumerate(hijos):
            esUltimoHijo = i == len(hijos) - 1
            nuevoPrefijo = prefijo + ("    " if esUltimo else "│   ")
            resultado += self._estructuraVisualRecursiva(hijo, nuevoPrefijo, esUltimoHijo)
        
        return resultado

if __name__ == "__main__":
    arbol1 = ArbolBinario()
    arbol1.insertar(100)
    arbol1.insertar(90)
    arbol1.insertar(120)
    arbol1.insertar(70)
    arbol1.insertar(75)
    arbol1.insertar(130)
    arbol1.insertar(200)
    
    print("Cantidad de nodos:", arbol1.contarNodos())
    print("InOrden:", arbol1.recorridoInOrden())
    print("PreOrden:", arbol1.recorridoPreOrden())
    print("PostOrden:", arbol1.recorridoPostOrden())
    print("Altura:", arbol1.obtenerAltura())