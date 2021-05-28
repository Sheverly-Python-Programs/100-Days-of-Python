student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)
total_height = sum(student_heights)
number_of_students = len(student_heights)
average_height = round(total_height / number_of_students)
print(average_height)

################################################################################################################################

student_heights = input("Input a list of student heights: \n").split()
for n in range(0, len(student_heights)): # The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
    student_heights[n] = int(student_heights[n])
total_height = 0
for height in student_heights:
    total_height += height
print(f"total height = {total_height}")
number_of_students = 0
for student in student_heights:
    number_of_students += 1
print(f"number of students = {number_of_students}")
average_height = round(total_height / number_of_students)
print(average_height)

################################################################################################################################
