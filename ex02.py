# 과목번호를 입력받아 강의실 번호를 출력하는 프로그램을 작성하세요
# 과목 code값이
# 1이면 “R101호 입니다.”
# 2이면 “R202호 입니다.”
# 3이면 “R303호 입니다.”
# 4이면 “R404호 입니다.”
# 나머지는 “상담원에게 문의하세요”
# 를 출력하세요

num = input("과목번호: ")
num = int(num)              #형변환 미적용시 전부 상담원으로 간다.
print(num)

if num == 1:
    print("R101호 입니다.")
elif num == 2:
    print("R202호 입니다.")
elif num == 3:
    print("R303호 입니다.")
elif num == 4:
    print("R404호 입니다.")
else:
    print("상담원에게 문의하세요")