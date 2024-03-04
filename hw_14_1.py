class UserException(Exception):

    def __init__(self, massage):
        super().__init__()
        self.massage = massage

    def get_exception_message(self):
        return print(self.massage)


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f'I am {self.last_name}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name
        self.record_book = record_book

    def __str__(self):
        return self.last_name


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) < 10:
            self.group.add(student)
        else:
            raise UserException('More than 10 students!')

    def delete_student(self, last_name):
        return self.group.discard(self.find_student(last_name))

    def find_student(self, last_name):
        group_list = []

        for student_ in self.group:
            group_list.append(student_.last_name)

            if last_name in group_list:
                return student_

    def __str__(self):
        all_students = ''
        self.number = 0

        for everyone_ in self.group:
            self.number += 1
            all_students += everyone_.last_name + ' '

        return f'Number:{self.number}\n{all_students}\n'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 29, 'Guido', 'van Rossum', 'AN146')
st4 = Student('Female', 22, 'Taylor', 'Swift', 'AN148')
st5 = Student('Male', 42, 'Homer', 'Simpson', 'AN150')
st6 = Student('Female', 23, 'Gretha', 'Thunberg', 'AN170')
st7 = Student('Male', 40, 'Joe', 'Rogan', 'AN295')
st8 = Student('Female', 30, 'Jennifer', 'Aniston', 'AN145')
st9 = Student('Male', 41, 'Yoshihiro', 'Fukuyama', 'AN145')
st10 = Student('Female', 19, 'Billie', 'Eilish', 'AN145')
st11 = Student('Male', 26, 'Max', 'Verstappen', 'AN145')

list_students = (st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11)

gr = Group('PD1')


try:
    for i in range(len(list_students)):
        gr.add_student(list_students[i])
except UserException:
    print('A group cannot have more than 10 students')
finally:
    print('The student limit has been verified')


print(gr)


assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод пошуку має повертати екземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!