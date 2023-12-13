from modelo.coneccion import conexion2023
from flask import jsonify, request

def buscar_pro(codigo):
    try:
        conn = conexion2023()
        cur = conn.cursor()
        cur.execute("""select * FROM promocion WHERE llave = %s""", (codigo,))
        datos = cur.fetchone()
        conn.close()

        if datos != None:
            estu = {'cedula_identidad': datos[0], 'nombre': datos[1],
                       'apell_pat': datos[2], 'apell_mat': datos[3],
                       'procedencia': datos[4]}
            return estu
        else:
            return None
    except Exception as ex:
            raise ex
    

class ModeloPromocion():
    @classmethod
    def listar_pro(self):
        try:
            conn = conexion2023()
            cursor=conn.cursor()
            cursor.execute("SELECT * FROM promocion")
            datos = cursor.fetchall()
            promocion = []

            for fila in datos:
                estu = {'llave': fila[0],
                       'nrop': fila[1],
                       'tviaje': fila[2],
                       'costo': fila[3]
                       }
                promocion.append(estu)

            conn.close()

            return jsonify({'promocion': promocion, 'mensaje': "promociones listados.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Errorr", 'exito': False})
    
    @classmethod
    def lista_pro(self,codigo):
        try:
            promo = buscar_pro(codigo)
            if promo != None:
                return jsonify({'promocion': promo, 'mensaje': "usuario encontrado.", 'exito': True})
            else:
                return jsonify({'mensaje': "promocion no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})

    @classmethod
    def registrar_pro(self):
        try:
            promo = buscar_pro(request.json['ci_e'])
            if promo != None:
                return jsonify({'mensaje': "la llave   ya existe, no se puede duplicar.", 'exito': False})
            else:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute('INSERT INTO promocion values(%s,%s,%s,%s)', (request.json['llave'], request.json['nrop'], request.json['tviaje'],
                                                                            request.json['costo']))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "promocion registrado.", 'exito': True})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})
    
    @classmethod
    def actualizar_pro(self,codigo):
        try:
            promo = buscar_pro(codigo)
            if promo != None:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute("""UPDATE promocion SET  nrop=%s, tviaje=%s,
                costo=%s WHERE llave=%s""",
                        (request.json['nrop'], request.json['tviaje'], request.json['costo'], codigo))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "estudiante actualizado.", 'exito': True})
            else:
                return jsonify({'mensaje': "estudiante  no encontrado.", 'exito': False})
        except Exception as ex:
                return jsonify({'mensaje': "Error", 'exito': False})
        
    @classmethod
    def eliminar_pro(self,codigo):
        try:
            promo = buscar_pro(codigo)
            if promo != None:
                conn = conexion2023()
                cur = conn.cursor()
                cur.execute("DELETE FROM promocion WHERE llave = %s", (codigo,))
                conn.commit()
                conn.close()
                return jsonify({'mensaje': "promocion eliminado.", 'exito': True})
            else:
                return jsonify({'mensaje': "promocion no encontrado.", 'exito': False})
        except Exception as ex:
            return jsonify({'mensaje': "Error", 'exito': False})