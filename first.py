import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('./iris.data')
target_variable = 'Class'
explainatory_variables = ['Sepal_length_in_cm', 'Sepal_width_in_cm',
                          'Petal_length_in_cm','Petal_width_in_cm']
['Iris-setosa', 'Iris-versicolor', 'Iris-virginica']

data_s = data[data['Class']=='Iris-setosa']
data_ve = data[data['Class']=='Iris-versicolor']
data_vi = data[data['Class']=='Iris-virginica']

plt.plot(data_s['Sepal_length_in_cm'],data_s['Petal_length_in_cm'],'ro',label='setosa')
plt.plot(data_ve['Sepal_length_in_cm'],data_ve['Petal_length_in_cm'],'bo',label='versicolor')
plt.plot(data_vi['Sepal_length_in_cm'],data_vi['Petal_length_in_cm'],'go',label='virginica')
plt.xlabel('Sepal_length_in_cm')
plt.ylabel('Petal_length_in_cm')
plt.legend()
plt.show()
