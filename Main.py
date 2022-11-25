#! /usr/bin/env python3

from encryption import *

class main:
    def __init__(self):

        """data = str(input("Enter text to encrypt:-\t"))
        newHandler = Handler(data)"""

        print("1.Encrypt data:-\t\n2.Decrypt data:-\t")
        number = int(input("Enter a number :-"))

        if number == 1:
            data = str(input("Enter text to encrypt:-\t"))
            newHandler = Handler(data,"enc")

            with open("user_detail1.db",'r') as file:
                print("Your Encryption text value is:-\t"+file.readline())


if __name__ == '__main__':
    Main = main()