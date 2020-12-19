# 2020-11-16

# print(5)
# print(-10)
# print(3.14)
# print(1000)
# print(5+3)
# print(2*8)
# print(3*(3+1))

# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ")
# print("ㅋ"*9)

# print(5>10)
# print(5<10)
# print(True)
# print(False)
# print(not True)
# print(not False)
# print(not(5>10))

# animal = "고양이"
# name = "해피"
# age = 4
# hobby = "낮잠"
# is_adult = age >=3


# print("우리집 " + animal + "의 이름은 " + name + "예요")
# hobby = "공놀이"
# #print(name + " 는 " + str(age) + "살이며, " + hobby + "을 아주 좋아해요")
# print(name, "는 ", age, "살이며, ", hobby, "을 아주 좋아해요")
# print(name + "는 어른일까요?" + str(is_adult))

# ''' 이렇게 
# 하면
# 여러문장이
# 주석처리
# 됩니다 '''

# station = "사당"
# print(station, "행 열차가 들어오고 있습니다.")

# station = "신도림"
# print(station, "행 열차가 들어오고 있습니다.")

# station = "인천공항"
# print(station, "행 열차가 들어오고 있습니다.")

# print(1+1)
# print(6/3)
# print(2**3)
# print(5%3)
# print(10%3)
# print(5//3)
# print(10//3)

# print(10 > 3)
# print(4 >= 7)
# print(10 < 3)
# print(5 <= 5)

# print(3 == 3)
# print(1 != 3 )
# print(not(1 != 3))
# print((3>0) and (3<5))
# print((3>0) & (3 < 5))

# print((3 > 0) or (3 >5))
# print((3 >0) | (3 >5))

# print( 5 > 4 >3 )
# print(5 >4 >7)
# print(2+3*4)
# print((2+3)*4)
# number = 2 + 3*4
# print(number)
# number = number + 2
# print(number)
# number += 2
# print(number)
# number *=2
# print(number)
# number /= 2
# print(number)
# number -= 2
# print(number)
# # number %= 2
# # print(number)

# number %= 5
# print(number)

# print(abs(-5))
# print(pow(4,2))
# print(max(5,12))
# print(min(5,12))
# print(round(3.14))
# print(round(4.99))

# from math import *
# print(floor(4.99))
# print(ceil(3.14))
# print(sqrt(16))

# from random import *

# print(random())
# print(random() * 10)
# print(int(random()*10))
# print(int(random()*10)+1)

# print(int(random() * 45) + 1)

# print(randrange(1, 46))
# print(randint(1, 45))

# x = randint(4, 28)
# print("오프라인 스터디 모임 날짜는 매월", x, "일로 선정되었습니다.")

# from random import *
# date = randint(4, 28)

# print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다.")

# sentence = '나는 소년입니다'
# print(sentence)
# sentence2 = "파이썬은 쉬워요"
# print(sentence2)
# sentence3 = """
# 나는 소년이고, 
# 파이썬은 쉬워요
# """
# print(sentence3)

# jumin = "990120-1234567"

# print("성별 : " + jumin[7])
# print("연 : " + jumin[0:2]) # 0부터 2 직전까지 (0, 1)
# print("월 : " + jumin[2:4])
# print("일 : " + jumin[4:6])

# print("생년월일 : " + jumin[:6])  # 처음부터 6 직전까지
# print("뒤 7자리 : " + jumin[7:])  # 7 부터 끝까지 
# print("뒤 7자리 (뒤에부터) : " + jumin[-7:])  # 맨 뒤에서 7번째부터 끝까지

# python = "Python is Amazing"
# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)
# index = python.index("n", index + 1)
# print(index)

# print(python.find("n"))
# print(python.find("Java"))
# # print(python.index("Java"))
# print("hi")

# print(python.count("n"))

# print("나는 %d살입니다." % 20) # 정수
# print("나는 %s을 좋아해요." % "파이썬") #문자든 정수든 모두 가능
# print("Apple은 %c로 시작해요." % "A") #문자
# print("나는 %s색과 %s색을 좋아해요." % ("파란", "빨간"))

