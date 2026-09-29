import streamlit as st
from PIL import Image

st.title("Portafolio Walter Benitez.")

with st.sidebar:
    st.subheader("Aplicaciones con Inteligencia Artificial.")
    parrafo = (
        "La inteligencia artificial permite mejorar la toma de decisiones con el uso de datos, "
        "automatizar tareas rutinarias y proporcionar análisis avanzados en tiempo real, lo que "
        "resulta en una mayor eficiencia y precisión en diversos campos."
    )
    st.write(parrafo)

url_ia = "https://sites.google.com/view/aplicacionesdeia/inicio"
st.subheader("En el siguiente enlace puedes encontrar páginas y ejercicios prácticos")
st.write(f"Enlace para páginas y ejercicios: [Enlace]({url_ia})")


def mostrar_app(titulo, imagen, descripcion, etiqueta, url, ancho=200):
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
        "OIG2.jpg",
        "En el siguiente enlace veremos una aplicación que identifica y clasifica frutas "
        "a partir de sus características usando un modelo de aprendizaje automático.",
        "Frutas",
        "https://appfrutasa.streamlit.app/",
    )

    mostrar_app(
        "Series de Tiempo",
        "data_analisis.png",
        "En el siguiente enlace veremos cómo analizar datos a lo largo del tiempo para "
        "identificar tendencias, estacionalidad y hacer pronósticos.",
        "Series de tiempo",
        "https://seriestiempo.streamlit.app/",
        ancho=190,
    )

    mostrar_app(
        "Regresión Logística",
        "OIG5.jpg",
        "En el siguiente enlace veremos un modelo de regresión logística que predice "
        "la probabilidad de que un dato pertenezca a una clase (por ejemplo, sí o no).",
        "Regresión logística",
        "https://regresionlogisticaweb.streamlit.app/",
    )

    mostrar_app(
        "Regresión",
        "OIG6.jpg",
        "En el siguiente enlace veremos un modelo de regresión que estima valores "
        "numéricos a partir de la relación entre variables.",
        "Regresión",
        "https://regresionapp.streamlit.app/",
    )

with col2:
    mostrar_app(
        "Preparación de Datos",
        "txt_to_audio.png",
        "En el siguiente enlace veremos cómo limpiar, transformar y organizar datos "
        "antes de usarlos para entrenar un modelo.",
        "Preparación de datos",
        "https://preparaciondatos.streamlit.app/",
    )

    mostrar_app(
        "Aplicación Interactiva con Streamlit",
        "OIG8.jpg",
        "En el siguiente enlace veremos una aplicación interactiva construida con "
        "Streamlit para explorar y visualizar información.",
        "Streamlit",
        "https://streamlyapp.streamlit.app/",
    )

    mostrar_app(
        "Análisis con Datos Reales",
        "OIG3.jpg",
        "En el siguiente enlace veremos cómo aplicar técnicas de análisis e "
        "inteligencia artificial sobre un conjunto de datos reales.",
        "Datos reales",
        "https://appdatosreales.streamlit.app/",
    )

    mostrar_app(
        "Descenso del Gradiente",
        "OIG4.jpg",
        "En el siguiente enlace veremos cómo funciona el descenso del gradiente, el "
        "algoritmo que usan los modelos para ajustar sus parámetros y reducir el error.",
        "Gradiente",
        "https://appgradient.streamlit.app/",
    )

with col3:
    mostrar_app(
        "Portafolio",
        "Chat_pdf.png",
        "En el siguiente enlace veremos un portafolio que reúne los proyectos y "
        "ejercicios desarrollados durante el curso.",
        "Portafolio",
        "https://appportafolioo.streamlit.app/",
        ancho=190,
    )

    mostrar_app(
        "Módulo 4",
        "txt_to_audio2.png",
        "En el siguiente enlace veremos la aplicación con los ejercicios y "
        "resultados del módulo 4.",
        "Módulo 4",
        "https://appmodulo4.streamlit.app/",
        ancho=190,
    )

    mostrar_app(
        "K Vecinos Más Cercanos (KNN)",
        "audio_to_txt.png",
        "En el siguiente enlace veremos el algoritmo KNN, que clasifica un dato "
        "según la clase de los ejemplos más parecidos a él.",
        "KNN",
        "https://aplicacionknn.streamlit.app/",
    )
