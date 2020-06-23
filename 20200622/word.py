###끝말잇기 만들기###

# 사용자로 부터 인풋이 들어온다
# 그 인풋을 받아서 끝자리 음절과
# 다음 인풋의 첫 음절이 같아야 통과
# 3글자만 허용

word1 = input("끝말잇기를 시작 합니다: ") #input 값은 기본적으로 str

if(len(word1)==3):   

    while True: 
    
        word2=input()
        
        if(len(word2)==3)and (word2[0]==word1[-1]):
            print("정답!")
        else:
            print("오답ㅠㅠ")
            break
else:
    print("오답(hint-단어는 3음절로 이루어 져야 합니다)")
    
print("Game Over")


# git  변경 체크용