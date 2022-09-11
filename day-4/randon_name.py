'''exercicio  random'''
import random
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
quantify = len(names)
random = random.randint(0, quantify - 1)

random = random.choice(names)

print(f"{names[random]} is going to buy the meal today!")
