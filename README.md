# Proyecto de Data Science

Este proyecto sigue una estructura modular para facilitar el análisis de datos, entrenamiento de modelos y generación de informes.

## Estructura:

- `data/`: almacena los datos en bruto y procesados.
- `notebooks/`: notebooks de análisis exploratorio y modelado.
- `src/`: scripts de código reutilizable.
- `tests/`: pruebas automáticas.
- `reports/`: figuras e informes generados.

## Cómo empezar:
1. Crea un entorno virtual:
2. 
   ```bash
   python -m venv env
   source env/bin/activate
   ```

3. Instala dependencias:
   
   ```bash
   pip install -r requirements.txt
   ```

4. Ejecuta notebooks desde `notebooks/`

5. Usa los scripts de `src/` para modularizar tus notebooks


## PDS

* https://cookiecutter-data-science.drivendata.org/

```
mi_proyecto_ds/
│
├── data/                     # Datos en bruto, procesados y externos
│   ├── raw/                  # Datos originales, sin modificar
│   ├── processed/            # Datos limpios y listos para análisis
│   └── external/             # Datos de terceros
│
├── notebooks/                # Notebooks exploratorios y finales
│   ├── 01_exploracion.ipynb
│   └── 02_modelo.ipynb
│
├── src/                      # Código fuente (procesamiento, modelos, utils)
│   ├── __init__.py
│   ├── features/             # Extracción y transformación de datos
│   │   └── build_features.py
│   ├── models/               # Entrenamiento y predicción
│   │   └── train_model.py
│   └── visualization/        # Gráficas y visualización
│       └── visualize.py
│
├── tests/                    # Pruebas unitarias
│   └── test_build_features.py
│
├── reports/                  # Reportes generados (PDF, HTML, etc.)
│   ├── figures/
│   └── informe_final.pdf
│
├── docs/                     # Documentación formal (con Sphinx si deseas)
│   ├── index.rst
│   └── ...
│
├── requirements.txt          # Dependencias
├── environment.yml           # Alternativa para usar con Conda
├── README.md                 # Descripción general del proyecto
├── .gitignore
└── main.py                   # Entrada para pipelines automáticos (opcional)
```

### Buenas practicas

* No pongas datos grandes en Git: usa .gitignore para omitir data/raw/.
* Versiona tus notebooks con nombres como 01_nombre_tema.ipynb, 02_....
* Exporta funciones importantes a src/ para mantener notebooks limpios.
* Separa código de entrenamiento, predicción, visualización y limpieza.
* Documenta tu código y usa README.md para explicar el flujo general.
* Usa requirements.txt o environment.yml para compartir el entorno.

## Referencias

* https://drivendata.co/open-source.html
* https://cookiecutter-data-science.drivendata.org/contributing/