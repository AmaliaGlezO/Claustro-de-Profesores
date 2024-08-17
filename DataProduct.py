import streamlit as st
import pandas as pd 

data=pd.read_excel('antiguedad-matematica.xlsx')

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
        
    elif subtema_seleccionado == "Análisis de Cargos":
        st.header("¿Cuál es la distribución de cargos en la facultad?")
        st.write("Examina cuántos profesores ocupan cada cargo (decano, profesor auxiliar, etc.).")
        
    elif subtema_seleccionado == "Proporción Docentes/No Docentes":
        st.header("¿Cuál es la proporción de docentes frente a no docentes?")
        st.write("Aquí se compara la cantidad de docentes frente a no docentes.")
    
    
elif seccion_seleccionada == "Entre Cátedras y Despachos: Mapeando la Estructura de la Facultad":
    st.header("Mapeando la Estructura de la Facultad")
    st.write("aquí va una introducción siguiendo con la historia de la estructura de la facultad y se menciona que se analizaran los departamentos")
    st.write("Aqui va una imagen que será composición.jpg")

    st.divider()
    # Subtemas para la sección de Datos
    subtemas_datos = ["Departamento de Matemática", "Departamento de Matemática Aplicada", "Departamento de Computación 1", "Departamento de Computación 2"]
    subtema_seleccionado = st.sidebar.radio("Subtemas de Datos", subtemas_datos)
    
    if subtema_seleccionado == "Departamento de Matemática":
        st.header("Análisis del departamento de matemática")
        st.write("breve explicación del departamento de matemática")
        st.divider()

        st.markdown("### 1. ¿Cuál es la edad promedio de los profesores?")
        st.write("Aqui el analisis y entre el análisis y la pregunta un grafico")
        st.markdown("### 2.¿Cuál es la distribución de género entre los profesores?")
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")    
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
        st.markdown("### 2.¿Cuál es la distribución de género entre los profesores?")
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")    
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
        st.markdown("### 2.¿Cuál es la distribución de género entre los profesores?")
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")    
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
        st.markdown("### 2.¿Cuál es la distribución de género entre los profesores?")
        st.write(" Aqui el analisis y entre el análisis y la pregunta un grafico")    
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
    
import streamlit as st

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

