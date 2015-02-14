from PIL import Image
from scipy import misc
import matplotlib.pyplot as plt
import numpy as np
import time
import math
import serial

PICTURE_TYPE = 'MALE'

def imblur(img, res_factor):
    img_res = misc.imresize(img, res_factor)
    img_res = misc.imresize(img_res, 1.0/res_factor)
    return img_res

plt.ion()
mng = plt.get_current_fig_manager()
mng.frame.Maximize(True)
plt.show()
plt.axis('off')

img = misc.imread('coast_qt.PNG')

import os
if PICTURE_TYPE  == 'FEMALE':
    rootdir = '.\\female'
else:
    rootdir = '.\\male'

file_list = []

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        file_list.append(os.path.join(subdir, file))

ser = serial.Serial('COM4', 9600, timeout=0)

scaling = -1
max_scaling = 8
cur_file_idx = 0
while 1:
    try:
        data = ser.readline()
        # print repr(data)
        if data == '1\r\n':
            if scaling == -1:
                img = misc.imread(file_list[cur_file_idx])
                cur_file_idx += 1
                min_dim = min(img.shape[0:2])
                scaling = int(math.log(min_dim, 2))
            print 'MATCH'
            im_res = imblur(img, 1.0/np.exp2(scaling))
            plt.imshow(im_res)
            plt.draw()
            scaling -= 1
        time.sleep(0.5)
    except ser.SeiralTimeoutException:
        print('Data could not be read')
        time.sleep(0.5)
