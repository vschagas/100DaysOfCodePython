'''High_sore'''
student_scores = input("Input a list of student scores ").split()

for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)

# student = len(student_scores)

RESULT = 0
for index in student_scores:
    if index > RESULT:
        RESULT = index
message = (f'The highest score in the class is: {RESULT}')
print(message)
