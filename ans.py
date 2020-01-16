class Student:
    def __init__(self, id, grade_list):
        self.__id = id
        self.__grade_list = grade_list

    def get_id(self):
        return self.__id

    def get_grade_list(self):
        return self.__grade_list


class AvgCalculator:
    def __init__(self):
        self.__dict = {}

    def calc_avg_grade(self, id, grade_list):
        sum = 0
        for grade in grade_list:
            sum += grade
        avg = sum / 3

        self.__dict[id] = avg

    def __str__(self):
        keys_list = list(self.__dict.keys())
        keys_list.sort()
        result = ""
        for key in keys_list:
            result += "Studetn ID : %s, Average Grade: %f\n" % (key, self.__dict[key])
        return result


stu1 = Student(id="2015104221", grade_list=[30, 60, 60])
stu2 = Student(id="2019311060", grade_list=[80, 70, 90])
stu3 = Student(id="2016105323", grade_list=[20, 30, 40])

calculator = AvgCalculator()
calculator.calc_avg_grade(stu1.get_id(), stu1.get_grade_list())
calculator.calc_avg_grade(stu2.get_id(), stu2.get_grade_list())
calculator.calc_avg_grade(stu3.get_id(), stu3.get_grade_list())
print(calculator)