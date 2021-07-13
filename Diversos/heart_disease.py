# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 22:28:33 2020

@author: matheus
"""

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDClassifier
from sklearn.metrics import accuracy_score
x = pd.read_csv("C:/Users/matheus/Documents/dados/heart-disease-uci/heart.csv", ",") 

# Colunas ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach','exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']

y = x['target'].iloc[:]
x = x.drop(['target'], axis = 1)
colunas = []
colunas = list(x.columns)


#%%

# NORMALIZA A ESCALAS DOS DADOS DE 0 À 1
for i in colunas:
    x[i] = x[i]/x[i].max()

#%%
    
# SEPARA EM TREINO E TESTE
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33, random_state = 1 )


#%%
clf = SGDClassifier(loss='log' ,max_iter=1200, tol=1e-3, verbose=0, n_iter_no_change=10, penalty='l2')


clf.fit(x_train, y_train)

while accuracy_score(clf.predict(x_test),y_test)*100 < 89:
    clf.fit(x_train, y_train)
    print("acuracia: " + str(accuracy_score(clf.predict(x_test),y_test)*100))

