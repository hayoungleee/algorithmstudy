#임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
#n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, 
#n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

def solution(n):
    answer = 0
    i = 1
    a = 1
    while True:
        if n == i ** 2 :
            answer = (i+1)**2
            break
        if n == i :
            answer = -1
            break
        i += 1
    return answer
print(solution(3))

# #sqrt = n ** (1/2)

#     if sqrt % 1 == 0:
#         return (sqrt + 1) ** 2
#     return 'no'
