#average height using for loops

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
print(student_heights)

total = 0
number = 0
for student in student_heights :
  total += student
print(f'total height is {total}')
for num in student_heights :
  number += 1
print(f'total number of students : {number}') 
average_height = total /number
print(f'Average height of the students is {average_height}')


