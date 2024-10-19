# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 18:18:03 2024

@author: honan
"""

while True:
    a = int(input("Nhap gia tri tu [-99,99]: "))
    if -99 <= a <= 99:
        print("Hop le", a)
        break
    else:
        print("Khong hop le")