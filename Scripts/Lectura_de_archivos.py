
import pandas as pd

def main():
    df = leer_archivos()
    df=agregar_filtros(df)
    #visualizar_datos(df)
    exportar_datos(df)


def leer_archivos():
    print("LEYENDO ARCHIVO")
    #import os
    lista_colums=[1,2,3,4,5]

    #path="..\input"
    #filename=input("Ingresar el nombre del archivo: ")+"xlsx"
    #fullpath=os.path.join(path,filename)
    
    datos=pd.read_excel("C:\\Users\\lucas\\Desktop\\AutoExcel\\input\\CARGA CATEGORIAS.xlsx",
                    sheet_name="Datos",
                    header=0,
                    usecols=lista_colums)
    return datos

def agregar_filtros(datos):
    print("AGREGANDO FILTROS")
    
    datos=  datos[datos["Producto Desc"]=="NALGA DE ADENTRO S/T (CAJA)"]
    return  datos

def visualizar_datos(datos):
    print("VISUALIZANDO LOS PRIMEROS 5 DATOS")
    datos_cols=datos.columns

    for col in datos_cols:
        print(datos[col].head(5))


def exportar_datos(datos):
    print("EXPORTANDO RESULTADOS")
    datos.to_csv("C:\\Users\\lucas\\Desktop\\AutoExcel\\Output\\Prueba.csv",
             sep = ",",
            header = True,
             index = False)


if __name__=="__main__":
    main()
    input("\tPROCESO FINALIZADO... Presiona enter para salir")