import struct
# -*- coding: utf-8 -*-

import tkinter as tk
from base64 import encode, decode
from tkinter import filedialog
import os

from numpy.f2py.crackfortran import endifs, reset_global_f2py_vars

flag = int(input("which your name(ChaoZhang—1，YunLiu-2)："))

# mcl = input("请输入阈值：")
# print("with filter")

# root = tk.Tk()
# root.withdraw()
f_path = filedialog.askopenfilename()


if flag == 1:
    num_start = 6
    num_step = 12
    pattern1 = b'\x1a\xcf\xfc\x1d'
elif flag == 2:
    num_start = 10
    num_step = 26
    pattern1 = b'\x1a\xcf\xfc\x1d\x1a\xcf\xfc\x1d'


file = open(f_path, 'rb')
file_name =f_path.split('.')[0]
file.seek(0,2)
eof = file.tell()
file.seek(0,0)
data = file.read()






f2 = open(file_name+"有效数据.dat",'wb')



















n = 0
while n <eof:

    m = data.find(pattern1,n,eof)
    if m != -1:
        data_temp = data[m+num_start:m+num_start+2]
        f2.write(data[m+num_start:m+num_start+2])

    else:
        break
    n=m+num_step

file.close()
f2.close()




print("helloworld")

# result = struct.unpack('format string', data)