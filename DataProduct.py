import streamlit as st
import pandas as pd 
import plotly.express as px
import plotly.graph_objects as go
from collections import Counter

with open('antiguedad-matematica.csv', 'r') as f:
    file=pd.read_csv(f)
data=pd.DataFrame(file)
ranges = [(20, 30), (30, 40), (40, 50), (50, 60), (60, 70), (70, 80)]
# Sección inicial
st.header("Análisis del claustro de profesores de MATCOM")
st.write("Aquí irá un texto de introducción")

st.divider()

# Opciones de la barra lateral
secciones = ["Radiografía de la Facultad: Un Análisis del Cuerpo Docente", "Entre Cátedras y Despachos: Mapeando la Estructura de la Facultad", "Más que Docentes: Profundizando en el Perfil Investigador del Profesorado", "Desentrañando la Matriz: Un Análisis Comparativo del Profesorado"]
seccion_seleccionada = st.sidebar.radio("Índice", secciones)

# Contenido basado en la sección seleccionada
if seccion_seleccionada == "Radiografía de la Facultad: Un Análisis del Cuerpo Docente":
    st.header("Un Análisis del Cuerpo Docente")
    st.write("Este parrafo explicara muy superficialmente lo que se analizará: se hablara de la distribución de los profesores, los cargos y su preparación como forma de introduccion a este tema...acordandonos de que es con la idea de una historia")
    
    st.divider()

    # Subtemas para la sección de Radiografía de la Facultad
    subtemas_datos = ["Distribución de Profesores", "Análisis de Cargos", "Proporción Docentes/No Docentes"]
    subtema_seleccionado = st.sidebar.radio("Subtemas de Datos", subtemas_datos)
    
    if subtema_seleccionado == "Distribución de Profesores":
        st.header("¿Cuál es la distribución de profesores por departamento?")
        st.write("Aquí se analiza la distribución de profesores por departamento.")
        newDf = data.groupby("Departamento")["Nombre y Apellidos"].count().reset_index()
        newDf.columns = ["Departamento", "Cantidad de Personas"]

        #Un gráfico de pastel para ver la cantidad de personas por departamentos
        fig = px.pie(newDf, names='Departamento', values='Cantidad de Personas', title='Distribución por Departamento')

        st.plotly_chart(fig)
                
    elif subtema_seleccionado == "Análisis de Cargos":
        st.header("¿Cuál es la distribución de cargos en la facultad?")
        st.write("Examina cuántos profesores ocupan cada cargo (decano, profesor auxiliar, etc.).")
        newDf1 = data.groupby("Cargo")["Nombre y Apellidos"].count().reset_index()
        newDf1.columns = ["Cargo", "Cantidad de Profesores"]

        #Un gráfico de barras para la cantidad de personas dependiendo del cargo
        fig1 = px.bar(newDf1, x='Cargo', y='Cantidad de Profesores', title='Cantidad de Profesores por Cargo')

        st.plotly_chart(fig1)
        
    elif subtema_seleccionado == "Proporción Docentes/No Docentes":
        st.header("¿Cuál es la proporción de docentes frente a no docentes?")
        st.write("Aquí se compara la cantidad de docentes frente a no docentes.")
        newDf2 = data.groupby("Clasif. Por escala")["Nombre y Apellidos"].count().reset_index()
        newDf2.columns = ["Escala", "Cantidad de Personas"]

        #Un gráfico de pastel para ver la cantidad de dependiendo de sugranos
        fig2 = px.pie(newDf2, names='Escala', values='Cantidad de Personas', title='Proprción Docentes/No Docentes')

        st.plotly_chart(fig2)
    
