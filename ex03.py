num = int(input("숫자를 입력해주세요."))

# value에는 조건식이 true일 때 출력값
# 가운데에는 조건식 else 뒤에는 false 일 때 출력값을 넣어준다.
value = "big" if num >= 5 else "small"
print(value)