#Let's learn Python
print('This is one hell of a basic Calculator!')
num1 = input('Enter the first number ')
num1_int = int(num1)
num2 = input('Enter the second number ')
num2_int = int(num2)

sum = str(num1_int + num2_int)
print('The sum of ' + num1 + ' & ' + num2 + ' is ' + sum)

quotient = str(num1_int / num2_int)
print('The quotient of ' + num1 + ' & ' + num2 + ' is ' + quotient)

power = str(num1_int ** num2_int)
print('The result of ' + num1 + ' to the power of ' + num2 + ' is ' + power)

average = str((num1_int + num2_int) / 2)
print('The average of ' + num1 + ' & ' + num2 + ' is ' + average)

print('Let\'s talk about areas! \nI shall now ask you to input the radius of a circle and length & breadth of a rectangle')
radius = input('Enter the radius: ')
radius_int = int(radius)
pi = 3.14159
length = input('Enter the length: ')
length_int = int(length)
breadth = input('Enter the breadth: ')
breadth_int = int(breadth)

area_circle = str(pi * (radius_int ** 2))
print('The area of a circle with radius ' + radius + ' is ' + area_circle)

area_rectangle = str(length_int * breadth_int)
print('The area of a rectangle with length ' + length + ' & breadth ' + breadth + ' is ' + area_rectangle )