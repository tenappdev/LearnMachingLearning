'''
study from  https://youtu.be/93VyGrbCMww
'''
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression #การสร้างตัว model มาจาก sklearn

rng = np.random

##การจำลองข้อมูล
x = rng.rand(50)*10 #random มา 50 ค่า ได้ 0 - 10 แต่ไม่ถึง 10
y = 2*x +rng.randn(50) #randn มา 50 ค่า ซึ่งติดลบได้

##linear regression model
model = LinearRegression() #สร้าง obj ที่เป็นตัว model โดยใช้เป็น LinearRegression

#print("ก่อน reshape",x)
x_new = x.reshape(-1,1) #(-1,1) จะไม่ได้เป็นการกำหนดค่าใหม่ลงไป
#print("หลัง reshape",x_new)

##train
#จะเข้า model.fit() ซึ่งเป็น array2D ใส่เข้าไป ต้องเอามา reshape เสียก่อน
model.fit(x_new,y) #เอาข้อมูลมา train 

'''
print("R-SQuare : ",model.score(x_new,y)) #ค่า R-SQuare เป็นค่าสัมประสิทธิใช้วัดค่าตัวแปรตอบสนอง นั้นคือตัวแปร y ใช้วัดค่าว่ามีทั้งหมดกี่เปอร์เซ็นต์ แล้วเอาค่า y ไปใช้งานต่อไป
print("intercept : ",model.intercept_)
print("Coefficient : ",model.coef_)
'''

##test model
#เราจะพยากรณ์จากผลลัพธ์ที่มี
#                start,stop
xfit = np.linspace(-1,11) # Generate จำนวนข้อมูลที่มีระยะห่างเท่าๆ กัน
#print("xfit : ",xfit)
xfit_new = xfit.reshape(-1,1)
#print("xfit_new : ",xfit_new)
#print("xfit_new.shape : ",xfit_new.shape) #ขนาดของ model

yfit = model.predict(xfit_new) #เอาไปtestไปใน model แล้วเอาผลลัพธ์ใส่ไปใน yfit

##analysis model & result

'''
plt.xlabel('x')
plt.ylabel('y')
plt.show()
'''

plt.scatter(x,y)    #plot จุด
plt.plot(xfit,yfit) #plot เส้น
plt.show()
