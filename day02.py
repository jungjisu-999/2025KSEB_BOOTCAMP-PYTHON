# dan = input("Input dan : ")
# for i in range(1, 10, 1):
#         print(f"{dan} * {i} = {dan*i}")



# for dan in range(2, 10, 1): #반복문 중괄호를 안쓰고 들여쓰끼
#     for i in range(1, 10, 1):
#         print(f"{dan} * {i} = {dan*i}")

n = int(input("Input number : "))
is_prime = True

if n >= 2:
        count = 0

        for i in range(2, n):
                if n % i == 0:
                    count = count + 1
                    break
else:
    is_prime = False

# if count == 0:
        print(f"{n} is prime number")
if is_prime:

else:
        print(f"{n} is NOT prime number!")


