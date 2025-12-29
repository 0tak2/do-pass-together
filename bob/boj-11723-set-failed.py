'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/11723
- 유형: 구현
실패 (메모리 초과)
'''
def solution_memory_failed(ops):
  data = set()
  outputs = []

  for op in ops:
    (command, value) = op
    if command == 'add':
      data.add(value)
    elif command == 'remove':
      data.discard(value)
    elif command == 'check':
      output = '1' if value in data else '0'
      outputs.append(output)
    elif command == 'toggle':
      if value in data:
        data.remove(value)
      else:
        data.add(value)
    elif command == 'all':
      data = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    elif command == 'empty':
      data = set()

  print('\n'.join(outputs))

def solution(ops):
  bits = 0
  outputs = []

  for op in ops:
    (command, value) = op
    if command == 'add':
      bits |= 1 << value
    elif command == 'remove':
      bits &= ~(1 << value)
    elif command == 'check':
      exists = bits & (1 << value)
      output = '1' if exists else '0'
      outputs.append(output)
    elif command == 'toggle':
      bits ^= (1 << value)
    elif command == 'all':
      bits = (1 << 21) - 1
    elif command == 'empty':
      bits = 0

  print('\n'.join(outputs))

result = []
opsCount = int(input())
ops = []

for _ in range(opsCount):
  inputs = input().split(" ")
  
  if len(inputs) == 1:
    ops.append((inputs[0], -1))
  elif len(inputs) > 1:
    ops.append((inputs[0], inputs[1]))

solution(ops)
