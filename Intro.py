import streamlit as st
from PIL import Image

st.title("Portafolio Walter Benitez.")

with st.sidebar:
    st.subheader("Aplicaciones con streamlit.")
   


def mostrar_app(titulo, imagen, descripcion, etiqueta, url, ancho=230):
    """Muestra una tarjeta con título, imagen, descripción y enlace."""
    st.subheader(titulo)
    image = Image.open(imagen)
    st.image(image, width=ancho)
    st.write(descripcion)
    st.write(f"{etiqueta}: [Enlace]({url})")
 
 
col1, col2, col3 = st.columns(3)
 
with col1:
    mostrar_app(
        "Clasificación de Frutas",
        "frutas.png",
        "En el siguiente enlace veremos cómo representar las características de las "
        "frutas como vectores para clasificarlas con aprendizaje automático.",
        "Frutas",
        "https://appfrutasa.streamlit.app/",
    )
 
    mostrar_app(
        "Series de Tiempo",
        "series_tiempo.png",
        "En el siguiente enlace veremos los fundamentos y modelos de series de tiempo, "
        "desde la teoría matemática hasta su uso en Machine Learning e IoT.",
        "Series de tiempo",
        "https://seriestiempo.streamlit.app/",
    )
 
    mostrar_app(
        "Regresión Logística",
        "regresion_logistica.png",
        "En el siguiente enlace veremos cómo la regresión logística toma decisiones "
        "binarias, prediciendo la probabilidad de que un dato pertenezca a una clase.",
        "Regresión logística",
        "https://regresionlogisticaweb.streamlit.app/",
    )
 
    mostrar_app(
        "Regresión",
        "regresion.png",
        "En el siguiente enlace veremos cómo predecir la sensación térmica con datos de "
        "sensores IoT, desde la captura de series temporales hasta la regresión lineal.",
        "Regresión",
        "https://regresionapp.streamlit.app/",
    )
 
with col2:
    mostrar_app(
        "Preparación de Datos",
        "preparacion_datos.png",
        "En el siguiente enlace veremos cómo limpiar, tipificar, escalar, dividir y "
        "validar datos crudos para dejarlos listos para entrenar un modelo.",
        "Preparación de datos",
        "https://preparaciondatos.streamlit.app/",
    )
 
    mostrar_app(
        "Ecosistema Predictivo",
        "streamly.png",
        "En el siguiente enlace veremos un sistema de alerta temprana que combina modelos "
        "como SARIMA, Holt-Winters y Machine Learning para pronosticar PM2.5 y PM10.",
        "Ecosistema predictivo",
        "https://streamlyapp.streamlit.app/",
    )
 
    mostrar_app(
        "Análisis con Datos Reales",
        "datos_reales.png",
        "En el siguiente enlace veremos datos ambientales reales de la región Cornare "
        "(precipitación, nivel de ríos y caudal) para identificar patrones.",
        "Datos reales",
        "https://appdatosreales.streamlit.app/",
    )
 
    mostrar_app(
        "Descenso del Gradiente",
        "gradiente.png",
        "En el siguiente enlace veremos cómo el gradiente indica la dirección en la que "
        "el modelo debe ajustar sus parámetros para reducir el error.",
        "Gradiente",
        "https://appgradient.streamlit.app/",
    )
 
with col3:
    mostrar_app(
        "Portafolio",
        "estacion_la_aduanilla.png",
        "En el siguiente enlace veremos un portafolio que reúne los proyectos y "
        "ejercicios desarrollados durante el curso.",
        "Portafolio",
        "https://appportafolioo.streamlit.app/",
    )
 
    mostrar_app(
        "Módulo 4",
        "modulo4.png",
        "En el siguiente enlace veremos la línea de ensamblaje de la IA: lógica "
        "proposicional, notación Big-O y vectorización.",
        "Módulo 4",
        "https://appmodulo4.streamlit.app/",
    )
 
    mostrar_app(
        "K Vecinos Más Cercanos (KNN)",
        "knn.png",
        "En el siguiente enlace veremos el algoritmo KNN y cómo el valor de k equilibra "
        "la sensibilidad al ruido y la estabilidad del modelo.",
        "KNN",
        "https://aplicacionknn.streamlit.app/",
    )
