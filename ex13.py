def plus(a,b):
    sum = a+b
    return sum

result = plus(3,7)
print(result)

result = plus("3","한글")
print(result)

print("=======================================")
def sum_many(*data):
    #data = (1,2,3,4,5)
    #data = (1,2)
    sum = 0;
    for num in data:
        sum  = sum +num

    return sum

print(sum_many(1,2,3,4,5,6,7,8))
print("=======================================")
def sum_mul(mode):
    args = (1,2,3)

    print(mode)
    #더하기
    result = 0
    for i in args:
        result = result +i

    return result

print(sum_mul("sum"))#더하기

