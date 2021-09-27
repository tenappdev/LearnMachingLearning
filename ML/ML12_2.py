'''
study from  https://youtu.be/ixT4dNbIveY
เราจะทำนายอุณหภูมิด้วย Linear Regression
เทนสามารถเปิดไฟล์ Weather.csv ที่ดาวโหลดมาแล้ว เพื่อศึกษาเองได้
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split #ใช้ในการแบ่งข้อมูล
from sklearn.linear_model import LinearRegression

#เอา dataset ที่ upload อยู่ที่เว็บ อ่านแล้วเก็บไว้ใน dataset
dataset = pd.read_csv("https://raw.githubusercontent.com/kongruksiamza/MachineLearning/master/Linear%20Regression/Weather.csv")

#train & test set
#ให้ x y กับค่า  Mintemp กัล Maxtemp
x = dataset["MinTemp"].values.reshape(-1,1) #reshape ทำให้เป็น array2D 
y = dataset["MaxTemp"].values.reshape(-1,1)

#80%       -    20%
#train set - test set
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

#training
model = LinearRegression()
model.fit(x_train,y_train)

#test
#จากสมการเขิงเส้น y=ax + b เลยใช้ x ซึ่ง x ก็คือ x_test
y_pred= model.predict(x_test)

'''
#เมื่อนำ x_test,y_test มาวางจุดบนกราฟ และวางกราฟเชิงเส้น (x_test,y_pred) จะเห็นว่ากราฟที่ได้มีแนวโน้มตามกราฟ x_test,y_testที่ plot 
plt.scatter(x_test,y_test)
plt.plot(x_test,y_pred,color="red",linewidth=2)
plt.show()
'''

#compare true data & predict data
#print(y_test.shape) #จะแสดง (23808, 1) เพราะเป็น 2D แต่จะเอาไปใช้ได้ต้องทำเป็น 1D เสียก่อน โดยใช้ flatten()
'''
ตัวอย่างการใช้ 
dict = {'column_1':['a','b','c'],'column_2':['d','e','f'],'column_3':['g','h','i']}
df = pd.DataFrame(dict)
'''
df=pd.DataFrame({'Actually':y_test.flatten(),'Predicted':y_pred.flatten()})

#เอาบางจำนวนไปเปรียบเทียบเพื่อประหยัดเวลาสอน
df1 = df.head(20)
df1.plot(kind="bar",figsize=(16,10))
plt.show()