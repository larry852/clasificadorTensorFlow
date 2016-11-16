import pandas as pd
import numpy as np
from sklearn import tree

#importando desde csv (resultado es un DataFrame)
df = pd.read_csv('winequality-red.csv', ';')
#se eextrae la etiqueta de la calidad y se convierte en arreglo, la cual esta en un rango de 0-10
targets = np.array(df['quality'])
#se extraen las caracateristicas a tener en cuneta, y se convierte a matriz
features = np.array(df[['fixed acidity','pH','alcohol']])

#imprimiendo caracteristicas y etiquetas para verficiar
#print features
#print targets

#creando clasificado (fue con el que mas resultados exactos daban)
my_classifier = tree.DecisionTreeClassifier()
#entrenado clasificador
my_classifier.fit(features,targets)

#obteniendo predcicion
def predict(acidez, ph, alcohol):
	predict = my_classifier.predict([[8.9,3.38,10.5]])
	#prediciendo en el clasificador a partir del archivo .csv que se lee (cambiar esos valores estaticos por lo que entra de la interfaz y retornar el resultado que se predice)
	return 'Calidad del vino: ' + str(predict)
