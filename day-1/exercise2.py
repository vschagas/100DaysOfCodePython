# string = "Hello"
# Number = 123_125
# Float = 123.00
# bool = True or False

name = len(input("What's your name"))
new_name = str(name)
print("your name has " + new_name + "characteres")

# Calculo IMC
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

# result = intWeigth / (intHeigth * intHeigth)
imc = int(weight) / float(height) ** 2
result = int(imc)

print(result)

#Exercicio 3 
# Descubra quantos dias meses e anos faltam até você completar 90 anos.

age = input("What is your current age?")

years = (90 - int(age))
days = years * 365
months = years * 12
weeks = years * 52
print(f"You have {days} days, {weeks} weeks, and {months} months left.")