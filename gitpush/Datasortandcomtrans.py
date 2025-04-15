import struct
# -*- coding: utf-8 -*-

import tkinter as tk
from base64 import encode, decode
from tkinter import filedialog
import os
import struct

from numpy.f2py.crackfortran import endifs

root = tk.Tk()
root.withdraw()
f_path = filedialog.askopenfilename()




file = open(f_path, 'rb')
file_name =f_path.split('.')[0]
file.seek(0,2)
eof = file.tell()
file.seek(0,0)
data = file.read()
t_temp1 = 0
fs = 10000

data_hold= [0,0,0,0,0,0]

f1 = open(file_name+"解析后结果.txt", "w+")
# f0 = open("数字通道1数据.dat",'wb')
# f1 = open("数字通道2数据.dat",'wb')
# f2 = open("模拟通道数据数据.txt",'w+')
# f3 = open("传感器数据.txt",'w+')
# for i in range(16):
#     f.write('\t'+'通道'+str(i+1))
# f.write('\n')
# title =  '帧头' +'\t'+ '时标'+'\t'+ '状态字'+'\t'+ '滚转角'\
#         + '\t'+ '滚转角速度'+ '\t'+ '重力基准'+ '\t'+ 'ay'+ '\t'+ 'az'\
#         + '\t'+ 'Y轴加表采样值' + '\t'+ 'Z轴加表采样值' + '\t'+ 'ZLB_ang' \
#         + '\t' + 'HRG_ZT'+ '\t'+ 'HRG_rate' + '\t'+ 'HRG_angle' \
#         + '\t' + 'HRG_freq'+ '\t'+ 'HRG_fz' + '\t'+ 'HRG_zj' \
#         + '\t' + 'HRG_CNT'+ '\t'+ '温度' + '\t'+ '校验和'
f1.write( '帧头' +'\t'+ '时标'+'\t'+ '状态字'+'\t'+ '滚转角'\
        + '\t'+ '滚转角速度'+ '\t'+ '重力基准'+ '\t'+ 'ay'+ '\t'+ 'az'\
        + '\t'+ 'Y轴加表采样值' + '\t'+ 'Z轴加表采样值' + '\t'+ 'ZLB_ang' \
        + '\t' + 'HRG_ZT'+ '\t'+ 'HRG_rate' + '\t'+ 'HRG_angle' \
        + '\t' + 'HRG_freq'+ '\t'+ 'HRG_fz' + '\t'+ 'HRG_zj' \
        + '\t' + 'HRG_CNT'+ '\t' + 'ZLB_CNT'+ '\t'+ '温度' + '\t'+ '校验和')
# f1.write('\n')
# f2.write(title)
f1.write('\n')





