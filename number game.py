#숫자게임
import random
NUM_TRIES=4
user=-1
tries=0
com = random.randint(1,20)
while tries < NUM_TRIES and user != com:
    guess = int(input("기회가 %d번 남았습니다. 1-20 사이의 숫자를 맞춰보세요 :" %(NUM_TRIES - tries)))

    if guess > com:
        tries += 1
        print("Down")
    elif guess < com:
        tries += 1
        print("Up")

if user == com:
    print("축하합니다. %d번만에 숫자를 맞추셨습니다" %(tries))

else:
    print("아쉽습니다. 정답은 %d였습니다." % (com))



