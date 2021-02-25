"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

while True:
    equation = input("Enter your equation here > ")
    equation_list = equation.split(" ")

    if equation_list[0] == "q":
        break
    elif equation_list[0] == "+":
        print(add(equation_list[1], equation_list[2]))

