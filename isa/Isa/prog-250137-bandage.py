'''
- 플랫폼: 프로그래머스
- URL: https://school.programmers.co.kr/learn/courses/30/lessons/250137
- 유형: 구현
'''

def solution(bandage, health, attacks):
    max_health = health # 최대 체력 설정 (초기 체력 = 최대체력)
    
    for i in range(len(attacks)):
        if i == 0:
            health += bandage[1]*(attacks[i][0] - 1) # 시간 당 체력 회복
            
            if attacks[i][0] // bandage[0] > 1:
                health += (attacks[i][0] // bandage[0])*bandage[2] # 추가 회복 체력
                
            if health > max_health: # 최대 체력으로 보정
                health = max_health
                   
        else:
            health += bandage[1]*(attacks[i][0] - attacks[i-1][0] - 1) # 시간 당 체력 회복
             
            if (attacks[i][0] - attacks[i-1][0] - 1) // bandage[0] > 0: # 보너스 추가 체력
                health += ((attacks[i][0] - attacks[i-1][0] - 1) // bandage[0])*bandage[2]
                
            if health > max_health: # 최대 체력으로 보정
                health = max_health
            
            
        health -= attacks[i][1] # 몬스터 공격 -> 체력 삭감
        
        if health <= 0: # 체력이 0 이하로 떨어지면 -1 반환
            return -1
    
    return health # 전부 다 돌면 현재 health 반환