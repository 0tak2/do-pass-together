'''
- 플랫폼: 백준
- 문제: [영단어 암기는 괴로워](https://www.acmicpc.net/problem/20920)
- 유형: 구현, 정렬
'''

import sys
from functools import cmp_to_key

inputFast = sys.stdin.readline
printFast = sys.stdout.write

def sort(wordsCount):
  def comp(a, b):
    if wordsCount[a] > wordsCount[b]:
      return -1
    elif wordsCount[a] < wordsCount[b]:
      return 1
    
    if len(a) > len(b):
      return -1
    elif len(a) < len(b):
      return 1
    
    if a < b:
      return -1
    elif a > b:
      return 1
    
    return 0

  result = list(wordsCount.keys())
  result.sort(key=cmp_to_key(comp))
  return result

n, m = map(int, inputFast().split())
wordsCount = {}
for _ in range(n):
  word = inputFast().rstrip()
  if len(word) < m:
    continue
  
  wordsCount[word] = wordsCount.get(word, 0) + 1

ans = sort(wordsCount)
printFast('\n'.join(ans))
