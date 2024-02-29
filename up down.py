import random


def check_int(s):
    if s.isdigit() is True:
        return int(s)
    elif s[0] in ('-', '+'):
        if s[1:].isdigit() is True:
            return int(s[1:])
    else:
        return False


def number_game():
    random_number = random.randint(1, 100)
    max_attempts = 7
    attempts = 0

    while attempts < max_attempts:
        user_input = input("업 다운 게임 기회 7번 숫자를 입력하세요: ")

        guess = check_int(user_input)

        if not guess:
            print("숫자를 입력해주세요")
            continue

        if guess < 1 or guess > 100:
            print("유효한 범위 내의 숫자를 입력하세요")
            continue

        attempts += 1

        if guess < random_number:
            print("업")
        elif guess > random_number:
            print("다운")
        else:
            print("정답입니다! 시도 횟수:", attempts)
            break
    else:
        print("입력횟수를 초과했습니다 게임오버")
        attempts = 0

    return attempts


def main():
    best_score = float('inf')

    while True:
        attempts = number_game()
        if attempts < best_score:
            best_score = attempts
            print("최고기록 달성!: ", best_score)
        else:
            print("이전 최고 기록: ", best_score)

        number_re = input("다시 하시겠습니까? (y/n): ")
        if number_re.lower() != "y":
            print("게임을 종료합니다")
            break


if __name__ == "__main__":

    main()
