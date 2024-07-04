import requests
from flask import( 
    Flask,
    redirect, 
    render_template, 
    request
)


app = Flask(__name__)

productos_dict = [
    dict(
        cod="11",
        name="Madera",
        monto="500",
        cant="3",
    ),
    dict(
        cod="12",
        name="Hierro",
        monto="1000",
        cant="4",
    ),
    dict(
        cod="13",
        name="Oro",
        monto="2000",
        cant="8",
    )
]
    
@app.route('/') # app es la instancia, route el metodo, '/' es el disparador
def index():
    return render_template(
        'index.html',
    )
    
@app.route('/productos') # app es la instancia, route el metodo, '/' es el disparador
def productos():
    listado = productos_dict
    return render_template(
        'productos.html',
        listado = listado
        )
    
    
@app.route('/productos_add', methods=['GET', 'POST'])
def agregar_productos():
    if request.method == 'POST':
    #Peticion-Formulario-Clave
        codigo = request.form['codigo']
        nombre = request.form['nombre'] 
        precio = request.form['precio']
        cantidad = request.form['cantidad']
        
        producto = dict(
                cod=codigo,
                name=nombre,
                monto=precio,
                cant=cantidad,
            )
        productos_dict.append(producto)
        return redirect("productos")
    
    return render_template('addproductos.html')    
