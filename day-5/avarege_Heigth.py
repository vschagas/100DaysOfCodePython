'''Exercise avarage heigth'''

student_heights = input("Input a list of student heights ").split()
  for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])

soma = 0
quantidade = 0
  for index in student_heights:
    soma += index
    quantidade += 1

  result = round(soma / quantidade)
  print(result)

