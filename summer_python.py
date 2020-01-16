'''

#스트링 최소값 구하기
t1 = '45678966642646'

idx = 1

for i in range(len(t1)):
    if t1[i] > t1[idx]:
        idx = i
print("value = %s, index = %d " %(t1[idx] , idx))
'''


#selection sort
arr = [3,5,1,9,8,7,5,4]
n  = len(arr)
for i in range(0,n):
    index = i
    for j in range (i+1,n):
        if arr[index] > arr[j]:
            index = j

    temp = arr[i]
    arr[i] = arr[index]
    arr[index] = temp
print(arr)



#Bubble sort
arr = [5,1,4,2,8]
for s in range(len(arr)-1):
    for idx in range(1,len(arr)-s):
        if arr[idx-1] > arr[idx]:
            temp = arr[idx-1]
            arr[idx-1] = arr[idx]
            arr[idx] = temp
print(arr)




#reverse
arr = [3,5,1,7,9,2,6,]

n = len(arr)
for i in range(0,n):
    idx = i
    for j in range(i+1,n):
        if arr[idx] < arr[j]:
            idx = j
    arr[i],arr[idx] = arr[idx],arr[i]

print(arr)


# *drawing

n = int(input("Input your number"))
i = 1
while i <= n:
    j = 1
    while j <= i:
        print('*',end='')
        j += 1
    print()
    i += 1

# * reverse

n = int(input("Input your number"))
i = 1
while i <= n:
    j = 1
    while j <= ((n+1)-i):
        print('*',end='')
        j+=1
    print()
    i += 1


####################

def getsum1(*n):
    total = 0
    for i in n:
        total += i
    return total

def getMax(n):
    idx = 0
    for i in range(len(n)):
        if n[idx] < n[i]:
            idx = i
    return n[idx]

def wordcount(n,wd):
    cnt = 0
    for a in n:
        if wd == a:
            cnt += 1
    return cnt

def getsum2(a,b=1,c=1):
    total =  a+b+C
    return total

#####################

def gcd1(n1,n2):
    gcd_value = 1
    i = 2
    while i <= n1 and i <n2:
        if n1%i ==0 and n2%i == 0:
            gcd_value = i
        i += 1
    return gcd_value

def gcd2(a,b):    #a를 b로 나눈 나머지와 b의 최대공약수는 같다
    while (b != 0):
        temp = a%b
        a = b
        b = temp
    return a

def gcd3(a,b):
    if ( b==0 ):
        return a
    return gcd3(b, a%b)









