import random

class Person:
    def __init__(self,name,age,sex):
        self.__name = name
        self.__age = age
        self.__sex = sex
        self.__useraccount = Account(self.__name)

    def get_account(self):
        return self.__useraccount

    def deposit(self):
        self.get_account().deposit(self.money)

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_sex(self):
        return self.__sex
    def get_account(self):
        return self.__useraccount
    def send(self, receiver , money):
        self.__useraccount.send(receiver,money)

    def __str__(self):
        userinform = print(" User name : %s \n User age : %s \n User sex : %s"%(self.get_name(),self.get_age(), self.get_sex()))

#상속
class VipPerson(Person):
    def __init__(self,name,age,sex,vipnumber):
        super().__init__(name,age,sex)
        self.__vipnumber = vipnumber

    def send(self, receiver, money):
        super().send(receiver, money)
        receiver.get_account().deposit(1000)



class Account:
    def __init__(self, name):
        self.__name = name
        self.__account_number = self.set_account()
        self.__rest = 0
    def get_account_number(self):
        return self.__account_number

    # 계좌번호 생성 (0000-0000 하고싶은데 어떻게 하는지 모르겠음)
    def set_account(self):
        everyaccount = []
        while True:
            randomnumber = random.randint(1, 1000)
            if randomnumber not in everyaccount:
                everyaccount.append(randomnumber)
                account_number = randomnumber
                print("%s new account number is %d ."%(self.__name, randomnumber))
                break
        return account_number

    # 남은 돈 확인시
    def get_rest(self):
        return self.__rest

    def set_owner(self, owner):
        self.__owner = owner

    # 예금
    def deposit(self, money):
        self.__rest += money
    # 출금
    def withdraw(self, money):
        self.__rest -= money

    #송금
    def send(self, reciver, money):
        while True:
            check = int(input("%s 씨에게 입금하는것이 맞습니까 ? (맞으면1 틀리면 0) :" % reciver. get_name()))
            if check == 1 :
                print("{}원을 송금하였습니다".format(money))
                reciver.get_account().deposit(money - 1000) #수수료천원

                break
            elif check == 0 :
                print("수취자를 확인해 주십시오. 입금 프로그램을 종료합니다. 재실행 하십시오")
                break

    def __str2__(self):
        accountinfor = print(" User account : %s \n Uzser account rest : %s " % (self.get_account_number(), self.get_rest()))


#객체 생성 인풋값

name=input("이름을 입력하세요:")
age = int(input("나이를 입력하세요:"))
sex = input("성별을 입력하세요 : ")

person1 = Person(name ,age , sex)
person1.__str__()
person1.get_account().__str2__()


name=input("이름을 입력하세요:")
age = int(input("나이를 입력하세요:"))
sex = input("성별을 입력하세요 : ")

person2 = Person(name,age,sex)
person2.__str__()
person2.get_account().__str2__()

name=input("이름을 입력하세요:")
age = int(input("나이를 입력하세요:"))
sex = input("성별을 입력하세요 : ")

jihyoun =VipPerson("jihyoun",name,age,sex)



person1.send(person2,1000)

