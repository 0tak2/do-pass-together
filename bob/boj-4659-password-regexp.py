import re

'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/4659
- 유형: 구현, 문자열
- 36980KB, 108ms

Gemini가 짜준 정규표현식으로 푸는 답안. 코드 양은 줄어들지만 속도는 훨씬 오래걸린다.
프로덕션 코드라면 정규표현식을 사용할 것이고, 코딩테스트에서 조건이 복잡하지 않다면 직접 구현하는 편이 낫겠다.
'''
def check_with_regex(password):
    # 정규식 패턴 정의
    # 1. 모음 한 개 이상 포함: (?=.*[aeiou])
    # 2. 모음 또는 자음 3개 연속 불가: (?!.*[aeiou]{3}) / (?!.*[^aeiou]{3})
    # 3. 같은 글자 연속 불가 (ee, oo 제외): (?!.*([^eo])\1)
    regex = r"^(?=.*[aeiou])(?!.*[aeiou]{3})(?!.*[^aeiou]{3})(?!.*([^eo])\1)[a-z]+$"
    
    # re.match는 패턴이 일치하면 객체를 반환하고, 아니면 None을 반환합니다.
    if re.match(regex, password):
        return True
    return False

while True:
    password = input().strip()
    if password == "end":
        break
    
    if check_with_regex(password):
        print(f'<{password}> is acceptable.')
    else:
        print(f'<{password}> is not acceptable.')
