class Area():
    PIE = 3.14
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def triangle(self):
        return self.width * self.height / 2

    def circle(self):
        return self.width * self.width * self.PIE

area = Area(10, 20)

print(area.square()) # 사각형의 넓이
print(area.triangle()) # 삼각형의 넓이
print(area.circle()) # 원의 넓이