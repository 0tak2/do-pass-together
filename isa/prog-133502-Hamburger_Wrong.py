'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/133502
- 유형: 구현, 스택, 인덱싱

- 아래 코드는 시간초과가 발생한 코드입니다. 문제가 발생한 지점은 18행에 있는 stack = stack[:-4] 인 것 같다고 합니다. (전체를 복사해서 새로 만들어야하기 때문에 오래걸린다고 합니다 - 제미나이 피셜)
'''

def solution(ingredient):
    answer = 0
    stack = []
    
    for ing in ingredient:
        stack.append(ing)
        
        if len(stack) > 3:
            if stack[-4:] == [1, 2, 3, 1]:
                stack = stack[:-4]
                answer += 1    
    
    return answer