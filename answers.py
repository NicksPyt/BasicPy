#challenge 1
A) (miss)
B) there we can use zip function, it allows us to 
combine 2 element in one, then we use index locations To 
print each of them.
C) i think that we can use there zip function too. 
if we create 2 list for model and speed, we will be able 
to combine them  and print them together using 
index locations.
#challenge 2
A) to get anything on display we need print() function
so this code have not any print element. then i think 
letter should be defined and has some value.
B) False
C)in the method "__init__" we definitely need "self" argument
combine them:
     class User:
   def __init__(self, user_name):
       self.user_name = user_name
D)first argument of the "__init__" method is self and this
argument should be definitely first
#challenge 3
 we can easily use split() method to reverse words,
 for example: 
     some_word = "i'm studing python"
     word = some_word.split()
and then with adding other stufs we will get reversed sentence.
#challenge 4
 (miss)
#challenge 5
A) args - syntax *args in function definitions in 
python is used to pass a variable number of arguments to a
 function. It is used to pass a non-key worded, 
 variable-length argument list. 
 
 kwargs - We use the name kwargs with the double star. 
 The reason is because the double star allows us to 
 pass through keyword arguments.
B) def find_word(arg, x):
    if arg in x:
        print(str(arg) +  " is inside the list")
    else:
        print(str(arg) +  " is not  in the list")
x = [1, "food", 2, "fruit", 3, "juice", 4, "Hello"]
find_word("fruit", x)

C) (miss)
#challenge 6
there is my calculator with few mistakes :D :
class calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def add(x, y):
        return x + y
    def subtract(x, y):
        return x - y
    def multiply(x, y):
        return x * y
    def divide(x, y):
        return x / y

print("Select operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")


wish = input("Enter Number(1; 2; 3; 4): ")
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")
if wish in ('1', '2', '3', '4'):
    if wish == '1':
            print(num1 + num2)
    elif wish == '2':
            print(num1 - num2)
    elif wish == '3':
            print(num1 * num2)
    elif wish == '4':
            print(num1 / num2)
else:
    print("Invalid Input")

