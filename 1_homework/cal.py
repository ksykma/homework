def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b != 0:
        return a / b
    else:
        print('잘못된 수식')



num1 = int(input())
num2 = int(input())
operator = input()


if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    if num2 == 0:
        print('0으로 나눌 수 없습니다.')
    else:
        print(num1 / num2)
else:
    print('잘못 입력 하셨습니다.')
