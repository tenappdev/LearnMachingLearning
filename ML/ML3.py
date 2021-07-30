#study from https://youtu.be/s7QumXDVG2o
#seaborn คือนำข้อมูลมาแสดงเป็นแผนภาพ
#โดยมี panda ในการโหลดข้อมูล
#We must install lib first by using "pip install seaborn"
#and "pip install pandas"

import seaborn as sb
import matplotlib.pyplot as plt
iris_dataset = sb.load_dataset('iris')

print(iris_dataset.head())

sb.set()
sb.pairplot(iris_dataset,hue='species',size=2) #แบ่งสีตามสายพันธุ์
plt.show()