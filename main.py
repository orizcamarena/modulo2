from models import Diccionario
from db import engine, Base, Session
import sys 

Base.metadata.create_all(engine)
session = Session()

try:
    
    def principal():
        menu = """
    \n--------------------------------------
            DICCIONARIO DE SLANG PANAMEÑO
    a) Agregar nueva palabra
    b) Editar palabra existente
    c) Eliminar palabra existente
    d) Ver listado de palabras
    e) Buscar significado de palabra
    f) Salir
    ----------------------------------------
    Selecciona una opción: """

        option = ""
        while option != "f":
            option = input(menu)
            if option == "a":
                palabra = input("Ingresa la palabra: ")
                posibleSignificado = obtenerSignificado(palabra)
                if posibleSignificado:
                    print(f"La palabra '{palabra}' ya existe")
                else:
                    significado = input("Ingresa el significado: ")
                    agregarPalabra (palabra, significado)
            if option == "b":
                palabra = input("Ingresa la palabra que quieres editar: ")
                nuevoSignificado = input("Ingresa el nuevo significado: ")
                editarpalabra (palabra, nuevoSignificado)
            if option == "c":
                palabra = input("Ingresa la palabra a eliminar: ")
                eliminarpalabra(palabra)
            if option == "d":
                palabras = obtenerPalabras()
                print("=== Lista de palabras ===")
                for palabra in palabras:
                    print(palabra)
            if option == "e":
                palabra = input("Ingresa la palabra de la cual quieres saber el significado: ")
                significado = obtenerSignificado(palabra)
                if significado:
                    print(f"El significado de '{palabra}' es: {significado}")
                else:
                    print(f"Palabra '{palabra}' no encontrada")
        else:
            print("\nEl programa ha finalizado,bye...")
            sys.exit()

    def agregarPalabra(palabra, significado):
        nueva_palabra = Diccionario(palabra=palabra, significado=significado)
        session.agregar
        (nueva_palabra)
        session.commit()
        print(f"Palabra agregada: {palabra}")

    def editarpalabra(palabra, nuevoSignificado):
        palabra_obj = session.query(Diccionario).filter_by(palabra=palabra).first()
        if palabra_obj:
            palabra_obj.significado= nuevoSignificado
            session.commit()
            print(f"Palabra actualizada: {palabra}")
        else:
            print(f"Palabra '{palabra}' no encontrada")

    def eliminarpalabra(palabra):
        palabra_obj = session.query(Diccionario).filter_by(palabra=palabra).first()
        if palabra_obj:
            session.delete(palabra_obj)
            session.commit()

    def obtenerPalabras():
        palabras = session.query(Diccionario.palabra).all()
        return [palabra for (palabra,) in palabras]

    def obtenerSignificado(palabra):
        palabra_obj = session.query(Diccionario).filter_by(palabra=palabra).first()
        if palabra_obj:
            return palabra_obj.significado
        else:
            return None

    if __name__ == '__main__':
        principal()


finally:
    session.commit()
    session.close()