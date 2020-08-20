# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 10:22:53 2020

@author: ansha
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 09:40:15 2020

@author: ansha
"""

text = input("Enter text: ")
#key = int(input("Enter Key: "))
key = 4
choice = input("Enter choice: 1. Encrypt 2. Decrypt ")

def encrypt(text, key):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result+=chr((ord(char) + key - 65) % 26 + 65)
        else:
            result+=chr((ord(char) + key - 97) % 26 + 97)
    return result

if choice == "1":
    print(encrypt(text,key))
elif choice == "2":
    print(encrypt(text,26-key))
else: 
    print("Invalid input")
            
    