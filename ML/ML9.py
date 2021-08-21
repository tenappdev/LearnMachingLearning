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
x = np.linspace(-5,5,100) #ตัวแปรอิสระ ที่นำมาวาดเส้น
print(x) #เมื่อ print ออกมาจะได้ x มาเป็นขโยง

#y = ax + b
y = 2*x + 1 #เมื่อเอา x ที่เป้นขโยงมาเข้าสมการนี้จะได้ y เป็นขโยงที่จำนวนสมาชิกเท่ากับ x

plt.plot(x,y,'-r',label='y=2x+1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')
plt.title("Graph y=2x+1")
plt.grid()
plt.show()