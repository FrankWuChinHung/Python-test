# -*- coding: utf-8 -*-
"""
Created on Mon Mar 14 19:14:42 2022

@author: USER
"""

x = {'013':'王小明','035':'張美麗','200':'李大','53':'吳三','007':'龐德'}
y = {'013':36000,'035':38000,'200':40000,'53':53000,'007':70000}

z = input("員工ID:")
print("員工ID是",z,"的人是",x[z])
print(x[z],"的薪水是:",y[z])

k = input("要查詢的員工id = ")
if k in x:
   print("員工id %s已經在名單裡了" % k)
   print("名字是%s" %x[k])
else:
    print("員工id %s不在名單裡了" % k)
    value1 = input("來建立他的資料，名字是？")
    value2 = input("他的薪水是多少？")
    x[k]= value1
    y[k]= value2
    print("資料已建好，請確認")
    print(x)  
    print(y)
   