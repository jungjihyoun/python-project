class Person:
    def __init__(self, name):
        self.name = name

    def set_account(self, account):
        self.account = account


class Account:
    def __init__(self):
        self.__rest = 0

    def get_rest(self):
        return self.__rest

    def set_owner(self, owner):
        self.owner = owner

    def send(self, money, receiver):
        print("{}원을 송금하였습니다".format(money))
        receiver.account.__rest += money

    def deposit(self, money):
        self.__rest += money

    def withdraw(self, money):
        self.__rest -= money


jihyoun_person = Person("jihyoun")
jihyoun_account = Account()
jihyoun_person.set_account(jihyoun_account)
jihyoun_account.set_owner(jihyoun_person)

sungjoo_person = Person("sungjoo")
sungjoo_account = Account()
sungjoo_person.set_account(sungjoo_account)
jihyoun_account.set_owner(sungjoo_person)

jihyoun_account.deposit(10000)
jihyoun_account.send(5000, sungjoo_person)

# 남은 돈 확인
print(jihyoun_account.get_rest())
