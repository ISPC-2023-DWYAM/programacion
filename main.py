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

    def ver_laws(self, conexion): #esta funcion se conecta a la bbdd y pide ver el contenido
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM laws")
        results = cursor.fetchall()
        results_df = pd.DataFrame(results, columns=["Nro", "TipoDeNormativa", "NumeroDeNormativa", "Fecha", "Descripcion", "Categoria", "Jurisdiccion", "OrganoLegislativo", "PalabraClave"])
        print(results_df)

def menu(): #menu mas completo igual falta agregar mucho
    print("------------------Menu------------------")
    print("Seleccione 1 para insertar Leyes")
    print("Seleccione 2 para ver las Leyes Existentes")
    print("Seleccione 3 para salir del programa")

def preguntarOtra(ob_ley):#esta funcion pregunta si quiere insertar otra ley de la opcion 1 del menu
    otro = input("Agregar Otra Ley? (si/no): ")
    if otro == "si":
        ob_ley.ingresar_datos()
        preguntarOtra(ob_ley)

with sqlite3.connect("Proyect") as P:#aca empieza el programa las de arriba son las funciones y clase
    cursor = P.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS laws (Nro INTEGER PRIMARY KEY AUTOINCREMENT, TipoDeNormativa VARCHAR(50), NumeroDeNormativa VARCHAR(50), Fecha VARCHAR(20), Descripcion VARCHAR(50), Categoria VARCHAR(50), Jurisdiccion VARCHAR(50), OrganoLegislativo VARCHAR(50), PalabraClave VARCHAR(50))")
    
    ob_ley = Leyes()#objeto que se crea cada vez que insertamos
    
    while True:#este bucle while impide que termine el programa hasta elegir opcion 3 de break
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
