 class book():
    def __init__(self, title, author): 
        self.title = title    
        self.author = author
    def get_title(self):
        return "Title: " + self.title 
    def get_author(self):
        return "Author: " + self.author
PP = book("pride and pragides", "jane ostin")
H = book("Hamlet", "william shakespear")
WP = book("war and peace", "lea Tolstoe") 
print(PP.get_title())
print(H.get_title())
print(WP.get_title())
print(PP.get_author())
print(H.get_author())
print(WP.get_author())  

class Employee:
	def __init__(self, firstname, lastname):
		self.firstname = firstname
		self.lastname = lastname
fullname = ("john", "smith")
email = ("john 40")
print(email.format())



       


    