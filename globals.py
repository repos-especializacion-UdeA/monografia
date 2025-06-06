# Archivo para configuraciones (rutas, parámetros, etc.)
# -*- coding: utf-8 -*-
"""
Archivo de configuración del proyecto de Machine Learning.
"""

import os
# Obtener la ruta absoluta del directorio raíz del proyecto

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))

# --- Rutas de Directorios ---
DATA_DIR = os.path.join(ROOT_DIR, 'data')
RAW_DATA_DIR = os.path.join(DATA_DIR, 'raw')
RAW_SUBSET_DATA_DIR = os.path.join(DATA_DIR, 'raw_subset')
PREPROCESSED_SUBSET_DATA_DIR = os.path.join(DATA_DIR, 'preprocessed_subset')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')
FEATURES_SUBSET_DATA_DIR = os.path.join(DATA_DIR, 'features_subset')
TRAIN_DATA_DIR = os.path.join(DATA_DIR, 'processed')
MODELS_DIR = os.path.join(ROOT_DIR, 'models')
REPORTS_DIR = os.path.join(ROOT_DIR, 'reports')
NOTEBOOKS_DIR = os.path.join(ROOT_DIR, 'notebooks')
SRC_DIR = os.path.join(ROOT_DIR, 'src')
TEST_DIR = os.path.join(ROOT_DIR, 'tests')

# --- Rutas de Archivos (Ejemplos - Ajusta según tus necesidades) ---
# RAW_DATA_FILE = os.path.join(RAW_DATA_DIR, 'tu_archivo_de_datos.csv')
# PROCESSED_TRAIN_FILE = os.path.join(PROCESSED_DATA_DIR, 'train_data.csv')
# PROCESSED_TEST_FILE = os.path.join(PROCESSED_DATA_DIR, 'test_data.csv')
# MODEL_FILE = os.path.join(MODELS_DIR, 'modelo_entrenado.pkl')  # Ejemplo para guardar un modelo con pickle

# --- Parámetros del Modelo (Ejemplos - Ajusta según tu modelo) ---
RANDOM_SEED = 42
TEST_SIZE = 0.2
# LEARNING_RATE = 0.01
# N_ESTIMATORS = 100
# ... otros hiperparámetros ...

# --- Nombres de Columnas (Ejemplos - Ajusta según tus datos) ---
#TARGET_COLUMN = 'nombre_de_la_columna_objetivo'
#FEATURE_COLUMNS = [
#    'columna_feature_1',
#    'columna_feature_2',
    # ... otras columnas de características ...
#]
# ID_COLUMN = 'identificador_unico'

# --- Otros parámetros o configuraciones ---
# LOGGING_LEVEL = 'INFO'
# ... cualquier otra configuración global que necesites ...

if __name__ == "__main__":
    # Puedes agregar código de prueba aquí si es necesario
    print("Configuraciones cargadas correctamente.")
    print(f"Directorio raíz del proyecto: {ROOT_DIR}")
    print(f"Directorio de datos crudos: {RAW_DATA_DIR}")
    print(f"Directorio de datos procesados: {PROCESSED_DATA_DIR}")
    print(f"Directorio de modelos: {MODELS_DIR}")
    print(f"Directorio de informes: {REPORTS_DIR}")
    print(f"Directorio de notebooks: {NOTEBOOKS_DIR}")