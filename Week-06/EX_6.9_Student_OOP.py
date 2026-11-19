class Student:
    school = "YearUp Academy"

    def __init__(self, name, grade, track):
        self.name = name
        self.__grade = grade
        self.track = track

    def get_grade(self):
        return self.__grade

    def set_grade(self, new_grade):
        if 0 <= new_grade <= 100:
            self.__grade = new_grade
        else:
            print("Invalid grade! Must be 0-100.")

    def display_info(self):
        print(f"""===== YearUp Academy - Student Report =====
School : {Student.school}
Name   : {self.name}
Grade  : {self.get_grade()}
Track  : {self.track}
===========================================""")


student1 = Student("Ricardo", 95, "Data Analytics")
student2 = Student("Brian", 88, "Software Development")

print(f"{student1.name}'s starting grade: {student1.get_grade()}")
print(f"{student2.name}'s starting grade: {student2.get_grade()}")

student1.set_grade(98)
student1.set_grade(150)
student2.set_grade(90)
student2.set_grade(-5)

print(f"{student1.name}'s final grade: {student1.get_grade()}")
print(f"{student2.name}'s final grade: {student2.get_grade()}")

student1.display_info()
student2.display_info()
