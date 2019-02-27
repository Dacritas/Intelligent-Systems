#Diego Alexander Chávez Ramírez & Jimmy Riaño Barrueto
#Import library
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import export_graphviz
from sklearn.preprocessing import StandardScaler
import pydot

#Read file 
data = pd.read_csv('FinancialDistress_Resumido.csv')
#Se borra variable Company
data.drop(['Company'], axis=1, inplace=True)
y = data['State']
x = data.drop(['State'], axis=1)

#Matriz de correlaciones, valores absolutos
corr_matrix = data.corr().abs()
print(corr_matrix)
#data  = data.drop('x80', 1)
#data  = data.drop('x82', 1)
#data  = data.drop('x83', 1)
datadumi = pd.get_dummies(data)
print(datadumi.iloc[:,5:].head(5))
labels = np.array(datadumi['State_HEALHTY'])
#print(labels)
datadumi = datadumi.drop('State_HEALHTY', axis = 1)
datadumi_list = list(datadumi.columns)
#print(datadumi_list)
datadumi = np.array(datadumi)
from sklearn.model_selection import train_test_split
train_features, test_features, train_labels, test_labels = train_test_split(datadumi, labels, test_size = 0.25, random_state = 52)
print('Training Features Shape:', train_features.shape)
print('Training Labels Shape:', train_labels.shape)
print('Testing Features Shape:', test_features.shape)
print('Testing Labels Shape:', test_labels.shape)
baseline_preds = test_features[:, datadumi_list.index('State_DISTRESS')]
baseline_errors = abs(baseline_preds - test_labels)
print('Average baseline error: ', round(np.mean(baseline_errors), 2))
rf = RandomForestRegressor(n_estimators = 1000, random_state = 42)
rf.fit(train_features, train_labels)
predictions = rf.predict(test_features)
errors = abs(predictions - test_labels)
print('Mean Absolute Error:', round(np.mean(errors), 2), 'degrees.')

x = StandardScaler().fit_transform(x)
print("\nConjunto de datos normalizado:\n")
print(x[0:5])

pca = PCA(n_components=4)
principalComponents = pca.fit_transform(x)
principalDf = pd.DataFrame(data = principalComponents, columns = ['PC1', 'PC2','PC3','PC4'])
print("\nComponentes principales:\n")
print(principalDf.head())
