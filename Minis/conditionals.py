# %% 1.
x = 5
y = 10
if 2 * x > 10:
    print("Question 1 works!")

#below prints, 2x = 10, not > 10
else:
    print("oooo needs some work")


# %% 2.
x = 5
y = 10

#below prints, dog = 3, < 5
if len("Dog") < x:
    print("Question 2 works!")

else:
    print("Still missing out")

# %% 3.
x = 2
y = 5

#below prints, 6 > 5 and 25 < 26
if (x ** 3 >= y) and (y ** 2 < 26):
    print("GOT QUESTION 3!")

else:
    print("Oh good you can count")

# %% 4.
name = "Dan"
group_one = ["Greg", "Tony", "Susan"]
group_two = ["Gerald", "Paul", "Ryder"]
group_three = ["Carla", "Dan", "Jefferson"]

if name in group_one:
    print(name + " is in the first group")
elif name in group_two:
    print(name + " is in group two")
    
#below prints, dan is in group three
elif name in group_three:
    print(name + " is in group three")
    
else:
    print(name + " does not have a group")


# %% 5.
height = 66
age = 16
adult_permission = True

if (height > 70) and (age >= 18):
    print("Can ride all the roller coasters")
elif (height > 65) and (age >= 18):
    print("Can ride moderate roller coasters")
elif (height > 60) and (age >= 18):
    print("Can ride light roller coasters")
    
#below prints
elif ((height > 50) and (age >= 18)) or ((adult_permission) and (height > 50)):
    print("Can ride bumper cars")
    
else:
    print("Stick to lazy river")
