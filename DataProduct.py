import streamlit as st
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter
import matplotlib.pyplot as plt
from streamlit_folium import st_folium
import folium 
from streamlit_agraph import agraph, Node, Edge, Config

with open('antiguedad-matematica.csv', 'r') as f:
    file=pd.read_csv(f)
data=pd.DataFrame(file)
ranges = [(20, 30), (30, 40), (40, 50), (50, 60), (60, 70), (70, 80)]

# Sección inicial
st.header("Análisis del claustro de profesores de MATCOM")
# Agregar una imagen
st.image("./Imagenes/matcom6.jpg", caption="Facultad de Matemática y computación", use_column_width=True)

# Introducción
st.markdown("""
<div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'>
    <h3 style='color: black;'>¿Qué veremos?</h3>
    <p style='color: black;'>
        La Facultad de Matemáticas y Computación ha demostrado ser un lugar donde convergen el talento y 
        la pasión por el conocimiento. Aquí, cada año cosechamos grandes éxitos en competiciones como el ICPC,
        y contamos con graduados que destacan en el mundo profesional, evidenciando el alto potencial de 
        nuestros estudiantes. Pero detrás de estos logros impresionantes, hay un equipo de personal altamente 
        cualificado que impulsa cada paso hacia el éxito.
        En este trabajo, nos proponemos analizar a fondo a los miembros 
        del claustro de profesores, desde una visión general hasta los 
        detalles más particulares de sus trayectorias. Vamos a explorar sus perfiles, 
        que incluyen su experiencia, títulos académicos y roles dentro de la facultad, 
        resaltando cómo esta diversidad contribuye al desarrollo de nuestra comunidad. 
        Con cada análisis, descubriremos las conexiones que hacen posible esos grandes resultados, 
        y así, entenderemos mejor cómo el esfuerzo conjunto crea un entorno propicio para el aprendizaje y 
        la innovación.
    </p>
</div>
""", unsafe_allow_html=True)
st.divider()

# Opciones de la barra lateral
secciones = ["La Facultad en Perspectiva: Un Retrato Completo", "Radiografía de la Facultad: Un Análisis del Cuerpo Docente", "Entre Cátedras y Despachos: Mapeando la Estructura de la Facultad", "Más que Docentes: Profundizando en el Perfil Investigador del Profesorado", "Desentrañando la Matriz: Un Análisis Comparativo del Profesorado"]
seccion_seleccionada = st.sidebar.radio("Ïndice", secciones)

