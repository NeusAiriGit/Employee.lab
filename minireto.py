#Rodrigo Hernández A01610903

#-----------Libreiras
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import matplotlib.pyplot as plt

#-----------Constantes y dtos
nameC = "Employees.csv"
nrowsC = 500

apptitle = 'Mini Reto: Employees'
app_Mat = 'Matricula: A01610903'
app_Name = 'Nombre: Rodrigo Hernández'

proyect_descrip = (
'''
Complementar el análisis de datos con la representación 
en un dashboard usando Streamlit de manera eficiente 
y atractiva para un usuario final.
''')

sidebar = st.sidebar
titleS = 'Controles'
descript = 'Controles para visualizar diferentes datos'

DesFil1 = 'Buscar Id del empleado'
DesFil2 = 'Buscar empleado por Hometown'
DesFil3 = 'Buscar empleado por Unit'

DesFil4 = 'Filtrar por Nivel Educativo'
DesFil5 = 'Filtrar por Unit'


#-----------Funciones
@st.cache(suppress_st_warning=True)
def showDataset(name,nrows):
    df=pd.read_csv(name,nrows=nrows)
    df.dropna(inplace=True)
    dfvis = df.copy()
    return df, dfvis

df, dfvis= showDataset(nameC,nrowsC)

@st.cache(suppress_st_warning=True)
def filter_data_by_EID(E_id):
    filtered_data_EID = df[df['Employee_ID'].str.lower().str.contains(E_id)]
    return filtered_data_EID

@st.cache(suppress_st_warning=True)
def filter_data_by_HT(Hometown):
    filtered_data_HT = df[df['Hometown'].str.lower().str.contains(Hometown)]
    return filtered_data_HT

@st.cache(suppress_st_warning=True)
def filter_data_by_UT(Unit):
    filtered_data_UT = df[df['Unit'].str.lower().str.contains(Unit)]
    return filtered_data_UT

@st.cache(suppress_st_warning=True)
def filter_data_by_NE(EL):
    filtered_data_NE = df[df['Education_Level'] == EL]
    return filtered_data_NE

@st.cache(suppress_st_warning=True)
def filter_data_by_UTF(UnitF):
    filtered_data_UTF = df[df['Unit'] == UnitF] 
    return filtered_data_UTF

#----------Sidebar
sidebar.title(titleS)
sidebar.header(descript)

#----------Web
st.title(apptitle)
colN, colM = st.columns([1,2])
colN.header(app_Mat)
colM.header(app_Name)
st.text(proyect_descrip)


EmpId = sidebar.text_input(DesFil1)
if sidebar.button('Buscar ID'):
    dfvis = (filter_data_by_EID(str(EmpId).lower()))

HtId = sidebar.text_input(DesFil2)
if sidebar.button('Buscar Hometown'):
    dfvis = (filter_data_by_HT(str(HtId).lower()))

UtId = sidebar.text_input(DesFil3)
if sidebar.button('Buscar Unit'):
    dfvis = (filter_data_by_UT(str(UtId).lower()))

sidebar.markdown('___')

NeFil = sidebar.selectbox(DesFil4,df['Education_Level'].unique())
if sidebar.button('Buscar por Nivel Educivo'):
    dfvis = (filter_data_by_NE(NeFil))

UtFil = sidebar.selectbox(DesFil5,df['Unit'].unique())
if sidebar.button('Buscar por Unit'):
    dfvis = (filter_data_by_UTF(UtFil))



if sidebar.checkbox('Visualizar Dataset?'):
    st.dataframe(dfvis)
    st.markdown('___')
    if dfvis.shape[0] == df.shape[0]:
        st.text('Sin filtros')        
    
    st.text(f'Total de empleados encontrados: {dfvis.shape[0]}')
    
    #Graficas
    st.markdown('___')
    st.header('Graficas analíticas')
    st.header('')
    st.header('Histiograma')
    fig, ax = plt.subplots()
    ax.hist(df.Age, rwidth=0.85)
    ax.set_title('Empleados grupados por edad')
    st.pyplot(fig)
    st.markdown('')

    st.header('Grafico de frecuencias')
    fig2, ax2 = plt.subplots()
    ax2.hist(df.Unit, rwidth=0.85, orientation="horizontal", color = "red")
    ax2.set_title('Empleados por Unidad')
    st.pyplot(fig2)
    st.markdown('')


if sidebar.button('Reiniciar DataFrame'):
    dfvis = df.copy()