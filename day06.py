memo = dict()


def fibonacci_recursion(n) -> int:...
"""
피보나치 수 계산함수 (재귀함수 버전)
"""
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
# 피보나치 오류가 너무 난다,,,


#배열의 성능

import numpy as np

narray = np.array([1, 3, 2, 9])
print(type(narray),  type(narray[2]), type(narray[3]))


array = [9, -11, '8', 7]
print(array[0], array[1], array[2], array[3])
print(type(array), type(array[2]), type(array[3]))
print(id(array[0]), id(array[1]), id(array[2]), id(array[3]))


#수상자 뽑기
import random
students = [] #file pointer --> fp




import csv
try:
    file = input("File name: ")
    fp = open('README.md', 'r')
    readme_list = fp.readlines()
    rls = readme_list[0].split()
    print(readme_list)
    print(rls)
    fp.close()
except FileNotFoundError as err:
    print(f"{file} is noe exist. {err}")






