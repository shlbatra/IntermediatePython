class person(object):
    
    population=50 #class variable 
    
    def __init__(self,name,age): #constructor method 
        self.name=name
        self.age=age 
        
    @classmethod 
    def getPopulation(cls):  #class method - ex. call it on any instance of class. not reqd object of class. parameter passed is a class here
        #access anything in class that is public in class
        return cls.population 
    
    @staticmethod
    def isAdult(age):  #static method. called without using class or object. not send class or object parameter, used when not need object, 
        #store methods in class. ex. ,math.round() , math.abs(), not access class parameters - just the ones passed as parameters. 
        return age >= 18 
    
    def display(self):
        print(self.name, ' is ', self.age, ' years old')
        

newPerson=person('Time',18)
print(person.getPopulation()) #can be called directly from class without creating object for that class.
print(newPerson.getPopulation()) 

print(person.isAdult(20))
print(newPerson.isAdult(17))