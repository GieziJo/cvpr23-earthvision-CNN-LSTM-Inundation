import numpy as np
import rasterio

def getScaledImage(image, dataRange):
    return np.interp(image, dataRange, (0.0, 1.0))

def getScaledHAND(file):
    with rasterio.open(file) as image:
        bOut = getScaledImage(image.read(1), [0.0, 7.0])
    return bOut

def getScaledElevation(file):
    with rasterio.open(file) as image:
        bOut = getScaledImage(image.read(1), [0.0, 100.0])
    return bOut

def getSlope(file):
    with rasterio.open(file) as image:
        bOut = image.read(1)
    return bOut
