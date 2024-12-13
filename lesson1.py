class Person:
    def __init__(self, full_name, age, is_married):
        self.full_name = full_name
        self.age = age
        self.is_married = is_married

    def introduce_myself(self):
        return f'{self.full_name}, {self.age}, {self.is_married}'


class Student(Person):
    def __init__(self, full_name, age, is_married, marks):
        super().__init__(full_name, age, is_married)
        self.marks = marks

    def gpa(self):
        summa = sum(self.marks.values())
        average = round(summa / len(self.marks), 1)
        return average


class Teacher(Person):
    def __init__(self, full_name, age, is_married, experience):
        super().__init__(full_name, age, is_married)
        self.experience = experience

    base_salary = 40000

    def salary(self):
        if self.experience > 3:
            final_salary = self.base_salary + (self.base_salary * 0.05 * self.experience)
            return final_salary
        else:
            return self.base_salary


teacher1 = Teacher('Авазкан кызы Таласкан', 35, True, 5)
print(teacher1.introduce_myself())
print(teacher1.salary())


def create_students():
    students = []
    student1 = Student('Адилет Толобаев', 14, False, {'math': 6, 'rus': 2, 'engl': 5})
    student2 = Student('Тендик Туратбеков', 36, False, {'math': 3, 'rus': 3, 'engl': 4})
    student3 = Student('Чынгыз Керинбаев', 27, False, {'math': 5, 'rus': 2, 'engl': 4})
    students.append(student1)
    students.append(student2)
    students.append(student3)
    return students


student = create_students()
for i in student:
    print(i.introduce_myself())
    print(i.gpa())
