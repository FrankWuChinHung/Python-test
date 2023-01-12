# -*- coding: utf-8 -*-
"""
Created on Fri Mar 11 20:14:59 2022

@author: USER
"""

y = [94,78,92,85,88,79,90,84,66,78,56]
y.sort(reverse=True) #y.sort(reverse=True)=>  新變數 = sorted(y,reverse=True)
z=0
w=0
print(y)
for x in y:
   z +=1    
   if x >= 90:
      w +=1
      print(x)
      
       
print("成績90分以上的人數是",w,"人")
  