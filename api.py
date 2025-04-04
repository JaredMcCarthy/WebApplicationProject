from flask import Flask, jsonify, request
import mysql.connector

app = Flask(__name__)

#Paso 10
@app.route('/tareas', methods=['POST'])
def agregar_tareas():
    data = request.json
    descripcion = data.get('descripcion')
    prioridad = data.get('prioridad', 'media')

    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456789",
        database="productividad"
    )

    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO tareas (descripcion, prioridad) VALUES (%s, %s)",
        (descripcion, prioridad)
    )

    conexion.commit()
    cursor.close()
    conexion.close()
    return jsonify({"Mensaje": "Tarea agregada"}), 201

#Paso 9
@app.route('/tareas', methods=['GET'])
def obtener_tareas():
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456789",
        database="productividad"
    )
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tareas")
    tareas = cursor.fetchall()
    cursor.close()
    conexion.close()
    return jsonify(tareas)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
