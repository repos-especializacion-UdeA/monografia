# src/models/train_model.py
from sklearn.linear_model import LinearRegression

def entrenar_modelo(X, y):
    """
    Entrena un modelo de regresión lineal.

    Args:
        X (pd.DataFrame): Variables independientes.
        y (pd.Series): Variable dependiente.

    Returns:
        LinearRegression: Modelo entrenado.
    """
    modelo = LinearRegression()
    modelo.fit(X, y)
    return modelo

