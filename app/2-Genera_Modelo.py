from venv import main
import networkx as nx
from network import funciones 
import csv
import os

def generateEdges(filename):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        edges = []
        for row in csv_reader:
            # print(row)
            edges.append((row[1], row[2]))
        return edges


def shortestPath(Graph, node1, node2):
    if nx.has_path(Graph, node1, node2):
        print(nx.shortest_path(Graph, source=node1, target=node2))
    else:
        print('No path specified')


def saveGraph(graph, fileoutput):
    nx.write_graphml(graph, fileoutput)

def generateShapefile(fileoutput, vrt_file, options=''):
    if options !='':
        os.system(
            "ogr2ogr -f GPKG {}.gpkg {}.vrt -lco IDENTIFIER={} {}".format(fileoutput, vrt_file, vrt_file,  options))
    else:
        os.system(
            "ogr2ogr -f GPKG {}.gpkg {}.vrt -lco IDENTIFIER={}".format(fileoutput, vrt_file, vrt_file))


if __name__ == "__main__":
    csv_path = os.getcwd()
    cod_circuito = '20_507'
    tramobt = r'tramobt_20_507' 
    tramomt = r'tramomt_20_507' 
    G = nx.Graph()
    G.add_edges_from(generateEdges(os.path.join( csv_path, 'csv', tramobt + '.csv')))
    G.add_edges_from(generateEdges(os.path.join( csv_path, 'csv', tramomt + '.csv')))
    print(G.number_of_nodes())
    print(G.number_of_edges())
    funciones.GenerateTramoBTVRT(os.path.join(csv_path, 'csv'), tramobt)
    funciones.GenerateTramoMTVRT(os.path.join(csv_path, 'csv'), tramomt)
    # os.chdir('.\\csv')
    # generateShapefile('circuito_' + cod_circuito, tramobt)
    # generateShapefile('circuito_' + cod_circuito, tramomt, '-append')
    # saveGraph( G, 'circuito_' + cod_circuito)
    print("fin")
