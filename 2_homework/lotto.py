import random
import time
from datetime import datetime

# CASE 1
"""
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(number_list)

random_numbers = number_list[0:length] # 0:5

print(random_numbers)
"""
# CASE 2
"""
number_list = [x for x in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

random_numbers = []

for _ in range(length):
    random_numbers.append(number_list.pop(random.randrange(0, len(number_list))))

print(random_numbers)
"""


# CASE 3
def main():
    length = int(input("자릿수를 입력해주세요 : "))
    random_numbers = set()

    while len(random_numbers) < length:
        random_numbers.add(random.randint(0, 9))

    random_numbers = list(random_numbers)
    random.shuffle(random_numbers)
    print(random_numbers)

    start_time = time.time()
    try_count = 0

    while True:
        input_number = input("값을 입력해주세요 (종료 - exit): ")
        if input_number == "exit":
            return

        try_count += 1
        out_count = 0

        ball_count = 0
        strike_count = 0

        for i, v in enumerate(input_number):
            v = int(v)
            if v not in random_numbers:  # 포함돼있지 않은 경우
                out_count += 1

            else:  # 포함돼 있는 경우
                if random_numbers[i] == v:
                    strike_count += 1
                else:
                    ball_count += 1

        if strike_count == length:
            print("########################")
            print("정답입니다!!")
            print(f"소요 시간 : {time.time() - start_time:.2f}")
            print(f"클리어 일자 : {datetime.now()}")
            print(f"도전 횟수 : {try_count}")
            print("########################")
            return

        print(f"{ball_count}볼 {strike_count}스트라이크 {out_count}아웃")


main()