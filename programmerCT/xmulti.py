#함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.

def solution(x, n):
    answer = []
    for i in range(1,n+1):
        answer.append(x * i)
    return answer

print(solution(-4,2))