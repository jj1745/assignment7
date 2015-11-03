'''
Created on Nov 2, 2015

@author: jj1745
'''

import numpy as np
import matplotlib.pyplot as plt

# Construc the grid
interval = 1000

x_axis = np.linspace(-2, 1, interval)
y_axis = np.linspace(-1.5, 1.5, interval)

x,y = np.meshgrid(x_axis,y_axis)

# Do the iteration
N_max = 50
some_threshold = 50

c = x + 1j*y

z = c
for v in range(N_max):
    z = z**2 + c
    
# Form the 2-D boolean mask
mask = (np.abs(z) < some_threshold)
plt.imshow(mask, extent = [-2,1,-1.5,1.5])
plt.gray()
plt.savefig('mandelbrot.png')