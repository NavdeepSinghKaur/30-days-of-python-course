#30_days_of_python_day_3#

import math

age = int(16)

height = float(1.76)

complex = (2j)

# triangle area script

input_base = float(input("Enter base: " ))

input_height = float(input("Enter height: "))

def triangle_area(base, height):
    area = 0.5 * base * height
    print("The area of the triangle is %s" %area)

triangle_area(input_base, input_height)


# tirangle perimeter script

side_a = float(input("Enter the side a of the triangle: "))

side_b = float(input("Enter the side b of the triangle: "))

side_c = float(input("Enter the side c of the triangle: "))

def perimeter(side_a, side_b, side_c):
    perimeter = side_a + side_b + side_c
    print("The perimeter of the triangle is %s" %perimeter)

perimeter(side_a, side_b, side_c)

#rectange area

rectangle_length = float(input("Enter the length of the rectangle: "))

rectangle_width = float(input("Enter the width of the rectangle: "))

def rectangle_area(length, width):
    area = length * width
    print("The area of the rectangle is: %s" %area)

def rectangle_perimeter(length, width):
    perimeter = 2*(length + width)
    print("The perimeter of the rectangle is: %s" %perimeter)

radius = float(input("Enter the radius of the circle: "))

def circle_area_and_circumference(radius):
    PI = math.pi

    area = PI * radius**2
    print("The area of the circle is %s" %area)

    circumference = 2*PI*radius
    print("The circumference of the circle is %s" %circumference)

circle_area_and_circumference(radius)


print(not(len("python") and len("dragon")))


print("on" in ("python" and "dragon"))


print("jargon" in ("I hope this course is not full of jargon"))


print(not ("on" in ("python" and "dragon")))


python_text_length = len("python")

float(python_text_length)

str(python_text_length)


number = float(input("Enter a number to comprove is is odd or even: "))

if (number % 2 == 0):
    print("is even")

else:
    print("is odd")


print((7 // 3 == int(2.7)))


print("10" == 10)


print(int(9.8) == 10)


hours = float(input("Enter the hours that you worked: "))

rate = float(input("Enter the rate per hour: "))

def weekly_earning(hours, rate):
    earning = hours * rate
    print("Your weekly earning is: %d" %earning)

weekly_earning(hours, rate)


years = float(input("Enter the number of years you have lived: "))

seconds_lived = years*3.1540000

print("You have lived: %f seconds" %seconds_lived)

print(""" 
          1 1 1 1 1
          2 1 2 4 8
          3 1 3 9 27
          4 1 4 16 64
          5 1 5 25 125 """)
