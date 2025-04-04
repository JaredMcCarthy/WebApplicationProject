import mysql.connector

conexion = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="123456789",
    database="productividad"
)

cursor = conexion.cursor()

cursor.execute("SELECT DATABASE()")
base_de_datos = cursor.fetchone()
print("Conectado a la base de datos:", base_de_datos[0] if base_de_datos else "No se pudo conectar")

cursor.close()
conexion.close()


def agregar_tarea(descripcion):
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456789",
        database="productividad"
    )
    cursor = conexion.cursor()

    # Insertar nueva tarea
    consulta = "INSERT INTO tareas (descripcion) VALUES (%s)"
    valores = (descripcion,)  # Asegúrate de que sea una tupla
    cursor.execute(consulta, valores)

    # Guardar info en la base de datos
    conexion.commit()

    print("Tarea agregada correctamente.")
    cursor.close()
    conexion.close()


def ver_tareas():
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456789",
        database="productividad"
    )
    cursor = conexion.cursor()

    consulta = "SELECT * FROM tareas"
    cursor.execute(consulta)
    tareas = cursor.fetchall()

    if tareas:
        print("\nLista de tareas:")
        for tarea in tareas:
            print(f"ID: {tarea[0]}, Descripcion: {tarea[1]}, Completado: {'Si' if tarea[2] else 'No'}")
    else:
        print("No hay tareas registradas.")

    cursor.close()
    conexion.close()


def marcar_completadas(id_tareas):
    conexion = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="123456789",
        database="productividad"
    )

    try:
        cursor = conexion.cursor()

        # Verificar si la tarea existe
        cursor.execute("SELECT id FROM tareas WHERE id = %s", (id_tareas,))
        tarea_existe = cursor.fetchone()

        if tarea_existe:
            # Marcar como completada
            consulta = "UPDATE tareas SET completado = TRUE WHERE id = %s"
            valores = (id_tareas,)
            cursor.execute(consulta, valores)

            conexion.commit()
            print(f"Tarea {id_tareas} marcada como completada.")
        else:
            print(f"Error: La tarea con ID {id_tareas} no existe.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conexion.close()

def menu():
    while True:
        print("----Menu de Tareas----")
        print("1. Ver tareas")
        print("2. Agregar Tareas")
        print("3. Marcar tarea como completada")
        print("4. Salir ")
        opcion = input("Seleccione una de las opciones: ")

        if opcion == "1":
            ver_tareas()
        elif opcion == "2":
            descripcion = input("Ingresa la descripcion de la tarea: ")
            agregar_tarea(descripcion)
        elif opcion == "3":
            id_tarea = input(" Ingrese el ID de la tarea a marcar como completada ")
            if id_tarea.isdigit():
                marcar_completadas(int(id_tarea))
            else:
                print("Error: El ID debe ser un numero.")
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opcion no valida. Intente de nuevo.")


menu()

























