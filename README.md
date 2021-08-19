# Code for replicating ERA5 analysis for Stroeve et al., 'Rain on Snow Understudied in Sea Ice Remote Sensing'

Analysis of the precipitation at Polarstern in September 2020 can be (and was) done locally on a machine. The data can be downloaded using download_ERA_ROS.ipynb, and then animated and analysed with Animate_ERA5_ROS_event.ipynb

Analysis of the annual ROS in the Central Arctic 1979-2020 must be done in the cloud unless you have a cluster etc. I did this with the Copernicus CDS toolbox: https://cds.climate.copernicus.eu/#!/home

The code required to perform the first part of the analysis with the toolbox can be found in ros_for_loop.py. The code runs in six-year chunks to avoid arrays that are too massive to handle. At the end of the analysis all the chunks are concatenated together for download.

The post-processing (masking out the CA, the spatial average and plotting the data) is done locally with Analyse_ERA5_trends.ipynb

To generate the figure in the supplement of the paper, the outputs of Analyse_ERA5_trends.ipynb and Animate_ERA5_ROS_event.ipynb are both saved as pickle files in the pickle directory.
The notebook make_combined_fig.ipynb reads these pickle files and makes the combined plot. 

cmaps.py generates the custom colorbar for the animation and the ptype axis for Figure S3 b.
