import os
import oracledb
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()


username = os.getenv("ORACLE_USER")
dsn = os.getenv("ORACLE_DSN")
password = os.getenv("ORACLE_PASSWORD")

# Función para obtener la conexión
def get_connection():
    return oracledb.connect(user=username, password=password, dsn=dsn)


def create_schema(query):
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(query)
                print(f"Tabla creada \n {query}")
    except oracledb.DatabaseError as error:
        print(f"No se pudo crear la tabla: {error}")


def create_all_tables():
    tables = [
        """
        CREATE TABLE usuario (
            nombre VARCHAR(45),
            rut VARCHAR(10) PRIMARY KEY,
            correo VARCHAR(30)
        );
        """,
        """
        CREATE TABLE estudiante (
            id_estudiante INTEGER PRIMARY KEY,
            nombre VARCHAR(45),
            rut VARCHAR(10),
            correo VARCHAR(30),
            FOREIGN KEY (rut) REFERENCES usuario(rut)
        );
        """,
        """
        CREATE TABLE docente (
            id_docente INTEGER PRIMARY KEY,
            nombre VARCHAR(45),
            rut VARCHAR(10),
            correo VARCHAR(30),
            FOREIGN KEY (rut) REFERENCES usuario(rut)
        );
        """,
        """
        CREATE TABLE investigador (
            id_investigador INTEGER PRIMARY KEY,
            nombre VARCHAR(45),
            rut VARCHAR(10),
            correo VARCHAR(30)
        );
        """,
        """
        CREATE TABLE libro (
            id_libro INTEGER PRIMARY KEY,
            titulo VARCHAR(50),
            autor VARCHAR(20),
            categoria VARCHAR(35),
            disponibilidad BOOLEAN
        );
        """,
        """
        CREATE TABLE prestamo (
            id_prestamo INTEGER PRIMARY KEY,
            fecha_inicio DATE,
            fecha_fin DATE,
            estado VARCHAR(20),
            rut_usuario VARCHAR(10),
            id_libro INTEGER,
            FOREIGN KEY (rut_usuario) REFERENCES usuario(rut),
            FOREIGN KEY (id_libro) REFERENCES libro(id_libro)
        );
        """
    ]
    for query in tables:
        create_schema(query)


def create_usuario(nombre, rut, correo):
    sql = "INSERT INTO usuario (nombre, rut, correo) VALUES (:nombre, :rut, :correo)"
    parametros = {"nombre": nombre, "rut": rut, "correo": correo}
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Usuario insertado correctamente")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato: {error}")

def create_estudiante(id_estudiante, nombre, rut, correo):
    sql = "INSERT INTO estudiante (id_estudiante, nombre, rut, correo) VALUES (:id_estudiante, :nombre, :rut, :correo)"
    parametros = {"id_estudiante": id_estudiante, "nombre": nombre, "rut": rut, "correo": correo}
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Estudiante insertado correctamente")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato: {error}")

def create_docente(id_docente, nombre, rut, correo):
    sql = "INSERT INTO docente (id_docente, nombre, rut, correo) VALUES (:id_docente, :nombre, :rut, :correo)"
    parametros = {"id_docente": id_docente, "nombre": nombre, "rut": rut, "correo": correo}
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Docente insertado correctamente")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato: {error}")

def create_investigador(id_investigador, nombre, rut, correo):
    sql = "INSERT INTO investigador (id_investigador, nombre, rut, correo) VALUES (:id_investigador, :nombre, :rut, :correo)"
    parametros = {"id_investigador": id_investigador, "nombre": nombre, "rut": rut, "correo": correo}
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Investigador insertado correctamente")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato: {error}")

def create_libro(id_libro, titulo, autor, categoria, disponibilidad):
    sql = "INSERT INTO libro (id_libro, titulo, autor, categoria, disponibilidad) VALUES (:id_libro, :titulo, :autor, :categoria, :disponibilidad)"
    parametros = {"id_libro": id_libro, "titulo": titulo, "autor": autor, "categoria": categoria, "disponibilidad": disponibilidad}
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Libro insertado correctamente")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato: {error}")

def create_prestamo(id_prestamo, fecha_inicio, fecha_fin, estado, rut_usuario, id_libro):
    sql = "INSERT INTO prestamo (id_prestamo, fecha_inicio, fecha_fin, estado, rut_usuario, id_libro) VALUES (:id_prestamo, :fecha_inicio, :fecha_fin, :estado, :rut_usuario, :id_libro)"
    parametros = {"id_prestamo": id_prestamo, "fecha_inicio": fecha_inicio, "fecha_fin": fecha_fin, "estado": estado, "rut_usuario": rut_usuario, "id_libro": id_libro}
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                cursor.execute(sql, parametros)
            connection.commit()
            print("Préstamo insertado correctamente")
    except oracledb.DatabaseError as error:
        print(f"No se pudo insertar el dato: {error}")


def read_usuarios():
    sql = "SELECT * FROM usuario"
    try:
        with get_connection() as connection:
            with connection.cursor() as cursor:
                resultados = cursor.execute(sql)
                for fila in resultados:
                    print(fila)
    except oracledb.DatabaseError as error:
        print(f"No se pudo ejecutar la query {error}")


def menu_usuario():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |         Menu: Usuario            |
                |----------------------------------|
                | 1. Insertar un dato              |
                | 2. Consultar todos los datos     |
                | 0. Volver al menu principal      |
                ====================================
            """
        )
        opcion = input("Elige una opción [1-2, 0]: ")
        if opcion == "1":
            os.system("cls")
            print("1. Insertar un Usuario")
            nombre = input("Ingrese nombre del usuario: ")
            rut = input("Ingrese rut del usuario: ")
            correo = input("Ingrese correo del usuario: ")
            create_usuario(nombre, rut, correo)
            input("Presione ENTER para continuar...")
        elif opcion == "2":
            os.system("cls")
            print("2. Consultar todos los usuarios")
            read_usuarios()
            input("Presione ENTER para continuar...")
        elif opcion == "0":
            break
        else:
            os.system("cls")
            print("Opción incorrecta, intente nuevamente.")
            input("Presione ENTER para continuar...")

# Menú principal
def main():
    while True:
        os.system("cls")
        print(
            """
                ====================================
                |     CRUD: Sistema de Biblioteca   |
                |----------------------------------|
                | 1. Crear todas las tablas        |
                | 2. Gestionar usuarios            |
                | 0. Salir del sistema             |
                ====================================
            """
        )
        opcion = input("Elige una opción [1-2, 0]: ")
        if opcion == "1":
            os.system("cls")
            create_all_tables()
            input("Presione ENTER para continuar...")
        elif opcion == "2":
            menu_usuario()
        elif opcion == "0":
            break
        else:
            os.system("cls")
            print("Opción incorrecta, intente nuevamente.")
            input("Presione ENTER para continuar...")


if __name__ == "__main__":
    main()
