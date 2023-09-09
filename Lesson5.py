#Task 1
string = input("enter your word")
strr = string
vowels=("A", "E", "I," "O", "U", "Y")
for l in string():
    if l not in vowels:
        strr = strr.replace()
    print("delete  Vowels")
    print(strr)


#Task 2
safj = [2, 3]

for number in safj:
    safj.append(1)
    print(safj) 


#Task 3 
age = [1, 2, 3, 21]
for x in age:
    if x < 21:
       continue
    print(x)


#Task 4
lists = [12, 44, 21, 'a', '2', 2.3]
for l in lists:
    if type(l) == type('2'):
        continue
    elif type(l) == type(1.2):
        continue
    elif type(l) == type(True):
        continue
    print(l) 


#Tasl 5
all_students = ['stud1', 'stud2', 'stud3', 'stud4', 'stud5', 'stud6']
students_in_poetry = ["special_student"]
print(all_students)
print(students_in_poetry)
while len(students_in_poetry) < 6:
    students_in_poetry.append(all_students.pop())
print(students_in_poetry)

 


