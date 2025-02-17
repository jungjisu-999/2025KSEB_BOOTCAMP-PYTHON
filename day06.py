memo = dict()


def fibonacci_recursion(n) -> int:...

def fibonacci_loop(n) -> int...

def fibonacci_memo(n) -> int:
    if n in memo: # 딕셔너리에 이미 계산된 결과가 있으면 그 값을 리턴
        return memo[n]
    elif n <= 1: # 0이나 1이 오면 그 값을 바로 리턴
        return n
    else:
        memo[n] = fibonacci_memo(n-2) + fibonacci_memo(n-1) #딕셔너리에 계산된 결과 값이 없을 경우 딕셔너리에 추가
        return memo[n]


n = int(input())
print(fibonacci_loop(n))
print(fibonacci_recursion(n))
print(fibonacci_memo(n))






