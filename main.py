import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage

from kernels import *

if __name__ == "__main__":
    Is = Image.open('images/Sample.jpg');
    I = Is.convert('L');
    I = numpy.asarray(I);
    I = I / 255.0;

    k0 = mexican_hat(9)
    k1 = gaussian(21)
    k2 = sharpen()

    J0 = ndimage.convolve(I, k0, mode='constant', cval=0.0)
    J1 = ndimage.convolve(I, k1, mode='constant', cval=0.0)
    J2 = ndimage.convolve(I, k2, mode='constant', cval=0.0)
    

    plt.figure(figsize = (15,15))

    plt.subplot(2,3,1)
    plt.imshow(Is)
    plt.xlabel('Input Image')

    plt.subplot(2,3,2)
    plt.imshow(J0)
    plt.xlabel('Mexican Hat')

    plt.subplot(2,3,3)
    plt.imshow(J1)
    plt.xlabel('Gaussian blur')

    plt.subplot(2,3,4)
    plt.imshow(J2)
    plt.xlabel('Sharpen')


    plt.grid(False)
    plt.show()
