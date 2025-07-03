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
f_sample = 200
data_long = time_long_min*60*f_sample*1000*2
# data_long = 5*f_sample*1000*2

# mcl = input("请输入阈值：")
# print("with filter")
f_path_high = "F:\\MS16E020C原始数据\\2工作稳定性测试原始数据2"
f_path_high1 = "F:\\MS16E020C原始数据\\2工作稳定性测试原始数据22"
# os.chdir(f_path_high)
#
# new_folder = "原始数据"
# os.makedirs(new_folder)

files = os.listdir(f_path_high)

# root = tk.Tk()
# root.withdraw()
# f_path = filedialog.askopenfilename()
for file in files:
    data_long = data_long + random.randint(0, 10000)*2
    file = open(f_path_high + "\\"+file, 'rb')
    file.seek(0,2)
    eof = file.tell()
    file.seek(0,0)
    data = file.read()
    file_name =(file.name.split('\\')[3]).split('.')[0]
    f2 = open(f_path_high1+"\\"+ file_name + "-" + str(time_long_min) + "min" + str(f_sample) + "kHz" + "数据.dat", 'wb')
    cishu = data_long // eof
    geshu = data_long % eof
    n = 0
    while n <cishu:
        f2.write(data)
        n=n+1

    f2.write(data[0:geshu])

    file.close()
    f2.close()








print("helloworld")

# result = struct.unpack('format string', data)