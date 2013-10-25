#       CS101
#       Program 1
#       Gregory Gagnon
#       gmg634@mail.umkc.edu        

#       Problem: Calculate the total grade from weighted assignments for a class

#       Algorithm:
            # 1: Input Grades
            # 2: Calculate based on weight
            # 3: Output Final Grade
            
#       Error Handling: None
#       Other Comments

programs_str = input("What is your PROGRAMS grade out of 100? ")
problems_str = input("What is your PROBLEMS grade out of 100? ")
quizzes_str = input("What is your QUIZZES grade out of 100? ")
exams_str = input("What is your EXAMS grade out of 100? ")
final_str = input("What is your FINAL EXAM grade out of 100? ")

programs_float = float(programs_str)
problems_float = float(problems_str)
quizzes_float = float(quizzes_str)
exams_float = float(exams_str)
final_float = float(final_str)

total_float = (programs_float * 0.3) + (problems_float * 0.1) + (quizzes_float * 0.1) + \
              (exams_float * 0.3) + (final_float * 0.2)

print("Your TOTAL grade in the class is ", total_float, " out of 100")
