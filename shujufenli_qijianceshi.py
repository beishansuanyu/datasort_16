import struct
# -*- coding: utf-8 -*-

import tkinter as tk
from base64 import encode, decode
from tkinter import filedialog
import os

from numpy.f2py.crackfortran import endifs, reset_global_f2py_vars

print("with filter")

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
ref_v = 1

t_temp = 0
fs_s = 2000
fs = 10000



f2 = open(file_name+"模拟通道数据数据.txt",'w+')

f2.write('时间'+'\t'+'数据')









def match_example(item):
    # pattern1 = b'\xEb\x90'
    # n=0
    # while n <2183:
    global t_temp
    t_temp += 1 / fs
    str1 = '\n' + str(t_temp)
    f2.write(str1)
    dat =(int.from_bytes(item, byteorder='big', signed=False)/2**16 -1/2) * ref_v
    str1 = '\t' + str(dat)
    f2.write(str1)







# pattern1 = b'\x1a\xcf\xfc\x1d'
pattern1 = b'\x1a\xcf\xfc\x1d\x00\x00'
pattern2 = b'\x1a\xcf\xfc\x1d\x00\x55'
n = 0
while n <100000000:
    m_1 = data.find(pattern2,n,eof)
    m_2 = data.find(pattern2,m_1+15,eof)
    m = data.find(pattern1,m_1,m_2)
    if m != -1:
        # temp = data[m+3]
        # # if data[m+3] == 16:
        # #     match data[m+4]:
        # #         case 17:
        # #             f0.write(data[m+8:m+2184])
        # #         case 34:
        # #             f1.write(data[m+8:m+2184])
        # #         case _:
        # #             print(data[m+7])
        # if data[m+3] == 29:
        if (data[m+4:m+5] =='\x00\x55' ) :
            k = 1
        else :# print(data[m+2182:m+2184])
            match_example(data[m + 6:m + 8])

        # elif data[m + 3] == 85:
        #     match_example1(data[m + 6:m + 2184])
    else:
        break
    n=m+12

file.close()
f2.close()




print("helloworld")

# result = struct.unpack('format string', data)