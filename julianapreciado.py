import pymongo
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import scipy.io as sio
import scipy.fftpack as fft
import cv2
import seaborn as sns

client = pymongo.MongoClient("mongodb+srv://julipreciado:1234@cluster0.p75sqrz.mongodb.net/?retryWrites=true&w=majority")
db = client.test
mydb=client["Hospital"]
mycol=mydb["neurología"]
  
    
def validardatos(n):
        try:
            entero=int(n) 
            return int(n)
        except ValueError:
            print("El dato ingresado no es un número, ingrese el dato de nuevo")

cedula=int(input("Ingrese la cédula del paciente: "))
nombre=input("Ingrese el nombre del paciente: ")
edad=int(input("Ingrese la edad del paciente: "))
mydict ={"nombre": nombre, "cedula":cedula, "edad":edad}
x=mycol.insert_one(mydict)

while True:
    print("-SISTEMA DE LECTURA DE SEÑALES-")
    ruta_señal="C:\\Users\\usuario\\Downloads\\drive-download-20230331T031844Z-001\\C032_EP_reposo.mat"
    newvalues={"$set": {"ruta de acceso":"C:\\Users\\usuario\\Downloads\\drive-download-20230331T031844Z-001\\C032_EP_reposo.mat"}}
    mycol.update_one(mydict, newvalues)

    mat_contents= sio.loadmat(ruta_señal)
    señal=mat_contents["data"]
    op=input("""
    Bienvenido al menú 1, ingrese la opción que desea ejecutar.
    1. Ver tamaño de la señal
    2. Graficar una señal de EEG continua
    3. Graficar una época de señal de EEG
    4. Graficar la señal de un color determinado
    5. Análisis de datos
    6. Salir
    >""")
    validardatos(op)
    if op=="1":
        print("Imprimir el tamaño de la señal")
        print("La señal tiene una dimensión de ", señal.ndim ," y una forma de ", señal.shape)

    elif op=="2":
        print("Graficar una señal de EEG continua")
        sensores=señal.shape[0]
        puntos=señal.shape[1]
        epocas=señal.shape[2]
        señal_continua=np.reshape(señal, (sensores, puntos*epocas), order="F")
        plt.subplot(1,1,1)
        plt.plot(señal_continua[0,0:1999])
        plt.title("Señal de EEG continua")
        plt.show()


    elif op=="3":
        print("Graficar una época de una señal de EEG")
        plt.subplot(1,1,1) 
        plt.plot(señal[0,0:1000,0]) 
        plt.title("Señal de una época")
        plt.show()
    elif op=="4":
        print("Graficar la señal con un color determinado y guardarla")
        color_ingresado=input("Ingrese un color en formato hexadecimal: ")
        plt.subplot(1,1,1) 
        plt.plot(señal[0,0:1000,0],color=color_ingresado) 
        plt.title("Señal con color determinado")
        plt.savefig("señalcolor2.jpg")
        plt.show()
        newvalues={"$set": {"ubicación imagen señal":"C:\\Users\\usuario\\Desktop\\info\\señalcolor2.jpg"}}
        mycol.update_one(mydict, newvalues)
    elif op=="5":
        print("Análisis de los datos")
        op5=input("""
        Bienvenido al menú 2, ingrese la opción que desea ejecutar:
        1. Ver el promedio de las 8 filas de la señal continua
        2. Ver el histograma del promedio del punto 1
        3. Ver una imagen de calor y guardarla
        4. Ver imagen en blanco y negro
        5. Salir
        >""")
        validardatos(op5)
        if op5=="1":
            print("Ver el promedio de las 8 filas de la señal continua")
            promedios_filas=np.mean(señal_continua, axis=1)
            y=np.arange(8)
            y1=y.reshape(-1,1)
            promedios=np.concatenate([y1, promedios_filas.reshape(-1,1)], axis=1)
            print (promedios)
        elif op5=="2":
            print("Ver el histograma del promedio del punto 1")
            plt.hist([promedios_filas, y], bins=8, label=["promedio", "fila"])
            plt.title("Histograma")
            plt.show()

        elif op5=="3":
            print("Ver una imagen de calor y guardarla")
            nuevaseñal=señal.reshape((señal.shape[0]*señal.shape[1]), señal.shape[2])
            nuevaseñal=nuevaseñal[:100, 100:]
            ax=sns.heatmap(nuevaseñal)
            plt.title("Mapa de calor a color")
            plt.savefig("mapadecalorcolor2.jpg")
            plt.show()
            newvalues={"$set": {"ubicación mapa de calor":"C:\\Users\\usuario\\Desktop\\info\\mapadecalorcolor2.jpg"}}
            mycol.update_one(mydict, newvalues)

        elif op5=="4":
            print("Ver imagen en blanco y negro y guardarla")
            ax=sns.heatmap(nuevaseñal, cmap="Greys")
            plt.title("Mapa de calor a blanco y negro")
            plt.savefig("mapadecalorbyn2.jpg")
            plt.show()
        elif op5=="5":
            print("Ha finalizado el menú 2")
            break
    
    elif op=="6":
        print("Ha finalizado el menú 1")
        break
        
