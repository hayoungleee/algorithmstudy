def solution(seoul):
    answer = ''
    i=0
    if "Kim" in seoul and len(seoul) >= 1 and len(seoul)<= 20:
        while True:
            if seoul[i] == "Kim" :
                answer = '김서방은 ' + str(i)+ ' 에 있다' 
                break
            elif i == len(seoul):
                 break
            else:
                i+=1
        return answer
seoul=['Jane','Kim']
print(solution(seoul))
