import random


def rsp_game():
    rsp_list = ['가위', '바위', '보']
    computer_choice = random.choice(rsp_list)
    max_attempts = 1

    while True:
        user_input = input("가위, 바위, 보 중 하나를 선택하세요: ")

        guess = user_input

        if guess in rsp_list:
            print("사용자: ", guess), print("컴퓨터: ", computer_choice)

            if ((guess == '가위' and computer_choice == '보') or
                (guess == '바위' and computer_choice == '가위') or
                    (guess == '보' and computer_choice == '바위')):
                print("사용자 승리!")
                return "승"

            elif guess == computer_choice:
                print("비겼습니다!")
                return "무승부"

            else:
                print("컴퓨터 승리!")
                return "패"

        else:
            print("유효한 입력이 아닙니다")
            continue


def main():
    win_count = 0
    lose_count = 0
    tie_count = 0

    while True:
        result = rsp_game()

        if result == "승":
            win_count += 1
        elif result == "무승부":
            tie_count += 1
        elif result == "패":
            lose_count += 1

        rsp_re = input("다시 하시겠습니까? (y/n): ")
        if rsp_re.lower() != "y":
            print("게임을 종료합니다")
            print(f"승: {win_count} 패: {lose_count} 무승부: {tie_count}")
            break


if __name__ == "__main__":

    main()
