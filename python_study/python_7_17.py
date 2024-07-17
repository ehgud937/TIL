'''
1. 함수의 이름
- 이 함수가 어떤 일을 하는지 알 수 있도록
- 동사

2. 함수의 역활
- 함수는 한 가지 역활만 할 수 있도록 구성

'''
# number_of_people = 0

# def increase_user() :
#     global number_of_people
#     number_of_people += 1

# increase_user()
# print(number_of_people)
# ###############################
# def create_user(name, age, address) :
#     increase_user()
#     print(f'{name}님 환영합니다!')
#     user_info = {}
#     user_info['name'] = name
#     user_info['age'] = age
#     user_info['address'] = address
#     return user_info

# print(f'현재 가입 된 유저 수 : {number_of_people}')   
# result = create_user('홍길동', 30, '서울')
# print(result)
# print(f'현재 가입 된 유저 수 : {number_of_people}')
# ######################################

# number_of_book = 100

# def rental_book(name, number) :
#     decrease_book(number)
#     print(f'{name}님이 {number}권의 책을 대여하였습니다.')

# def decrease_book(number) :
#     global number_of_book
#     number_of_book -= number
#     print(f' 남은 책의 수 : {number_of_book}')

# ################################

# # 풀이 1
# number_of_people = 0

# def increase_user() :
#     global number_of_people
#     number_of_people += 1

# def create_user(name, age, address) :
#     increase_user()
#     print(f'{name}님 환영합니다!')
#     user_info = {}
#     user_info['name'] = name
#     user_info['age'] = age
#     user_info['address'] = address
#     return user_info

# name = ['김시습', '허균', '남영로', '임제', '박지원']
# age = [20, 16, 52, 36, 60]
# address = ['서울', '강릉', '조선', '나주', '한성부']

# result_4 = list(map(create_user,name,age,address))
# print(result_4)

# # 풀이 2
# result_4_2 = []
# for name, age, address in zip(name, age, address) :
#     result_4_2.append(create_user(name, age, address))
# print(result_4_2)

#############################################################
name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

number_of_book = 100

def create_user(name, age, address) :
    print(f'{name}님 환영합니다!')
    user_info = {}
    user_info['name'] = name
    user_info['age'] = age
    user_info['address'] = address
    return user_info

def decrease_book(number) :
    global number_of_book
    number_of_book -= number
    print(f' 남은 책의 수 : {number_of_book}')

many_user = list(map(create_user,name,age,address))

#기존 회원 정보에서 이름과 몇권 빌릴지 계산해서 새로운 회원 정보 딕셔너리를 반환하는 함수
def get_user(user) :
    user_dict = {
        'name' : user['name'],
        'age' : user['age'] // 10
    }
    return user_dict


def rental_book(info) :
    decrease_book(info['age'])
    print(f'{info["name"]}가 {info["age"]}을 대여했습니다.')

print(list(map(rental_book, list(map(get_user,many_user)))))
