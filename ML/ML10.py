'''
study from https://youtu.be/bALu2G_iu1c
from equation y = ax +b
x ตัวแปรอิสระ
y ตัวแปรตาม
a ความชันของเส้นตรง
b ระยะตัดแกน y

We must install "pip install numpy" first
'''
import numpy as np
import matplotlib.pyplot as plt

rng = np.random
#print(rng.rand(10)) #random มา 10 ค่า ได้ 0 - 1 แต่ไม่ถึง 1
x = rng.rand(50)*10 #random มา 10 ค่า ได้ 0 - 10 แต่ไม่ถึง 10
#print(x)

y = 2*x +rng.randn(50) #randn มา 50 ค่า ซึ่งติดลบได้
print(y)

#plt.plot(x,y)
plt.scatter(x,y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

