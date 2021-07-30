#learn from  https://youtu.be/MVzqI7z3zq0
#We must install lib first by using "pip install scikit-learn"
import pylab #to draw shape
from sklearn import datasets


digit_dataset = datasets.load_digits()
print(digit_dataset.target[0]) #จะแสดงเลข 0 ซึ่งเป็นตำแหน่งเดียวกับ images[0]
pylab.imshow(digit_dataset.images[0],cmap=pylab.cm.gray_r) #cmap คือ color map  gray_r คือสีเทา
pylab.show() #แสดงรูป digit_dataset.images[0]