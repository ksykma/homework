import random
import time
from datetime import datetime

def main():
    num = int(input("자릿수를 입력하세요 : "))
    baseball = set()

    while len(baseball) < num:
        baseball.add(random.randint(0,9))
    baseball = list(baseball)
    random.shuffle(baseball)
    print(baseball)

    start_time = time.time()
    try_count = 0

    while True:
        input_number = input("숫자를 입력하세요 : ")
        if input_number == "exit":
            return
        try_count += 1
        out_count = 0
        ball_count = 0
        strike_count = 0
        for i, b in enumerate(input_number):
            b = int(b)
            if b not in baseball:
                out_count += 1
            else:
                if baseball[i] == b:
                    strike_count += 1
                else:
                    ball_count += 1
        if strike_count == num:
            print("정답입니다!")
            print(f"시도 횟수 : {try_count}")
            print(f"실행 시간 : {time.time()-start_time:.2f}")
            print(f"종료 날짜 및 시각 : {datetime.now()}")
            return

        print(f"{ball_count}볼 {strike_count}스트라이크 {out_count}아웃")
main()