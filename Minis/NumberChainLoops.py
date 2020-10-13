# -*- coding: utf-8 -*-
"""
Created on Wed Oct  7 22:38:13 2020

@author: Steven
"""
# %%
def game():
    num = int(input("How many numbers do you want the list to be? "))
    for numbers in range(num):
        print(numbers)
    answer = input("Do you want to continue? (y)es or (n)o? ")
    if answer == "y":
        game()
game()

        
# %%
answer2 = "y"

while answer2 == "y":
    num = int(input("How many numbers do you want the list to be? "))
    for numbers in range(num):
        print(numbers)
    answer2 = input("Do you want to continue? (y)es or (n)o? ")






    


        
    
    
    
    
    