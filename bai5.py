# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 18:18:21 2024

@author: honan
"""

while True:
    a = float(input("Nhap vao so tu [-89.9; 88.8]: "))
    if -89.9 <= a <= 88.8:
        break
    else:
        print("Khong hop le")