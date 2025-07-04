# 1. 프로젝터 선정 이유
   최근 tv 프로그램의 다시보기로 무한도전 야구 게임 편을 시청하게 되면서 오랜만에 이 게임에 대해 다시 떠올리게 되었습니다. 종이와 연필만 있다면 쉬는 시간에 간단하게 즐길 수 있는 게임이고, 초등학생 시절 친구들과 재미있게 게임을 하던 추억도 떠올랐습니다.<br />
   규칙은 단순하지만 추리력과 사고력이 요구되어 여러 판 해도 쉽게 질리지 않고 중독성 있는 점이 매력적인 게임입니다. 다만, 게임을 진행하기 위해서는 정답 숫자를 알고있고, 스트라이크/볼/아웃의 개수를 알려줄 진행자가 필요하기 때문에 혼자서는 즐기기 어렵다는 한계가 있었습니다. 이러한 점에서 착안하여, 파이썬을 이용해 진행자 역할을 대신해줄 수 있는 프로그램을 만들면 혼자서도 충분히 즐길 수 있겠다는 생각이 들었고 프로젝트 주제로 선정하게 되었습니다.<br />
   
# 2. 파일 설명
 야구 게임을 두 가지 버전으로 만들어 보았습니다. 콘솔 창에서 print문으로만 게임이 진행되는 "final_hw_250620.py" 파일과, tkinter을 사용하여 GUI로 구현한 "final_hw_tk.py" 파일입니다.<br />
 
 * 주의할 점: tkinter를 실행하고 버튼 등을 클릭할 때, 반응 속도가 느려 일시적으로 오류가 난 것처럼 보일 수 있습니다. 하지만 잠시만 기다리시거나 버튼을 한 번 더 눌러보시면 정상적으로 실행되는 것을 확인하실 수 있습니다. 실행 속도가 느린 점 양해 부탁드립니다.<br />

# 3. 코드 설명
\- "final_hw_250620.py" 파일 기준 - <br /><br />
게임 진행에 필요한 함수들을 간단히 설명하겠습니다.

<img width="451" alt="Image" src="https://github.com/user-attachments/assets/d22de0f2-fe28-4011-8374-88fcce7fe754" /><br />
상/중/하에 따라 다른 try 값을 리턴하도록 함수를 만들었습니다.<br /><br />

<img width="434" alt="Image" src="https://github.com/user-attachments/assets/9a064c85-8486-46cd-a854-359a69002b5b" /><br />
진행자(컴퓨터)만이 알고 있는 서로 다른 4자리 숫자로 이루어진 수를 랜덤으로 생성합니다.<br /><br />

<img width="217" alt="Image" src="https://github.com/user-attachments/assets/549aa1c8-65e7-4b63-ad82-e6777ff92987" /><br />
게임 플레이어가 입력한 값이 유효한 값인지 판단하는 함수입니다. 예를 들어 플레이어가 5자리 이상의 수를 입력했을 때, 숫자가 아닌 문자를 입력했을 때, 중복되는 숫자를 입력했을 때 다시 수를 입력할 수 있도록합니다.<br /><br />

<img width="481" alt="Image" src="https://github.com/user-attachments/assets/08c26a68-dc1f-48dd-8035-7a8eba295b34" /><br />
입력받은 수와 정답 수를 비교하며 s/b/o의 결과가 어떻게 되는 지 판단해주는 함수입니다.<br /><br />

<img width="239" alt="Image" src="https://github.com/user-attachments/assets/133f1999-8143-4b87-916e-297ab63d3d2e" /><br /><br /><br />
모든 입력에 대해 정답인지 아닌지 판단하기 위해 만든 함수입니다.<br /><br />

<img width="626" alt="Image" src="https://github.com/user-attachments/assets/bdebd16c-ea15-45c0-a563-b962194b2f5e" /><br />
리턴받은 try 값에 따라 while문을 반복해줍니다.<br /><br />

<img width="535" alt="Image" src="https://github.com/user-attachments/assets/e508f03c-7ffe-493a-b108-bf698064bd1d" /><br />
정답을 맞췄을 때 게임을 계속 할 것인지 조건을 나누어줍니다.<br /><br />

# 4. 실행 화면 설명
\- "final_hw_tk.py" 파일 기준 - <br /><br />
<img width="90" alt="Image" src="https://github.com/user-attachments/assets/0e1caaff-f83f-4a0a-955a-a92e9f0152b1" /><br />
실행 버튼을 누르면 '게임 시작' 버튼이 뜨게 됩니다.<br /><br />

<img width="257" alt="Image" src="https://github.com/user-attachments/assets/bbef0d65-1f14-4b13-a7f9-3ff63a4c9526" /><br />
시작 버튼을 눌러 게임을 시작하게 되면 게임 규칙에 대한 간단한 설명 창이 나옵니다.<br /><br />

<img width="377" alt="Image" src="https://github.com/user-attachments/assets/03f66f78-a971-49f6-a9c3-9c8d1b9a7f1f" /><br />
난이도를 선택할 수 있습니다. 선택한 난이도에 따라 게임 실행 횟수가 달라집니다.<br /><br />

<img width="283" alt="Image" src="https://github.com/user-attachments/assets/741049e4-edc2-402c-89b5-6b4c4375fbee" /><br />
본격적으로 게임이 시작한 후의 화면입니다. 빈칸에 숫자를 입력할 수 있고, 입력 후 확인 버튼을 누르면 스트라이크/아웃/볼에 대한 결과를 볼 수 있습니다.<br /><br />

<img width="151" alt="Image" src="https://github.com/user-attachments/assets/316e1a9e-5705-485f-a6eb-9120f60acb2a" /><br />
게임 그만두기 버튼을 만들어 게임을 언제든지 종료할 수 있게 만들었습니다. 버튼을 누르면 진행 중이던 창이 꺼지면서 실행이 중단됩니다.<br /><br />

# 4. 보완할 점
현재 구현된 숫자 야구 게임은 한 명만 진행할 수 있는 형태로 구성되어 있지만, 나중에 스케일을 더 확장하여 두 명 이상이 함께 플레이할 수 있도록 기능을 추가해보고 싶습니다. 두 명이 동시에 같은 정답을 맞히는 경쟁 방식으로 구성하여 더 많은 사람과 함께 즐길 수 있는 형태로 발전시키고 싶습니다.<br />또한 점수 카운트 기능을 추가하여, 한 판으로 끝나는 구조가 아닌 여러 라운드를 연속적으로 진행하면서 누적 점수를 기록하고, 최종 점수에 따라 승패가 결정되는 방식으로 게임을 구성해보고 싶습니다.
