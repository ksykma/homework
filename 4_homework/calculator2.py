class Calc():
    def set_number(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def plus(self):
        try:
            result = self.num1 + self.num2
            return result
        except ValueError:
            print("숫자만 입력 가능합니다")
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다")

    def minus(self):
        try:
            result = self.num1 - self.num2
            return result
        except ValueError:
            print("숫자만 입력 가능합니다")
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다")

    def multiple(self):
        try:
            result = self.num1 * self.num2
            return result
        except ValueError:
            print("숫자만 입력 가능합니다")
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다")

    def divide(self):
        try:
            result = self.num1 / self.num2
            return result
        except ZeroDivisionError:
            print("0으로 나눌 수 없습니다")
        except ValueError:
            print("숫자만 입력 가능합니다")

calc = Calc()
calc.set_number('a', 'd')

print(calc.plus()) # 더한 값
print(calc.minus()) # 뺀 값
print(calc.multiple()) # 곱한 값
print(calc.divide()) # 나눈 값