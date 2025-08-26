class ClaseNodo:
    """Nodo de un árbol binario."""
    
    def __init__(self, valor):
        self.valor = valor
        self.hijoIzquierdo = None
        self.hijoDerecho = None

    def getHijoIzquierdo(self):
        """Devuelve el hijo izquierdo"""
        return self.hijoIzquierdo

    def getHijoDerecho(self):
        """Devuelve el hijo derecho."""
        return self.hijoDerecho
    
    def setHijoIzquierdo(self, nodo):
        """Asigna el hijo izquierdo."""
        self.hijoIzquierdo = nodo

    def setHijoDerecho(self, nodo):
        """Asigna el hijo derecho."""
        self.hijoDerecho = nodo

    def getValor(self):
        """Devuelve el valor del nodo."""
        return self.valor
    
    def setValor(self, valor):
        """Asigna el valor al nodo."""  
        self.valor = valor

    def verificarRaiz(self):
        """True si el nodo no tiene hijos (es una hoja)."""
        return self.hijoIzquierdo is None and self.hijoDerecho is None