"""
This scripts takes the grey-scale image and apply rooling ball algorithm to subtract backgound

The details and examples are in https://scikit-image.org/docs/stable/auto_examples/segmentation/plot_rolling_ball.html

The rolling ball algorithm only works on grey-scale images
1. invert the image because the image has bright background
2. rolling ball
3. invert the result

Prerequisite: 
$ pip install pandas
$ pip install scikit-image

To use this script, in terminal 
$ python 02-rooling_ball.py list_images.csv

For example
$ python 02-rolling_ball.py mapping_files/00-list_images-B2-green.csv

"""

import os
import sys
import pandas as pd
import imageio
import skimage
from skimage import data, restoration, util, io, color

list_images = pd.read_csv(str(sys.argv[1]))

def rolling_ball_light(image):
    # invert the image
    image_inverted = util.invert(image)
    
    # rolling ball
    background_inverted = restoration.rolling_ball(image_inverted, radius = 110, num_threads = 10)
    
    # invert the result
    image_rolled_inverted = image_inverted - background_inverted
    image_rolled = util.invert(image_rolled_inverted)
    return image_rolled

for i in range(list_images.shape[0]):
    image_name = str(list_images.iloc[i]['image_name'])  
    color_channel = str(list_images.iloc[i]['color_channel']) 

    image_path = os.path.join(list_images.iloc[i]['folder_channel'], color_channel, image_name + '.tiff')
    image = io.imread(image_path)
    image_rolled = rolling_ball_light(image)
    io.imsave(list_images.iloc[i]['folder_rolled'] + color_channel + "/" + image_name + '.tiff', image_rolled)
    print(color_channel + " channel rolled\t" + str(i+1) + "/" + str(list_images.shape[0]) + "\t" + image_name)
    
    




