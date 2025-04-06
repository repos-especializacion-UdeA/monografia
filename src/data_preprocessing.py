import os
import sys
import scipy.io  # Asegúrate de importar scipy.io para cargar archivos .mat
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.io
from scipy import signal
from scipy.signal import butter, filtfilt


# Agregar el directorio raíz del proyecto al PYTHONPATH
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

F_SAMPLING = 100  # Frecuencia de muestreo (Hz)
F_CUTOFF = 1  # Frecuencia de corte (Hz)
BUTT_ORDER = 2  # Orden del filtro Butterworth

####################################################################################################
# Funciones sobre las señales
####################################################################################################


# Numero del estimulo
def num_index(df, num):
  return (df.index[df == num][0],df.index[df == num][-1])

# Cambios de nivel
def detect_level_changes(signal, valor):
    cambios = []
    for i in range(1, len(signal)):
        if signal[i] == valor and signal[i-1] != valor:
            cambios.append((i-1,0))
            cambios.append((i,valor))
        elif signal[i] != valor and signal[i-1] == valor:
            cambios.append((i-1,valor))
            cambios.append((i,0))
    cambios.pop(0)
    cambios.pop()
    return cambios

# Hecho por ChatGPT = Skynet
def segment_signal(signal, window_size, step_size):
    """
    Segmenta una señal en ventanas deslizantes.

    Parámetros:
        signal (array): Señal de entrada.
        window_size (int): Número de muestras por ventana.
        step_size (int): Desplazamiento entre ventanas.

    Retorna:
        list: Lista de arrays con las ventanas segmentadas.
    """
    return [signal[start:start + window_size] 
            for start in range(0, len(signal) - window_size + 1, step_size)]

# Hecho por ChatGPT = Skynet
def normalize_signal(signal):
    """
    Normaliza la señal entre 0 y 1.

    Parámetros:
        signal (array): Señal a normalizar.

    Retorna:
        array: Señal normalizada.
    """
    return (signal - np.min(signal)) / (np.max(signal) - np.min(signal))


def standardize_signal(signal):
    """
    Estandariza la señal a media 0 y desviación estándar 1.

    Parámetros:
        signal (array): Señal a estandarizar.

    Retorna:
        array: Señal estandarizada.
    """
    return (signal - np.mean(signal)) / np.std(signal)


def calculate_rms(signal, window_size, step_size):
    """
    Calcula la raíz cuadrática media (RMS) de una señal en ventanas.

    Parámetros:
        signal (array): Señal de entrada.
        window_size (int): Tamaño de la ventana (en muestras).
        step_size (int): Paso del desplazamiento (en muestras).

    Retorna:
        array: Señal de RMS.
    """
    rms = []
    for start in range(0, len(signal) - window_size + 1, step_size):
        window = signal[start:start + window_size]
        rms.append(np.sqrt(np.mean(window ** 2)))
    return np.array(rms)

def remove_artifacts(signal, threshold=3):
    """
    Elimina artefactos extremos (valores atípicos).

    Parámetros:
        signal (array): Señal de entrada.
        threshold (float): Umbral en desviaciones estándar.

    Retorna:
        array: Señal con artefactos suavizados.
    """
    mean = np.mean(signal)
    std = np.std(signal)
    return np.where(np.abs(signal - mean) > threshold * std, mean, signal)


def interpolate_missing(signal):
    """
    Interpola valores faltantes (NaN) en una señal.

    Parámetros:
        signal (array): Señal con posibles NaNs.

    Retorna:
        array: Señal interpolada.
    """
    return pd.Series(signal).interpolate().to_numpy()


