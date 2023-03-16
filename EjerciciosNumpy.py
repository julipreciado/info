import numpy as np
#Ejercicio 1:
#Crear una matriz de ceros tipo entero 3x4
matrizceros=np.zeros((3,4), dtype=int)
print(f"Matriz ceros: \n{matrizceros}")

#Crear una matriz de ceros de tipo entero 3x4 excepto la primera fila que será uno
matrizceros1=np.zeros((2,4),dtype=int)
matrizunos=np.ones((1,4), dtype=int)
union=np.concatenate([matrizunos, matrizceros1])
print(f"Matriz unos y ceros: \n{union}")

#Crear una matriz de ceros de tipo entero 3x4 excepto la última fila que será el rango entre 5 y 8
matriz2=np.array([5,6,7,8],dtype=int)
union1=np.vstack([matrizceros1, matriz2])
print(f"Matriz de ceros y rango 5 y 8: \n{union1}")


#Ejercicio 2:
#Crear un vector de 10 elementos, siendo los índices impares unos y los índices pares dos
arr=np.arange(10)
arr[(arr%2==0)]=2
arr[(arr%2!=0)]=1
print(f"Vector con índices impares unos e índices pares dos: \n{arr}")

#Crear un tablero de ajedrez con unos en las casillas negras y ceros en las blancas
ajedrez=np.zeros((6,6), dtype=int)
ajedrez[::2, 1::2]=1
ajedrez[1::2, ::2]=1
print(f"Ajedrez: \n{ajedrez}")


#Ejercicio 3:
#Crear una matriz aleatoria 5x5 y hallar máximo y mínimo
semi=np.random.default_rng(1)
aleatoria=semi.random((5,5))
maximo=aleatoria.max()
minimo=aleatoria.min()
norma=(aleatoria-minimo)/(maximo-minimo)
print (f"Matriz aleatoria 5x5: \n{aleatoria}")
print(f"Valor máximo: {maximo}, Valor mínimo: {minimo}")
print(f"Normalizada: \n{norma}")
