"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_mult, add_cubes)

print("""INSTRUCTIONS:
Hi and welcome to my super prefix calculator!
Please enter your equation when prompted using the proper notation for the following operations:
+ 1 2 : for addition of two numbers
- 1 2: for subtraction of two numbers 
* 1 2: for multiplication of two numbers
/ 1 2: for division of two numbers 
square 1: to get the square of one number
cube 1: to get the cube of one number
power 1 2: to get one number raised to the power of a second number 
mod 1 2: to get the remainder of one number divided by a second number 
x+ 1 2 3: to get (num1 + num2) * num3
cubes+ 1 2: to take two numbers, then add together the cubes of those numbers
""")

while True:
    equation = input("Enter your equation here > ")
    equation_list = equation.split(" ")

    if equation_list[0].lower().startswith("q"):
        break
    elif equation_list[0] == "+":
        print(add(int(equation_list[1]), int(equation_list[2])))
    elif equation_list[0] == "-":
        print(subtract(int(equation_list[1]), int(equation_list[2])))
    elif equation_list[0] == "*":
        print(multiply(int(equation_list[1]), int(equation_list[2])))
    elif equation_list[0] == "/":
        print(divide(int(equation_list[1]), int(equation_list[2])))
    elif equation_list[0] == "square":
        print(square(int(equation_list[1])))
    elif equation_list[0] == "cube":
        print(cube(int(equation_list[1])))
    elif equation_list[0] == "power":
        print(power(int(equation_list[1]), int(equation_list[2])))
    elif equation_list[0] == "mod":
        print(mod(int(equation_list[1]), int(equation_list[2])))    
    elif equation_list[0] == "x+":
        print(add_mult(int(equation_list[1]), int(equation_list[2]), int(equation_list[3])))
    elif equation_list[0] == "cubes+":
        print(add_cubes(int(equation_list[1]), int(equation_list[2])))



    


