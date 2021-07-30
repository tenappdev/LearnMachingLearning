#learn from https://youtu.be/ETFJiNaRJIo
#We must install lib first by using "pip install scikit-learn"

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris_dataset = load_iris()

#print(iris_dataset.data.shape) #ขนาด data แถว 150, col 4 

#ต้องการแบ่ง training 75%, test 25% 

x_train,x_test,y_train,y_test = train_test_split(iris_dataset["data"],iris_dataset["target"],random_state=0)
'''
print(x_train.shape) #(112,4)
print(x_test.shape)  #(38,4)
print(y_train.shape) #(112,)
print(y_test.shape)  #(38,)
'''
#150
#train 75% = 112
#test  25% = 38

#test size มี 20%
x_train,x_test,y_train,y_test = train_test_split(iris_dataset["data"],iris_dataset["target"],test_size=0.2,random_state=0)
print(x_train.shape) #(120,4)
print(x_test.shape)  #(30,4)
print(y_train.shape) #(120,)
print(y_test.shape)  #(30,)
#150
#train 80% = 120
#test  20% = 30
