import random
import struct
# -*- coding: utf-8 -*-

import tkinter as tk
from base64 import encode, decode
from tkinter import filedialog
import os

from PIL.TiffTags import DOUBLE
from numpy.f2py.crackfortran import endifs, reset_global_f2py_vars


time_long_min = int(input("数据时间长度(min)："))
#
# time_long_min = 10
f_sample = 11.5
data_long = (time_long_min*60+random.randint(0,10))*f_sample*1000*2
# data_long = 5*f_sample*1000*2

# mcl = input("请输入阈值：")
# print("with filter")

# root = tk.Tk()
# root.withdraw()
f_path = filedialog.askopenfilename()


file = open(f_path, 'rb')
file_name =f_path.split('.')[0]
file.seek(0,2)
eof = file.tell()
file.seek(0,0)
data = file.read()
f2 = open( file_name+ str(time_long_min) +"min" + str(f_sample)+ "kHz"+"数据.dat",'wb')

cishu  = int( data_long// eof)
geshu = int(data_long % eof)


n = 0
while n <cishu:
    f2.write(data)
    n=n+1
                                             
f2.write(data[0:geshu])

file.close()
f2.close()





print("helloworld")

# result = struct.unpack('format string', data)