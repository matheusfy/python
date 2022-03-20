from numpy.lib.type_check import imag


max_iter = 1000
images = []
for iter in range(max_iter):
    zeros = [0]*(len(str(max_iter))-len(str(iter)))
    img_name = 'image_'+''.join(str(item) for item in zeros)+str(iter)+'.png'
    images.append(img_name)

for i in images:
    print(i)