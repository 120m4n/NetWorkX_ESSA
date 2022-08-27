import cx_Oracle
import csv
from network import funciones
from network.configuraciones import consultas
import os

path_registro = os.getcwd()

tns_name = funciones.ArmaConnect(path_registro)
print('		'+tns_name)

con = cx_Oracle.connect(tns_name)
cur = con.cursor()

cur.execute('ALTER SESSION SET CURRENT_SCHEMA = INVENTARIO')

circuito = '20 507'
cur.execute(consultas['tramomt'], circuito = circuito)

rows = -1
if rows > 0:
    res = cur.fetchmany(numRows=rows)
else:
    res = cur.fetchall()


with open('./csv/tramomt_'+ circuito.replace(' ', '_') +'.csv', mode='w', newline="") as data_file:
    data_writer = csv.writer(data_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(['CODIGOELEMENTO', 'NODO1', 'NODO2', 'CODCTO1', 'CODCTO2', 'X', 'Y', 'X1', 'Y1'])
    for row in res:
        data_writer.writerow(row)


cur.execute(consultas['tramobt'], circuito=circuito)

if rows > 0:
    res = cur.fetchmany(numRows=rows)
else:
    res = cur.fetchall()


with open('./csv/tramobt_' + circuito.replace(' ', '_') + '.csv', mode='w', newline="") as data_file:
    data_writer = csv.writer(data_file, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    data_writer.writerow(['CODIGOELEMENTO','NODO1','NODO2','CODTRAFODIS','X','Y','X1','Y1'])
    for row in res:
        data_writer.writerow(row)

