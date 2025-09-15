#employee class is created and employee details as perameters
import main
import person
class Employee(person.Person):
    def __init__(self,name,employee_id,subject,branch,salary):
        super().__init__(name)
        self.employee_id = employee_id
        self.subject = subject
        self.branch = branch
        self.salary = salary
        main.lg.debug("user in employee class")
    def display_employee(self):
        print(super().display())
        main.lg.debug(f"employee id is {self.employee_id} and branch is {self.branch} and subject is {self.subject}")
        return f"employee id is {self.employee_id} and branch is {self.branch} and subject is {self.subject}"