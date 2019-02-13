#Diego Alexander Chávez Ramírez
#Import library
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew

#Read file 
data = pd.read_csv('Mall_Customers_Diego_Chavez.csv')
#Drop Variable de clase 
data = data.drop('CustomerID', 1)
#Group data by Gender
grouped_data = data.groupby('Gender')
print("\nDatos Estadísticos:")

#Print media 
print("\nMedia:")
print(grouped_data.mean())

#Print Mediana
print("\nMediana:")
print(grouped_data.median())

#Separate gender Male and print moda
print("\nModa")
datos_m = data.loc[data['Gender'] == "Male"]
print("Moda Age Male")
print(datos_m["Age"].mode())
print("Moda Annual Income(k$) Male")
print(datos_m["AnnualIncome(k$)"].mode())
print("Moda Spending Score (1-100) Male")
print(datos_m["SpendingScore(1-100)"].mode())

#Separate gender Female and print Moda
datos_f = data.loc[data['Gender'] == "Female"]
print("Moda Age Female")
print(datos_f["Age"].mode())
print("Moda Annual Income(k$) Female")
print(datos_f["AnnualIncome(k$)"].mode())
print("Moda Spending Score (1-100) Female")
print(datos_f["SpendingScore(1-100)"].mode())

#Print Cuartiles
print("\nCuartiles:")
print(data.quantile([.25, .50, .75]))

#Print Mínimos
print("\nMínimos:")
print(grouped_data.min())

#Print Máximos
print("\nMáximos:")
print(grouped_data.max())

#Print Varianza
print("\nVarianza - Male:")
print(datos_m.var())
print("Varianza - Female:")
print(datos_f.var())

#Print Desviación estándar

print("\nDesviación Estándar - Male:")
print(datos_m.std())
print("\nDesviación Estándar - Female:")
print(datos_f.std())

#Make Age Histrogram 

plt.subplot(2, 2, 1)
plt.title('Age Histogram')
tab = pd.crosstab(index=data["Age"],columns="frecuency")
plt.bar(tab.index,tab["frecuency"])
plt.savefig("Age histogram.png")
tab1 = pd.crosstab(index=data["AnnualIncome(k$)"],columns="frecuency")

#Make Annual Income Histogram

plt.subplot(2, 2, 2)
plt.title('\n Annual Income Histrogram')
tab2 = pd.crosstab(index=data["AnnualIncome(k$)"], columns="frecuency")
plt.bar(tab1.index,tab1["frecuency"])
plt.savefig("Annual Income.png")

#Make Spending Score Histogram
plt.subplot(2, 2, 3)
plt.title('\n\n\nSpending Score Histogram')
tab3 = pd.crosstab(index=data["SpendingScore(1-100)"],columns="frecuency")
plt.bar(tab2.index,tab2["frecuency"])
plt.savefig("SpendingScor.png")

#Print Curtosis 

print("\nCurtosis")
print(data.kurt())

#Print Matriz de correlación
print("\nMatriz de correlación")
print(data.corr())

#Print Matriz de covarianza
print("\nMatriz de Covarianza")
print(data.cov())

#Assign values
print("\nAsimetría")
symAge = skew(data["Age"])
symAni = skew(data["AnnualIncome(k$)"])
symSs = skew(data["SpendingScore(1-100)"])

#Print Simmetry 
print(symAge)
print(symAni)
print(symSs)
