#1
import math
x = int(input("Input degree: "))
radian = math.radians(x)
print("Output radian: ", radian) #round() устанавливает количество цифр после запятой 

#2
h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))
area = ((a + b)/2)*h
print("Expected Output: ", area)

#3
n = int(input("Input number of sides: "))
l = int(input("Input the length of a side: "))
area = (n * (l**2)) / 4 * (1 / (math.tan(math.radians(180) / n)))
print("The area of the polygon is: ", area )

#4
a = int(input("Length of base: "))
b = int(input("Height of parallelogram: "))
area = a * b
print("Expected Output: ", area)



