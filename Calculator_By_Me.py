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


wish = int(input("Enter Number(1; 2; 3; 4): "))
if(wish > 4):
    print("Please Type Numbers Between 1 and 4! ")
    
if(wish > 0 and wish < 5):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
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