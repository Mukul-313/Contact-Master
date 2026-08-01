# class Person:
#     first_name="Mukul"  # class Variable
#     def __init__(self,first_name,Last_name):
#         self.Last_name=Last_name

# p1=Person('Mukul','Gupta')
# print(p1.first_name,p1.Last_name)


# class Laptop:
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = price
#     def percentage_off(self,num):
#        off = (num//100)*self.price
#        return self.price - off
# obj=Laptop('Consistence','H61','65000')
# # print(f"Brand Name is {obj.brand_name}")
# # print(f"Model Name is {obj.model_name}")
# # print(f"Price is {obj.price}")

# # print(obj.percentage_off(20))

# print(obj.__dict__)   

# class Person:
#     count_instance=0 # CLASS VARIABLE/CLASS ATTRTIBUTE
#     def __init__(self,first_name,last_name,age): # Constructor 
#         Person.count_instance += 1
#         self.first_name = first_name #INSATANCE VARIABLE
#         self.last_name = last_name 
#         self.__age = age # NAME MANGLING 
#     def full_name(self):
#         return f"{self.first_name} {self.last_name}"
    
#     @classmethod
#     def from_string(cls,string):
#         first,last,age=string.split(',')
#         return cls(first,last,age)
    
#     @staticmethod 
#     def hello():
#         print("Static mrthod called")

# p1=Person('mukul','gupta',24)   # CLASS INSTANCE
# p2=Person('mukul','gupta',24)
# p3=Person('mukul','gupta',24)
# print(Person.count_instance)
# print(p1.full_name())

# p4=Person.from_string('Mukul,Gupta,19')
# print(p4.full_name())
# print(Person.hello()) 

# class Phone:
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = max(price,0)
#     @property   
#     def complete_specification(self):
#       return  f"{self.brand_name} {self.model_name} and price is {self.price}"
    


#     def make_a_call(self,phone_number):
#         print(f"calling {phone_number}...")

#     def full_name(self):
#         return f"{self.brand_name} {self.model_name}"

# phone1=Phone('Nokia','1100',1000)

# print(phone1.brand_name)
# print(phone1.model_name)
# phone1.price=1500
# print(phone1.price)
# print(phone1.complete_specification)


                #INHERITANCE



class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        
    def make_sound(self):
        print("Sound made by the animal")

class Cat(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self, name, species="Cat")
        self.breed = breed
        
    def make_sound(self):
        print("Meaow!")

obj1 = Cat("Cat", "Hell Cat")
obj1.make_sound()

# class Phone: #BASE CLASS / PARENT CLASS
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = max(price,0)
    
#     def make_a_call(self,phone_number):
#         print(f"calling {phone_number}...")

#     def full_name(self):
#         return f"{self.brand_name} {self.model_name}"
    


# class Smartphone(Phone): # DERIVED CLASS / CHILD CLASS
#     def __init__(self,brand_name,model_name,price,ram,internal_memory,rear_camera):
#         # Phone.__init__(self,brand_name,model_name,price) # UNCOMMON WAY 
#         super().__init__(brand_name,model_name,price)  # SUPER METHOD
#         self.ram=ram
#         self.internal_memory=internal_memory
#         self.rear_camera=rear_camera

#     def make_a_call(self,phone_number):
#         print(f"calling {phone_number}...")

#     def full_name(self):
#         return f"{self.brand_name} {self.model_name}"
    
# phone1=Phone('Nokia','1100',1000)
# smartphone=Smartphone('Redmi','Note 9',13000,'6GB','128GB','48MP')
# print(phone1.full_name())
# print(smartphone.full_name()+f" price is {smartphone.price}")

                    # MULTILEVEL INHERITANCE 

# class Phone: #BASE CLASS / PARENT CLASS
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = max(price,0)
    
#     def make_a_call(self,phone_number):
#         print(f"calling {phone_number}...")

#     def full_name(self):  # POLYMORPHISM
#         return f"{self.brand_name} {self.model_name}"
    


# class Smartphone(Phone): # DERIVED CLASS / CHILD CLASS
#     def __init__(self,brand_name,model_name,price,ram,internal_memory,rear_camera):
#         # Phone.__init__(self,brand_name,model_name,price) # UNCOMMON WAY 
#         super().__init__(brand_name,model_name,price)  # SUPER METHOD
#         self.ram=ram
#         self.internal_memory=internal_memory
#         self.rear_camera=rear_camera

#     def make_a_call(self,phone_number):
#         print(f"calling {phone_number}...")

#     def full_name(self):  # POLYMORPHISM / METHOD OVERIDING
#         return f"{self.brand_name} {self.model_name} and price is {self.price}"

# class Flagship(Smartphone):
#     def __init__(self, brand_name, model_name, price, ram, internal_memory, rear_camera,front_camera):
#         super().__init__(brand_name, model_name, price, ram, internal_memory, rear_camera)
#         self.front_camera=front_camera 


# flagship=Flagship('Redmi','Note 9',13000,'6GB','128GB','48MP','13MP')
# print(flagship.full_name())


#                       #METHOD RESOLUTION ORDER

# # print(help(flagship))


#                       # IS INSTANCE IS SUBCLASS

# print(isinstance(flagship,Flagship)) # CHECK OBJECT AND CLASS
# print(issubclass(Smartphone,Phone)) # CHECK WEITHER THE CLASS IS SUBLASS OR NOT 

                        # DUNDER METHODS 

# class Phone: #BASE CLASS / PARENT CLASS
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name = brand_name
#         self.model_name = model_name
#         self.price = max(price,0)

#     def full_name(self):
#         return f"{self.brand_name} {self.model_name}"
    
#                         # STR & REPR 

#     def __str__(self):
#         return  f"{self.brand_name} {self.model_name}"

#     def __repr__(self):
#         return  f"Phone({self.brand_name} {self.model_name} {self.price})"   # SAME AS OBJECT   

#     def __len__(self):
#         return len(self.full_name())
    
#     def __add_(self,other):
#         return self.price + other.price



# my_phone=Phone('Redmi','Note 9',13000)
# my_phone1=Phone('Redmi','Note 9',10000)
# print(str(my_phone))
# print(my_phone.__repr__())
# print(len(my_phone))
# print(my_phone + my_phone1)

# from abc import ABC, abstractmethod

# class Animal(ABC):
#     @abstractmethod
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print("Woof!")

# class Cat(Animal):
#     def make_sound(self):
#         print("Meow!")

# R = Dog()
# R.make_sound()

# K = Cat()
# K.make_sound()