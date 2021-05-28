student_scores = input("Input a list of student scores: \n").split()
for number in range(0, len(student_scores)):
    student_scores[number] = int(student_scores[number])
print(max(student_scores))

############################################################################################################################################
student_scores = input("Input a list of student scores: \n").split()
for number in range(0, len(student_scores)):
    student_scores[number] = int(student_scores[number])
print(max(student_scores))

for score in student_scores:
  if score > highest_score:
    highest_score = score
    # print(highest_score)
    
print(f"The highest score in the class is: {highest_score}")
