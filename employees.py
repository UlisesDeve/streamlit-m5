import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np 

tam_cache = 500
url =('Employees.csv')

st.title('Análisis de deserción de empleados')
st.subheader("Creado por: Ulises Martínez Chávez")
st.info('_Sitio que permite al usuario conocer diferentes análisis de deserción de empleados a través del ***menú de opciones*** que aparece en la barra del lado izquierdo._', icon="ℹ️")

sidebar = st.sidebar
st.sidebar.image("logo.png")
sidebar.title("Menú de opciones")
sidebar.write("Selecciona la opción:")

#--------------------- Funciones ---------------------#
def load_data_nocache():
    data = pd.read_csv(url)
    return data

@st.cache
def load_data(nrows):
    data = pd.read_csv(url, nrows=nrows)
    return data

@st.cache
def buscar_id(id_empleado, nrows):
    data = load_data(nrows)   
    filtro_id = data[data['Employee_ID'].str.upper().str.contains(id_empleado)]
    return filtro_id

@st.cache
def buscar_ciudad(ciudad, nrows):
    data = load_data(nrows)   
    filtro_ciudad = data[data['Hometown'].str.upper().str.contains(ciudad)]
    return filtro_ciudad

@st.cache
def buscar_unidad(unidad, nrows):
    data = load_data(nrows)   
    filtro_unidad = data[data['Unit'].str.upper().str.contains(unidad)]
    return filtro_unidad

@st.cache
def buscar_nivel(nivel, nrows):
    data = load_data(nrows)
    filtro_nivel = data[data['Education_Level'] == nivel]
    return filtro_nivel

@st.cache
def buscar_ciudades(ciudades, nrows):
    data = load_data(nrows)
    filtro_ciudades = data[data['Hometown'] == ciudades]
    return filtro_ciudades

@st.cache
def buscar_unidades(unidades, nrows):
    data = load_data(nrows)
    filtro_unidades = data[data['Unit'] == unidades]
    return filtro_unidades


if sidebar.checkbox('Mostrar Dataframe'):
    data = load_data_nocache()
    count_row = data.shape[0]  
    st.write(f"Total de registros en el Dataframe = {count_row}")
    st.dataframe(data)

#--------------------- Separador ---------------------#
st.sidebar.markdown("-" * 34)

id_empleado = st.sidebar.text_input('Búsqueda por Id Empleado:')
btnBuscar_id = st.sidebar.button('Buscar por Id')

if (btnBuscar_id):
   data_id = buscar_id(id_empleado.upper(), tam_cache)
   count_row = data_id.shape[0]  
   st.write(f"Total de empleados encontrados por Id = {count_row}")
   st.write(data_id)

ciudad = st.sidebar.text_input('Búsqueda por Ciudad:')
btnBuscar_ciudad = st.sidebar.button('Buscar por Ciudad')

if (btnBuscar_ciudad):
   data_ciudad = buscar_ciudad(ciudad.upper(), tam_cache)
   count_row = data_ciudad.shape[0]  
   st.write(f"Total de empleados encontrados por Ciudad = {count_row}")
   st.write(data_ciudad)

unidad = st.sidebar.text_input('Búsqueda por Unidad:')
btnBuscar_unidad = st.sidebar.button('Buscar por Unidad')

if (btnBuscar_unidad):
   data_unidad = buscar_unidad(unidad.upper(), tam_cache)
   count_row = data_unidad.shape[0]  
   st.write(f"Total de empleados encontrados por Unidad = {count_row}")
   st.write(data_unidad)

#--------------------- Separador ---------------------#
st.sidebar.markdown("-" * 34)
nivel = st.sidebar.selectbox("Búsqueda por Nivel Educativo:", load_data(tam_cache)['Education_Level'].unique())
btnBuscar_nivel = st.sidebar.button('Buscar por Nivel Educativo')

