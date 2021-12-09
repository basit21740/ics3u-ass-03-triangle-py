#!/usr/bin/env python3

# Created by: Abdul Basit
# Created on: Nov 2021
# this program tells about the triangle type


def main():
    # this function tells about the triangle type

    print("We will find out the type of triangle")

    type = int(input("Enter the number of sides that are of same length: "))

    if type == 2:
        print("It is an Isosceles triangle.")
    elif type == 3:
        print("It is an Equilateral triangle.")
    elif type == 0:
        print("It is a Scalene triangle!")
    else:
        print("It is not a triangle")

    print("\nDone.")


if __name__ == "__main__":
    main()
