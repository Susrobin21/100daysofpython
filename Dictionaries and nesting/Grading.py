student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
  "Luna" : 87
}
for student in student_scores :
    if student_scores[student] > 90 :
        student_scores[student] = 'Outstanding'
    elif student_scores[student] >80 :
        student_scores[student] = 'Exceeded expectations'
    elif student_scores[student] >70 :
        student_scores[student] = 'Acceptable'
    else :
        student_scores[student] = "Need to work better"
print(student_scores)