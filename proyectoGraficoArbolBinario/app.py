from flask import Flask, render_template, request, jsonify, redirect, url_for
from ArbolBinario import ArbolBinario

app = Flask(__name__)

arbol_global = ArbolBinario()

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/insertar', methods=['POST'])
def insertar():
    """Insertar un valor en el árbol"""
    try:
        valor = int(request.form['valor'])
        arbol_global.insertar(valor)
        return jsonify({
            'success': True, 
            'mensaje': f'Valor {valor} insertado correctamente',
            'estructura': arbol_global.obtenerEstructuraVisual(),
            'cantidad_nodos': arbol_global.contarNodos()
        })
    except ValueError:
        return jsonify({'success': False, 'mensaje': 'Por favor ingresa un número válido'})
    except Exception as e:
        return jsonify({'success': False, 'mensaje': f'Error: {str(e)}'})
    

@app.route('/eliminar', methods=['POST'])
def eliminar():
    """Eliminar un valor del árbol"""
    try:
        valor = int(request.form['valor'])
        if arbol_global.buscar(valor):
            arbol_global.eliminar(valor)
            return jsonify({
                'success': True, 
                'mensaje': f'Valor {valor} eliminado correctamente',
                'estructura': arbol_global.obtenerEstructuraVisual(),
                'cantidad_nodos': arbol_global.contarNodos()
            })
        else:
            return jsonify({'success': False, 'mensaje': f'El valor {valor} no existe en el árbol'})
    except ValueError:
        return jsonify({'success': False, 'mensaje': 'Por favor ingresa un número válido'})
    except Exception as e:
        return jsonify({'success': False, 'mensaje': f'Error: {str(e)}'})
    
@app.route('/buscar', methods=['POST'])
def buscar():
    """Buscar un valor en el árbol"""
    try:
        valor = int(request.form['valor'])
        encontrado = arbol_global.buscar(valor)
        mensaje = f'El valor {valor} {"SÍ" if encontrado else "NO"} se encuentra en el árbol'
        return jsonify({
            'success': True, 
            'mensaje': mensaje,
            'encontrado': encontrado
        })
    except ValueError:
        return jsonify({'success': False, 'mensaje': 'Por favor ingresa un número válido'})
    except Exception as e:
        return jsonify({'success': False, 'mensaje': f'Error: {str(e)}'})
    
@app.route('/recorridos', methods=['GET'])
def obtener_recorridos():
    """Obtener todos los recorridos del árbol"""
    try:
        if arbol_global.isVacio():
            return jsonify({
                'success': False,
                'mensaje': 'El árbol está vacío'
            })
        
        return jsonify({
            'success': True,
            'inorden': arbol_global.recorridoInOrden(),
            'preorden': arbol_global.recorridoPreOrden(),
            'postorden': arbol_global.recorridoPostOrden()
        })
    except Exception as e:
        return jsonify({'success': False, 'mensaje': f'Error: {str(e)}'})
    
@app.route('/informacion', methods=['GET'])
def obtener_informacion():
    """Obtener información general del árbol"""
    try:
        return jsonify({
            'success': True,
            'cantidad_nodos': arbol_global.contarNodos(),
            'altura': arbol_global.obtenerAltura(),
            'vacio': arbol_global.isVacio(),
            'estructura': arbol_global.obtenerEstructuraVisual()
        })
    except Exception as e:
        return jsonify({'success': False, 'mensaje': f'Error: {str(e)}'})

@app.route('/limpiar', methods=['POST'])
def limpiar():
    """Limpiar todo el árbol"""
    try:
        arbol_global.limpiarArbol()
        return jsonify({
            'success': True, 
            'mensaje': 'Árbol limpiado correctamente',
            'estructura': arbol_global.obtenerEstructuraVisual(),
            'cantidad_nodos': 0
        })
    except Exception as e:
        return jsonify({'success': False, 'mensaje': f'Error: {str(e)}'})

@app.route('/ejemplo', methods=['POST'])
def cargar_ejemplo():
    """Cargar un ejemplo predefinido"""
    try:
        arbol_global.limpiarArbol()
        valores_ejemplo = [100, 50, 150, 25, 75, 125, 175, 10, 30, 60, 80]
        
        for valor in valores_ejemplo:
            arbol_global.insertar(valor)
        
        return jsonify({
            'success': True, 
            'mensaje': 'Ejemplo cargado correctamente',
            'estructura': arbol_global.obtenerEstructuraVisual(),
            'cantidad_nodos': arbol_global.contarNodos(),
            'valores_insertados': valores_ejemplo
        })
    except Exception as e:
        return jsonify({'success': False, 'mensaje': f'Error: {str(e)}'})
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

#GET
#POST
#DELETE
#PATCH PUT