def write(item,f_temp):
    # f_temp.write(str('{:.6f}'.format(t_temp1)))
    a =0
    a = 0

    for a in range(21):
        if a == 0: #帧头
            m = item[0:2]
            m = str(m)
            f_temp.write(m)
        elif a == 1: #时标
            dat = int.from_bytes(item[2:5], byteorder='big')
            str1 = '\t' + str(dat)
            f_temp.write(str1)
        elif a == 2: #状态字
            f_temp.write('\t' +str(item[5]))
        elif a == 3: #滚转角
            dat = int.from_bytes(item[6:8], byteorder='big')/90
            str1 = '\t' + str(dat)
            f_temp.write(str1)
        elif a == 4: #滚转角速度
            dat = int.from_bytes(item[8:10], byteorder='big',signed=True)
            M = item[8:10]
            str1 = '\t' + str(dat)
            f_temp.write(str1)
        elif a == 5: #重力基准
            dat = int.from_bytes(item[10:12], byteorder='big',signed=True)/10
            str1 = '\t' + str(dat)
            f_temp.write(str1)
        elif a == 6: #ay
            dat = int.from_bytes(item[12:14], byteorder='big',signed=True)/1000
            str1 = '\t' + str(dat)
            f_temp.write(str1)
        elif a == 7: #az
            dat = int.from_bytes(item[14:16], byteorder='big',signed=True)/1000
            str1 = '\t' + str(dat)
            f_temp.write(str1)
        elif a == 8: #y轴加表采样值
            dat = int.from_bytes(item[16:19], byteorder='big',signed=True)
            str1 = '\t' + str(dat)
            f_temp.write(str1)
        elif a == 9: #z轴加表采样值
            dat = int.from_bytes(item[19:22], byteorder='big',signed=True)
            str1 = '\t' + str(dat)
            f_temp.write(str1)
        elif a == 10: #ZLB_ang
            dat = int.from_bytes(item[22:24], byteorder='big',signed=True)/10
            str1 = '\t' + str(dat)
            f_temp.write(str1)
        elif a == 11: #HRG_ZT
            dat = int.from_bytes(item[24:26], byteorder='big',signed=True)
            str1 = '\t' + str(dat)
            f_temp.write(str1)
        elif a == 12: #HRG_rate
            byte_data = item[26:30]
            dat = struct.unpack(">f", byte_data)

            str1 = '\t' + str(dat)
            f_temp.write(str1)
        elif a == 13:  # HRG_angle
            byte_data = item[30:34]
            dat = struct.unpack(">f", byte_data)
            str1 = '\t' + str(dat)
            f_temp.write(str1)
        elif a == 14:  # HRG_freq
            byte_data = item[34:38]
            dat = struct.unpack(">f", byte_data)
            str1 = '\t' + str(dat)
            f_temp.write(str1)
        elif a == 15:  # HRG_fz
            dat = int.from_bytes(item[38:42], byteorder='big',signed=True)
            str1 = '\t' + str(dat)
            f_temp.write(str1)
        elif a == 16:  # HRG_zj
            dat = int.from_bytes(item[42:46], byteorder='big',signed=True)
            str1 = '\t' + str(dat)
            f_temp.write(str1)
        elif a == 17:  # HRG_CNT
            dat = int.from_bytes(item[46:48], byteorder='big',signed=False)
            str1 = '\t' + str(dat)
            f_temp.write(str1)
        elif a == 18:  # ZLB_CNT
            dat = int.from_bytes(item[48:50], byteorder='big',signed=False)
            str1 = '\t' + str(dat)
            f_temp.write(str1)
        elif a == 19:  # 温度
            dat = item[50]
            str1 = '\t' + str(dat/2)
            f_temp.write(str1)
        elif a == 20:  # 校验和
            str1 = '\t' + str(item[51])
            f_temp.write(str1)
        else:
            break

    f_temp.write('\n')

# def write1(item):
#
#     f3.write(str('{:.6f}'.format(t_temp1-1)))
#     a =0
#     b = 0
#
#
#
#
#     for i in range(3):
#         dat = item[a:a+3]
#         dat = int.from_bytes(dat, byteorder='big')
#         x = dat & 0x800000
#         y = dat & 0x7fffff
#         m = 2 ** 23
#         if x == 0:
#             y = y
#         else:
#             y = y - m
#
#         y = y/209715
#         if abs(data_hold[b]-data_hold[b+1])>0.5 and abs(y-data_hold[b+1])>0.5 :
#
#             data_hold[b+1] = (data_hold[b]+y)/2
#         else:None
#
#
#
#
#         formatted_num = '{:.6f}'.format(data_hold[b+1])
#         str1 = '\t'+ str(formatted_num)
#         f3.write(str1)
#         data_hold[b] = data_hold[b+1]
#         data_hold[b + 1] = y
#         b= b+2
#         a = a + 3
#     f3.write('\n')




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

# def match_example1(item):
#     pattern1 = b'\xEb\x90'
#     n=0
#     while n <2183:
#
#         m = item.find(pattern1, n, 2183)
#         if m != -1:
#             write1(item[m+2:m+11])
#             global t_temp1
#             t_temp1 += 1/fs_s
#         else:
#             break
#         n = m+9
#
# def match_example2(item):
#
#     pattern1 = b'\xEb\x90'
#     n=0
#     while n <2183:
#
#         m = item.find(pattern1, n, 2183)
#         if m != -1:
#             write1(item[m+2:m+11])
#             global t_temp1
#             t_temp1 += 1/fs_s
#         else:
#             break
#         n = m+9


pattern1 = b'\xEB\xEA'
n = 0
while n <eof:
    m = data.find(pattern1,n,eof)
    if m != -1 and m+52<eof:
        write(data[m:m + 52], f1)

    else:
        break
    n = m+52



f1.close()


print("helloworld")

# result = struct.unpack('format string', data)