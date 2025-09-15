# student class is created and  student details as parameters
import main
import person
class StudentDetails(person.Person):
    
    def __init__(self,name,roll_number,branch,email:str=None):
        super().__init__(name)
        self.roll_number = roll_number
        self.branch = branch
        self.email = email
        main.lg.debug("user in student class")
    def display_student(self):
        print(super().display())
        main.lg.debug(f"student roll number is {self.roll_number} and branch is {self.branch}")
        return f"student roll number is {self.roll_number} and branch is {self.branch}"