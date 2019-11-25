# -------------------------------------------------------------------------------
# Name:        random image creator
#
# Author:      Wojciech
#
# Created:     25.11.2019
# Copyright:   (c) Wojciech 2019
# Licence:     Za darmo w celach edukacyjnych
# -------------------------------------------------------------------------------

import argparse
import datetime
import os
from random import randint as rint
from random import choice as chc

# set datestamp
now = datetime.datetime.now()

# default value
value = [600, 600, 'output\\', 'img_[ddmmYYYYHHMMSS]_[width]x[height].raw', 'fc']

# arguments
parser = argparse.ArgumentParser()
parser.add_argument("-hh", "--height", type=int, help=f"image's height in pixels (default: {value[0]}px)")
parser.add_argument("-w", "--width", type=int, help=f"image's width in pixels (default: {value[1]}px)")
parser.add_argument("-d", "--directory", type=str, help=f"path to file (default: {value[2]}")
parser.add_argument("-f", "--filename", type=str, help=f"file name (default: {value[3]}")
parser.add_argument("-c", "--colormode", type=str, help=f"mode of color: 'bw' only black nad white., 'fc': full color. {value[4]} is default")

# change template in value[3] on real filename
value[3] = 'img_{:%d%m%Y%H%M%S}_{}x{}.raw'.format(now,value[1],value[0]) 

args = parser.parse_args()

if args.height:
    value[0] = args.height

if args.width:
    value[1] = args.width

if args.directory:
    value[2] = args.directory

if args.filename:
    value[3] = args.filename
    if '.' in args.filename:
        value[3] = value[3][::-1]
        value[3] = value[3][value[3].find('.') + 1:]
        value[3] = value[3][::-1]
    value[3] += '.raw'

if args.colormode:
    value[4] = args.colormode

if not os.path.exists(value[2]):
    os.mkdir(value[2])

pathname = value[2] + value[3]
contets = []
pixel = 0


with open(pathname, 'wb') as fimg:
    for i in range (value[0] * value[1]):
        if value[4] == 'bw':
            pixel = chc([0, 255])
        else:
            pixel = rint(0, 255)
        contets.append(pixel)
    fimg.write(bytearray(contets))