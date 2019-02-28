
import csv

with open('E:/data science/car.csv') as csvfile:
	car = list(csv.DictReader(csvfile))

print(car[:])

print(len(car))

hwy= sum(float(d['hwy']) for d in car)/len(car)
print('average ecomony on highway is :')
print(hwy)

city=sum(float(d['city']) for d in car)/len(car)
print('average ecomony in city is :')
print(city)


if(city<hwy):
	print('more fuel economy on highway than in the city')
else:
	print('more fuel economy in city than on the highway')

cylinder= set(d['cylinder']for d in car)
print("available cylinders are")
print(cylinder)


