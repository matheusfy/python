# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 01:11:53 2020

@author: Matheus Yokoyama
"""


import numpy as np
import matplotlib.pyplot as plt
from numpy.core.fromnumeric import size
aux = np.load("objeto/objeto.npy")
reconhecidos = aux
#reconhecidos[:] = reconhecidos[:][:,:,::-1]

embedded_TSNE = np.load("objeto/embedded.npy")
rotulo = np.load("objeto/label.npy")
#teste = aux[0][:,:,::-1]
plt.imshow(reconhecidos[0])
#print(reconhecidos)

#%%


from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import numpy as np; np.random.seed(42)

# Generate data x, y for scatter and an array of images.


# create figure and plot scatter
fig = plt.figure()
ax = fig.add_subplot(111)

line, = ax.plot(embedded_TSNE[:,0], embedded_TSNE[:,1], ls="", marker="x",)


# create the annotations box
im = OffsetImage(reconhecidos[0,:,:], zoom=1, cmap = "gray")

xybox=(50., 50.)

ab = AnnotationBbox(im, (0,0), xybox=xybox, xycoords='data',
        boxcoords="offset points",  pad=0.2,  arrowprops=dict(arrowstyle="->"))
# add it to the axes and make it invisible
ax.add_artist(ab)
ab.set_visible(False)

def hover(event):
    # if the mouse is over the scatter points
    if line.contains(event)[0]:
        # find out the index within the array from the event
        ind, = line.contains(event)[1]["ind"]
        # get the figure size
        w,h = fig.get_size_inches()*fig.dpi
        ws = (event.x > w/2.)*-1 + (event.x <= w/2.) 
        hs = (event.y > h/2.)*-1 + (event.y <= h/2.)
        # if event occurs in the top or right quadrant of the figure,
        # change the annotation box position relative to mouse.
        ab.xybox = (xybox[0]*ws, xybox[1]*hs)
        # make annotation box visible
        ab.set_visible(True)
        # place it at the position of the hovered scatter point
        ab.xy =(embedded_TSNE[:,0][ind], embedded_TSNE[:,1][ind])
        # set the image corresponding to that point
        im.set_data(reconhecidos[ind,:,:])
    else:
        #if the mouse is not over a scatter point
        ab.set_visible(False)
    fig.canvas.draw_idle()

# add callback for mouse moves
fig.canvas.mpl_connect('motion_notify_event', hover)           
plt.show()

#%%

plt.figure()
 
plt.scatter(embedded_TSNE[:,0], embedded_TSNE[:,1], marker = 'o', size= 0.5, s = 2, c= rotulo[:])

plt.show()

#%%

plt.imshow(reconhecidos[0,:,:],cmap="gray")


