'''
- 플랫폼: 백준
- URL: https://www.acmicpc.net/problem/11723
- 유형: 비트마스크
'''

import sys

bits = 0
opsCount = int(sys.stdin.readline())

for _ in range(opsCount):
  inputs = sys.stdin.readline().split()
  command = inputs[0]
  value = int(inputs[1]) if len(inputs) > 1 else -1

  if command == 'add':
    bits |= 1 << value
  elif command == 'remove':
    bits &= ~(1 << value)
  elif command == 'check':
    exists = bits & (1 << value)
    sys.stdout.write('1\n' if exists else '0\n')
  elif command == 'toggle':
    bits ^= (1 << value)
  elif command == 'all':
    bits = (1 << 21) - 1
  elif command == 'empty':
    bits = 0
