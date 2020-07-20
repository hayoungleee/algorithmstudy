def solution(s):
    answer = ''
    if len(s) % 2 == 0 :
        mid = int(len(s) / 2 )-1
        answer = s[mid:mid+2]
    else:
        mid = int(len(s) / 2 )
        answer =s[mid]
    return answer

s = "asdfd"
print(solution(s))
#def string_middle(str):

    # return str[(len(str)-1)//2:len(str)//2+1]