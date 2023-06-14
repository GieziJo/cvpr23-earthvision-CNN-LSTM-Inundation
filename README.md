This repo contains the code and data to reproduce the work published in the paper ["**Giezendanner et al.** , *Inferring the past: a combined CNN--LSTM deep learning framework to fuse satellites for historical inundation mapping*, CVPR 23 Earthvision workshop"](https://openaccess.thecvf.com/content/CVPR2023W/EarthVision/html/Giezendanner_Inferring_the_Past_A_Combined_CNN-LSTM_Deep_Learning_Framework_To_CVPRW_2023_paper.html), as well as the inferred dataset.

Use the following citation when these data or model are used:
> Giezendanner, J.; Mukherjee, R.; Purri, M.; Thomas, M.; Mauerman, M.; Islam, A. K. M. S.; Tellman, B. Inferring the Past: A Combined CNN-LSTM Deep Learning Framework to Fuse Satellites for Historical Inundation Mapping. Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition (CVPR) Workshops, June, 2023. https://openaccess.thecvf.com/content/CVPR2023W/EarthVision/html/Giezendanner_Inferring_the_Past_A_Combined_CNN-LSTM_Deep_Learning_Framework_To_CVPRW_2023_paper.html

# Inferred dataset
## Fractional Inundated Area for Bangladesh, 2001-2022, 500 meters resolution, every 8 days

The model output dataset contains 985 `.tiff` files covering most of Bangladesh every 8 days, at 500 meters resolution, from 2001 to 2022.
The dataset can be found at [10.25739/2edm-jh03](https://datacommons.cyverse.org/browse/iplant/home/shared/commons_repo/curated/Giezendanner_BangladeshInundationHistory_Mai2023).


# Model and data
## Data

The data for training (cross-validation) and inference can be downloaded [here](https://data.cyverse.org/dav-anon/iplant/home/jgiezendanner/CVPR23Data)

The following data is available:
- Fractional inundated area generated from [Sentinel-1 binary map](https://ieeexplore.ieee.org/document/10042166)
- MODIS Terra 8-days composite
- DEM and slope derived from [FABDEM](https://meetingorganizer.copernicus.org/EGU22/EGU22-8994.html?pdf) upscaled to 500 meters
- HAND upscaled to 500 meters ([MERIT Hydro](https://agupubs.onlinelibrary.wiley.com/doi/10.1029/2019WR024873))

The data is expressed in 32x32 500 meter resolution chips.

## Code
The code is organised as follow:
- `Source/0_ModelTraining` contains the code to train and cross-validate the model.
- `Source/1_Inference` contains the code to run inference on the trained model.
- `Source/Helpers` contains diverse helper functions
- `Source/ModelClasses` contains the classes of the model

Both the code for the CNN-LSTM proposed in the paper, as well as the trained weights (see [release](https://github.com/GieziJo/cvpr23-earthvision-CNN-LSTM-Inundation/releases/tag/v1.0.0)) are provided.
