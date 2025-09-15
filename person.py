import main
# base class person was created
class Person:
    # name parameter is added
    
    def __init__(self,name):
        self.name = name
        main.lg.debug("user in person class")
    # method creation
    def display(self):
        main.lg.debug(f"name of a person is {self.name}")
        return f"name of a person is {self.name}"