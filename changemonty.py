# 원(￦)에서 달러($)로 바꿔주는 함수
def krw_to_usd(won):
    return won / 1000


# 달러($)에서 엔(￥)로 바꿔주는 함수
def usd_to_jpy(dollars):
    return dollars / (8 * 1000)


# 원(￦)으로 각각 얼마인가요?
amounts = [1000, 2000, 3000, 5000, 8000, 13000, 21000, 34000]
print("한국 화폐: " + str(amounts))

# amounts를 원(￦)에서 달러($)로 바꿔주기
i = 0
while i < len(amounts):
    amounts[i] = krw_to_usd(amounts[i])
    i += 1

# 달러($)로 각각 얼마인가요?
print("미국 화폐: " + str(amounts))

# amounts를 달러($)에서 엔(￥)으로 바꿔주기
j = 0
while j < len(amounts):
    amounts[j] = usd_to_jpy(amounts[j])
    j += 1
print("일본 화폐: " + str(amounts))
