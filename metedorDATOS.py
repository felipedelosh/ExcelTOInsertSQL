"""
FelipedelosH

meter desde el CMD a la base de datos en oracle.
NOTA: Hecho en windows
NOTA: Las carpetas de la ruta no pueden tener espacios


Nota: 50mil registros tardarón 4 horas.

"""

import os
from os import system

print("Programa creado por el loco")
print("Abriendo el terminal...")

DB_user = "SYSTEM"
DB_pass = "kmzwa8awaa"
DB_name = "XE" #select name from V$database;
script_PATH = str(os.path.dirname(os.path.abspath(__file__)))+"\\script.sql"
script_test_PATH = str(os.path.dirname(os.path.abspath(__file__)))+"\\test.sql"

sql = ""

#print("Ejecutando el script de las tablas...")
#sql = "sqlplus"+" "+DB_user+"/"+DB_pass+"@"+DB_name+" @"+script_test_PATH
#print(sql)
#print("=======Ejecutando...========")
#system(sql) # Aca imprime las tabalas de multiplicar
#print("============Test Finalizado...===============")

print("Creando el archivo desde el excel ")
f = open('temp.csv', 'r', encoding="UTF-8")
data = []

for i in f.read().split("\n"):
    temp_data = i.split(",")
    depto = ""
    try:
        depto = temp_data[0]
    except:
        depto = "NULL"
    city = ""
    try:
        city = temp_data[1]
    except:
        city = "NULL"
    placa_vehiculo = ""
    try:
        placa_vehiculo = temp_data[2]
    except:
        placa_vehiculo = "NULL"
    fecha = ""
    try:
        fecha = temp_data[3]
    except:
        fecha = "NULL"
    codigo = ""
    try:
        codigo = temp_data[4]
    except:
        codigo = "NULL"
    TEMP_QUERY = "'"+depto+"', '"+city+"', '"+placa_vehiculo+"', '"+fecha+"', '"+codigo+"'"
    #print(TEMP_QUERY)
    data.append(TEMP_QUERY)

print("Termine de cargar los datos....")


"""create table ejemplo(
departamento varchar2(50),
ciudad varchar2(50),
placa_vehiculo varchar2(50),
fecha varchar2(50),
codigo_infraccion varchar2(50)
);
"""
SQL_encabezado = "insert into ejemplo(departamento, ciudad, placa_vehiculo, fecha, codigo_infraccion) values("

data_OUTPUT = ""
con = 0
total_datos = len(data)
for i in data:
    print("Cargando info...", con, " de ", total_datos)
    con = con + 1
    data_OUTPUT = data_OUTPUT + SQL_encabezado+i+");\n"

print("Creando el archivo script.sql")

f = open('script.sql', 'w', encoding="UTF-8")
f.write(data_OUTPUT)
f.close()


print("Archivo script.sql creado...")
