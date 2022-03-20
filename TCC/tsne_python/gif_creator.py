import os
from PIL import Image, ImageDraw

images = []

for image in os.listdir('images/imgs_n_iter1000/'):
    print(image)    
    im = Image.open('images/imgs_n_iter1000/'+image)
    images.append(im)

images[0].save('mnist_2500_iter_1000.gif',
               save_all=True, append_images=images[1:450:2], optimize=False, duration=20, loop=0)