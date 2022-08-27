import configparser
import os

template_tramobt = """
<OGRVRTDataSource>
	<OGRVRTLayer name="filename">
		<SrcDataSource>filename.csv</SrcDataSource>
		<SrcSQL dialect="sqlite"> SELECT *, MakeLine(MakePoint(CAST(X AS float),CAST(Y AS float)) , MakePoint(CAST(X1 AS float),CAST(Y1 AS float))) FROM filename</SrcSQL>		
		<Field name="CODIGOELEMENTO"	src="CODIGOELEMENTO"	type="String"	width="15"    />	
		<Field name="NODO1"				src="NODO1"				type="String"	width="10"   />	
		<Field name="NODO2"				src="NODO2"				type="String"	width="10"   />	
		<Field name="CODTRAFODIS"		src="CODTRAFODIS"		type="String"	width="10"   />		
		<Field name="X"					src="X"					type="Real"		width="16" 	 precision="7"  />
		<Field name="Y"					src="Y"					type="Real"		width="16" 	 precision="7"  />
		<Field name="X1"				src="X1"				type="Real"		width="16" 	 precision="7"  />
		<Field name="Y1"				src="Y1"				type="Real"		width="16" 	 precision="7"  />
		<GeometryType>wkbLineString</GeometryType>
		<LayerSRS>EPSG:3116</LayerSRS>
	</OGRVRTLayer>
</OGRVRTDataSource>
"""

template_tramomt = """
<OGRVRTDataSource>
	<OGRVRTLayer name="filename">
		<SrcDataSource>filename.csv</SrcDataSource>
		<SrcSQL dialect="sqlite"> SELECT *, MakeLine(MakePoint(CAST(X AS float),CAST(Y AS float)) , MakePoint(CAST(X1 AS float),CAST(Y1 AS float))) FROM filename</SrcSQL>		
		<Field name="CODIGOELEMENTO"		   src="CODIGOELEMENTO"		type="String"	width="15"    />	
		<Field name="NODO1"					src="NODO1"				type="String"	width="10"   />	
		<Field name="NODO2"					src="NODO2"				type="String"	width="10"   />	
		<Field name="CODCTO1"				src="CODCTO1"			type="String"	width="10"   />	
		<Field name="CODCTO2"				src="CODCTO2"			type="String"	width="10"   />			
		<Field name="X"					src="X"				type="Real"		width="16" 	 precision="7"  />
		<Field name="Y"					src="Y"				type="Real"		width="16" 	 precision="7"  />
		<Field name="X1"					src="X1"				type="Real"		width="16" 	 precision="7"  />
		<Field name="Y1"					src="Y1"				type="Real"		width="16" 	 precision="7"  />
		<GeometryType>wkbLineString</GeometryType>
		<LayerSRS>EPSG:3116</LayerSRS>
	</OGRVRTLayer>
</OGRVRTDataSource>
"""

def KeyCartographyini(ruta, section, key, filename="configuracion.ini"):
	if os.path.exists(ruta):
		os.chdir(ruta)
		Config = configparser.ConfigParser()
		Config.read(filename)
		try:
			return Config.get(section, key)
		except configparser.NoOptionError:
			return 'None'
		except configparser.NoSectionError:
			return 'None'
	else:
		return 'Ruta o path no existe'

def ArmaConnect(path):
	connect = KeyCartographyini(path, 'CONFIGURACION', 'Esquema')
	connect += '/'
	connect += KeyCartographyini(path, 'CONFIGURACION', 'Clave')
	connect += '@'
	connect += KeyCartographyini(path, 'CONFIGURACION', 'Host')
	connect += ':'
	connect += KeyCartographyini(path, 'CONFIGURACION', 'Puerto')
	connect += '/'
	connect += KeyCartographyini(path, 'CONFIGURACION', 'Instancia')
	#print(connect)
	return connect

def GenerateTramoBTVRT(path, filename):
	tramobt = template_tramobt.replace('filename', filename)
	with open(path + '/' + filename + '.vrt',  'w', newline="") as file:
		file.writelines(tramobt)


def GenerateTramoMTVRT(path, filename):
	tramomt = template_tramomt.replace('filename', filename)
	with open(path + '/' + filename + '.vrt',  'w', newline="") as file:
		file.writelines(tramomt)
