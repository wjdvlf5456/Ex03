'''
ifelse 4번
숫자를 입력받아
0이상이면 '양수' 아니면 '음수' 을 출력하세요
'''

num = int(input("숫자: "))

value = "양수" if num >= 0 else "음수"
print(value)