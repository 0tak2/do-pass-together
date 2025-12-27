'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/1158
- 유형: 연결리스트
'''
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next
  
  def printAll(self):
    print(self.value)
    cur = self.next
    while cur != self:
      print(cur.value)
      cur = cur.next

def solution(n, k):
  # 환형리스트
  head = Node(1)
  cur = head
  for i in range(2, n + 1):
    cur.next = Node(i)
    cur = cur.next
  cur.next = head 
  
  # 제거
  result = []
  prev = cur
  cur = head
  
  for _ in range(n):
    # k-1번 이동 (현재 위치 포함해서 k번째)
    for _ in range(k - 1):
      prev = cur
      cur = cur.next
    
    # cur 제거
    result.append(cur.value)
    prev.next = cur.next
    cur = cur.next
  
  return result

[n, k] = list(map(lambda x: int(x), input().split(' ')))
answer = list(map(lambda x: str(x), solution(n, k)))
print('<' + ', '.join(answer) + '>')
