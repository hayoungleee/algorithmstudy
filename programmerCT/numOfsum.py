#자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
#예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
def solution(n):
    answer = 0
    str_n = str(n)
    for i in range(len(str_n)):
        answer += int(str_n[i])
    return answer

print(solution(987))

#return sum([int(i) for i in str(number)])
