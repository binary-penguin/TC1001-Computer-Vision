import matplotlib.pyplot as plt
import numpy
from PIL import Image
from scipy import ndimage

from kernels import *

if __name__ == "__main__":
    Is = Image.open('images/Sample.png');
    I = Is.convert('L');
    I = numpy.asarray(I);
    I = I / 255.0;

    k0 = vh()
    k1 = horizontal()
    k2 = vertical()
    k3 = mexican_hat(3)

    J0 = ndimage.convolve(I, k0, mode='constant', cval=0.0)
    J1 = ndimage.convolve(I, k1, mode='constant', cval=0.0)
    J2 = ndimage.convolve(I, k2, mode='constant', cval=0.0)
    J3 = ndimage.convolve(I, k2, mode='constant', cval=0.0)

    plt.figure(figsize = (15,15))

    plt.subplot(3,3,1)
    plt.imshow(Is)
    plt.xlabel('Input Image')

    plt.subplot(3,3,2)
    plt.imshow(J0)
    plt.xlabel('VH direction')

    plt.subplot(3,3,3)
    plt.imshow(J1)
    plt.xlabel('Horizontal direction')

    plt.subplot(3,3,4)
    plt.imshow(J2)
    plt.xlabel('Vertical direction')

    plt.subplot(3,3,5)
    plt.imshow(J3)
    plt.xlabel('Mexican Hat')


    plt.grid(False)
    plt.show()
