import sqlite3
import pandas as pd
#crear clase Leyes
class Leyes:
    def __init__(self): #definimos el constructor
        self.tipoNorma = None #inicializamos todo en 0 o nulo
        self.numNorma = None
        self.fecha = None
        self.desc = None
        self.cat = None
        self.jur = None
        self.org = None
        self.keyW = None

    def ingresar_datos(self): #pedimos al usuario insertar los datos
        self.tipoNorma = input("Tipo de Normativa: ")
        self.numNorma = input("Numero de Normativa: ")
        self.fecha = input("Fecha: ")
        self.desc = input("Descripcion: ")
        self.cat = input("Categoria: ")
        self.jur = input("Jurisdiccion: ")
        self.org = input("Organo Legislativo: ")
        self.keyW = input("Palabra Clave: ")

    def insertar_ley(self, conexion):#esta parte guarda los datos recien pedidos, en la bbdd
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO laws (TipoDeNormativa, NumeroDeNormativa, Fecha, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabraClave) VALUES (?,?,?,?,?,?,?,?)",
                       (self.tipoNorma, self.numNorma, self.fecha, self.desc, self.cat, self.jur, self.org, self.keyW))
        conexion.commit()
