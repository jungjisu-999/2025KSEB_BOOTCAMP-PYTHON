# 입력 받은 수의 합을 구하는 코드를 작성하자
# ex : 10 55 . 100 5050
#O(n) ==> 선형시간

n = int(input())
r = 0
for i in range(n+1):
    r = r + i
print(r)





