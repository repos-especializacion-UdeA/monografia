import os
import sys
import scipy.io  # Asegúrate de importar scipy.io para cargar archivos .mat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

####################################################################################################
# Funciones de graficado
####################################################################################################

def graficar_medida1(medida, 
                    fs = None,
                    columnas = None, 
                    titulo = None, 
                    etiqueta_x = None, 
                    etiqueta_y = None):
    plt.figure(figsize=(20, 5))  # Tamaño del gráfico
    
    # Iterar sobre cada columna en la lista de columnas
    if fs is None:
        t = medida.index
    else:
        t = 1/fs*medida.index

    if not isinstance(medida, pd.DataFrame):
        t = np.arange(0,len(medida))
        if fs is not None:
            t = 1/fs*t
        plt.plot(t,medida)  # Graficar cada columna
    else:
        if (columnas is None):
            columnas = medida.columns      
        for columna in columnas:
            plt.plot(t, medida[columna], label=columna)  # Graficar cada columna

    # Añadir títulos y etiquetas
    if etiqueta_x is None: 
        etiqueta_x = "muestras [n]"
        if fs is not None:
            etiqueta_x = "tiempo [s]"

    if etiqueta_y is None: 
        etiqueta_y = "Amplitud"
    
    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    plt.legend()  # Añadir la leyenda para distinguir las columnas
    plt.grid(True)  # Añadir cuadrícula
    plt.show()

    """
    graficar_varias_columnas(emgs,
                         columnas = emgs.columns,
                         titulo = "Grafico canales EMG",
                         etiqueta_x="n",
                         etiqueta_y="Amplitud")
    """


def graficar_medida2(medida, 
                     columnas = None, 
                     labels = None,
                     num = 0, 
                     fs = None,
                     titulo=None, 
                     etiqueta_x=None, 
                     etiqueta_y=None):
    [inicio,fin]= indice_numero(labels, num)
    num_puntos = fin - inicio
    ban_end = False
    ban_add_vertical_lines = False
    lim = [0 , 0]
    limites_x = []

    """
    IMPORTANTE: Aun no funciona para graficar en escala de segundos
    """

    # Si se especifica num_puntos, selecciona solo los primeros num_puntos de la Serie
    fig, ax = plt.subplots(figsize=(20, 5))
    
    # Iterar sobre cada columna en la lista de columnas
    


    if num_puntos:
        if (columnas is None):
            columnas = medida.columns      
        for columna in columnas:
            df_col = medida[columna].iloc[inicio:inicio + num_puntos]
            if fs is None:
                t = df_col.index
            else:
                t = 1/fs*df_col.index
            plt.plot(t, df_col, label=columna)  # Graficar cada columna



    cambios_nivel = detectar_cambios_nivel(labels, num)
    # Añadir las bandas verticales sombreadas con los límites proporcionados
    for cambio_nivel in cambios_nivel:
      if(cambio_nivel[1] == 0):
        if ban_end == False:
          lim[0] = cambio_nivel[0]
          ban_end = True
        else:
          lim[1] = cambio_nivel[0]
          ban_end = False
          ax.axvspan(lim[0], lim[1], color='gray', alpha=0.3, label=f'Sombreado entre {lim[0]} y {lim[1]}')

    # Añadir títulos y etiquetas
    if etiqueta_x is None: 
        etiqueta_x = "muestras [n]"
        if fs is not None:
            etiqueta_x = "tiempo [s]"

    if etiqueta_y is None: 
        etiqueta_y = "Amplitud"

    plt.title(titulo)
    plt.xlabel(etiqueta_x)
    plt.ylabel(etiqueta_y)
    plt.grid(True)  # Activa la cuadrícula
    plt.show()
