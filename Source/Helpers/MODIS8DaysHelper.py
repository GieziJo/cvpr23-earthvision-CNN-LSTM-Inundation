import numpy as np
import rasterio

bandNames = ["sur_refl_b01", "sur_refl_b02", "sur_refl_b03", "sur_refl_b04", "sur_refl_b05", "sur_refl_b06", "sur_refl_b07", "QA", "SolarZenith", "ViewZenith", "RelativeAzimuth", "StateQA", "DayOfYear"]
ranges = [[-100, 16000],[-100, 16000],[-100, 16000],[-100, 16000],[-100, 16000],[-100, 16000],[-100, 16000],[],[],[],[],[],[]]

def getBandNumbers(names):
    return [bandNames.index(entry) for entry in names]

def getBandNumber(name):
    return bandNames.index(name)

def convertToRasterioNumbers(numbers):
    return [number + 1 for number in numbers]

def getBandRange(name):
    return ranges[getBandNumber(name)]
def getBandRanges(names):
    return [ranges[i] for i in getBandNumbers(names)]

def getByteImage(image, dataRange):
    return np.interp(image, dataRange, (0, 255)).astype(np.uint8)

def getScaledImage(image, dataRange):
    return np.interp(image, dataRange, (0.0, 1.0))

def getModisFileBandsAsUInt8Matrix(modisFile, bandNames):
    banNumbers = getBandNumbers(bandNames)
    with rasterio.open(modisFile) as modisImage:
        bandValues = modisImage.read(convertToRasterioNumbers(banNumbers))
        bandRanges = getBandRanges(bandNames)
        bOut = np.zeros(bandValues.shape).astype(np.uint8)
        for i in range(len(bandRanges)):
            bOut[i,:] = getByteImage(bandValues[i,:], bandRanges[i])
        return bOut

def getScaledModisFileBands(modisFile, bandNames):
    banNumbers = getBandNumbers(bandNames)
    with rasterio.open(modisFile) as modisImage:
        bandValues = modisImage.read(convertToRasterioNumbers(banNumbers))
        bandRanges = getBandRanges(bandNames)
        bOut = np.zeros(bandValues.shape)
        for i in range(len(bandRanges)):
            bOut[i,:] = getScaledImage(bandValues[i,:], bandRanges[i])
    return bOut

def getScaledModisFileBandsWithOpenRaster(modisRasterImage, bandNames):
    banNumbers = getBandNumbers(bandNames)
    bandValues = modisRasterImage.read(convertToRasterioNumbers(banNumbers))
    bandRanges = getBandRanges(bandNames)
    bOut = np.zeros(bandValues.shape)
    for i in range(len(bandRanges)):
        bOut[i,:] = getScaledImage(bandValues[i,:], bandRanges[i])
    return bOut

def getModisFileBands(modisFile, bandNames):
    banNumbers = getBandNumbers(bandNames)
    with rasterio.open(modisFile) as modisImage:
        return modisImage.read(convertToRasterioNumbers(banNumbers))

def getModisFileBandsWithOpenRaster(modisRasterImage, bandNames):
    banNumbers = getBandNumbers(bandNames)
    return modisRasterImage.read(convertToRasterioNumbers(banNumbers))
