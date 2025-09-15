import student,employee
import main
class University:
    def __init__(self,university_name:str,courses_lst:list[str]):
        self.university_name = university_name
        self.courses_lst = courses_lst
        self.students_lst = {}
        self.employee_lst = {}
        main.lg.debug("user in university class")
    def add_student(self,student):
        main.lg.debug("user in add_student method")
        if student.roll_number not in self.students_lst:
            self.students_lst[student.roll_number] = [student.name,student.branch,student.email]
            main.lg.info("student successfully added into university")
            return "student successfully added into university"
        else:
            main.lg.warning("student is already existed")
            return "student is already existed"
    def add_employee(self,employee):
        main.lg.debug("user in add_employee method")
        if employee.employee_id not in self.employee_lst:
            self.employee_lst[employee.employee_id] = [employee.name,employee.subject,employee.branch,employee.salary]
            main.lg.info("employee successfully added into university")
            return "employee successfully added into university"
        else:
            main.lg.warning("employee is already existed")
            return "employee is already existed"
    def add_course(self,new_course):
        main.lg.debug("user in add_course method")
        if new_course not in self.courses_lst:
            self.courses_lst.append(new_course)
            main.lg.info(f"{new_course} is successfully added into course list")
            return f"{new_course} is successfully added into course list"
        else:
            main.lg.warning(f"{self.new_course} is already existed")
            return f"{self.new_course} is already existed"
    def totalStudents(self,branch_name:str=None,search_id:str=None):
        main.lg.debug("user in totalstudents method")
        if branch_name:
            for item in self.students_lst.items():
                if item[1][1] == branch_name:
                    main.lg.info(item)
                    print(item)
        elif(branch_name and search_id):
            for item in self.students_lst.items():
                if item[1][1] == branch_name and item[1] == search_id:
                    main.lg.info(item)
                    print(item)
        else:
            for item in self.students_lst.items():
                main.lg.info(item)
                print(item)


        def totalEmployee(self,search_branch:str=None,search_subject:str=None):
            main.lg.debug("user in totalemployees method")
            if search_branch:
                for item in self.employee_lst.items():
                    if item[1][2] == search_branch:
                        main.lg.info(item)
                        print(item)
            elif(search_branch and search_subject):
                for item in self.employee_lst.items():
                    if item[1][2] == search_branch and item[1][1] == search_subject:
                        main.lg.info(item)
                        print(item)
            elif(search_subject):
                for item in self.employee_lst.items():
                    if item[1][1] == search_subject:
                        main.lg.info(item)
                        print(item)
            else:
                for item in self.employee_lst.items():
                    main.lg.info(item)
                    print(item)
