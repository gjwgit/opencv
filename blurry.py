# -*- coding: utf-8 -*-

# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
# Author: Graham.Williams@microsoft.com
#
# This demo is inspired by Adrian Rosebrock's post on 7 September 2015
# in Image Processing Tutorials:
# https://www.pyimagesearch.com/2015/09/07/blur-detection-with-opencv/

import os
import argparse
import cv2

import numpy as np

from imutils import paths
from mlhub.pkg import is_url
from mlhub.utils import get_cmd_cwd
from urllib.request import Request, urlopen

def variance_of_laplacian(image):
    # Compute the Laplacian of the image and then return the focus
    # measure as the variance of the Laplacian. TODO - don't really
    # need a function?
    return cv2.Laplacian(image, cv2.CV_64F).var()
 
# ----------------------------------------------------------------------
# Parse command line arguments
# ----------------------------------------------------------------------

option_parser = argparse.ArgumentParser(add_help=False)

option_parser.add_argument(
    'path',
    help='path or url to image')

args = option_parser.parse_args()

# ----------------------------------------------------------------------
# URL or path
# ----------------------------------------------------------------------

path = args.path

# ----------------------------------------------------------------------
# Defaults - should be set and changable by argparse - TODO
# ----------------------------------------------------------------------

threshold = 100

# Load the image, convert it to grayscale, and compute the focus
# measure of the image.

if is_url(path):
    req = Request(path, headers={'User-Agent' : "Magic Browser"}) 
    con = urlopen(req)
    img = np.asarray(bytearray(con.read()), dtype="uint8")
    img = cv2.imdecode(img, cv2.IMREAD_COLOR)
else:    
    path = os.path.join(get_cmd_cwd(), path)
    with open(path, 'rb') as fstream:
        img = cv2.imread(path)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
fm = variance_of_laplacian(gray)

# If the focus measure is less than the supplied threshold, then the
# image is considered "blurry".

if fm < threshold:
    text = "Blurry"
else:
    text = "Okay"
 
print("{} {}".format(text, int(round(fm))))
    
