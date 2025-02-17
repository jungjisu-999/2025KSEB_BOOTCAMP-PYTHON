#8진수로 바꾸는 코드 작성

def dec_oct(n) -> int:
    if n == 0:
        return ""
    else:
        return dec_oct(n // 8) + str(n % 8)
        # return dec_oct(n // 2) + str(n % 2)


##재귀함수 사용 재귀를 어디다가 사용했다는거임
n = int(input())
print(dec_oct(n))
# print(n, oct(n))
