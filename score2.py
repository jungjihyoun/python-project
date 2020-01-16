class Student:
    def __init__(self, no=None, name=None, major=None, grade=None):
        self.no = no
        self.name = name
        self.major = major
        self.grade = grade

    def __str__(self):
        return '웅이대학 학부 -> 학번: %d, 이름: %s, 전공: %s, 학점: %s' % (self.no, self.name, self.major, self.grade)

    def changeMajor(self, newMajor):
        self.major = newMajor

    def changeGrade(self, newGrade):
        self.grade = newGrade

student1 = Student(190511, '홍길동', '토목과', 'A')
print(student1)
student1.changeMajor('건축과')
print(student1)
student1.changeGrade('B')
print(student1)

