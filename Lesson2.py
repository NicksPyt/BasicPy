#Task I
someone=int(input("what is your age? "))
if(someone >= 18):
   print("You can go :)")
if(someone < 18):
   print("Stop :x")


#Task II
User = input("Type Your Email")
if User == "brennan":
    print("Get Off My Computer")


#Task III
students_credit = int(input("Choose your credit"))
if not (students_credit >= 120):
    print("you dont have enough credits to graduate.")
students_gpa = int(input("Choose your GPA"))
if not (students_gpa > 2.0):
    print("your GPA is not high enough to graduate.")
if(students_credit or students_credit < 120 or 2.0):
    print("you dont meet either requirement to graduate!")


#Task IV
grade = int(input("type your grade"))
if(grade >= 90):
    print("A")
elif(grade >= 80):
    print("B")
elif(grade >= 70):
    print("C")
elif(grade >= 60):
    print("D")
else:
     print("F")
    