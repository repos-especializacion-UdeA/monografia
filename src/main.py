import os
import sys
import scipy.io  # Asegúrate de importar scipy.io para cargar archivos .mat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Agregar el directorio raíz del proyecto al PYTHONPATH

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

from globals import RAW_DATA_DIR
from data_ingestion import load_all_mat_files, load_mat_file, get_signal_data_by_features, FEATURES
from visualization import graficar_medida1
from data_preprocessing import detect_level_changes, butter_lowpass_filter, \
      apply_filter_to_dataframe, segment_signal, segment_signal2, segment_signal_as_matrix

if __name__ == '__main__':
    signal_data = load_mat_file(RAW_DATA_DIR, 'S1_A1_E1.mat')
    signal_data_df = get_signal_data_by_features(signal_data, FEATURES)
    print(signal_data_df.head())
    mascara_emg = signal_data_df.columns.str.contains('emg')
    signal_data_emg_df = signal_data_df.loc[:,mascara_emg]
    

    # signal_data_emg_df = signal_data_df[signal_data_df.columns.str.contains('emg')]
    """
    graficar_medida1(signal_data_emg_df,
                     columnas = signal_data_emg_df.columns,
                     titulo = "Grafico canales EMG",
                     etiqueta_x="n",
                     etiqueta_y="Amplitud")
    """
    print()
    # print(signal_data_emg_df.head())
    print(signal_data_emg_df.iloc[:,0])
    # emg0_filter = butter_lowpass_filter(signal_data_emg_df.iloc[:,0])
    # print()
    # print(emg0_filter)
    signal_data_emg_df_filter = apply_filter_to_dataframe(signal_data_emg_df)
    print(signal_data_emg_df_filter.head())

    # Ejemplo de uso
    w_size = 30  # Tamaño de la ventana
    overlap = 0.33  # 50% de solapamiento

    # Segmentacion vieja
    # ventanas = segment_signal(signal_data_emg_df.iloc[:,0], window_size = w_size, overlap = overlap)
    # print(f"Se generaron {len(ventanas)} ventanas de tamaño 30 con 33% de solapamiento.")
    # print(ventanas[0])
    # print(ventanas[1])
    # Segmentacion vieja 2
    # _,index_ventanas = segment_signal2(signal_data_emg_df.iloc[:,0], window_size = w_size, overlap = overlap)
    # print(index_ventanas)
    # Segmentacion nueva
    ventanas = segment_signal_as_matrix(signal_data_emg_df.iloc[:,0], window_size = w_size, overlap = overlap)
    print(f"Se generaron {len(ventanas)} ventanas de tamaño 30 con 33% de solapamiento.")
    print(f"Tamaño de la matriz: {ventanas.shape}")






    
