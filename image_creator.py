# -------------------------------------------------------------------------------
# Name:        ranndom image creator
# Purpose:     skrypt przygotowany w czasie wakacji 2018
#
# Author:      Wojciech
#
# Created:     19.07.2018
# Copyright:   (c) Wojciech 2018
# Licence:     Za darmo w celach edukacyjnych
# -------------------------------------------------------------------------------

import sys
import datetime
from random import randint as rint
from random import choice as chc
from random import randint as rint

now = datetime.datetime.now()
height = width = 600
directory = 'output\\'
filename = 'img_{:%d%m%Y%H%M%S}_{}x{}.raw'.format(now,width,height)
pathname = directory + filename


if len(sys.argv) != 3:
        print('Program wywołany z domyślnymi ustawieniami:')
        print('-obraz 600px x 600px')
        print('-obraz zostanie zapisany w katalogu {} pod nazwą {}.'.format(directory[:-1], filename))
        print('Wywołanie z parametrami: python {} height width [path_to_folder]'.format(sys.argv[0]))
else:
    height = int(sys.argv[1])
    width = int(sys.argv[2])
    if len(sys.argv) == 4:
        pathname = sys.argv[3]

contents = []
pixel = 0

with open(pathname, 'wb') as fimg:
    for i in range(height * width):
        """
        chc -> wybiera tylko z tych elementów: chc([1, 2, 3, 10]) 
        rint -> wybiera z zakresu: rnt(1, 20)
        """
        pixel = chc([0, 255])
        contents.append(pixel)
    fimg.write(bytearray(contents))
