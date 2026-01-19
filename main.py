"""course class"""
class Course:                   
    def __init__(self, course_name):
        self.course_name = course_name

    def get_course_name(self):
        return self.course_name
    

"""student class"""   
class Student:                  
    def __init__(self, name, roll, password):
        self.name = name
        self.roll = roll
        self.__password = password #Private variable     
        self.courses = []

    def enroll_course(self, course):
        self.courses.append(course)
        self.__save_to_file(course)

    def __save_to_file(self,course):
        with open("students.txt","a") as file:
            file.write(
                f"Name: {self.name}, Roll: {self.roll}, Course: {course.get_course_name()}\n"
            )

    def get_password(self): #Getter Method                
        return self.__password

"""Read Data"""   
def show_all_students():                   
    try:
        with open("students.txt", "r") as file:
            print("\n___ALL ENROLLED STUDENTS__")
            for line in file:
                print(line.strip())

    except FileNotFoundError:
        print("NO STUDENT FOUNDED!")


"""Testing Part"""
course1 = Course("Python")
course2 = Course("Django")

student1 = Student("sami", 101, "sami@123")

student1.enroll_course(course1)
student1.enroll_course(course2)

password = student1.get_password()

show_all_students()


