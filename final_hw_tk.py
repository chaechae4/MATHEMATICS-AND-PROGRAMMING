import random
import tkinter as tk
from tkinter import messagebox

def show_rules():
    rules = (
        "컴퓨터가 랜덤으로 생성한 4개의 숫자를 맞추는 게임입니다.\n\n"
        "- 숫자는 0000부터 9999까지 생성됩니다.\n"
        "- 4개의 숫자는 모두 다릅니다.\n"
        "- 숫자와 위치가 모두 일치하면 Strike\n"
        "- 숫자만 일치하면 Ball\n"
        "- 입력한 숫자가 모두 다르면 Out\n"
        "- 기회는 난이도에 따라 다릅니다:\n"
        "    • 상: 8번\n"
        "    • 중: 15번\n"
        "    • 하: 20번"
    )
    messagebox.showinfo("게임 규칙", rules)
    lvl_frame.pack(pady=10)  # 규칙창 확인 후 난이도 선택 보여주기

# 난이도별 기회 선택
def choice_level(level):
    return {'상':8, '중':15, '하':20}.get(level, 10)

# 중복 없는 4자리 랜덤 생성
def make_random_num():
    while True:
        num = f"{random.randint(0, 9999):04d}"
        if len(set(num)) == 4:
            return num

# 스트라이크 계산
def isit_strike(ans, guess):
    return sum(1 for i in range(4) if guess[i] == ans[i])

# 볼 계산
def isit_ball(ans, guess):
    return sum(1 for i in range(4) for j in range(4)
               if i!=j and guess[i]==ans[j])

# 난이도 버튼 콜백
def start_game(level):
    global attempts_left, answer
    attempts_left = choice_level(level)
    answer = make_random_num()
    start_btn.pack_forget()
    lvl_frame.pack_forget()
    setup_rows()

def setup_rows():
    for widget in frame_rows.winfo_children():
        widget.destroy()
    rows.clear()
    for i in range(attempts_left):
        ent = tk.Entry(frame_rows, width=4, font=('consolas', 18), justify='center')
        btn = tk.Button(frame_rows, text='확인', state='normal',
                        command=lambda r=i: check_guess(r))
        lbl = tk.Label(frame_rows, text='?', width=20)
        ent.grid(row=i, column=0, padx=5, pady=2)
        btn.grid(row=i, column=1, padx=5)
        lbl.grid(row=i, column=2, padx=5)
        rows.append((ent, btn, lbl))

    btn_quit.config(text="게임 그만두기")
    btn_quit.pack(pady=10)

# 정답 확인
def check_guess(row):
    ent, btn, lbl = rows[row]
    guess = ent.get()

    # 유효성 검사 먼저
    if not guess.isdigit() or len(guess) != 4 or len(set(guess)) != 4:
        messagebox.showwarning("입력 오류", "4자리 서로 다른 숫자를 입력하세요.")
        return

    strike = isit_strike(answer, guess)
    ball = isit_ball(answer, guess)
    out = 4 - strike - ball

    lbl.config(text=f"{strike}S {ball}B {out}O")
    btn.config(state='disabled')
    ent.config(state='disabled')

    if strike == 4:
        messagebox.showinfo("정답!", f"정답입니다! '{answer}'")
        btn_quit.config(text="게임 다시 시작")

    elif all(r[1]['state'] == 'disabled' for r in rows):
        messagebox.showinfo("끝!", f"기회 소진! 정답은 '{answer}'")
        btn_quit.config(text="게임 다시 시작")

# 게임 종료 및 재시작
def quit_or_restart():
    if btn_quit['text'] == "게임 그만두기":
        root.destroy()
    else:
        for widget in frame_rows.winfo_children():
            widget.destroy()
        btn_quit.pack_forget()
        start_btn.pack(pady=20)
        lvl_frame.pack(pady=10)

# UI 생성
root = tk.Tk()
root.title("숫자 야구 게임")

start_btn = tk.Button(root, text="게임 시작", font=('Helvetica',14), command=show_rules)
start_btn.pack(pady=20)

lvl_frame = tk.Frame(root)
for lvl in ['상','중','하']:
    btn = tk.Button(lvl_frame, text=lvl, width=6,
                    command=lambda l=lvl: start_game(l))
    btn.pack(side='left', padx=5)

frame_rows = tk.Frame(root)
frame_rows.pack()

btn_quit = tk.Button(root, text="게임 그만두기", font=('Helvetica',14), command=quit_or_restart)

rows = []
attempts_left = 0
answer = ""

root.mainloop()