# print("나는 {}살입니다.".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))

# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요.")

# \n : 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")

# # \\ : 문장 내에서 \
# print("저는 '나도코딩'입니다.")
# print('저는 "나도코딩"입니다.')
# print("저는 \"나도코딩\"입니다.")
# print('저는 \"나도코딩\"입니다.')

# print("C:\\Users\\USER\\Desktop\\PythonWorkspace>")

# # \r : 커서를 맨 앞으로 이동
# print("Red Apple\rPine")

# # \b : 백스페이스 (한 글자 삭제)
# print("Redd\bApple")

# \t : 탭
# print("Red\tApple") 

# url = "http://naver.com"
# my_str = url.replace("http://", "")
# # print(my_str)
# # my_str = my_str[:my_str.index(".")] # my_str[0:5] -> 0~5직전까지. (0,1,2,3,4)
# # print(my_str)
# # password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
# # print("{0}의 비밀번호는 {1} 입니다.".format(url, password))

# # 2020-11-17

# # subway1 = 10
# # subway2 = 20
# # subway3 = 30

# # subway = [10,20,30]
# # print(subway)

# # subway = ["유재석", "조세호", "박명수"]
# # # print(subway)
# # # print(subway.index("조세호"))
# # # subway.append("하하")
# # # print(subway)
# # # subway.insert(1,"정형돈")
# # # print(subway)

# # print(subway.pop())
# # print(subway)

# # # print(subway.pop())
# # # print(subway)

# # subway.append("유재석")
# # print(subway)
# # print(subway.count("유재석"))

# num_list = [5,2,4,3,1]
# # num_list.sort()
# # print(num_list)
# # num_list.reverse()
# # print(num_list)
# # num_list.clear()
# # print(num_list)

# # mix_lilst = ["조세호",20,True]
# # print(mix_lilst)

# # num_list.extend(mix_lilst)
# # print(num_list)


# # cabinet = {3:"유재석", 100:"김태호"}
# # # print(cabinet[3])
# # # print(cabinet[100])

# # # print(cabinent.get(3))
# # # print(cabinet[5])
# # # print(cabinet.get(5))
# # # print(cabinet.get(5,"사용 가능"))
# # # print("hi")

# # print(3 in cabinet)
# # print(5 in cabinet)

# cabinet = {"A-3":"유재석", "B-100":"김태호"}
# print(cabinet["A-3"])
# print(cabinet["B-100"])

# print(cabinet)
# cabinet["A-3"] = "김종국"
# cabinet["C-20"] = "조세호"
# print(cabinet)

# del cabinet["A-3"]
# print(cabinet)

# # print(cabinet.keys())
# # print(cabinet.values())
# # print(cabinet.items())

# # cabinet.clear()
# # print(cabinet)

# # menu = ("돈까스", "치즈까스")
# # print(menu[0])
# # print(menu[1])

# # (name, age, hobby) = ("김종국", 20, "코딩")
# # print(name, age, hobby)

# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# print(java & python)
# print(java.intersection(python))

# print(java|python)
# print(java.union(python))

# print(java - python)
# print(java.difference(python))

# python.add("김태호")
# print(python)

# java.remove("김태호")
# print(java)

# menu = {"커피", "우유", "주스"}
# print(menu, type(menu))

# menu = list(menu)
# print(menu, type(menu))

# menu = tuple(menu)
# print(menu, type(menu))

# menu = set(menu)
# print(menu, type(menu))

# 퀴즈 4
# 치킨 당첨자 : 1
# 커피 당첨자 : [2,3,4]

# from random import*
# lst = [1,2,3,4,5]
# print(lst)
# shuffle(lst)
# print(lst)
# print(sample(lst,1))

# from random import * 
# users = range(1,21) # 1부터 20까지 숫자를 생성
# # print(type(users))
# users=list(users)
# # print(type(users))

# print(users)
# shuffle(users)
# print(users)

# winners = sample(users,4)
# print("치킨 당첨자 : {0}".format(winners[0]))
# print("커피 당첨자 : {0}".format(winners[1:]))

