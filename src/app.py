from flask import Flask
from decouple import config
from modelo.promocion import ModeloPromocion
from config import config

app = Flask(__name__)

# RUTA PARA PETICION GET

@app.route("/")
def hello_world():
    return  " hola mundo "

#mostrar todos los estudiantes
@app.route("/promocion", methods=['GET'])
def listar_pro():
    resul=ModeloPromocion.listar_pro()
    return resul

#buscar solo un estudiante
@app.route("/promocion/:<codigo>", methods=['GET'])
def lista_pro(codigo):
    resul=ModeloPromocion.lista_pro(codigo)
    return resul

#registrar estudiante
@app.route("/promocion",methods=['POST'])
def guardar_pro():
    resul=ModeloPromocion.registrar_pro()
    return resul


#actualizar estudiante
@app.route("/promocion/:<codigo>",methods=['PUT'])
def actualizxar_pro(codigo):
    resul=ModeloPromocion.actualizar_pro(codigo)
    return resul


#eliminar estudiante
@app.route("/promocion/:<codigo>",methods=['DELETE'])
def elimineycion_pro(codigo):
    resul=ModeloPromocion.eliminar_pro(codigo)
    return resul

def pag_noencontrada(error):
    return "<h1>Página no Encontrada</h1>", 404

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,pag_noencontrada)
    app.run(host='0.0.0.0')
