'''
learn from  https://youtu.be/JQNyE2wul-A
download file matlab from osf.io/jda6s

We must install lib first by using "pip install scikit-learn" for using dataset and
 "pip install matplotlib" for draw shape and
 "pip install scipy" for reading file matlab
'''
from scipy.io import loadmat 
import matplotlib.pyplot as plt

mnist_raw = loadmat("mnist_original.mat")

mnist = {
    "data":mnist_raw["data"].T,
    "target":mnist_raw["label"][0]
}  
print(mnist["data"].shape) #(70000,784) จำนวนรูปภาพ, pixel x pixel
x,y=mnist["data"],mnist["target"]

print(x.shape) #(70000,784)

number = x[15000] #จะดึงภาพออกมา เป็นตำแหน่ง
number_image = number.reshape(28,28) #จะเป็นรูปภาพหนึ่งที่มีขนาด 28x28 pixel 

print(y[15000]) #2.0

plt.imshow(
    number_image,
    cmap=plt.cm.binary,
    interpolation ="nearest")
plt.show()
#จะแสดงรูปลายมือ 2 
