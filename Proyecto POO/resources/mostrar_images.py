import streamlit as st
import os

# Función para verificar si la imagen existe antes de mostrarla
def mostrar_imagen(si_encontrada, ruta, caption, width=None):
    if os.path.exists(ruta):
        st.image(ruta, caption=caption, width=width)
    else:
        st.warning(f'Imagen no encontrada: {ruta}')

# Mostrar el contenido según el estado de la aplicacion
def mostrar_logo_uni1():
    mostrar_imagen(True, 'https://upload.wikimedia.org/wikipedia/commons/f/f7/Uni-logo_transparente_granate.png', 'UNIVERSIDAD NACIONAL DE INGENIERIA')

def mostrar_logo_uni():
    st.sidebar.image('images/LOGO_UNI.png', caption='UNIVERSIDAD NACIONAL DE INGENIERIA', use_column_width=True)

def mostrar_images_facultades():
    mostrar_imagen(True, 'images/FAUA.jpg', 'Arquitectura, Urbanismo y Arte', width=300)
    mostrar_imagen(True, 'images/FIC.png', 'Ingeniería Civil', width=300)
    mostrar_imagen(True, 'images/FIQT.jpg', 'Ingeniería Química y Textil', width=300)
    mostrar_imagen(True, 'images/FIP.png', 'Ingeniería de Petróleo, Gas Natural y Petroquímica', width=300)
    mostrar_imagen(True, 'images/FIEECS.png', 'Ingeniería Económica, Estadística y Ciencias Sociales', width=300)
    mostrar_imagen(True, 'images/FIIS.jpg', 'Ingeniería Industrial y de Sistemas', width=300)
    mostrar_imagen(True, 'images/FIA.png', 'Ingeniería Ambiental', width=300)
    mostrar_imagen(True, 'images/FIGMM.png', 'Ingeniería Geológica, Minera y Metalúrgica', width=300)
    mostrar_imagen(True, 'images/FIEE.png', 'Ingeniería Eléctrica y Electrónica', width=300)
    mostrar_imagen(True, 'images/FIM.png', 'Ingeniería Mecánica', width=300)
    mostrar_imagen(True, 'images/FC.png', 'Ciencias', width=300)
