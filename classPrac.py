class dog:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def display(self):
        print(f"Name : {self.name}\nAge : {self.age}")
    


d = dog("Charlie",5)

d.display()