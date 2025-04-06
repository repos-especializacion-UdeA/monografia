# src/data_ingestion.py
import os
import sys
import scipy.io  # Asegúrate de importar scipy.io para cargar archivos .mat
import numpy as np
import pandas as pd

# Agregar el directorio raíz del proyecto al PYTHONPATH
# Agregar el directorio raíz del proyecto al PYTHONPATH
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from globals import RAW_DATA_DIR
print(RAW_DATA_DIR)

FEATURES = ['emg', 'repetition', 'restimulus']

# ...skynet...
def load_all_mat_files(directory_path = RAW_DATA_DIR):
    """
    Carga todos los archivos .mat de un directorio y devuelve sus contenidos.

    Parameters:
    directory_path (str): Ruta al directorio que contiene los archivos .mat.

    Returns:
    dict: Un diccionario donde las claves son los nombres de los archivos y los valores son los contenidos de los archivos .mat.
    """
    mat_files_data = {}
    try:
        # Iterar sobre todos los archivos en el directorio
        for file_name in os.listdir(directory_path):
            if file_name.endswith('.mat'):  # Verificar si el archivo tiene extensión .mat
                file_path = os.path.join(directory_path, file_name)
                try:
                    # Cargar el archivo .mat
                    mat_contents = scipy.io.loadmat(file_path)
                    mat_files_data[file_name] = mat_contents
                except Exception as e:
                    print(f"Error al cargar el archivo {file_name}: {e}")
        return mat_files_data
    except FileNotFoundError:
        print(f"Error: El directorio {directory_path} no fue encontrado.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al leer los archivos .mat en el directorio: {e}")
        return None


def load_mat_file(directory_path, file_name):
    """
    Carga un archivo .mat y devuelve su contenido.

    Parameters:
    directory_path (str): Ruta al directorio que contiene el archivo .mat.
    file_name (str): Nombre del archivo .mat.

    Returns:
    dict: Contenido del archivo .mat.
    """
    try:
        # Construir la ruta completa del archivo
        file_path = os.path.join(directory_path, file_name)
        
        # Cargar el archivo .mat
        mat_contents = scipy.io.loadmat(file_path)
        return mat_contents
    except FileNotFoundError:
        print(f"Error: El archivo {file_path} no fue encontrado.")
        return None
    except Exception as e:
        print(f"Ocurrió un error al cargar el archivo .mat: {e}")
        return None

def get_signal_data_by_features(mat_data, features):
    """
    Extrae datos de una señal específica por características desde un archivo .mat y los organiza en un DataFrame.

    Parameters:
    mat_data (dict): Contenido del archivo .mat cargado como un diccionario.
    features (list): Lista de características (claves) a extraer del archivo .mat.

    Returns:
    pd.DataFrame: Un DataFrame donde cada columna corresponde a una característica extraída.
                  Si una característica tiene múltiples columnas, estas se concatenan con nombres únicos.
                  Si una característica no se encuentra, se muestra una advertencia.
    """
    signal_data_df = pd.DataFrame()  # Crear un DataFrame vacío para almacenar los datos
    try:
        for feature in features:
            if feature in mat_data:  # Verificar si la característica está en los datos
                # Convertir los datos de la característica en un DataFrame
                data_frame_feature = pd.DataFrame(mat_data[feature])                
                # Si la característica tiene múltiples columnas, concatenarlas con nombres únicos
                if mat_data[feature].shape[1] > 1:
                    signal_data_df = pd.concat([signal_data_df, data_frame_feature], axis=1)
                    # Renombrar las columnas para incluir el nombre de la característica
                    signal_data_df.columns = [feature + '_' + str(col + 1) for col in range(signal_data_df.shape[1])]
                else:
                    # Si la característica tiene una sola columna, agregarla directamente
                    signal_data_df[feature] = data_frame_feature.squeeze()
            else:
                # Mostrar advertencia si la característica no está presente
                print(f"Advertencia: La característica '{feature}' no se encontró en los datos.")
        return signal_data_df  # Retornar el DataFrame con los datos procesados
    except Exception as e:
        print(f"Ocurrió un error al extraer los datos por características: {e}")
        return None
    

if __name__ == '__main__':
    # Test varios archivos
    mat_files_data = load_all_mat_files()
    print(mat_files_data.keys())

    # Test un archivo específico
    signal_data = load_mat_file(RAW_DATA_DIR, 'S1_A1_E1.mat')
    signal_data_df = get_signal_data_by_features(signal_data, FEATURES)
    print(signal_data_df.head())

