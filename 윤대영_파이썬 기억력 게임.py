
## 이 게임은    1. 모드 입력
## 이렇게       2  기회 입력
## 구성되어     3. 틀려서 다시 기회를 줄 때
## 있다.        4-1. 기회를 다 썼을 때         4-2. 마지막 라운드까지 달성했을 때
##              5. replay 여부 입력
##              6. 마지막 인사

#################
#초기 게임 설정!#
#################

import random                                             # random 함수를 쓰기 위함
lastround = 27                                            # 1 round에서 lastround 까지

while True:     
  list1=[]                                                # 매 게임마다 빈 리스트로 초기화!
  list2=[]
  k = 1                                                   # 나중에 -1이 되면 for i 문을 탈출
  m = 0                                                   # 매 게임마다 모드 초기화
    
  a = '♥'                                                # 기회 아이콘
  b = '♡'
   
  p = 0                                                   # 조건에 따라 문장 출력
  q = 0                                                   # replay 여부

  print('안녕! 나는 이 게임을 개발한 윤대영이라고 해!\n'
        '너의 기억력이 정말 뛰어나서 시험공부는 하루면 충분하다고 하던데.. 확인 좀 해볼까?\n\n'
        '각 round마다 랜덤으로 숫자를 보여주면 이를 기억하고 Enter를 누른 뒤\n'
        '처음에 보여준 숫자부터 차례대로 입력해주면 돼! 27round까지 있어! \n'
        '너무 많다고? 오른쪽 숫자판을 이용하면 외우기 더 쉬울거야!\n\n'
        '네가 뭘 좋아할지 몰라 여러가지 모드를 준비해봤어.\n')
        
  ################
  # 1. 모드 입력 #
  ################
    
  while True:                                             # 올바른 모드 선택 루프문
    if p == 1:  
      print("숫자를 입력해줄래? ㅎㅎ")
      p = 0
    elif p == 2:
      print('미안, 그건 준비하지 못했어.')
      p = 0
    
    x = input('여기서 네가 원하는 모드(1 ~ 3)를 선택해줘\n'
          '1: 랜덤 수가 1 ~ 3\n'
          '2: 랜덤 수가 1 ~ 6\n'
          '3: 랜덤 수가 1 ~ 9\n')
    
    if x.isdecimal() == True:                             # 입력값이 숫자면
      g = int(x)                                          # 정수형으로 바꿔주고
      if 1 <= g <= 3:                                     # 주어진 모드값의 범위면 num1값을 주고 탈출  
        if g == 1:
          num1 = 3
          break
        elif g == 2:
          num1 = 6
          break
        else:
          num1 = 9
          break
      else:                                               # 주어진 모드값을 벗어나면 사과
         print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
         print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
         print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
         p = 2
          
    else:                                                 # 입력값이 숫자가 아니면 숫자 입력 유도 
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
      p = 1 
  
  m = g                                                   # 모드 키 저장
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  
  ################  
  # 2. 기회 입력 #  
  ################
 
  while True:                                             # 기회 입력
    if p == 1:  
      print("숫자를 입력해줄래? ㅎㅎ")
      p = 0
    elif p == 2:
      print('그렇게 많이 줄 순 없지!')
      p = 0
    elif p == 3:
      print('게임을 하지 말자는 거니?')
      p = 0
    x = input('기회를 몇 번 줄까? (1 ~ 5): ')
    if x.isdecimal() == True:                             # 입력값이 숫자면
      g = int(x)                                          # 정수형으로 바꿔주고
      if 1<= g <= 5:  
        c = g                                             # 초기 하트 갯수 = 처음 주어진 기회
        d = 0
        break  
      elif g <= 0:                                        # 0 이하면 투정
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        p = 3
    
      else:                                               # 6 이상이면 약올리기
         print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
         print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
         print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
         p = 2
          
    else:                                                 # 입력값이 숫자가 아니면 숫자 입력 유도 
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
      p = 1   

  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

  ##############
  # 게임 시작! #
  ##############
    
  for i in range(0,lastround):                            # i는 0 ~ lastround-1 
    n = random.randint(1,num1)                            # n은 1 ~ num1 에서 랜덤 수를 생성하여
    list1.append(n)                                       # list1 끝에 추가함
    print('')                                             # 개행하려고 추가
    print("%dround의 숫자는 %d" %(i+1,n))                 # i+1은 1 ~ lastround 즉, round가 총 1 ~ lastround round까지 있음. 그리고 랜덤 수 n을 출력 
    x = input('기억했으면 Enter!')                        # 기억할 시간을 줌 
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")      
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")   # 방금 보여준 랜덤 수를 위로 보내서 보이지 않게 하기
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
    for j in range(0,i+1):                                # i+1 round일 때 j는 0 ~ i 즉, i+1 round일 때 일반적으로 i+1번 물어볼 것임
      while True:                                         # 첫번째 숫자 입력 입력 루프문
        print('남은 기회:',c*a + d*b, end=' ')
        if p == 1:
          print('숫자를 입력해줄래? ㅎㅎ')
          p = 0
        elif p == 0:
          print('')

        x = input("%dround의 숫자는 뭐였지?: "%(j+1))     # j+1은 1 ~ i+1 즉, i+1 round의 숫자를 차례대로 물어볼 것임
        if x.isdecimal() == True:                         # 입력값이 숫자면
          g = int(x)                                      # 정수형으로 바꿔주고
          list2.append(g)                                 # list2 끝에 추가하고 탈출
          break  
        else:                                             # 숫자가 아니면 숫자 입력을 유도
          print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
          print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
          print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
          p = 1
        
      ###############################
      # 3. 틀려서 다시 기회를 줄 때 #
      ###############################
        
      if list1[j] != g:                                   # 입력받은 수가 j+1 round의 숫자와 다르면 발동
        print('')                                         # 개행하려고 추가
        c = c-1                                           # 일단 하트를 하나 깎고 
        d = d+1  
            
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            
        while True:                                       # 맞거나 c = 0 될 때까지 다시 질문
          if c == 0:                                      # c = 0이라면 즉, 기회를 모두 써버린 경우 탈출하여 
            break                                         # 바로 아래의 if문으로 들어가게 유도하여 게임 종료     
  
          print('남은 기회:',c*a + d*b, end=' ')
          if p == 1:
            print('숫자를 입력해줄래? ㅎㅎ')              # 입력값이 숫자가 아니면 하트 옆으로 숫자 입력을 유도
            p = 0
          elif p == 0:                                    # 일반적인 상황인 p = 0이면 빈칸을 하트 옆에 붇임
            print('잘 생각해봐!')
            
          x = input("%dround의 숫자는 뭐였지?: "%(j+1))   # 다시 같은 라운드 숫자를 질문
          if x.isdecimal() == True:                       # 입력값이 숫자면
            g = int(x)                                    # 정수형으로 바꿔주고
            list2[j] = g                                  # 새로운 g 값을 list2[j]에 새로 넣고
              
            if list1[j] == g:                             # 새로운 g가 랜덤 수와 같으면 다음 라운드 질문으로 넘어감 
              break                                         
            else:                                         # 틀렸으면 다시 하트 하나를 깎고 다시 질문
              c = c-1
              d = d+1
               
              print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
              print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
              print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                
          else:
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            p = 1                 
            
        ##########################
        # 4-1. 기회를 다 썼을 때 #
        ##########################
            
        if c == 0:                                        # 기회를 모두 썼으면
          if i == 0:                                      # 1 round에서 틀린 경우
            print("처음부터 헷갈린 거 실화..? 제대로 해봐!")
          elif 1<= i <= 4:                                # 2 ~ 5 round에서 틀린 경우
            print("%dround까지 왔구나! 더 외울 수 있지?"%(i+1),end=' ')
            if j == 0:                                    # 1round 숫자를 틀린 경우
              print("1round에서 틀린 걸 보니 실수한건가?")
            elif j == i:                                  # 마지막 숫자를 틀린 경우
              print("아쉽게 마지막에서 틀렸네. ㅜㅜ")
            else:
              print("")
            
          else:
            print("%dround까지 왔구나! 대단한걸!"%(i+1), end=' ')  
            if j == 0:                                    # 1round 숫자를 틀린 경우
              print("1round에서 틀린 걸 보니 실수한건가?")
            elif j == i:                                  # 마지막 숫자를 틀린 경우
              print("아쉽게 마지막에서 틀렸네. ㅜㅜ")
            else:
              print("")
                
          print('')                                       # 개행하려고 추가
          print("올바른 순서:",list1)                     # 저장된 각 round 랜덤 수의 리스트 출력
          print("입력된 순서:",list2)                     # 저장된 플레이어의 입력값 리스트 출력 
          
          #######################
          # 5. replay 여부 입력 #
          #######################
        
          while True:                                     # 다시 할건지 끝낼 건지 묻는 루프문, 1 or 2를 입력해야 탈출
            if p == 1:
              print("숫자를 입력해줄래? ㅎㅎ")
              p = 0
            elif p == 2:
              print('어쩌겠다는 거니?')
              p = 0
            else:
              print("")
                    
            x = input('처음 화면으로 돌아갈래?\n1: 응!\n2: 아니, 그만할래.\n')
            if x.isdecimal() == True:                     # 입력값이 숫자면
              g = int(x)                                  # 정수형으로 바꿔주고
              if g == 1:                                  # 주어진 모드값의 범위면 num1값을 주고 탈출  
                q = 1 
                break
              elif g == 2:
                q = 2
                break  
              else:   # 1, 2 이외의 숫자면 따짐
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                p = 2
            else:     # 입력값이 숫자가 아니면 숫자 입력 유도
              print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
              print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
              print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
              p = 1
        
          k = -1                                          # k = -1로 바꾸어 for i를 탈출하기 위한 큰 그림
          break                                           # 틀렸으니까 for j을 탈출한다
        
      ######################################
      # 4-2. 마지막 라운드까지 달성했을 때 #
      ######################################
      if i+1 == lastround and j+1 == lastround:           # lastround에서 마지막 숫자까지 맞춘 경우
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
        print("대단해! 옆에 적어둔건 아니겠지? 어쨌든 널 암기천재로 인정할게!\n")
        print("제시된 순서:",list1)
        #######################
        # 5. replay 여부 입력 #
        #######################
        
        while True:                                       # 다시 할건지 끝낼 건지 묻는 루프문, 1 or 2를 입력해야 탈출
            if p == 1:
              print("숫자를 입력해줄래? ㅎㅎ")
              p = 0
            elif p == 2:
              print('어쩌겠다는 거니?')
              p = 0
            else:
              print("")
            
            x = input('처음 화면으로 돌아갈래?\n1: 응!\n2: 아니, 그만할래.\n')
            if x.isdecimal() == True:                     # 입력값이 숫자면
              g = int(x)                                  # 정수형으로 바꿔주고
              if g == 1:                                  # 주어진 모드값의 범위면 num1값을 주고 탈출  
                q = 1 
                break
              elif g == 2:
                q = 2
                break  
              else:                                       # 1, 2 이외의 숫자면 따짐
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
                p = 2
            else:                                         # 입력값이 숫자가 아니면 숫자 입력 유도
              print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
              print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
              print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
              p = 1
        
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n") #  방금 입력한 값을 위로 보내서 보이지 않게 하기
      print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")      
      
    
    list2=[]                                              # for j문을 탈출하면 list2를 다시 받기 위해 비운다.
    if k == -1:                                           # k = -1이라면 즉, 랜덤 수를 잘못 입력했거나 끝까지 갔다면 for i를 탈출
      break
  
  ##################
  # 6. 마지막 인사 #
  ##################
    
  if q == 2:                                              # q = 2 즉, 게임 종료를 원하므로 전체 while문 탈출하여 종료
    while True:                                           # 마지막 인사
      if q == 100:
        break
      q = q + 1  
      print("\n플레이 해줘서 고마워! 안ㄴㅕㅇㅓㅇㅇ엉~~") 
    break                                                 # 전체 while문 탈출하여 종료
  
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")     # 335줄