def butter_lowpass_filter(signal, 
                f_sampling = F_SAMPLING, 
                cutoff = F_CUTOFF,
                butterworth_order = BUTT_ORDER):
    """
    Aplica un filtro pasa baja Butterworth a la señal.

    Parámetros:
        signal (array): Señal a filtrar.
        f_sampling (float): Frecuencia de muestreo de la señal (Hz). Por defecto, usa F_SAMPLING.
        cutoff (float): Frecuencia de corte del filtro (Hz). Por defecto, usa F_CUTOFF.
        fs (float): Frecuencia de muestreo (Hz).
        butterworth_order (int): Orden del filtro Butterworth. Por defecto, usa BUTT_ORDER.

    Retorna:
        array: Señal filtrada.
    """

    nyquist = f_sampling/2
    normal_cutoff = cutoff/nyquist
    b, a = butter(butterworth_order, normal_cutoff, btype = 'lowpass')

    return filtfilt(b, a, signal)

def apply_filter_to_dataframe(df, f_sampling = F_SAMPLING, cutoff = F_CUTOFF, butterworth_order = BUTT_ORDER):
    """
    Aplica el filtro pasa-bajos Butterworth a cada columna de un DataFrame.

    Parámetros:
    df (pd.DataFrame): DataFrame cuyas columnas representan señales a filtrar.
    f_sampling (float): Frecuencia de muestreo de las señales (Hz).
    cutoff (float): Frecuencia de corte del filtro (Hz).
    butterworth_order (int): Orden del filtro Butterworth.

    Retorna:
    pd.DataFrame: DataFrame con las señales filtradas.
    """
    return df.apply(lambda col: butter_lowpass_filter(col, f_sampling, cutoff, butterworth_order), axis=0)

def segment_signal(signal, window_size, overlap):
    """
    Segmenta una señal en ventanas con solapamiento.

    Parámetros:
        signal (array): Señal de entrada (1D).
        window_size (int): Tamaño de la ventana en muestras.
        overlap (float): Porcentaje de solapamiento entre ventanas (entre 0 y 1).

    Retorna:
        list: Lista de arrays con las ventanas segmentadas.
    """
    step_size = int(window_size * (1 - overlap))
    if step_size < 1:
        raise ValueError("El solapamiento es demasiado alto. Reduce el valor de 'overlap'.")
    
    segments = []
    for start in range(0, len(signal) - window_size + 1, step_size):
        segments.append(signal[start:start + window_size])
    return segments

# Devuelve indices lo cual es mejor...
def segment_signal2(signal, window_size, overlap):
    """
    Segmenta una señal en ventanas con solapamiento y retorna los índices de inicio.

    Parámetros:
        signal (array): Señal de entrada (1D).
        window_size (int): Tamaño de la ventana en muestras.
        overlap (float): Porcentaje de solapamiento entre ventanas (entre 0 y 1).

    Retorna:
        tuple:
            - list: Lista de arrays con las ventanas segmentadas.
            - list: Lista de índices de inicio de cada ventana.
    """
    if not 0 <= overlap < 1:
        raise ValueError("El solapamiento debe estar entre 0 y 1 (no incluido).")

    step_size = int(window_size * (1 - overlap))
    if step_size < 1:
        raise ValueError("El solapamiento es demasiado alto. Reduce el valor de 'overlap'.")

    segments = []
    start_indices = []

    for start in range(0, len(signal) - window_size + 1, step_size):
        segments.append(signal[start:start + window_size])
        start_indices.append(start)

    return segments, start_indices


def apply_segment_signal_to_dataframe(df, window_size, overlap):
    """
    Aplica la función segment_signal a todas las columnas de un DataFrame.

    Parámetros:
    df (pd.DataFrame): DataFrame cuyas columnas representan señales a segmentar.
    window_size (int): Tamaño de la ventana en muestras.
    overlap (float): Porcentaje de solapamiento entre ventanas (entre 0 y 1).

    Retorna:
    dict: Un diccionario donde las claves son los nombres de las columnas y los valores son listas de segmentos.
    """
    return df.apply(lambda col: segment_signal(col.to_numpy(), window_size, overlap), axis=0).to_dict()


## Hecho por ChatGPT = Skynet
def detrend_signal(signal):
    """
    Elimina tendencias lineales de la señal.

    Parámetros:
        signal (array): Señal a corregir.

    Retorna:
        array: Señal sin tendencia.
    """
    return detrend(signal)