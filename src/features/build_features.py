# src/features/build_features.py
def limpiar_datos(df):
    """
    Limpia un DataFrame eliminando duplicados y valores nulos.

    Args:
        df (pd.DataFrame): DataFrame original.

    Returns:
        pd.DataFrame: DataFrame limpio.
    """
    df = df.drop_duplicates()
    df = df.dropna()
    return df

