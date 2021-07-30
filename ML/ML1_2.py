#learn from https://youtu.be/fMZV6q0_ZZg
#We must install lib first by using "pip install scikit-learn"
from sklearn import datasets

digit_dataset = datasets.load_digits()

#print(digit_dataset.keys())
#print(digit_dataset['DESCR'])
#print(digit_dataset['data']) #แสดง data 
#print(digit_dataset['images'].shape) #ขนาดของภาพแต่ละภาพ ซึ่งเป็น 8 X 8 pixel
#print(digit_dataset['target_names']) #แสดง type เป้าหมายที่เก็บ
#print(digit_dataset.target_names) #เหมือนกับ print(digit_dataset['target_names'])

#print(digit_dataset.images[0]) #ได้ค่า pixel 8x8 ภาพแรก มาแสดง
#print(digit_dataset.images[0].shape) #print ขนาดออกมาให้แสดง

print(digit_dataset.images[:15]) #ได้ค่า pixel 8x8 ถึงภาพที่ 15 มาแสดง