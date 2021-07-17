# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 21:30:33 2020

@author: matheus
"""
import pandas as pd
import numpy as np


Mega = pd.read_csv("C:/Users/matheus/Documents/dados/megasena/sorteios.csv", ",")

Dezenas = pd.DataFrame(Mega['1ª Dezena'].tolist() + Mega['2ª Dezena'].tolist() + Mega['3ª Dezena'].tolist() + Mega['4ª Dezena'].tolist() + Mega['5ª Dezena'].tolist() + Mega['6ª Dezena'].tolist(), columns=['numeros'])
Dezenas['numeros'].value_counts().sort_values(ascending=False).head(60).plot(kind='barh', title='Dezenas mais sorteadas', figsize=(10,5), fontsize=12, legend=True, color='gray')

