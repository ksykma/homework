class Calc():
    def set_number(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def plus(self):
        result = self.num1 + self.num2
        return result

    def minus(self):
        result = self.num1 - self.num2
        return result
    def multiple(self):
        result = self.num1 * self.num2
        return result
    def divide(self):
        result = self.num1 / self.num2
        return result

calc = Calc()
calc.set_number(20, 10)

print(calc.plus()) # 더한 값
print(calc.minus()) # 뺀 값
print(calc.multiple()) # 곱한 값
print(calc.divide()) # 나눈 값