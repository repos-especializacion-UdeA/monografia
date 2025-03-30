import os
import sys
import scipy.io  # Asegúrate de importar scipy.io para cargar archivos .mat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Agregar el directorio raíz del proyecto al PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config.config import RAW_DATA_DIR
from data_ingestion import load_all_mat_files, load_mat_file, get_signal_data_by_features, FEATURES
from visualization import graficar_medida1

if __name__ == '__main__':
    signal_data = load_mat_file(RAW_DATA_DIR, 'S1_A1_E1.mat')
    signal_data_df = get_signal_data_by_features(signal_data, FEATURES)
    print(signal_data_df.head())
    mascara_emg = signal_data_df.columns.str.contains('emg')
    signal_data_emg_df = signal_data_df.loc[:,mascara_emg]
    

    # signal_data_emg_df = signal_data_df[signal_data_df.columns.str.contains('emg')]
    graficar_medida1(signal_data_emg_df,
                     columnas = signal_data_emg_df.columns,
                     titulo = "Grafico canales EMG",
                     etiqueta_x="n",
                     etiqueta_y="Amplitud")
    
