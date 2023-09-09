#Task I
def loading_screen():
    print("This page is loading...")

loading_screen()


#Task II
def mult_x_add_y(number,x,y):
    print(number*x+y)

mult_x_add_y(5,6,7)


#Task III
def user(some):    
    return 20-some
print(user(int(input("What is your awesomness?"))))


#Task IV
def multireturn(a,b):
    return a-b, a+b
x,y=multireturn(5,2)
print(x)
print(y)
 

#Task V
def user(x):
    if x == 1:
        return 1
    else:
        return (x*user(x-1))
x = int(input("what is your number?"))
print("your factorial is", user(x))





