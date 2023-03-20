- Dunder methods are part of Python DataModel
- Syntax such as + - and other basic operators on list object or any user defined class is implemented under the hood using dundar methods
- Link -> https://docs.python.org/3/reference/datamodel.html
- Examples 
    - print -> __repr__
    - + -> __add__
    - - -> __sub__
    - () -> __call__
- You can modify existing built in classes and extend from that class to your class and add any dunder method that is useful in your case but not already defined before