# Contenido basado en la sección seleccionada
if seccion_seleccionada == "La Facultad en Perspectiva: Un Retrato Completo":
    st.header("MATCOM")
    # galeria de fotos
    imagen1,imagen2 = st.columns(2)
    imagen3,imagen4 = st.columns(2)

    with imagen1:
        st.image('./Imagenes/matcom1.jpg')
        st.markdown("""
        <div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'>
            <p style='color: black;'>
                El edificio Felipe Poey donde se encuentra la facultad sirvió en el pasado como facultad de Ciencias Exactas y Naturales.
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    with imagen2:
        st.image('./Imagenes/matcom2.jpg')
        st.markdown("""
        <div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'>
            <p style='color: black;'>
                En este centro también funcionó por algunos años la Carrera de Geografía.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        
    with imagen3:
        st.image('./Imagenes/matcom4.jpg')
        st.markdown("""
        <div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'>
            <p style='color: black;'>
                En nuestro programa de pregrado impartimos las carreras de Licenciatura en Matemática, Licenciatura en Ciencia de la Computación y Licenciatura en Ciencia de Datos.
            </p>
        </div>
        """, unsafe_allow_html=True)
        
    with imagen4:
        st.image('./Imagenes/matcom5.jpg')
        st.markdown("""
        <div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'>
            <p style='color: black;'>
                La facultad acoge a dos museos con temáticas muy diferentes a los perfiles profesionales que se imparten en el centro. Constituyen muestras de su pasado como Facultad de Ciencias Naturales.
        </div>
        """, unsafe_allow_html=True)
        
        
    st.divider()

    st.write("La Facultad de Matemática y Computación se encuentra ubicada en el Edificio Felipe Poey y Aloy en la Colina Universitaria. En 1939 culminan las obras de construcción del nuevo edificio que albergaría a la Escuela de Ciencias que comprendía las secciones de Ciencias Físico-Matemáticas, Ciencias Físico-Químicas y Ciencias Naturales. Bello edificio patrimonial que alberga dos carreras, así como dos museos, un observatorio astronómico y otras instancias universitarias como son el Archivo Central y el CEPES. Además de contar con un sitial histórico donde se encuentran los restos de Felipe Poey y Aloy. En la actualidad en el centro se estudian dos carreras de excelencia : Matemática y Ciencia de la Computación.")
    st.image('./Imagenes/uh.jpg', caption="Colina Universitaria", use_column_width=True)
    m = folium.Map(location=[23.134302777778,-82.382033333333], zoom_start = 16)
    folium.Marker(
        [23.134302777778,-82.382033333333],
        popup ="Facultad de Matemática y Computación",
        tootlip ="Facultad de Matemática y Computació",
        icon=folium.Icon(icon="info-sign")
    ) .add_to(m)
    st_data = st_folium(m,width =725)


elif seccion_seleccionada == "Radiografía de la Facultad: Un Análisis del Cuerpo Docente":
    st.header("Un Análisis del Cuerpo Docente")
    st.write("En el corazón de cada escuela late un ritmo singular, marcado por la energía y la pasión de sus profesores.  Cada uno, un maestro con su propio legado, su experiencia y su visión, conforman un mosaico complejo y fascinante.  En esta sección, nos adentraremos en el análisis de la facultad, explorando la distribución de los profesores, los cargos que desempeñan y su preparación, para comprender cómo este tejido humano da forma al alma de la institución")
    
    st.divider()

    # Subtemas para la sección de Radiografía de la Facultad
    subtemas_datos = ["Distribución de Profesores", "Análisis de Cargos", "Proporción Docentes/No Docentes"]
    subtema_seleccionado = st.sidebar.radio("Análisis del cuerpo docente", subtemas_datos)
    
    if subtema_seleccionado == "Distribución de Profesores":
        st.header("¿Cuál es la distribución de profesores por departamento?")
        st.write("La distribución de profesores por departamentos en la Facultad de Matemática es un aspecto crucial para entender la estructura y funcionamiento de la institución.")
        st.write('La facultad cuenta con los siguientes departamentos:')
        st.write('• Matemática  • Matemática Aplicada  • Computación I  • Computación II')
        st.write('Además, cuenta con:')
        st.write('• Secretaría • Laboratorio de Computación • Instituto de Criptografía')
        st.write('La representación de los profesores de matemática es mayor respecto a los de computación. La minoría la componen los demás trabajadores de secretaría y laboratorio.'
                  'Sin embargo, hay un gran porcentaje de trabajadores de la facultad que no tienen una asignación específica de departamento.')

        newDf = data.groupby("Departamento")["Nombre y Apellidos"].count().reset_index()
        newDf.columns = ["Departamento", "Cantidad de Personas"]
        # Definir una escala de azules para los colores
        color_scale = px.colors.sequential.Blues_r
        # Un gráfico de pastel para ver la cantidad de personas por departamentos
        fig = px.pie(newDf, names='Departamento', values='Cantidad de Personas', title='Distribución por Departamento', color_discrete_sequence=color_scale)
        st.plotly_chart(fig)  

    elif subtema_seleccionado == "Análisis de Cargos":
        st.header("¿Cuál es la distribución de cargos en la facultad?")
        st.write('Para entender mejor la estructura y composición del claustro de profesores, es necesario analizar los diferentes cargos que desempeñan.'
        'La mayor cantidad de profesores se encuentra en las categorías de Instructor y Profesor Titular. Estos dos grupos, por lo general, abarcan la mayor parte de las actividades de enseñanza e investigación de la facultad.'
        'A continuación, se presenta una visualización que muestra la cantidad de personas que ocupan los diferentes cargos en la facultad. Esta información nos permite visualizar la estructura de los cargos, así como su distribución.')
        newDf1 = data.groupby("Cargo")["Nombre y Apellidos"].count().reset_index()
        newDf1.columns = ["Cargo", "Cantidad de Profesores"]

        #Un gráfico de barras para la cantidad de personas dependiendo del cargo
        fig1 = px.bar(newDf1, x='Cantidad de Profesores', y='Cargo', title='Cantidad de Profesores por Cargo')

        st.plotly_chart(fig1)
        
    elif subtema_seleccionado == "Proporción Docentes/No Docentes":
        st.header("¿Cuál es la proporción de docentes frente a no docentes?")
        st.write("Los docentes, con su rol central en la enseñanza y la investigación, y los no docentes, con su apoyo crucial en la gestión y el funcionamiento diario, son componentes esenciales del funcionamiento de la institución."
        "Los trabajadores docentes representan aproximadamente un 81%, mientras que los no docentes representan un pequeño porcentaje, aproximadamente un 16%.")
        newDf2 = data.groupby("Clasif. Por escala")["Nombre y Apellidos"].count().reset_index()
        newDf2.columns = ["Escala", "Cantidad de Personas"]
        color_scale = px.colors.sequential.Blues_r
        #Un gráfico de pastel para ver la cantidad de dependiendo de su grado
        fig2 = px.pie(newDf2, names='Escala', values='Cantidad de Personas', title='Proprción Docentes/No Docentes',color_discrete_sequence=color_scale)

        st.plotly_chart(fig2)
    

elif seccion_seleccionada == "Entre Cátedras y Despachos: Mapeando la Estructura de la Facultad":
    st.header("Mapeando la Estructura de la Facultad")
    st.write("En la escuela, como en cualquier reino, hay un orden. Los maestros, nuestros héroes, no están distribuidos al azar. Cada uno tiene su lugar, su cargo, su responsabilidad. Algunos, con experiencia acumulada, guían con sabiduría; otros, con energía juvenil, encienden la pasión por aprender. Cada uno, una pieza clave en el engranaje de la educación,  formado para forjar las mentes del futuro.  Y en este viaje, vamos a explorar cómo se entrelazan estas piezas para construir un sistema educativo vibrante y dinámico.  ")
    st.image('./Imagenes/composicion.jpg')

    st.markdown("## Distribución general de los profesores por departamento")
    # Leer los datos desde el archivo CSV
    df = pd.read_csv('nodos.csv')

    # Crear listas para nodos y aristas
    nodes = []
    edges = []

    # Agregar el nodo central (Decano)
    nodes.append(Node(id="Decano", label="Decano", size=30))

    # Crear un diccionario para almacenar los departamentos
    departments = {}

    # Agregar nodos de departamentos y miembros
    for index, row in df.iterrows():
        department = row['Departamento']
        member_id = f"{row['Nombre']}-{row['Apellidos']}"
    
        # Si el departamento no existe, crearlo y conectarlo al Decano
        if department not in departments:
            department_id = f"Dept_{department}"
            departments[department] = department_id
            nodes.append(Node(id=department_id, label=department, size=25))
            edges.append(Edge(source="Decano", target=department_id))
    
        # Agregar el nodo del miembro y conectarlo al departamento
        nodes.append(Node(id=member_id, label=f"{row['Nombre']} {row['Apellidos']}", size=20))
        edges.append(Edge(source=departments[department], target=member_id))

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

    st.divider()

    # Subtemas para la sección de Datos
    subtemas_datos = ["Departamento de Matemática", "Departamento de Matemática Aplicada", "Departamento de Computación 1", "Departamento de Computación 2"]
    subtema_seleccionado = st.sidebar.radio("Subtemas de Datos", subtemas_datos)
    
    if subtema_seleccionado == "Departamento de Matemática":
        st.header("Análisis del departamento de Matemática")
        st.write("El Departamento de Matemática se dedica a la docencia y la investigación en temas de Matemática Fundamental y Aplicada. Los principales temas de investigación están relacionados a áreas como: Álgebra, Ecuaciones Diferenciales y Aplicaciones, Mecánica de Sólidos, Métodos de Aproximación de Funciones, Escalamiento Multidimensional, Historia y Metodología de la Matemática, y Enseñanza de la Matemática. El departamento está encargado de impartir la docencia de 6 disciplinas de la carrera de Licenciatura en Matemática; estas son Análisis Matemático, Álgebra, Geometría y Topología, Ecuaciones Diferenciales, Medida e Integración y Análisis Funcional, e Historia y Metodología de la Matemática. De igual manera se imparten dos asignaturas de la disciplina Práctica Profesional del Matemático. Además, el departamento atiende la docencia de la disciplina Matemática Básica de la carrera Licenciatura en Ciencia de la Computación, también de nuestra facultad, y presta el servicio de docencia en la disciplina de Matemática Básica de otras diez carreras de la UH. Son impartidas por profesores de nuestro departamento un total de 34 asignaturas en 12 carreras.")
        st.divider()

        st.markdown("### 1. ¿Cuál es la edad promedio de los profesores?")
        st.write("La edad de los docentes puede influir en diversos factores, como la experiencia, la innovación en métodos de enseñanza y la capacidad de adaptación a nuevas tecnologías y enfoques pedagógicos."
        'En este departamento, existe una mezcla de edades, con un grupo considerable de profesores con edades entre 20 y 30 años, lo que indica una presencia significativa de profesionales jóvenes. Sin embargo, también se observa una cantidad similar de personas en el rango de 70 a 80 años, representando la edad más avanzada, y la edad promedio se ubica entre 40 y 50 años.' )

        data_filtred=data[data['Departamento']=='Matematica']
        ages=[] #para guardar todas las edades de los profes
        for i in data_filtred['CI']:
            if pd.notna(i): 
                var = str(i)
                year = var[:2]
            
                if int(year)<=24:
                    n=2000+int(year)
                    ages.append(2024-n)
                else:
                    n=1900+int(year)
                    ages.append(2024-n)
        age_counter = Counter()
        for i in ages:
            for start, end in ranges:
                if start <= i <= end:
                    age_counter[(start, end)] += 1
                    break

        frequency = [age_counter[i] for i in ranges]
        
        fig3 = go.Figure()
        fig3.add_trace(go.Bar(
            x=[f'{start}-{end}' for start, end in ranges],
            y=frequency,
            name='Edades',
            marker_color='skyblue'
        ))

        average = pd.Series(ages).mean()

        for start, end in ranges:
            if start <= average <= end:
                average_range = (start, end)
                break

        fig3.add_shape(
            type="line",
            x0=f'{average_range[0]}-{average_range[1]}',
            y0=0,
            x1=f'{average_range[0]}-{average_range[1]}',
            y1=max(frequency),
            line=dict(color='red', dash='dash'),
            name=f'Promedio: {average:.2f}'
        )

        fig3.update_layout(
            title='Frecuencia y promedio de las edades de los profesores',
            xaxis_title='Rango de Edad',
            yaxis_title='Frecuencia',
            legend_title='Leyenda'
        )

        st.plotly_chart(fig3)

        st.markdown("### 2.¿Cuál es la distribución de género entre los profesores?")
        st.write('Un análisis que se centra en la distribución de género dentro de la facultad nos ayuda a identificar posibles disparidades. Los resultados muestran que la mayoría de los profesores son hombres, aunque no existe una gran diferencia en cuanto a la cantidad de mujeres.' )
        
        cant_gender1 = data_filtred['Sexo'].value_counts()

        cant_man1 = cant_gender1.get('M', 0)
        cant_woman1 = cant_gender1.get('F', 0)

        df_gender = pd.DataFrame({
            'Sexo': ['Masculino', 'Femenino'],
            'Cantidad': [cant_man1, cant_woman1]
        })

        fig8 = px.bar(df_gender, x='Sexo', y='Cantidad', color='Sexo', title='Cantidad de Hombres y Mujeres')
        st.plotly_chart(fig8)

        st.markdown("### 3.¿Cuántos años de servicio tienen en promedio los profesores?")
        st.write("La experiencia de los profesores juega un papel crucial en la calidad de la educación impartida."
        'El siguiente gráfico de barras muestra una comparación del promedio de años de experiencia de los profesores de cada departamento.'
        'El departamento de Matemática, en comparación con los años de experiencia de los demás departamentos, se coloca como penúltimo, con una pequeña diferencia respecto al último.')
       
        # Calcular los promedios de los años de servicio
        promedios = data.groupby('Departamento')['Annos de servicio'].mean()
        colors = ['blue' if Departamento == 'Matematica' else 'gray' for Departamento in promedios.index]
        fig = go.Figure(data = [go.Bar(x=promedios.index,y=promedios,marker_color=colors)])
        fig.update_layout(
            title = 'Comparación de los promedios de años de servicio por departamento',
            xaxis_title = 'Departamento',
            yaxis_title = 'Años de servicio',
            bargap = 0.1
        )
        st.plotly_chart(fig)   

        
    elif subtema_seleccionado == "Departamento de Matemática Aplicada":
        st.header("Análisis del departamento de matemática aplicada")
        st.write("El Departamento de Matemática Aplicada cuenta con un claustro de 19 profesores, de ellos 12 con categoría docente superior (10 PT, 2 PA) y 12 doctores en Ciencias Matemáticas y Maestros en Ciencias, que desarrollan actividades docentes y de investigación científica. Se imparte docencia de Pregrado y Posgrado en temas de, Estadística y Probabilidades, Matemática Numérica, Optimización; organizada con nombres análogos en tres menciones para la Maestría en Ciencias Matemáticas, en tres disciplinas para la carrera de Licenciatura en Matemática y en la disciplina Matemática Aplicada para la carrera Ciencia de la Computación. También se imparten cursos de Estadística para las carreras de Geografía y Sociología y se coordina la disciplina Práctica Profesional para la carrera de Licenciatura en Matemática. En el Departamento existen cuatro Grupos de Investigación (GI) con más de 30 años de experiencia: GI de Probabilidades y Estadística, GI de Optimización, GI de Análisis Numérico y de Imágenes y el GI de Modelación Biomatemática; a los cuales se vinculan anualmente un número considerable de estudiantes de Pregrado y Posgrado. Líneas de investigación con resultados relevantes son el Análisis de datos en aplicaciones Médicas y Climáticas, la Optimización de procesos logísticos, el desarrollo de modelos en la Biomatemática, el Procesamiento de Imágenes, la Modelación y desarrollo de algoritmos numéricos para problemas en múltiples escalas, algoritmos de aproximación con funciones wavelets. El claustro participa en tres proyectos de investigación del Programa Nacional de Ciencias Básicas y a varios proyectos internacionales y territoriales.")
        st.divider()

        st.markdown("### 1. ¿Cuál es la edad promedio de los profesores?")
        st.write(" La edad de los docentes puede influir en diversos factores, como la experiencia, la innovación en métodos de enseñanza, y la capacidad de adaptación a nuevas tecnologías y enfoques pedagógicos."
        'En el departamento de Matemática Aplicada, la edad habitual de los docentes es de 60 a 70 años, una edad relativamente avanzada. Sin embargo, la edad promedio es de 50 a 60 años')

        data_filtred1=data[data['Departamento']=='Matematica Aplicada']
        ages1=[] 
        for i in data_filtred1['CI']:
            if pd.notna(i): 
                var1 = str(i)
                year1 = var1[:2]
            
                if int(year1)<=24:
                    n=2000+int(year1)
                    ages1.append(2024-n)
                else:
                    n=1900+int(year1)
                    ages1.append(2024-n)
        age_counter1 = Counter()
        for i in ages1:
            for start, end in ranges:
                if start <= i <= end:
                    age_counter1[(start, end)] += 1
                    break

        frequency1 = [age_counter1[i] for i in ranges]
        
        fig4 = go.Figure()
        fig4.add_trace(go.Bar(
            x=[f'{start}-{end}' for start, end in ranges],
            y=frequency1,
            name='Edades',
            marker_color='skyblue'
        ))

        average1 = pd.Series(ages1).mean()

        for start, end in ranges:
            if start <= average1 <= end:
                average_range = (start, end)
                break

        fig4.add_shape(
            type="line",
            x0=f'{average_range[0]}-{average_range[1]}',
            y0=0,
            x1=f'{average_range[0]}-{average_range[1]}',
            y1=max(frequency1),
            line=dict(color='red', dash='dash'),
            name=f'Promedio: {average1:.2f}'
        )

        fig4.update_layout(
            title='Frecuencia y promedio de las edades de los profesores',
            xaxis_title='Rango de Edad',
            yaxis_title='Frecuencia',
            legend_title='Leyenda'
        )

        st.plotly_chart(fig4)


        st.markdown("### 2.¿Cuál es la distribución de género entre los profesores?")
        st.write("Un análisis que se centra en la distribución de género dentro de la facultad nos ayuda a identificar posibles disparidades. Los resultados de este análisis en este departamento demostraron que la mayoría son mujeres, con una pequeña diferencia respecto a los hombres.")
        
        cant_gender=[]#Aqui se almacena la cantidad de cada genero
        cant_woman=0
        cant_man=0
        for i in data_filtred1['Sexo']: 
            if i=='F': 
                cant_woman+=1
            if i=='M':
                cant_man+=1
        cant_gender.append(cant_man)
        cant_gender.append(cant_woman)

        df = pd.DataFrame({
            'Género': ['Hombres', 'Mujeres'],
            'Cantidad': cant_gender
        })

        fig7 = px.bar(df, x='Género', y='Cantidad', color='Género', title='Cantidad de Hombres y Mujeres')

        st.plotly_chart(fig7)

        st.markdown("### 3.¿Cuántos años de servicio tienen en promedio los profesores?")
        st.write("La experiencia de los profesores juega un papel crucial en la calidad de la educación impartida."
        'El siguiente gráfico de barras muestra una comparación del promedio de años de experiencia de los profesores de cada departamento.'
        'El departamento de Matemática Aplicada se ubica como el departamento con más años de experiencia en comparación con los demás.')
    
        # Calcular los promedios de los años de servicio
        promedios = data.groupby('Departamento')['Annos de servicio'].mean()
        colors = ['blue' if Departamento == 'Matematica Aplicada' else 'gray' for Departamento in promedios.index]
        fig = go.Figure(data = [go.Bar(x=promedios.index,y=promedios,marker_color=colors)])
        fig.update_layout(
            title = 'Comparación de los promedios de años de servicio por departamento',
            xaxis_title = 'Departamento',
            yaxis_title = 'Años de servicio',
            bargap = 0.1
        )
        st.plotly_chart(fig)    

    elif subtema_seleccionado == "Departamento de Computación 1":
        st.header("Análisis del departamento de computación1")
        st.write("El Departamento de Programación agrupa las disciplinas de Programación e Ingeniería de Software, Sistemas de Bases de Datos y Práctica Profesional. Estas disciplinas están constituidas por asignaturas fundamentales en el perfil de un graduado de Ciencia de la Computación y sirven de base para otras disciplinas de esta especialidad. Tal es el caso de la asignatura de Programación que introduce conceptos y técnicas de algoritmos y programación orientada a objetos, que luego se desarrollan por otras asignaturas.  Por su parte la asignatura Ingeniería de Software introduce a los estudiantes en las técnicas de la planificación, organización y ejecución del proceso de desarrollo de software. ")
        st.divider()

        st.markdown("### 1. ¿Cuál es la edad promedio de los profesores?")
        st.write(" La edad de los docentes puede influir en diversos factores, como la experiencia, la innovación en métodos de enseñanza, y la capacidad de adaptación a nuevas tecnologías y enfoques pedagógicos."
        'Gran parte del claustro de este departamento tiene una edad de 20 a 30 años, y la misma proporción se observa en el rango de 30 a 40 años, siendo este último el rango de la edad promedio. ')

        data_filtred2=data[data['Departamento']=='Computacion I']
        ages2=[] 
        for i in data_filtred2['CI']:
            if pd.notna(i): 
                var2 = str(i)
                year2 = var2[:2]
            
                if int(year2)<=24:
                    n=2000+int(year2)
                    ages2.append(2024-n)
                else:
                    n=1900+int(year2)
                    ages2.append(2024-n)
        age_counter2 = Counter()
        for i in ages2:
            for start, end in ranges:
                if start <= i <= end:
                    age_counter2[(start, end)] += 1
                    break

        frequency2 = [age_counter2[i] for i in ranges]
        
        fig5 = go.Figure()
        fig5.add_trace(go.Bar(
            x=[f'{start}-{end}' for start, end in ranges],
            y=frequency2,
            name='Edades',
            marker_color='skyblue'
        ))

        average2 = pd.Series(ages2).mean()

        for start, end in ranges:
            if start <= average2 <= end:
                average_range = (start, end)
                break

        fig5.add_shape(
            type="line",
            x0=f'{average_range[0]}-{average_range[1]}',
            y0=0,
            x1=f'{average_range[0]}-{average_range[1]}',
            y1=max(frequency2),
            line=dict(color='red', dash='dash'),
            name=f'Promedio: {average2:.2f}'
        )

        fig5.update_layout(
            title='Frecuencia y promedio de las edades de los profesores',
            xaxis_title='Rango de Edad',
            yaxis_title='Frecuencia',
            legend_title='Leyenda'
        )

        st.plotly_chart(fig5)

        st.markdown("### 2.¿Cuál es la distribución de género entre los profesores?")
        st.write("Un análisis que se centra en la distribución de género dentro de la facultad nos ayuda a identificar posibles disparidades. Los resultados muestran que en este departamento hay la misma cantidad de hombres que de mujeres. ")
        
        cant_gender2=[]#Aqui se almacena la cantidad de cada genero
        cant_woman2=0
        cant_man2=0
        for i in data_filtred2['Sexo']: 
            if i=='F': 
                cant_woman2+=1
            if i=='M':
                cant_man2+=1
        cant_gender2.append(cant_man2)
        cant_gender2.append(cant_woman2)

        df2= pd.DataFrame({
            'Género': ['Hombres', 'Mujeres'],
            'Cantidad': cant_gender2
        })

        fig9 = px.bar(df2, x='Género', y='Cantidad', color='Género', title='Cantidad de Hombres y Mujeres')

        st.plotly_chart(fig9)

        st.markdown("### 3.¿Cuántos años de servicio tienen en promedio los profesores?")
        st.write("La experiencia de los profesores juega un papel crucial en la calidad de la educación impartida."
        'El siguiente gráfico de barras muestra una comparación del promedio de años de experiencia de los profesores de cada departamento.'
        'El departamento de Computación I se ubica en último lugar en cuanto a experiencia promedio de sus profesores, en comparación con los demás departamentos.')
        

        # Calcular los promedios de los años de servicio
        promedios = data.groupby('Departamento')['Annos de servicio'].mean()
        colors = ['blue' if Departamento == 'Computacion I' else 'gray' for Departamento in promedios.index]
        fig = go.Figure(data = [go.Bar(x=promedios.index,y=promedios,marker_color=colors)])
        fig.update_layout(
            title = 'Comparación de los promedios de años de servicio por departamento',
            xaxis_title = 'Departamento',
            yaxis_title = 'Años de servicio',
            bargap = 0.1
        )
        st.plotly_chart(fig)     

        
    elif subtema_seleccionado == "Departamento de Computación 2":
        st.header("Análisis del departamento de computación 2")
        st.write("El Departamento de Computación II se encarga de las Disciplinas de Sistemas Computacionales e Inteligencia Artificial. El grupo de investigación de Inteligencia Artificial es uno de los grupos más jóvenes de la facultad y que ha tenido resultados relevantes en los últimos años. Al mismo pueden vincularse estudiantes desde el primer año de sus carreras que tengan interés en las ramas como: Aprendizaje de Máquina, Ciencia de Datos, Robótica, Procesamiento de Lenguajes, entre otras. Se encarga adicionalmente de los eventos de programación competitiva, para los cuáles se preparan un conjunto de estudiantes liderados por el profesor Alfredo Somoza que han alcanzado los mejores resultados del país en los últimos años. ")
        st.divider()

        st.markdown("### 1. ¿Cuál es la edad promedio de los profesores?")
        st.write(" La edad de los docentes puede influir en diversos factores, como la experiencia, la innovación en métodos de enseñanza, y la capacidad de adaptación a nuevas tecnologías y enfoques pedagógicos."
        'En el departamento de Computación II, la mayoría de los profesores se encuentran en el rango de 70 a 80 años, una edad bastante avanzada. Su edad promedio se ubica entre 60 y 70 años, no muy distante de la mayoría. En este departamento, no se encuentran profesores muy jóvenes, ya que no hay representantes en el rango de 20 a 30 años, lo que podría indicar una posible falta de innovación proveniente de la juventud.')

        data_filtred3=data[data['Departamento']=='Computacion II']
        ages3=[] 
        for i in data_filtred3['CI']:
            if pd.notna(i): 
                var3 = str(i)
                year3 = var3[:2]
            
                if int(year3)<=24:
                    n=2000+int(year3)
                    ages3.append(2024-n)
                else:
                    n=1900+int(year3)
                    ages3.append(2024-n)
        age_counter3 = Counter()
        for i in ages3:
            for start, end in ranges:
                if start <= i <= end:
                    age_counter3[(start, end)] += 1
                    break

        frequency3 = [age_counter3[i] for i in ranges]
        
        fig6 = go.Figure()
        fig6.add_trace(go.Bar(
            x=[f'{start}-{end}' for start, end in ranges],
            y=frequency3,
            name='Edades',
            marker_color='skyblue'
        ))

        average3 = pd.Series(ages3).mean()
        
        for start, end in ranges:
            if start <= average3 <= end:
                average_range = (start, end)
                break
        
        fig6.add_shape(
                type="line",
                x0=f'{average_range[0]}-{average_range[1]}',
                y0=0,
                x1=f'{average_range[0]}-{average_range[1]}',
                y1=max(frequency3),
                line=dict(color='red', dash='dash'),
                name=f'Promedio: {average3:.2f}'
            )

        fig6.update_layout(
            title='Frecuencia y promedio de las edades de los profesores',
            xaxis_title='Rango de Edad',
            yaxis_title='Frecuencia',
            legend_title='Leyenda'
        )

        st.plotly_chart(fig6)

        st.markdown("### 2.¿Cuál es la distribución de género entre los profesores?")
        st.write(" Un análisis que se centra en la distribución de género dentro de la facultad nos ayuda a identificar posibles disparidades. Los resultados muestran que en este departamento hay la misma cantidad de hombres que de mujeres.") 

        cant_gender3=[]#Aqui se almacena la cantidad de cada genero
        cant_woman3=0
        cant_man3=0
        for i in data_filtred3['Sexo']: 
            if i=='F': 
                cant_woman3+=1
            if i=='M':
                cant_man3+=1
        cant_gender3.append(cant_man3)
        cant_gender3.append(cant_woman3)

        df3 = pd.DataFrame({
            'Género': ['Hombres', 'Mujeres'],
            'Cantidad': cant_gender3
        })

        fig10 = px.bar(df3, x='Género', y='Cantidad', color='Género', title='Cantidad de Hombres y Mujeres')

        st.plotly_chart(fig10)   

        st.markdown("### 3.¿Cuántos años de servicio tienen en promedio los profesores?")
        st.write("La experiencia de los profesores juega un papel crucial en la calidad de la educación impartida."
        'El siguiente gráfico de barras muestra una comparación del promedio de años de experiencia de los profesores de cada departamento.'
        'En el caso del departamento de Computación II, es el segundo con más años de experiencia, pero solo lo separa una pequeña diferencia del primero.')
        
        # Calcular los promedios de los años de servicio
        promedios = data.groupby('Departamento')['Annos de servicio'].mean()
        colors = ['blue' if Departamento == 'Computacion II' else 'gray' for Departamento in promedios.index]
        fig = go.Figure(data = [go.Bar(x=promedios.index,y=promedios,marker_color=colors)])
        fig.update_layout( 
            title = 'Comparación de los promedios de años de servicio por departamento',
            xaxis_title = 'Departamento',
            yaxis_title = 'Años de servicio',
            bargap = 0.1
        )
        st.plotly_chart(fig)               

    
elif seccion_seleccionada == "Más que Docentes: Profundizando en el Perfil Investigador del Profesorado":
    st.header("Profundizando en el Perfil Investigador del Profesorado")
    st.write("La labor de los profesores en la facultad va más allá de la enseñanza convencional; se extiende hacia un compromiso profundo con la investigación y el desarrollo académico. En este análisis, nos centraremos en las actividades extraescolares de los docentes, su participación en proyectos de investigación y cómo sus contribuciones enriquecen tanto el entorno académico como la preparación de los estudiantes en programas de maestría. Al explorar el perfil investigador del profesorado, desvelaremos las dinámicas que sustentan la excelencia académica y el impacto significativo que tienen en la formación de futuros profesionales.")
    st.divider()

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

    config = Config(width=950,
                    height=950,
                    directed=True, 
                    physics=True, 
                    hierarchical=False)

    return_value = agraph(nodes=nodes, 
                          edges=edges, 
                          config=config)

    st.divider()
    st.header("Grupos de investigación")
    st.write("La investigación académica es un pilar fundamental en el desarrollo y avance del conocimiento. En esta facultad, los grupos de investigación desempeñan un papel crucial en la generación de nuevas ideas, la resolución de problemas complejos y la contribución al progreso científico y tecnológico.")
    st.write('Los grupos de investigación de la facultad son: ')
    st.write('.Probabilidades y Estadísticas .Sistemas de Información e Inteligencia de Negocios .Visualización y Gráficos por Computadora .Álgebra')
    st.write('Gran parte de los profesores pertenecen al grupo de Probabilidades y Estadísticas, y el grupo con menor participación es el de Álgebra.')
    
    group_counts = df['Grupo de investigación'].value_counts()

    # Crear el gráfico de barras con Plotly
    fig = go.Figure(data=[go.Bar(
        x=group_counts.index,
        y=group_counts.values,
        marker_color=px.colors.sequential.Blues_r
    )])

    fig.update_layout(
        title='Cantidad de Profesores por Grupo de Investigación',
        xaxis_title='Grupos de Investigación',
        yaxis_title='Cantidad de Profesores',
        bargap=0.1
    )

    st.plotly_chart(fig, use_container_width=True)
    
    st.divider()
    subtemas_datos = ["Grupo de Algebra", "Grupo de Vizualizacion y gráficos por computadora", "Grupo de Sistemas de Información e Inteligencia de Negocios", "Grupo de Probabilidades y Estadística"]
    subtema_seleccionado = st.radio("Grupos de investigación", subtemas_datos)
    
    if subtema_seleccionado == "Grupo de Algebra":
        st.markdown("### Grupo de Algebra")
        st.write("El grupo de investigación en álgebra se enfoca en la exploración profunda de la teoría de representaciones, un área fundamental que estudia las propiedades de la categoría de módulos. Esta rama del álgebra se centra en cómo los objetos algebraicos, como álgebras y grupos, pueden ser representados mediante matrices y transformaciones lineales. A través de seminarios, talleres y colaboraciones interdisciplinarias, nuestro grupo busca fomentar un ambiente dinámico donde se puedan compartir ideas y avances en la investigación. Estamos comprometidos con la formación de nuevos investigadores en el campo del álgebra y la promoción del conocimiento matemático en general.")
        st.markdown("""
        <div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'>
            <h4 style='color: black;'>Logros y Publicaciones del grupo</h4>
            <p style='color: black;'>
                    . 5 Trabajos de Diploma  <br>
                    . 4 Tesis de Maestría  <br>
                    . 5 ponencias en Compumat 2015, 3 ponencias en Compumat 2017, 1 ponencia en Compumat 2019 
            </p>
        </div>
        """, unsafe_allow_html=True)

    elif subtema_seleccionado == "Grupo de Vizualizacion y gráficos por computadora":
        st.markdown("### Grupo de Vizualizacion y gráficos por computadora")
        st.write("El grupo de investigación en Visualización y Gráficos por Computadora se dedica a la exploración y desarrollo de técnicas avanzadas para el renderizado en tiempo real, con un enfoque particular en fenómenos complejos como la iluminación global, el renderizado de volúmenes y los medios participativos. Una de nuestras principales áreas de investigación es el renderizado en tiempo real, que permite generar imágenes de alta calidad de manera instantánea. Esto es crucial en aplicaciones como videojuegos, simulaciones interactivas y realidad virtual. Nuestros profesores trabajan en optimizar algoritmos y técnicas que permiten lograr una representación visual impresionante sin sacrificar el rendimiento, lo que es fundamental para ofrecer experiencias inmersivas.")
        st.markdown("""
        <div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'>
            <h4 style='color: black;'>Logros y Publicaciones del grupo</h4>
            <p style='color: black;'>
                    . E-Buffer: Una Representación en Espacio de Vista para Aplicaciones de Iluminación Global en Tiempo Real. Alejandro Piad, Ludwig Leonard. 2014. Ciencias Matemáticas <br> 
                    . A-PIT: Estructura de Subdivisión Espacial Aceleración de Raytracing en GPU. Jean L’Clerc, Alejandro Piad, Ludwig Leonard. 2016. Ciencias Informáticas.  <br>
                    . GSL – Un Lenguaje de Dominio Específico para la definición de Gráficos. Ernesto Izquierdo, Ludwig Leonard. 2013. CIbSE. Uruguay.  
            </p>
        </div>
        """, unsafe_allow_html=True)
        

    elif subtema_seleccionado == "Grupo de Sistemas de Información e Inteligencia de Negocios":
        st.markdown("### Grupo de Sistemas de Información e Inteligencia de Negocios")
        st.write("La esencia del grupo de Sistemas de Información e Inteligencia de Negocios (ISBIG – Information Systems and Business Intelligence) es la labor de investigación e innovación en diversas áreas del conocimiento científico y la aplicación práctica, que se caracterizan por su interrelación estrecha con el almacenamiento, el análisis y la obtención de información desde el procesamiento de los datos primarios hasta la generación de conocimiento con vista a la toma de decisiones pertinentes, certeras y oportunas. Se trabaja en la profundización teórico-conceptual y metodológica en relación con el espectro de los enfoques contemporáneos de las bases de datos, que favorecen la actualización incesante de la disciplina Sistemas de Información, impulsan el trabajo científico-estudiantil y asegura el reto en las actividades de posgrado. Dada la diversidad de escenarios y el creciente desvanecimiento de los límites entre las más disímiles ramas de la ciencia y la tecnología, se enfatiza en la interrelación de paradigmas como contribución al manejo de datos heterogéneos e información espacial, el fomento de la calidad de los datos y el control de los proyectos con vistas a propiciar el éxito de la gestión del conocimiento organizacional. Para el desarrollo de soluciones computacionales a problemas complejos se incursiona en la integración de resultados desde la perspectiva de los datos en ramas afines como Sistemas de Bases de Datos, Inteligencia y Analítica de Negocios, Recuperación de Información, Optimización de Consultas, Minería de Datos, Big Data, Detección de Anomalías, Aprendizaje Automático, Procesamiento del Lenguaje Natural.")
        st.markdown("""
        <div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'>
            <h4 style='color: black;'>Logros y Publicaciones del grupo</h4>
            <p style='color: black;'>
                    . Fernández Montoto, C; Inguanzo Rey, H. J. Utilización de los mundos virtuales en el proceso de enseñanza aprendizaje. Congreso Internacional UNIVERSIDAD 2020. La Habana, Cuba. Febrero de 2020. <br>
                    . Montes de Oca Richardson, M. Estrategias para la capacitación del personal involucrado en proyectos de desarrollo municipal. Evento Provincial de UNIVERSIDAD 2020. La Habana, Cuba. julio de 2020. <br>
                    . Quintana-Wong, C.; García Hernández, L. Recommender System in a Transactional Analytical Solution for Health Care and Health Promotion. Revista Cubana de Transformación Digital. Vol. 1 Núm. 1 (2020) https://rctd.uic.cu/rctd/artcle/view/58 <br>
                    . Quintana-Wong, C. A Deep Learning Model for Semantic Relation Classification in Spanish based on Distant Supervision (International Conference on Operations Research ICOR 2020) <br>
                    . Prado-Romero, M.A., Fernández Oliva, A., García Hernández, L., Cardentey-Fundora, V.M. Predicting Topic Popularity using Neural Networks and a Time Sensitive Topic Model. (International Conference on Operations Research ICOR 2020) <br>
                    . Prado-Romero, M.A., Celi, A., Stilo, G., Coto-Santiesteban, A. TSTM a Time Sensitive Topics´ Model for Popularity Prediction on News Providers, Ibero-American Congress on Pattern Recognition (CIARP) 2019, Springer, Cham, 2019. https://doi.org/10.1007/978-3-030-33904-3_9 <br>
                    . Prado-Romero, M.A., Fernández Oliva, A., García Hernández, L. Discovering Influencers on Social Networks (International Workshop on Operations Research IWOR 2019) <br>
                    . Quintana-Wong, C. Integrating Latent Factor and Neighborhood Models to obtain Accurate Recommendations (International Workshop on Operations Research IWOR 2019) <br> 
                    . Quintana-Wong, C. Combining Collaborative Filtering and Topic Modeling for Information Recommendation. (Escuela Latinoamericana de Verano de Investigación de Operaciones ELAVIO 2019 – Lleida, España) <br>
                    . Quintana-Wong, C. Recommendations for Healthcare using document-oriented NoSQL. (COMPUMAT 2019). ISBN: 978-959-16-4341-4 <br>
                    . Fernández Montoto, C. La enseñanza de las Matemáticas mediante mundos virtuales. Compumat 2019. ISBN: 978-959-16-4341-4 <br>
                    . Montes de Oca Richardson, M. Estrategias para el control de proyectos de desarrollo municipal sustentadas en la gestión del conocimiento. Memorias del III Congreso Internacional de Marketing desarrollo local y turismo 2019. La Habana, Cuba. 2019 <br>
                    . Montes de Oca Richardson, M. La DIP aplicada a los programas de la vivienda en el marco del desarrollo local. III Congreso Internacional de Marketing desarrollo local y turismo 2019. La Habana, Cuba. 2019 <br>
                    . Montes de Oca Richardson, M. El desarrollo local en el Consejo de la Administración en la Dirección Integrada por proyecto. III Congreso Internacional de Marketing desarrollo local y turismo 2019. La Habana, Cuba. 2019 <br>
                    . Montes de Oca Richardson, M. SCCPM Sistema Computacional para el control de los proyectos de desarrollo municipal. Evento Provincial de Economía de la ANEC. La Habana, Cuba. <br>
                    . Montes de Oca Richardson, M. Estrategias para el desarrollo municipal enmarcadas en la transformación digital. Evento Provincial de Economía de la ANEC. La Habana, Cuba. <br>
                    . Prado-Romero, M. A.; Fernández Oliva, A.; García Hernández, L. Identifying Twitter Users Influence and Open Mindedness Using Anomaly Detection. International Workshop on Artificial Intelligence and Pattern Recognition. Springer, Cham, 2018. https://doi.org/10.1007/978-3-030-01132-1_19 <br>
                    . García Hernández, L.; Quintana Wong, C. (ponente); Guillot Jiménez, J.; Fleitas Aparicio, C. (2017) Solución computacional transaccional y analítica para la promoción de la salud. Proyecto del Grupo Multicéntrico de Investigaciones en Salud GMIS-Sanología de la Unión de Universidades de América Latina (UDUAL). COMPUMAT 2017. Ciudad Universitaria “José Antonio Echevarría”, Cuba. Noviembre 2017. ISBN: 978-959-261-562-5. <br>
                    . Avellaneda González, R.; García Hernández, L. (ponente); Guillot Jiménez, J. (2017). Solución BI NoSQL para el análisis del ingreso a la Educación Superior. COMPUMAT 2017. Ciudad Universitaria “José Antonio Echevarría”, Cuba. Noviembre 2017. <br>
                    . López López, A.; García Hernández, L.; et al (2017). Proyecto de gestión de conocimiento en Desoft: Conjunto de herramientas para la gestión del conocimiento [1]. Revista Nueva Empresa, Cuba. Abril 2017. ISSN 1682 – 2455. <br>
                    . Simón A., Torres, M., García L., Simón A., Ravelo R. (2016) Comparing Tabular and Multidimensional Model in a real BI solution. IEEE Latin American Transactions. Vol. 14, No. 7, Julio 2016. IEEE (3393-3399). ISSN: 1548-0992. <br>
                    . Guillot Jiménez, J.; García Hernández, L. (2016) Bases de datos NoSQL para la gestión de datos geoespaciales. Memorias de la XVI Convención y Feria Internacional Informática 2016: Conectando Sociedades. Marzo 2016. Editorial Joven Club (959-289). ISBN: 978-959-289-122-7. <br>
                    . Reyes Gaspar, P. L. Estrategia para la promoción del autocuidado de la salud en la Universidad Surcolombiana. Tesis Doctoral en Ciencias de la Salud. (Ph. D.) Tutoras: Amable Ambrós, Z. (ENSP) y García Hernández, L. (UH) Proyecto del Grupo Multicéntrico de Investigaciones en Salud GMIS-Sanología de la Unión de Universidades de América Latina (UDUAL). Escuela Nacional de Salud Pública. La Habana, Cuba, Marzo de 2016. <br>
                    . Simón Cuevas, A.; Torres Sánchez, M.; García Hernández, L.; Ravelo Suárez, R. (2015) Evolución de la gestión del conocimiento en el Grupo Empresarial CIMEX. Revista Digital Gestión del Conocimiento y Tecnologías. España, Diciembre de 2015. ISSN: 2255-5648. <br>
            </p>
        </div>
        """, unsafe_allow_html=True)
        

    elif subtema_seleccionado == "Grupo de Probabilidades y Estadística":
        st.markdown("### Grupo de Probabilidades y Estadística")
        st.write("El grupo de investigación en Probabilidades, Estadística y Optimización se dedica a ejecutar proyectos que integran las tendencias actuales y aportan significativamente al área de estudio. Nuestro enfoque se centra en desarrollar nuevos algoritmos, métodos y modelos teóricos que mejoren los procesos existentes, especialmente en el contexto del análisis de información cuantitativa en medicina y otros campos. Una de nuestras principales metas es ejecutar proyectos de investigación vinculados al desarrollo de nuevos algoritmos y métodos. Esto incluye la creación de modelos teóricos en probabilidades y estadística que optimicen el procesamiento, distribución, análisis e interpretación de datos cuantitativos. Nuestro trabajo busca mejorar la eficacia de los softwares existentes, facilitando así la toma de decisiones informadas en diversas áreas, especialmente en la medicina. Nos enfocamos también en el perfeccionamiento y desarrollo de nuevas técnicas analíticas. Estas técnicas están diseñadas para fortalecer la capacidad del país en la realización de mediciones precisas y evaluaciones exhaustivas en un amplio espectro de aplicaciones. Esto incluye estudios sobre factores medioambientales y la gestión de sistemas urbanos, con especial atención a los problemas de transporte, donde la estadística y la optimización juegan un papel crucial. A través de estos esfuerzos, el grupo de investigación en Probabilidades, Estadística y Optimización busca no solo avanzar en el conocimiento científico, sino también contribuir al desarrollo social y económico del país mediante la aplicación efectiva de estos principios en múltiples áreas.")
        st.markdown("""
        <div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'>
            <h4 style='color: black;'>Logros y Publicaciones del grupo</h4>
            <p style='color: black;'>
                    2011-2013 <br>
                    . Modelos Matemáticos para el Estudio de Medio Ambiente, Salud y Desarrollo Humano. <br>
                    2014-2016 <br>
                    . Modelos, métodos y algoritmos para la toma de decisiones. <br>
                    Aplicaciones en la salud humana y el medio ambiente
                    2015-2016 <br>
                    . Proyecto adjunto al Convenio de Colaboración Académico-Cientifica entre la Universidade Federal de Minas Gerais y la Universidad de La Habana <br>
                    2018-2020 <br>
                    . A Cuban-Flemish Training and Research Program in Data Science and Big Data Analysis. Cuba-Bélgica <br>
                    2020-2021 <br>
                    . Proyecto LASSO de Modelación Matemática para la lucha contra el COVID <br>
                    . Métodos cuantitativos para estudios problemas médicos, medio-ambientales y de Bienestar Humano. pNCB, Cuba Participación en Redes <br>
                    2016-2019 <br>
                    . Red CYTED 516RT0513 “RED IBEROAMERICANA DE AGROBIGDATA Y «DECISION SUPPORT SYSTEMS» (DSS) PARA UN SECTOR AGROPECUARIO SOSTENIBLE”, Comunidad Europea <br>
                    2018-2020 <br>
                    . Red Iberoamericana de Investigación en Modelos de Optimización y Decisión y sus Aplicaciones. Comunidad Europea <br>
                    2017- <br>
                    . Red BIOMED (UH) <br>
                    2014- <br>
                    . Grupo de Aplicaciones en Salud Humana y Medio Ambiente (GRASHUMEDIA) <br>
                    2012- <br>
                    . Red Iberoamericana de Estudios Cuantitativos Aplicados (RIDECA) <br>
            </p>
        </div>
        """, unsafe_allow_html=True)
    

    st.divider()
    st.header("Profeores de Maestría")
    st.write("La calidad de un programa de maestría está profundamente influenciada por la experiencia y el conocimiento de sus profesores. En las maestrías en Ciencia de la Computación y Ciencias Matemáticas, los docentes desempeñan un papel crucial en la formación de los estudiantes, guiándolos a través de conceptos complejos y fomentando un ambiente de aprendizaje colaborativo.")
    st.markdown("#### Profesores por maestría")
    st.write("Los profesores de maestría son fundamentales para el éxito de los programas de posgrado de la facultad."
    'En la facultad se imparte la maestría en Ciencias de la Computación y en Ciencias Matemáticas. La cantidad de profesores en ambas maestrías es la misma, por lo que existe un equilibrio.') 
    # Contar la cantidad de profesores por grupo de investigación
    group_counts = df['Maestría'].value_counts()

    # Crear el gráfico de barras con Plotly
    fig = go.Figure(data=[go.Bar(
        x=group_counts.index,
        y=group_counts.values,
        marker_color=px.colors.sequential.Blues_r
    )])

    # Personalizar el gráfico
    fig.update_layout(
        title='Cantidad de profesores en grupos de maestrías',
        xaxis_title='Grupos de Maestrías',
        yaxis_title='Cantidad de Profesores',
        bargap=0.1
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
    
    st.divider()
    subtemas_datos = ["Maestría en Ciencias de la Computación", "Maestría en Ciencias Matemáticas"]
    subtema_seleccionado = st.radio("Maestrías", subtemas_datos)

    if subtema_seleccionado == "Maestría en Ciencias de la Computación":
        st.markdown("### Maestría en Ciencias de la Computación")
        st.markdown("#### Profesores que imparten Maestría")
        st.write("Dra. C. Lucina García Hernández ")
        st.write("Dr. C. Alberto Fernández Oliva")
        st.write("Dr. C. Yudivián Almeyda Cruz")
        st.write("Dr. C. Alejandro Mesejo Chiong")
        st.write("Dr. C. Ricardo Sánchez Casanova")
        st.write("Cs. Eduardo Quesada Orozco")
        st.write("Cs. Ludwig Leonard Méndez")
        st.markdown("""
        <div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'>
            <h4 style='color: black;'>Cursos de posgrado</h4>
            <p style='color: black;'>
                    Modelos analíticos y data warehousing <br>
                    Análisis de datos. Introducción al Big Data <br>
                    Análisis de redes <br>
                    Minería de textos <br>
                    Machine Learning <br> 
                    Introducción a la criptografía y blockchain <br>
                    Estrategias de impacto y visibilidad en los resultados de las investigaciones <br>
                    Sistemas de Bases de Datos en Arquitectura Cliente Servidor <br>
                    Multiparadigmas de Programación <br>
                    Gráficos por computadora <br>
                    Algoritmos Heurísticos y Metaheurísticos <br>
                    Sistemas de extracción de conocimiento <br>
                    Buenas Prácticas de Desarrollo de Software Ágil <br>
                    Metodología de la investigación <br>
                    Estructuras de Datos Avanzadas <br>
                    Inteligencia y Analítica de Negocios <br>
                    Simulación Basada en Principios Físicos <br>
            </p>
        </div>
        """, unsafe_allow_html=True)
    elif subtema_seleccionado == "Maestría en Ciencias Matemáticas":
        st.markdown("### Maestría en Ciencias Metemáticas")
        st.markdown("#### Profesores que imparten Maestría")
        st.write("Dr.C. Ángela Mireya León Mecías ")
        st.write("Dr.C. Rita Roldán Inguanzo")
        st.write("Dr.C. Fidel Hernández Advíncula")
        st.write("Dr.C. Mariano Rodríguez Ricard")
        st.write("Dr.C. Marta L. Baguer Díaz-Romañach")
        st.write("Dr.C. Gemayqzel Bouza Allende")
        st.write("Dr.C. Carlos Bouza Herrera")
        st.markdown("""
        <div style='background-color: #f0f0f0; padding: 10px; border-radius: 5px;'>
            <h4 style='color: black;'>Cursos de posgrado</h4>
            <p style='color: black;'>
                    Análisis Matemático <br>
                    Álgebra <br>
                    Ecuaciones Diferenciales <br>
                    Mecánica <br>
                    Enseñanza de la Matemática <br>
                    Matemática Numérica <br>
                    Optimización <br>
                    Probabilidades y Estadística  <br> 
            </p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    st.header("Profesores miembro del consejo científico")
    st.write("Órgano asesor del Consejo de Dirección para la concepción e instrumentación de la política científica en su sentido más general que incluye la actividad docente y metodológica de investigación de pregrado, de superación y la actividad académica en su conjunto. Entre sus actividades precuentes tenemos: Análisis de los proyectos nacionales e internacionales, otorgamiento de avales. Aprobación de temas de doctorados, constituye el Comité Académico del Programa de Doctorado en Ciencias Matemáticas. Análisis de premios de investigación     Anualmente Convocamos y otorgamos el Premio del Consejo Científico a trabajos de investigación de estudiantes relevantes presentados en la JCE")
    st.markdown("### 1.¿Cuántos profesores son miembros del consejo científico?")
    st.write("En nuestra facultad, contamos con un grupo destacado de profesores que forman parte del consejo científico. Ellos no solo se dedican a la enseñanza y la investigación, sino que también desempeñan un papel crucial en la toma de decisiones estratégicas."
    'El consejo científico está formado por un presidente, vicepresidente, secretario, miembro permanente y los demás miembros. ') 
    
    group_counts = df['Actividad en el Consejo Científico'].value_counts()

    # Crear el gráfico de barras con Plotly
    fig = go.Figure(data=[go.Bar(
        x=group_counts.index,
        y=group_counts.values,
        marker_color=px.colors.sequential.Blues_r
    )])

    # Personalizar el gráfico
    fig.update_layout(
        title='Distribución de las actividades en el consejo científico',
        xaxis_title='Actividades',
        yaxis_title='Cantidad de Profesores',
        bargap=0.1
    )

    # Mostrar el gráfico en Streamlit
    st.plotly_chart(fig, use_container_width=True)
    
# Sección seleccionada
if seccion_seleccionada == "Desentrañando la Matriz: Un Análisis Comparativo del Profesorado":
    st.header("Un Análisis Comparativo del Profesorado")
    st.write("Esta sección presenta las conclusiones del análisis.")
    st.divider()
    # Opciones abreviadas para las preguntas
    opciones = [
        "1. Antigüedad y Cargo",
        "2. Género y Cargo",
        "3. Edad y Participación en Investigación",
        "4. Distribución de Cargos por Departamento",
        "5. Comparación de Género en Programas de Maestría",
        "6. Dr y Años de Servicio"
    ]
    
    # Selección de opción en la barra lateral
    opcion_seleccionada = st.sidebar.selectbox("Selecciona una opción:", opciones)

    # Contenido basado en la opción seleccionada
    if opcion_seleccionada == "1. Antigüedad y Cargo":
        st.markdown("### ¿Cómo varía la antigüedad promedio de los profesores según su cargo?")
        st.write("En este análisis, se examina la antigüedad de los profesores que ocupan diversos cargos dentro de la facultad, tales como decano, profesor titular, profesor auxiliar, entre otros. La comparación de la antigüedad en estos roles nos permitirá entender mejor la distribución de la experiencia y el conocimiento acumulado."
        'También proporcionará una visión integral de cómo la experiencia se distribuye entre los diferentes niveles de responsabilidad.')
        
        # Calcular la antigüedad promedio por cargo
        antiguedad_promedio = data.groupby('Cargo')['Annos de servicio'].mean().reset_index(name='Antigüedad Promedio')

        # Crear el gráfico de barras
        fig = px.bar(antiguedad_promedio, 
                    x='Antigüedad Promedio', 
                    y='Cargo', 
                    title='Antigüedad Promedio de Profesores por Cargo',
                    color='Antigüedad Promedio',
                    color_continuous_scale=px.colors.sequential.Blues_r)

        # Personalizar el diseño del gráfico
        fig.update_traces(hoverinfo='x+y')
        fig.update_layout(margin=dict(t=50, l=0, r=0, b=0),
                        xaxis_title='Cargo',
                        yaxis_title='Antigüedad Promedio (años)',
                        yaxis=dict(tickmode='linear'),
                        height=900,  
                        width=1000) 
        

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig, use_container_width=True)
    
    elif opcion_seleccionada == "2. Género y Cargo":
        st.markdown("### ¿Existen diferencias en la distribución de género según el cargo en la facultad?")
        st.write("En este análisis, se investigará la representación de géneros en los diferentes niveles de cargo dentro de nuestra facultad. El objetivo es determinar si existe una distribución equitativa entre hombres y mujeres en roles como decano, profesor titular, profesor auxiliar, entre otros.")
        
        # Agrupar por cargo y sexo, y contar la cantidad de cada uno
        distribucion_genero = data.groupby(['Cargo', 'Sexo']).size().reset_index(name='Cantidad')
        # Crear el gráfico de pastel en forma de anillo
        fig = px.sunburst(distribucion_genero, 
                          path=['Cargo', 'Sexo'], 
                          values='Cantidad', 
                          title='Distribución de Género según Cargo',
                          color='Cantidad',
                          color_continuous_scale= px.colors.sequential.Blues_r)

        # Personalizar el diseño del gráfico
        fig.update_traces(hoverinfo='label+value+percent entry')
        fig.update_layout(margin=dict(t=50, l=0, r=0, b=0))

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig)

    elif opcion_seleccionada == "3. Edad y Participación en Investigación":
        st.markdown("### ¿Hay diferencias en la participación en grupos de investigación según la edad de los profesores?")
        st.write("Compara la participación en investigación entre diferentes categorías científicas.")

        # Filtrar los miembros del consejo científico
        miembros_consejo = data[data['Miembros del Consejo cientifico'] == 1]

        nombres_apellidos = miembros_consejo[['Nombre y Apellidos']] 
        st.write("### Miembros del Consejo Científico")
        st.write(nombres_apellidos)

    
    elif opcion_seleccionada == "4. Distribución de Cargos por Departamento":
        st.markdown("### ¿Cómo se distribuyen los diferentes cargos entre los departamentos?")
        st.write("Analiza si ciertos departamentos tienen más profesores en posiciones de liderazgo.")
    
        # Agrupar por departamento y cargo, y contar la cantidad de cada uno
        distribucion_cargos_departamento = data.groupby(['Departamento', 'Cargo']).size().reset_index(name='Cantidad')

            # Crear el gráfico de barras apiladas
        fig = px.bar(distribucion_cargos_departamento, 
                     x='Departamento', 
                     y='Cantidad', 
                     color='Cargo',
                     barmode='stack',
                     title='Distribución de Cargos por Departamento',
                     labels={'Departamento': 'Departamento', 'Cantidad': 'Cantidad de Profesores', 'Cargo': 'Cargo'})

        # Personalizar el diseño del gráfico
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            font_color='black',
            xaxis_tickangle=-45
        )

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig)


