from network import funciones
import os

def generateShapefile(fileoutput, vrt_file, options=''):
    if options !='':
        os.system(
            "ogr2ogr -f GPKG {}.gpkg {}.vrt -lco IDENTIFIER={} {}".format(fileoutput, vrt_file, vrt_file,  options))
    else:
        os.system(
            "ogr2ogr -f GPKG {}.gpkg {}.vrt -lco IDENTIFIER={}".format(fileoutput, vrt_file, vrt_file))


tramobt = 'tramobt_20_504'
cod_circuito = '20_504'
funciones.GenerateTramoBTVRT('./csv', tramobt)
os.chdir('./csv')
generateShapefile('circuito_' + cod_circuito, tramobt)