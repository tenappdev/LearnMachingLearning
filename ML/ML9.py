'''
study from https://youtu.be/TMcSRhiam98
from equation y = ax +b
x ตัวแปรอิสระ
y ตัวแปรตาม
a ความชันของเส้นตรง
b ระยะตัดแกน y

We must install "pip install numpy" first
'''
import numpy as np
import matplotlib.pyplot as plt

#สร้างตัวเลข -5 ถึง 5 จำนวน 100 ชุด
x = np.linspace(-5,5,100) #ตัวแปรอิสระ
print(x)

#y = ax + b
y = 2*x + 1

plt.plot(x,y,'-r',label='y=2x+1')
plt.xlabel('x')
plt.ylabel('y')
plt.grid()
plt.show()