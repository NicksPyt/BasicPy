names= ['nick', 'mary' ]
height = [ 42, 42]
students= { key:value for key, value in zip(names, height)}
print(students['nick'])


country = ["Turkey", "Austria", "France", "Georgia", "Germany", "Italy"]
capital = ["Ankara", "Vienna", "Paris", "Tbilisi", "Berlin", "Rome"]

country_capitals = {key:value for key,value in zip(country,capital)}
print(country_capitals) 

class Myclass:
    v = 5
my_instance = Myclass()  
print(type(my_instance)) 

    
class MyClass:
    def first_method():
        print("This is my first method")

my_instance = MyClass
print(MyClass)   



class MyClass:
    def return_list(self, input_list):
        return input_list

my_instance = MyClass()
answer = my_instance.return_list([1,2,3])
print(answer)





