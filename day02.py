# dan = input("Input dan : ")
# for i in range(1, 10, 1):
#         print(f"{dan} * {i} = {dan*i}")



# for dan in range(2, 10, 1): #반복문 중괄호를 안쓰고 들여쓰끼
#     for i in range(1, 10, 1):
#         print(f"{dan} * {i} = {dan*i}")


# n = int(input("Input number : "))
# is_prime = True
#
# if n >= 2:
#         count = 0
#
#         for i in range(2, n):
#                 if n % i == 0:
#                     is_prime = False
#                     break
# else:
#     is_prime = False
#
# # if count == 0:
#
# if is_prime:
#         print(f"{n} is prime number")
# else:
#         print(f"{n} is NOT prime number")


# print(type(2**10))
# print(type(16**0.5))
# n = int(input("Input number : "))
# is_prime = True



# def is_prime(num): -> bool:
# ''' 소수 여부를 판정해서 소수변 True를 아니면 False를 사용한다.
#     :param num '''
#
#     if num >= 2:
#         for i in range(2, int(num ** 0.5) + 1):
#             if num % i == 0:
#                 return False
#                 #is_prime = False
#                 #break
# #print(i, end = ' ')
#
#     else:
#         return False
#     return True
#
# #main
# #help(abs)
# help(is_prime)
# n = int(input("Input Number : "))
#
# if is_prime(n)

#github에 올려서 싱크를 맞춘다,,??branch가 뭐고

# (100°F − 32) × 5/9 = 37.778°C
# (0°C × 9/5) + 32 = 32°F

menu = input("1) Fahrenheit -> Celsius   2) Celsius -> Fahrenheit   3) Quit program : ")

if menu == '1':
    fahrenheit = float(input('Input Fahrenheit : '))
    print(f'Fahrenheit : {fahrenheit}F, Celsius : {((fahrenheit-32.0)*5.0/9.0):.4f}C')
elif menu == '2':
    celsius = float(input('Input Celcius : '))
    print(f'Celsius : {celsius}C, Fahrenheit : {((celsius*9.0/5.0)+32.0):.4f}F')






