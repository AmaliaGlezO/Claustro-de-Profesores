import streamlit as st
import pandas as pd 
from streamlit_agraph import agraph, Node, Edge, Config

# Cargar los datos desde el CSV
df = pd.read_csv('maestría e investigación.csv')

# Crear listas para nodos y aristas
nodes = []
edges = []

# Agregar el nodo central
nodes.append(Node(id="Extras_Profesores", label="Extras de los profesores", size=30))

# Crear nodos para cada actividad
maestria_node = Node(id="Maestria", label="Imparten Maestría", size=25)
grupos_investigacion_node = Node(id="Grupos_Investigacion", label="Grupos de Investigación", size=25)
consejo_cientifico_node = Node(id="Consejo_Cientifico", label="Consejo Científico", size=25)

# Agregar nodos de actividades a la lista de nodos
nodes.append(maestria_node)
nodes.append(grupos_investigacion_node)
nodes.append(consejo_cientifico_node)

# Conectar el nodo central a los nodos de actividades
edges.append(Edge(source="Extras_Profesores", target="Maestria"))
edges.append(Edge(source="Extras_Profesores", target="Grupos_Investigacion"))
edges.append(Edge(source="Extras_Profesores", target="Consejo_Cientifico"))

# Agregar nodos de profesores y conexiones a los nodos de actividades
for index, row in df.iterrows():
    profesor_id = f"{row['Nombre']} {row['Apellidos']}"
    nodes.append(Node(id=profesor_id, label=profesor_id, size=20))
    
    # Conectar a los nodos de actividades
    if row['Imparte Maestria'] == 1:
        edges.append(Edge(source=maestria_node.id, target=profesor_id))
    
    if row['Participa en grupos de investigación'] == 1:
        edges.append(Edge(source=grupos_investigacion_node.id, target=profesor_id))
    
    if row['Miembro del consejo científico'] == 1:
        edges.append(Edge(source=consejo_cientifico_node.id, target=profesor_id))

# Configuración del gráfico
config = Config(width=950,
                height=950,
                directed=True, 
                physics=True, 
                hierarchical=False)

# Generar el gráfico
return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)
