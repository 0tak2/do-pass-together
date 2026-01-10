'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/1244
- 유형: 구현
'''

def mutateByBoy(switches, number):
    for i in range(len(switches)):
        switchNumber = i + 1
        if switchNumber % number == 0:
            switches[i] = not switches[i]

def mutateByGirl(switches, number):
    for n in range(number):
        leftIndex = number - n - 1
        rightIndex = number + n - 1

        if leftIndex >= 0 and rightIndex < len(switches) and switches[leftIndex] == switches[rightIndex]:
            switches[leftIndex] = not switches[leftIndex]
            switches[rightIndex] = not switches[rightIndex]
        else:
            break
    
    switches[number-1] = not switches[number-1]

def solution(switches, students):
    for isBoy, number in students:
        if isBoy:
            mutateByBoy(switches, number)
        else:
            mutateByGirl(switches, number)
    
    return switches

input()

switches = [ True if x == '1' else False for x in input().split()]
numberOfStudents = int(input())
students = []
for _ in range(numberOfStudents):
    [genderCode, number] = map(int, input().split())
    isBoy = False
    if genderCode == 1:
        isBoy = True
    
    students.append((isBoy, number))

ans = solution(switches, students)
converted = [ '1' if x else '0' for x in ans]

while converted:
    sliced = converted[:20]
    converted = converted[20:]
    print(" ".join(sliced))
