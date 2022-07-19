print("숫자를 입력해 주세요")

num = input("숫자: ") #input == 자바의 스캐너
#print(num, type(num))

num = int(num)
#print(num,type(num))

if num > 0 :
    print("양수")
elif num < 0:
    print("음수")
else:
    print("0입니다.")