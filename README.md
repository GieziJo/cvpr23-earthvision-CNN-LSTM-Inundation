> :warning: Repo is being built, should be updated with the code and data soon

This repo contains the code and data to reproduce the work published in the paper "**Giezendanner et al.** , *Inferring the past: a combined CNN--LSTM deep learning framework to fuse satellites for historical inundation mapping*, CVPR 23 Earthvision workshop", as well as the inferred dataset.

# Inferred dataset (Fractional Inundated Area for Bangladesh, 2001-2022, 500 meters resolution, every 8 days)

The model output dataset contains 985 `.tiff` files covering most of Bangladesh every 8 days, at 500 meters resolution, from 2001 to 2022.
The dataset can be found at [10.25739/2edm-jh03](https://datacommons.cyverse.org/browse/iplant/home/shared/commons_repo/curated/Giezendanner_BangladeshInundationHistory_Mai2023).


# Model and data
## Data
The data can either be re-generated using the code available in `Source/0_DataGeneration/`, or it will be made available to download as a ready made package soon.

The following data is generated/available:
- Fractional inundated area generated from Sentinel-1 binary map
- MODIS Terra 8-days composite
- DEM and slope derived from FABDEM upscaled to 500 meters
- HAND upscaled to 500 meters

The data is expressed in 32x32 500 meter resolution chips.

## Code
The code is organised as follow:
- `Source/0_DataGeneration` contains the code to generate the data.
- `Source/1_ModelTraining` contains the code to train and cross-validate the model.
- `Source/2_Inference` contains the code to run inference on the trained model.

Both the code for the model baseline (CNN) and the CNN-LSTM proposed in the paper, as well as the trained weights are provided.
