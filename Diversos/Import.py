# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 20:49:53 2020

@author: matheus
"""
#from PIL import Image
import os
from matplotlib import image
from skimage import io, transform

#from numpy import asarray
import numpy as np
Arquivo = 'C:/Users/matheus/Documents/dados/indoorCVPR_09/Images/artstudio/art_painting_studio_01_10_altavista.jpg'
#im = Image.open(Arquivo)
#im = im.resize((180,180))

#data = asarray(im)
# C:Users\matheus\Documents\dados\indoorCVPR_09\Images

pasta = 'C:/Users/matheus/Documents/dados/indoorCVPR_09/Images'
print(os.listdir(pasta))
#%%
def load_images_from_folder(folder):
    
    image_carregada = []
    label = []
    i = 0
    for filename in os.listdir(folder):
    
        caminho = folder + '/' + filename
        
        for arquivo in os.listdir(caminho):
            data = caminho + '/' + arquivo
            img_data = io.imread(data)
            img_data = transform.resize(img_data, (180,180,3))
            image_carregada.append(img_data)
            label.append(i)
        i+=1
    
    return image_carregada, label


#%%

image_carregada, rotulo = load_images_from_folder(pasta)
#lista = load_images_from_folder(pasta)

image_carregada = np.array(image_carregada)   
rotulo = np.array(rotulo)
#%%
    
import matplotlib.pyplot as plt

plt.imshow(image_carregada[0])
