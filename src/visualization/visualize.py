# src/visualization/visualize.py
import matplotlib.pyplot as plt

def graficar_histograma(df, columna):
    """
    Grafica un histograma de una columna específica.

    Args:
        df (pd.DataFrame): DataFrame con los datos.
        columna (str): Nombre de la columna a graficar.
    """
    df[columna].hist()
    plt.title(f"Histograma de {columna}")
    plt.xlabel(columna)
    plt.ylabel("Frecuencia")
    plt.show()