elif seccion_seleccionada == "Entre Cátedras y Despachos: Mapeando la Estructura de la Facultad":
    st.header("Mapeando la Estructura de la Facultad")
    st.write("aquí va una introducción siguiendo con la historia de la estructura de la facultad y se menciona que se analizaran los departamentos")
    st.image('./Imagenes/composicion.jpg')

    st.divider()
    # Subtemas para la sección de Datos
    subtemas_datos = ["Departamento de Matemática", "Departamento de Matemática Aplicada", "Departamento de Computación 1", "Departamento de Computación 2"]
    subtema_seleccionado = st.sidebar.radio("Subtemas de Datos", subtemas_datos)
    
    if subtema_seleccionado == "Departamento de Matemática":
        st.header("Análisis del departamento de Matemática")
        st.write("breve explicación del departamento de matemática")
        st.divider()

        st.markdown("### 1. ¿Cuál es la edad promedio de los profesores?")
        st.write("Aqui el analisis y entre el análisis y la pregunta un grafico")
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
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")  

        cant_gender1=[]#Aqui se almacena la cantidad de cada genero
        cant_woman1=0
        cant_man1=0
        for i in data_filtred['Sexo']: 
            if i=='F': 
                cant_woman1+=1
            if i=='M':
                cant_man1+=1
        cant_gender1.append(cant_man1)
        cant_gender1.append(cant_woman1)

        df1 = pd.DataFrame({
            'Género': ['Hombres', 'Mujeres'],
            'Cantidad': cant_gender1
        })

        fig8 = px.bar(df1, x='Género', y='Cantidad', color='Género', title='Cantidad de Hombres y Mujeres')
        st.plotly_chart(fig8)

        st.markdown("### 3.¿Cuántos años de servicio tienen en promedio los profesores?")
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")


        st.markdown("### 4.¿Cuántos profesores tienen una categoría científica y cuáles son estas categorías?")
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")
        
    elif subtema_seleccionado == "Departamento de Matemática Aplicada":
        st.header("Análisis del departamento de matemática aplicada")
        st.write("breve explicación del departamento")
        st.divider()

        st.markdown("### 1. ¿Cuál es la edad promedio de los profesores?")
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")

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
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")  

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
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")

        st.markdown("### 4.¿Cuántos profesores tienen una categoría científica y cuáles son estas categorías?")
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")

    elif subtema_seleccionado == "Departamento de Computación 1":
        st.header("Análisis del departamento de computación1")
        st.write("breve explicación del departamento ")
        st.divider()

        st.markdown("### 1. ¿Cuál es la edad promedio de los profesores?")
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")

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
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")    

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
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")

        st.markdown("### 4.¿Cuántos profesores tienen una categoría científica y cuáles son estas categorías?")
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")

        
    elif subtema_seleccionado == "Departamento de Computación 2":
        st.header("Análisis del departamento de computación 2")
        st.write("breve explicación del departamento")
        st.divider()

        st.markdown("### 1. ¿Cuál es la edad promedio de los profesores?")
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")

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
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico") 

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
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")

        st.markdown("### 4.¿Cuántos profesores tienen una categoría científica y cuáles son estas categorías?")
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")

    
elif seccion_seleccionada == "Más que Docentes: Profundizando en el Perfil Investigador del Profesorado":
    st.header("Profundizando en el Perfil Investigador del Profesorado")
    st.write("An parrafo mas profundo sobre las actividades extraescoleres de los profesores y una breve introducción a los análisis de esta zona.")
    st.divider()
    st.markdown("### 1. ¿Cuántos profesores tienen una categoría científica y cuáles son estas categorías?")
    st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")
    st.markdown("### 2.¿Cuántos profesores son responsables de la enseñanza de maestría?")
    st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")    
    st.markdown("### 3.¿Qué porcentaje de profesores participa en grupos de investigación?")
    st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")

