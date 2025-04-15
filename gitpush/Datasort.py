import struct
# -*- coding: utf-8 -*-

import tkinter as tk
from base64 import encode, decode
from tkinter import filedialog
import os

from numpy.f2py.crackfortran import endifs
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
t_temp1 = -1
t_temp2 = 0
fs_s = 2000
fs = 10000

data_hold= [0,0,0,0,0,0]

f = open(file_name+"处理后结果.dat", "wb+")
f0 = open("数字通道1数据.dat",'wb')
f1 = open("数字通道2数据.dat",'wb')
f2 = open("模拟通道数据数据.txt",'w+')
f3 = open("传感器数据.txt",'w+')
f2.write('时间')
for i in range(16):
    f2.write('\t'+'通道'+str(i+1))
f2.write('\n')

f3.write('时间' +'\t'+ 'X轴' +'\t'+ 'Y轴'+'\t'+ 'Y轴')
f3.write('\n')


files = [f,f0,f1,f2]
mcl = input("请输入阈值：")
mcl_float = float(mcl)

def write(item):
    f2.write(str('{:.6f}'.format(t_temp2)))
    a =0
    for i in range(16):
        dat = item[a:a+2]
        dat = int.from_bytes(dat, byteorder='big')
        x = dat & 0x8000
        y = dat & 0x7fff
        m = 2 ** 15
        if x == 0:
            y = y
        else:
            y = y - m
        match i:
            case 0 | 1| 6| 7| 9 |10:
                y = y*2.2
            case 2| 3| 4| 5| 8| 11| 12|13|14| 15:
                y = y
            case _:
                print('匹配到其他通道')
        y = y / m * 10
        formatted_num = '{:.6f}'.format(y)
        str1 = '\t'+ str(formatted_num)
        f2.write(str1)
        a = a + 2
    f2.write('\n')

def write1(item):

    f3.write(str('{:.6f}'.format(t_temp1-1)))
    a =0
    b = 0




    for i in range(3):
        dat = item[a:a+3]
        dat = int.from_bytes(dat, byteorder='big')
        x = dat & 0x800000
        y = dat & 0x7fffff
        m = 2 ** 23
        if x == 0:
            y = y
        else:
            y = y - m

        y = y/209715

        if abs(data_hold[b]-data_hold[b+1])>mcl_float and abs(y-data_hold[b+1])>mcl_float :

            data_hold[b+1] = data_hold[b]
        else:None




        formatted_num = '{:.6f}'.format(data_hold[b+1])
        str1 = '\t'+ str(formatted_num)
        f3.write(str1)
        data_hold[b] = data_hold[b+1]
        data_hold[b + 1] = y
        b= b+2
        a = a + 3
    f3.write('\n')




def match_example(item):
    pattern1 = b'\xEb\x90'
    n=0
    while n <2183:

        m = item.find(pattern1, n, 2183)
        if m != -1:
            write(item[m+2:m+34])
            global t_temp2
            t_temp2 += 1/fs
        else:
            break
        n = m+34

def match_example1(item):
    pattern1 = b'\xEb\x90'
    n=0
    while n <2183:

        m = item.find(pattern1, n, 2183)
        if m != -1:
            write1(item[m+2:m+11])
            global t_temp1
            t_temp1 += 1/fs_s
        else:
            break
        n = m+9




pattern = b'\x1a\xcf\xfc'
n = 0
while n <eof:
    m = data.find(pattern,n,eof)
    if m != -1:
        temp = data[m+3]
        if data[m+3] == 16:
            match data[m+4]:
                case 17:
                    f0.write(data[m+8:m+2184])
                case 34:
                    f1.write(data[m+8:m+2184])
                case _:
                    print(data[m+7])
        # elif data[m+3] == 29:
        #     # print(data[m+2182:m+2184])
        #     match_example(data[m + 8:m + 2184])
        #
        # elif data[m + 3] == 85:
        #     match_example1(data[m + 6:m + 2184])
    else:
        break
    n=m+2184



while file in files:
    file.close()


print("helloworld")

# result = struct.unpack('format string', data)