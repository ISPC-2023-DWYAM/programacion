import sqlite3
import pandas as pd


# Clase Leyes para insertar y ver leyes
class Leyes:
    def __init__(self):
        self.tipoNorma = None
        self.numNorma = None
        self.fecha = None
        self.desc = None
        self.cat = None
        self.jur = None
        self.org = None
        self.keyW = None

    def ingresar_datos(self):
        self.tipoNorma = input("Tipo de Normativa: ")
        self.numNorma = input("Numero de Normativa: ")
        self.fecha = input("Fecha: ")
        self.desc = input("Descripcion: ")
        self.cat = input("Categoria: ")
        self.jur = input("Jurisdiccion: ")
        self.org = input("Organo Legislativo: ")
        self.keyW = input("Palabra Clave: ")

    def insertar_ley_tabla1(self, P):
        cursor = P.cursor()
        cursor.execute("INSERT INTO tabla1 (TipoDeNormativa, NumeroDeNormativa, Fecha, Descripcion) VALUES (?,?,?,?)",
                       (self.tipoNorma, self.numNorma, self.fecha, self.desc))

    def insertar_ley_tabla2(self, P):
        cursor = P.cursor()
        cursor.execute("INSERT INTO tabla2 (Nro, Categoria, Jurisdiccion) VALUES (?,?,?)",
                       (self.numNorma, self.cat, self.jur))

    def insertar_ley_tabla3(self, P):
        cursor = P.cursor()
        cursor.execute("INSERT INTO tabla3 (Nro, OrganoLegislativo, PalabraClave) VALUES (?,?,?)",
                       (self.numNorma, self.org, self.keyW))

    def ver_laws_unificadas(self, P):
        cursor = P.cursor()
        cursor.execute("SELECT t1.Nro, t1.TipoDeNormativa, t1.NumeroDeNormativa, t1.Fecha, t1.Descripcion, t2.Categoria, t2.Jurisdiccion, t3.OrganoLegislativo, t3.PalabraClave "
                       "FROM tabla1 AS t1 "
                       "JOIN tabla2 AS t2 ON t1.NumeroDeNormativa = t2.Nro "
                       "JOIN tabla3 AS t3 ON t1.NumeroDeNormativa = t3.Nro")
        results = cursor.fetchall()
        results_df = pd.DataFrame(results, columns=["Nro", "TipoDeNormativa", "NumeroDeNormativa", "Fecha",
                                                    "Descripcion", "Categoria", "Jurisdiccion",
                                                    "OrganoLegislativo", "PalabraClave"])
        print(results_df)