# Sección seleccionada
if seccion_seleccionada == "Desentrañando la Matriz: Un Análisis Comparativo del Profesorado":
    st.header("Un Análisis Comparativo del Profesorado")
    st.write("Esta sección presenta las conclusiones del análisis.")
    st.divider()
    # Opciones abreviadas para las preguntas
    opciones = [
        "1. Antigüedad y Cargo",
        "2. Género y Cargo",
        "3. Categoría Científica y Participación en Investigación",
        "4. Edad y Participación en Investigación",
        "5. Antigüedad y Participación en Grupos de Investigación",
        "6. Distribución de Cargos por Departamento",
        "7. Comparación de Género en Programas de Maestría",
        "8. Categoría Científica y Años de Servicio",
        "9. Participación en Grupos de Investigación por Departamento",
        "10. Antigüedad y Clasificación por Escala",
        "11. Impacto de la Categoría Científica en la Enseñanza de Maestría",
        "12. Años de Servicio y Género",
        "13. Participación en Grupos de Investigación y Cargo",
        "14. Antigüedad y Formación Académica",
        "15. Comparación de Departamentos en Términos de Diversidad",
        "16. Relación entre Antigüedad y Categoría Científica",
        "17. Distribución de Profesores de Maestría",
        "18. Participación en Grupos de Investigación según Cargo"
    ]
    
    # Selección de opción en la barra lateral
    opcion_seleccionada = st.sidebar.selectbox("Selecciona una opción:", opciones)

    # Contenido basado en la opción seleccionada
    if opcion_seleccionada == "1. Antigüedad y Cargo":
        st.markdown("### ¿Cómo varía la antigüedad promedio de los profesores según su cargo?")
        st.write("Compara la antigüedad de los profesores en diferentes cargos (decano, profesor titular, profesor auxiliar, etc.).")
    
    
    elif opcion_seleccionada == "2. Género y Cargo":
        st.markdown("### ¿Existen diferencias en la distribución de género según el cargo en la facultad?")
        st.write("Analiza si hay una representación equitativa de géneros en los distintos niveles de cargo.")

        # Agrupar por cargo y sexo, y contar la cantidad de cada uno
        distribucion_genero = data.groupby(['Cargo', 'Sexo']).size().reset_index(name='Cantidad')
        # Crear el gráfico de pastel en forma de anillo
        fig = px.sunburst(distribucion_genero, 
                          path=['Cargo', 'Sexo'], 
                          values='Cantidad', 
                          title='Distribución de Género según Cargo',
                          color='Cantidad',
                          color_continuous_scale=px.colors.sequential.Viridis)

        # Personalizar el diseño del gráfico
        fig.update_traces(hoverinfo='label+value+percent entry')
        fig.update_layout(margin=dict(t=50, l=0, r=0, b=0))

        # Mostrar el gráfico en Streamlit
        st.plotly_chart(fig)

    elif opcion_seleccionada == "3. Categoría Científica y Participación en Investigación":
        st.markdown("### ¿Los profesores con categorías científicas más altas participan más en grupos de investigación?")
        st.write("Compara la participación en investigación entre diferentes categorías científicas.")
    
    elif opcion_seleccionada == "4. Edad y Participación en Investigación":
        st.markdown("### ¿Hay diferencias en la participación en grupos de investigación según la edad de los profesores?")
        st.write("Examina si los profesores más jóvenes tienden a participar más en investigación que los mayores.")
    
    elif opcion_seleccionada == "5. Antigüedad y Participación en Grupos de Investigación":
        st.markdown("### ¿Los profesores con más años de servicio participan menos en grupos de investigación?")
        st.write("Compara la antigüedad de los profesores con su nivel de participación en investigación.")
    
    elif opcion_seleccionada == "6. Distribución de Cargos por Departamento":
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


    elif opcion_seleccionada == "7. Comparación de Género en Programas de Maestría":
        st.markdown("### ¿Cuál es la proporción de hombres y mujeres que enseñan en programas de maestría?")
        st.write("Examina si hay diferencias significativas en la representación de género en la enseñanza de maestría.")
    
    elif opcion_seleccionada == "8. Categoría Científica y Años de Servicio":
        st.markdown("### ¿Los profesores con más años de servicio tienden a tener categorías científicas más altas?")
        st.write("Compara la antigüedad con la categoría científica para identificar tendencias.")
    
    elif opcion_seleccionada == "9. Participación en Grupos de Investigación por Departamento":
        st.markdown("### ¿Qué departamentos tienen mayor o menor participación en grupos de investigación?")
        st.write("Analiza la participación en investigación entre diferentes departamentos.")
    
    elif opcion_seleccionada == "10. Antigüedad y Clasificación por Escala":
        st.markdown("### ¿Cómo se relaciona la antigüedad de los profesores con su clasificación por escala (docente o no docente)?")
        st.write("Examina si hay diferencias en la antigüedad promedio entre docentes y no docentes.")
    
    elif opcion_seleccionada == "11. Impacto de la Categoría Científica en la Enseñanza de Maestría":
        st.markdown("### ¿Los profesores con categorías científicas más altas son más propensos a enseñar en programas de maestría?")
        st.write("Compara la participación en la enseñanza de maestría según la categoría científica.")
    
    elif opcion_seleccionada == "12. Años de Servicio y Género":
        st.markdown("### ¿Existen diferencias en la antigüedad promedio entre hombres y mujeres en la facultad?")
        st.write("Analiza si hay una diferencia significativa en los años de servicio según el género.")
    
    elif opcion_seleccionada == "13. Participación en Grupos de Investigación y Cargo":
        st.markdown("### ¿Los decanos participan más o menos en grupos de investigación en comparación con otros cargos?")
        st.write("Compara la participación en investigación entre decanos y otros cargos.")
    
    elif opcion_seleccionada == "14. Antigüedad y Formación Académica":
        st.markdown("### ¿Los profesores con más años de servicio tienden a tener títulos académicos más altos (por ejemplo, doctorados)?")
        st.write("Examina la relación entre antigüedad y nivel educativo.")
    
    elif opcion_seleccionada == "15. Comparación de Departamentos en Términos de Diversidad":
        st.markdown("### ¿Cómo se compara la diversidad de género y categoría científica entre los diferentes departamentos?")
        st.write("Analiza la diversidad en términos de género y categorías científicas en cada departamento.")
    
    elif opcion_seleccionada == "16. Relación entre Antigüedad y Categoría Científica":
        st.markdown("### ¿Hay alguna relación entre la antigüedad y la categoría científica de los profesores?")
        st.write("Examina si los profesores con más años de servicio tienden a tener categorías científicas más altas.")
    
    elif opcion_seleccionada == "17. Distribución de Profesores de Maestría":
        st.markdown("### ¿Cómo se distribuyen los profesores de maestría entre los diferentes departamentos?")
        st.write("Analiza si hay departamentos con mayor o menor representación de profesores de maestría.")
    
    elif opcion_seleccionada == "18. Participación en Grupos de Investigación según Cargo":
        st.markdown("### ¿Existen diferencias en la participación en grupos de investigación según el cargo?")
        st.write("Compara la participación en grupos de investigación entre diferentes cargos (por ejemplo, decanos versus profesores auxiliares).")

