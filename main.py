import student,employee
import university
import logging as lg
lg.basicConfig(
    filename="main.log",
    level = lg.DEBUG,
    format = "[%(asctime)s - %(levelname)s]-%(message)s"
)


#main function
if __name__ == "__main__":
    uni = university.University("codegnan",["pfs","jfs","ds","da"])
    s1 = student.StudentDetails("vishnu","21bce8891","ds")
    s2 = student.StudentDetails("neha","21bce9574","ds")
    s3 = student.StudentDetails("vyshu","21mis7031","da")
    e1 = employee.Employee("srinu","1001","ds","cse","70000")
    e2 = employee.Employee("venkat","1002","da","IT","80000")
    e3 = employee.Employee("jai","1003","jfs","cse","50000")
    
    e = [e1,e2,e3]
    s = [s1,s2,s3]
    for i in s:
        print(uni.add_student(i))
    for i in e:
        print(uni.add_employee(i))
    uni.totalEmployee(search_subject = "ds")

    

