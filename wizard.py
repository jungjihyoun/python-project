# 마법사 클래스를 만든다
class Wizard:
    # 생성자
    def __init__(self, name):
        self.name = name  # 이름을 결정합니다
        self.__hp = 10  # hp를 10으로 초기화합니다
        self.__mp = 90  # mp를 90으로 초기화힙니다

    # 스킬
    # hp를 다시 세팅할 수 있도록 합니다
    def set_hp(self, input_hp):
        if input_hp > 10:
            print("마법사의 hp는 10을 넘지 못합니다")
        elif 0 < input_hp < 10:
            print("마법사의 hp가 결정되었습니다")
            self.__hp = input_hp
        else:
            print("최소 hp는 1입니다")

    def get_hp(self):
        return self.__hp

    def fire_ball(self):
        print("파이어볼!")
        self.__mp -= 10


my_first_wizard = Wizard("정지현")
my_first_wizard.set_hp(99999999999)
my_first_wizard.set_hp(-100)
my_first_wizard.set_hp(5)
print(my_first_wizard.get_hp())
my_first_wizard.fire_ball()
print()


# Wizard 클래스를 상속받은 FireWizard 클래스를 만들자
class FireWizard(Wizard):
    # 생성자
    def __init__(self, name):
        # 부모의 생성자를 일단 호출하고
        super().__init__(name)
        # 추가로 세팅하고 싶은 변수를 세팅한다
        self.fire_love = 99

    # 부모 클래스의 모든 스킬을 사용할 수 있다
    # 새로운 스킬을 만들 수 있다
    def double_fire_ball(self):
        self.fire_ball()
        self.fire_ball()


my_second_wizard = FireWizard("파이어 정지현")
my_second_wizard.set_hp(9)
print(my_second_wizard.get_hp())
my_second_wizard.double_fire_ball()