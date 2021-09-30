'''
เรียนจาก https://youtu.be/AB3wbvuIkaA
'''

from scipy.io import loadmat
import numpy as np
import matplotlib.pyplot as plt

mnist_raw = loadmat("mnist_original.mat")

mnist ={
    "data":mnist_raw["data"].T,
    "target":mnist_raw["label"][0]
}

#print(mnist["data"].shape) #แสดง (70000, 784)
#print(mnist["target"].shape) #แสดง (70000,)

# x เก็บ data พร้อมขนาด pixel
# y เก็บเพื่อบอกว่าตัวเลขนี้คือตัวไร 
x,y=mnist["data"],mnist["target"]
'''
print(x) จะแสดง
[[0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 ...
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]
 [0 0 0 ... 0 0 0]]
print(y) จะแสดง
[0. 0. 0. ... 9. 9. 9.]
'''
#training, test
#1-60000 training set
# 60001 - 70000 test set
'''
                            ตำแหน่งแรกจนถึง60000
                                        ตำแหน่ง60000จนถึงสุดท้าย
'''
x_train,x_test,y_train,y_test = x[:60000],x[60000:],y[:60000],y[60000:]

print(x_train.shape) #(60000, 784)
print(x_test.shape)  #(10000, 784)
print(y_train.shape) #(60000,)
print(y_test.shape)  #(10000,)

#จะมี class 0-9
#โจทย์คือ ตำแหน่งที่ 5000 มีค่าเป็น 5 จริงไหม โดยจะ return true/false