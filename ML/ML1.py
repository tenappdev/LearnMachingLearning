#learn from https://youtu.be/581WLpL870o
#We must install lib first by using "pip install scikit-learn"
from sklearn import datasets

iris_dataset = datasets.load_iris() #จะ return เป็นโครงสร้าง dictionary
#print(iris_dataset.keys())
'''
dict_keys(['data', 'target', 'frame', 'target_names', 'DESCR', 'feature_names', 'filename'])
'''

#print(iris_dataset['target']) #จะแสดงเป็นตัวเลข ตาม data ที่เก็บไว้ ซึ่งเป็นสายพันธุ์
#print(iris_dataset['target_names']) #จะแสดงเป็นชื่อสายพันธุ์ ตาม data ที่เก็บไว้
#print(iris_dataset['feature_names']) #จะแสดงเป็น data ที่เก็บไว้ มีอะไรบ้าง ความกว้าง สูงของแต่ละสายพันธุ์
#['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']

#print(iris_dataset['DESCR']) #จะแสดงเป็นคำอธิบาย 

#print(iris_dataset['data']) #จะแสดงความกว้างยาว ทั้งหมด
print(iris_dataset['data'][0:10])  #จะแสดงความกว้างยาว 10 แถวแรก