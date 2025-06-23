import random

def choice_level():
    while True:
        level = input("난이도를 선택하십시오. (상/중/하) ").strip()
        if level == '상':
            print("난이도 '상' 선택: 기회는 8번입니다.\n")
            return 8
        elif level == '중':
            print("난이도 '중' 선택: 기회는 15번입니다.\n")
            return 15
        elif level == '하':
            print("난이도 '하' 선택: 기회는 20번입니다.\n")
            return 20
        else:
            print("잘못된 입력입니다. 상/중/하 중에서 선택하십시오.")


def make_random_num():
    while True:
        ans_num = random.randint(0, 9999)
        ans_num_lst = [int(d) for d in f"{ans_num:04d}"]
        if len(set(ans_num_lst)) == 4:
            # print(ans_num_lst)
            return ans_num, ans_num_lst

def is_valid_input(n):
    if not n.isdigit():
        return False
    if len(n) != 4:
        return False
    if len(set(n)) != 4:
        return False
    return True

def isit_strike(ans_lst, num_lst):
    strike = 0
    for i in range(4):
        if num_lst[i] == ans_lst[i]:
            strike += 1
    return strike

def isit_ball(ans_lst, num_lst):
    ball = 0
    for i in range(4):
        if num_lst[i] != ans_lst[i] and num_lst[i] in ans_lst:
            for j in range(4):
                if i != j and num_lst[i] == ans_lst[j]:
                    ball += 1
                    break
    return ball

def isit_answer(ans_num, num):
    return ans_num == int(num)

def main():
    ans_num, ans_num_lst = make_random_num()
    # print(ans_num)

    print("=" * 15, "숫자 야구 게임", "=" * 15)
    print("컴퓨터가 랜덤으로 생성한 4개의 숫자를 맞추는 게임입니다.")
    print("*** 규칙 설명 ***\n- 4개의 숫자는 모두 다릅니다."
          "\n- 숫자와 위치가 모두 일치하면 strike\n- 숫자만 일치하면 ball\n- 입력한 숫자가 모두 다르면 out\n"
          "- 기회는 난이도에 따라 다릅니다. (상 - 8번, 중 - 15번, 하 - 20번).\n")

    try_cnt = 0
    level_cnt = choice_level()

    while try_cnt <= (level_cnt - 1):
        num = input(f"서로 다른 4자리 숫자를 입력하십시오. (게임 종료: q) [시도 횟수: {try_cnt}번] ")

        if num.lower() == 'q':
            print("게임을 종료합니다.")
            break

        if not is_valid_input(num):
            print("잘못된 입력입니다. 서로 다른 4자리 숫자를 입력하십시오.")
            continue

        num_lst = [int(d) for d in f"{int(num):04d}"]
        try_cnt += 1

        strike = isit_strike(ans_num_lst, num_lst)
        ball = isit_ball(ans_num_lst, num_lst)
        out = 4 - strike - ball

        print("%d strike %d ball %d out" % (strike, ball, out))

        if isit_answer(ans_num, num):
            print(f"{ans_num:04d} 정답입니다! 시도 횟수 %d번에 맞추셨습니다." % try_cnt)
            conti = input("게임을 계속 하시겠습니까? (y/n) ")
            if conti.lower() == 'y':
                print()
                try_cnt = 0
                level_cnt = choice_level()
                ans_num, ans_num_lst = make_random_num()
                # print(ans_num_lst)
                continue
            elif conti.lower() == 'n':
                print(f"게임을 종료합니다.")
                break

main()