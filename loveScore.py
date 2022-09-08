print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

join_names = name1 + name2
lower_join_names = join_names.lower()

t = lower_join_names.count("t")
r = lower_join_names.count("r")
u = lower_join_names.count("u")
e = lower_join_names.count("e")
true = t + r + u + e

l = lower_join_names.count("l")
o = lower_join_names.count("o")
v = lower_join_names.count("v")
e = lower_join_names.count("e")
love = l + o + v + e

result = str(true) + str(love)

if int(result) < 10 or int(result) > 90:
    print(f"Your score is {result}, you go together like coke and mentos.")
elif int(result) >= 40 and int(result) <= 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")