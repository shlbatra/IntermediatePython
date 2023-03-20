#Example 2
#use the code multiple times and change it in the future: split the code in classes/methods/function +more make readable and debug-able
#Number guessing game 
'''
how reuse code in future ?
1. Change number then change at two places -> not optimal as human error. if game complex, then change number at multiple places - so use constant
2. Change range from 0-100 where printed
3. run this code with random guessing number -> it wont work 

guess=1
while True:
    num=input("Guess number between 0-100 :")
    try:
        num=int(num)
    except:
        print("Invalid number, guess again")
        continue 
    
    if num < 45:
        print("guess was under")
    elif num > 45:
        print("guess was over")
    else:
        break 
    
    guess+=1
print(f"you guessed it in {guess} guesses")
'''
'''
Soln2 
Class that is scalable, flexible and work multiple times 
reuse code - when change value so use class that handle that change for us
Reuse code again by creating new objects with new number

Things that are coehsive within class and functions - methods that perform a certain operation/task. If change one aspect of code, 
change code in 1 method. Method not have side effects -> they modify value/change/call methods if not necessary. Fn do one thing only. 

dont put all code in 1 mega method -> run in bug then difficult determine where bug is exactly - test each method individually and check if it is functioning correctly

'''

class GuessNumber():
    def __init__(self,number,mn=0,mx=100):#design flexibility - optional arguments with standard case
        self.number=number
        self.guesses=0
        self.mn=mn
        self.mx=mx
        
    def get_guess(self):  #gets guess from user
        guess = input(f"Guess number between ({self.mn} - {self.mx})")
        
        if self.valid_number(guess): #another method checking if number input is valid or not
            return int(guess)
        else:
            print("Please enter valid number")
            return self.get_guess()
        
    def valid_number(self,str_number):
        try:
            number=int(str_number)
        except:
            return False 
        return self.mn <= number <= self.mx
    
    def play(self):
        while True:
            self.guesses+=1
            guess=self.get_guess()
            
            if guess < self.number:
                print("guess was under")
            elif guess > self.number:
                print("guess was over")
            else:
                break 
        print(f"you guessed it in {self.guesses} guesses")
        
game=GuessNumber(56)
game.play()  
        



