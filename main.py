import sqlite3
import pandas as pd

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

    def insertar_ley(self, conexion):
        cursor = conexion.cursor()
        cursor.execute("INSERT INTO laws (TipoDeNormativa, NumeroDeNormativa, Fecha, Descripcion, Categoria, Jurisdiccion, OrganoLegislativo, PalabraClave) VALUES (?,?,?,?,?,?,?,?)",
                       (self.tipoNorma, self.numNorma, self.fecha, self.desc, self.cat, self.jur, self.org, self.keyW))
        conexion.commit()

    def ver_laws(self, conexion):
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM laws")
        results = cursor.fetchall()
        results_df = pd.DataFrame(results, columns=["Nro", "TipoDeNormativa", "NumeroDeNormativa", "Fecha", "Descripcion", "Categoria", "Jurisdiccion", "OrganoLegislativo", "PalabraClave"])
        print(results_df)

def menu():
    print("------------------Menu------------------")
    print("Seleccione 1 para insertar Leyes")
    print("Seleccione 2 para ver las Leyes Existentes")
    print("Seleccione 3 para salir del programa")

def preguntarOtra(ob_ley):
    otro = input("Otra? (si/no): ")
    if otro == "si":
        ob_ley.ingresar_datos()
        preguntarOtra(ob_ley)

with sqlite3.connect("Proyect") as P:
    cursor = P.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS laws (Nro INTEGER PRIMARY KEY AUTOINCREMENT, TipoDeNormativa VARCHAR(50), NumeroDeNormativa VARCHAR(50), Fecha VARCHAR(20), Descripcion VARCHAR(50), Categoria VARCHAR(50), Jurisdiccion VARCHAR(50), OrganoLegislativo VARCHAR(50), PalabraClave VARCHAR(50))")
    
    ob_ley = Leyes()
    
    while True:
        menu()
        opcion = input("Ingrese una opción: ")
        
        if opcion == "1":
            ob_ley.ingresar_datos()
            ob_ley.insertar_ley(P)
            preguntarOtra(ob_ley)
            
        elif opcion == "2":
            ob_ley.ver_laws(P)
            
        elif opcion == "3":
            print("Adios...")
            break
