#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 23 22:20:59 2023

@author: s
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Oct  9 12:53:45 2023

@author: baniyaghoubm
"""
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Load the Iris dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
iris_data = pd.read_csv(url)

a=[]

for i in range(0,30):
    a.append(i)
for i in range(50,70):
    a.append(i)
for i in range(100,140):
    a.append(i)
    
print(a)

iris_subsets = iris_data.loc[a]
setosa_sub = iris_data.loc[0:29]
versicolor_sub = iris_data.loc[50:69]
virginica_sub = iris_data.loc[100:139]

# Scatter Plot: Sepal Width vs. Sepal Length
plt.figure(figsize=(8, 6))
plt.scatter(setosa_sub["sepal_length"], setosa_sub["sepal_width"],color='red',alpha=1)
plt.scatter(versicolor_sub["sepal_length"], versicolor_sub["sepal_width"],color='red',alpha=0.7)
plt.scatter(virginica_sub["sepal_length"], virginica_sub["sepal_width"],color='red',alpha=0.4)
plt.title("Sepal Width vs Sepal Length",fontsize=13)
plt.xlabel("Sepal Length [cm]",fontsize=13)
plt.ylabel("Sepal Width [cm]",fontsize=13)
plt.legend(loc='best')
plt.grid(True)
plt.show()

# Line Chart: Petal Length over Species ID
plt.figure(figsize=(8, 6))
species_ids = range(len(iris_subsets))
plt.plot(a[0:30], setosa_sub["petal_length"],color='red',alpha=1)
plt.plot(a[30:50], versicolor_sub["petal_length"],color='red',alpha=0.7)
plt.plot(a[50:90], virginica_sub["petal_length"],color='red',alpha=0.4)
plt.title("Petal Length over Species ID",fontsize=13)
plt.xlabel("Species ID",fontsize=13)
plt.ylabel("Petal Length [cm]",fontsize=13)
plt.grid(True)
plt.show()

# Bar Chart: Species Distribution
species_counts = iris_subsets["species"].value_counts()
plt.figure(figsize=(8, 6))
plt.bar(species_counts.index[0], species_counts.values[0],color='red',alpha=1)
plt.bar(species_counts.index[1], species_counts.values[1],color='red',alpha=0.7)
plt.bar(species_counts.index[2], species_counts.values[2],color='red',alpha=0.4)
plt.title("Species Distribution",fontsize=13)
plt.xlabel("Species",fontsize=13)
plt.ylabel("Number of Samples",fontsize=13)
plt.grid(axis='y')
plt.show()

# Pie Chart: Species Distribution as a percentage
plt.figure(figsize=(8, 6))
p=plt.pie(species_counts, labels=species_counts.index, autopct='%1.1f%%',colors='r')
p[0][1].set_alpha(0.7)
p[0][2].set_alpha(0.4)
plt.title("Species Distribution [%]",fontsize=13)
plt.show()

# 3D Scatter Plot: 3D visualization of sepal length, sepal width, and petal length
fig = plt.figure(figsize=(10, 14))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(setosa_sub["sepal_length"], setosa_sub["sepal_width"], setosa_sub["petal_length"],color='red',alpha=1)
ax.scatter(versicolor_sub["sepal_length"], versicolor_sub["sepal_width"], versicolor_sub["petal_length"],color='red',alpha=0.7)
ax.scatter(virginica_sub["sepal_length"], virginica_sub["sepal_width"], virginica_sub["petal_length"],color='red',alpha=0.4)
ax.set_xlabel("Sepal Length [cm]",fontsize=13)
ax.set_ylabel("Sepal Width [cm]",fontsize=13)
ax.set_zlabel("Petal Length [cm]",fontsize=13)
ax.set_title("Petal Length by Sepal Width and Sepal Length",fontsize=14)
ax.dist = 11
plt.show()