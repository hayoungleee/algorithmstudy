#정수 num이 짝수일 경우 Even을 반환하고 홀수인 경우 Odd를 반환하는 함수, 
#solution을 완성해주세요.
def solution(num):
    answer = ''
    if num % 2 == 0 or num == 0 :
        answer = "Even"
    else:
        answer = "Odd"
    return answer
print(solution(3))