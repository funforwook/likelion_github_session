# # for 을 이용하여 구구단을 만들기

# for a in range(2,10):
#     for b in range(1,10):
#         print(a,"*",b ,'=', a*b)
        
print("곱하기 계산기 입니다.")

a = int(input('a:'))
b = int(input('b:'))

if (a>0) & (b>0):
    print("결과값:",format((a*b),","),"원")
else:
    print("입력한 값이 양수가 아닙니다")