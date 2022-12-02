class Person():
    def __init__(self, first_name, family, age, nationality):
        self.first_name = first_name
        self.family = family
        self.age = age
        self.nationality = nationality

    def print_names(self):
        print(self.first_name, self.family, self.age, self.nationality)


MyPerson = Person("Nikolay", "Kachev", 19, "Bulgarian")
MyPerson.print_names()


class Student(Person):
    def __init__(self, first_name, family, age, nationality, university, yearofstudy):
        super().__init__(first_name, family, age, nationality)
        self.university = university
        self.yearofstudy = yearofstudy

    def print_names(self):
        print(self.first_name, self.family, self.age, self.nationality, self.university, self.yearofstudy)


NewStudent = Student("Nikolay", "Kachev", 19, "Bulgarian", "Technical University of Sofia", "First-year")
NewStudent.print_names()
