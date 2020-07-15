#배열 arr가 주어집니다. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다. 
#이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다.
# 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.

def samenum(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1,len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
    return answer
arr = [1,1,3,3,0,1,1]
print(samenum(arr))
#def no_continuous(s):
    # a = [] 
    # for i in s:
    #     if a[-1:] == [i]: continue
    #     a.append(i)
    # return a

