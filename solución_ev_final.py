import pandas as pd
import numpy as np

#1 descargar archivo “detalle_boletas.csv”. Crea un Data Frame de nombre “detalle_boletas”
detalle_boletas=pd.read_csv("detalle_boletas.csv",encoding="latin-1",sep=",")
print(detalle_boletas)
print(detalle_boletas.dtypes)

#2a Eliminar la columna Precio_prod
del detalle_boletas["Precio_prod"]
print(detalle_boletas)

#2b Crear una columna “Pais_Venta”
detalle_boletas["Pais_Venta"]="Chile"
print(detalle_boletas)

#2c Cambiar el nombre de la columna “NXXX” por “Num Boleta”.
detalle_boletas=detalle_boletas.rename(columns={"NXXX":"Num Boleta"})
print(detalle_boletas)

#3a Hay productos con ID “4XXXXX” y Num Boletas “55417XXXXXXX”. Eliminar cualquier fila que contenga alguno de los dos.
detalle_boletas=detalle_boletas.loc[(~detalle_boletas["ID"].str.contains("4XXXXX"))&(~detalle_boletas["Num Boleta"].str.contains("55417XXXXXXX"))]
print(detalle_boletas)

#3b Eliminar caracteres extra en la columna "Fecha"
detalle_boletas["Fecha"]=detalle_boletas["Fecha"].str.replace(".","")
detalle_boletas["Fecha"]=detalle_boletas["Fecha"].str.replace("{","")                                 
detalle_boletas["Fecha"]=detalle_boletas["Fecha"].str.replace("-","")
detalle_boletas["Fecha"]=detalle_boletas["Fecha"].str.replace("!","")
print(detalle_boletas)

#4Calcular e imprimir estadísticos descriptivos de la columna "Cantidad" para todos los productos del Data Frame 
pivot_table=detalle_boletas.pivot_table(index="ID",values="Cantidad",aggfunc={np.mean,np.min,np.max,np.std})
print(pivot_table)

#5 Separar la columna "Fecha" en tres columnas: "Anho", "Mes" y "Dia".Eliminar columna Fecha.
detalle_fecha=detalle_boletas["Fecha"].str.split("/",expand=True)
detalle_fecha.columns=["Anho","Mes","Dia"]
detalle_boletas=detalle_boletas.join(detalle_fecha)
print(detalle_boletas)
del detalle_boletas["Fecha"]
print(detalle_boletas)

#6 Descarga el archivo “Lista productos.csv” de la plataforma y crea DF "lista_productos".
lista_productos=pd.read_csv("Lista productos.csv",encoding="latin-1",sep=",")
lista_productos=lista_productos.rename(columns={"ï»¿ID":"ID"})
lista_productos["ID"]=lista_productos["ID"].astype("object")
print(lista_productos)
print(lista_productos.dtypes)

#7  Unir lista_productos a detalle_boletas en base a la información de columna "ID". Asignar nuevo DF llamado detalle_boletas2
detalle_boletas["ID"]=detalle_boletas["ID"].astype(str)
lista_productos["ID"]=lista_productos["ID"].astype(str)
detalle_boletas2=detalle_boletas.merge(lista_productos,on="ID")
print(detalle_boletas2)

#8 Crear columna "Ingreso total" como la multiplicación de la columna "Precio Unitario" y "Cantidad" en detalle_boletas2. Imprimir.
detalle_boletas2["Ingreso total"]=detalle_boletas2["Precio Unitario"]*detalle_boletas2["Cantidad"]
print(detalle_boletas2)

#9 Calcular e imprimir estadísticos descriptivos de la columna "Ingreso total" para todos los productos del Data Frame detalle_boletas2.
pivot_table2=detalle_boletas2.pivot_table(index="ID",values="Ingreso total",aggfunc={np.mean,np.min,np.max,np.std,np.sum})
print(pivot_table2)


