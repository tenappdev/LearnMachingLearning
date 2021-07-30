#learn from  https://youtu.be/MVzqI7z3zq0
#We must install lib first by using "pip install scikit-learn" and "pip install matplotlib"
import matplotlib.pyplot as plt #to draw shape
from sklearn import datasets

digit_dataset = datasets.load_digits()
print(digit_dataset.target[0]) #จะแสดงเลข 0 ซึ่งเป็นตำแหน่งเดียวกับ images[0]
plt.imshow(digit_dataset.images[0],cmap=plt.get_cmap('gray')) 
plt.show() #แสดงรูป digit_dataset.images[0]

'''
pylab จะได้ที่ว่างเป็นสีขาว
matplotlib.pyplot  จะได้ที่ว่างเป็นสีดำ
'''