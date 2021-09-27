'''
study from  https://youtu.be/ixT4dNbIveY
เราจะทำนายอุณหภูมิด้วย Linear Regression
เทนสามารถเปิดไฟล์ Weather.csv ที่ดาวโหลดมาแล้ว เพื่อศึกษาเองได้
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

#เอา dataset ที่ upload อยู่ที่เว็บ
dataset = pd.read_csv("https://raw.githubusercontent.com/kongruksiamza/MachineLearning/master/Linear%20Regression/Weather.csv")

#print(dataset.shape) #ตามข้อมูลล่าสุดจะ print (119040,31)  คือ row แล้วตามด้วย column

#print(dataset.describe()) #จะอธิบายตาราง

#ให้กราฟเอาค่าจาก column 'MinTemp' มาใส่ในแนวแกน x แล้ว column 'MaxTemp' มาใส่ในแนวแกน y
dataset.plot(x='MinTemp',y='MaxTemp',style=".")
plt.title('Min & Max Temp')
plt.xlabel("Mintemp")
plt.ylabel("Maxtemp")
plt.show()
