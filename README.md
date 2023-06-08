> :warning: Repo is being built, should be updated with the code and data soon

This repo contains the code and data to reproduce the work published in the paper ["**Giezendanner et al.** , *Inferring the past: a combined CNN--LSTM deep learning framework to fuse satellites for historical inundation mapping*, CVPR 23 Earthvision workshop"](https://openaccess.thecvf.com/content/CVPR2023W/EarthVision/html/Giezendanner_Inferring_the_Past_A_Combined_CNN-LSTM_Deep_Learning_Framework_To_CVPRW_2023_paper.html), as well as the inferred dataset.

Use the following citation when these data or model are used:
> Giezendanner, J.; Mukherjee, R.; Purri, M.; Thomas, M.; Mauerman, M.; Islam, A. K. M. S.; Tellman, B. Inferring the Past: A Combined CNN-LSTM Deep Learning Framework to Fuse Satellites for Historical Inundation Mapping. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops, June, 2023. https://openaccess.thecvf.com/content/CVPR2023W/EarthVision/html/Giezendanner_Inferring_the_Past_A_Combined_CNN-LSTM_Deep_Learning_Framework_To_CVPRW_2023_paper.html

# Inferred dataset
## Fractional Inundated Area for Bangladesh, 2001-2022, 500 meters resolution, every 8 days

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