if (btnBuscar_nivel):
   data_nivel = buscar_nivel(nivel, tam_cache)
   count_row = data_nivel.shape[0]
   st.write(f"Total de empleados encontrados por Nivel Educativo = {count_row}")
   st.write(data_nivel)

ciudades = st.sidebar.selectbox("Búsqueda por Ciudades:", load_data(tam_cache)['Hometown'].unique())
btnBuscar_ciudades = st.sidebar.button('Buscar por Ciudades')

if (btnBuscar_ciudades):
   data_ciudades = buscar_ciudades(ciudades, tam_cache)
   count_row = data_ciudades.shape[0]
   st.write(f"Total de empleados encontrados por Ciudades = {count_row}")
   st.write(data_ciudades)

unidades = st.sidebar.selectbox("Búsqueda por Unidades:", load_data(tam_cache)['Unit'].unique())
btnBuscar_unidades = st.sidebar.button('Buscar por Unidades')

#--------------------- Separador ---------------------#
st.sidebar.markdown("-" * 34)

if (btnBuscar_unidades):
   data_unidades = buscar_unidades(unidades, tam_cache)
   count_row = data_unidades.shape[0]
   st.write(f"Total de empleados encontrados por Unidades = {count_row}")
   st.write(data_unidades)

if sidebar.checkbox('Mostrar Histograma por Edad'):
    data = load_data_nocache()
    fig, ax = plt.subplots()
    ax.hist(data.Age)
    st.header("Histograma por Edad de los Empleados")
    ax.set_ylabel("Conteo")
    ax.set_xlabel("Edad")
    st.pyplot(fig)

if sidebar.checkbox('Mostrar Gráfica por Unidad'):
    data = load_data_nocache()[['Employee_ID','Unit']].groupby('Unit').count()    
    fig2, ax2 = plt.subplots()    
    y_pos = data.index
    x_pos = data['Employee_ID']   
    ax2.barh(y_pos, x_pos)
    ax2.set_ylabel('Unidad')
    ax2.set_xlabel('Conteo')    
    st.header("Grafica por Unidad Funcional")        
    st.pyplot(fig2)
    
if sidebar.checkbox('Análisis Deserción por Ciudad'):
    data = load_data_nocache()[['Attrition_rate','Hometown']].groupby('Hometown').sum()    
    st.write(data.style.highlight_max(axis=0))
    st.bar_chart(data)

    st.markdown("**Análisis**")
    st.markdown("""Podemos observar que las cuidades de Lebanon y Springfield son las que tienen mayor índice de deserción, con una tase del 387.1 y 336.9 respectivamente.\
                   Mientras que la ciudad de Clinton es la que representa menor índice de deserción.""")

if sidebar.checkbox('Análisis Deserción por Edad'):
    data = load_data_nocache()[['Attrition_rate','Age']].groupby('Age').sum()    
    st.write(data.style.highlight_max(axis=0))
    st.area_chart(data)      

    st.markdown("**Análisis**")
    st.markdown("""El índice de deserción es alto en las edades jóvenes desde los 19 hasta los 38 años como lo observamos en la gráfica. \
                   No se observa una regularidad en la tasa de deserción, solo en las edades como los 40, 50 y 62 años se presentan los menores índices.""")
    st.markdown("""La tasa promedio de deserción es: """)
    st.write(data['Attrition_rate'].mean())  

if sidebar.checkbox('Análisis Deserción por Tiempo de Servicio'):
    data = load_data_nocache()[['Attrition_rate','Time_of_service']].groupby('Time_of_service').sum()    
    st.write(data.style.highlight_max(axis=0))
    st.line_chart(data)      

    st.markdown("**Análisis**")
    st.markdown("""El índice de deserción incrementa desde los 0 hasta los 6 años de servicio, donde en este último existe el índice más alto. \
                   Después de los 6 años de servicio la tasa de deserción tiene una tendencia a la baja, podemos interpretar que a más años de servicio \
                   la tasa de deserción disminuye conforme pasan los años.""") 