# Makefile
# Comandos automáticos para flujo de trabajo
data:
	python src/features/build_features.py

train:
	python src/models/train_model.py

notebook:
	jupyter notebook notebooks/

docs:
	cd docs && make html

mlflow:
	mlflow ui

dvc:
	dvc status
