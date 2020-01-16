gradeset = {'A+': 4.3, 'A0': 4.0, 'A-': 3.7, 'B+': 3.4, 'B0': 3.1, 'B-': 2.8, 'C+': 2.5, 'C0': 2.2, 'C-': 1.9,
            'D+': 1.6,  'D0': 1.0, 'D-': 0.7, 'F': 0.0}


class Student:
    def __init__(self):
        self.name = None
        self.st_num = None
        self.grade = {}  # 과목별 성적 나타내주는 사전 (과목 : 시수, 성적) 형태
        pass

    def tell_grade(self, subject):
        if (subject in self.grade) == False:
            print('없는 과목')
            return None
        else:
            return self.grade[subject][1]
        pass

    def tell_grade_all(self):
        self.temp = 0
        self.temp_grade = 0
        for subject in self.grade:
            
            self.grade = self.grade[subject][1]
            self.temp_grade = (float)(self.time) * gradeset[self.grade]
            self.temp = self.temp + (int)(self.time)
        if self.temp == 0:
            print("입력 노")
            return 0
        else:
            self.temp_grade = (float)(self.temp_grade)/(float)(self.temp)
            return self.temp_grade
        pass

    def tell_name(selfself):
        return self.name
    def tell_s_num(self):
        return self.st_num

import classjihyoun

st_list = {}  #이름 클래스
command = ''

while not command == '종료':
    command = input("하실 작업 선택")
    if command == '학생추가':
        stdname = input("학생 이름 선택")
        st_list[stdname] = Student.student()
        stdnum = input("학번을 선택")
        st_list[stdname].st_num = stdnum

    elif command == '성적입력':
        stdname = input("학생 이름 선택")
        if (stdname in st_list) == True:
            print("성적을 갱신합니다 성적을 입력해주세요 끝날때는 과목 이름에다가 종료 입력")

            subject = None
            grade = None
            while not subject == '종료':
                subject = input("과목 이름 : ")
                if subject == '종료':
                    break
                time = input("강의 시수:")
                grade = input("학점:")
                st_list[stdname].grade[subject] = time,grade
            else:
                print("없는 사람이니 다시 선택 해주세요 \n")
        elif command == '학생정보확인':
            stdname = input("학생 이름 선택")
            if (stdname in st_list) ==True:
                command2 = input(" 무엇을 확인 하시겠습니까? 1. 학번 2. 성적(한 과목) 3.전체성적")
                if command2 == "1":
                    print(st_list[stdname].tell_st_num())
                elif command2 == "2":
                    command3 = input("성적을 확인할 과목은?")
                    if(command3 in st_list[stdname].grade) == True:
                        print('성적은 %s 입니다'%st_list[stdname].tell_grade(command3))
                    else:
                        print("없느 과목입니다")
                elif command2 == "3":
                    final_grade = st_list[stdname].tell_grade_all()
                    print("성적은 %d 입니다" %final_grade)
                else:
                    print("없는 입력값 입니다.")
            else:
                print("없는 입력값 입니다.")
        else:
            continue
