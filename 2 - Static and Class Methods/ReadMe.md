- Both methods are part of class
- need to use decorator to make a method static or class method 
- class method - Call it on any instance of class or class itself.Parameter passed is a class here ex. cls. This method can access anything in class that is public in class.
- static method - it is called without using class or object. In this method, we do not send class or object parameter, it is used to store methods in class. ex. ,math.round() , math.abs(). Static methods can not access class parameters - just the ones passed as parameters. 