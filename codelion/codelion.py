###점심메뉴골라주는 Product###
import random
import time

lunch=["된장찌개","피자","제육볶음","짜장면"]

while True:
    print("최초메뉴: ", lunch)
    item=input("메뉴를 추가해 주세요: ")
    if(item=="q"):
        break
    else:
        lunch.append(item)
print(lunch)


set_lunch=set(lunch)
while True:
    print(set_lunch)
    item=input("메뉴를 삭제해 주세요")
    if(item == "q"):
        break
    else:
        set_lunch = set_lunch-set([item])
        
print("최종메뉴: ", set_lunch, "중에서 선택 합니다.")

print("카운트 다운!!!!")

print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print(random.choice(list(set_lunch)))  
