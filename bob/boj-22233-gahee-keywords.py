'''
- 플랫폼: 백준
- 문제: [가희와 키워드](https://www.acmicpc.net/problem/22233)
- 유형: 문자열, 셋
'''

import sys
input = sys.stdin.readline
print = sys.stdout.write

totalKeywords, totalPosts = map(int, input().split())

keywords = set()

for _ in range(totalKeywords):
  keyword = input().strip()
  keywords.add(keyword)

for _ in range(totalPosts):
  usedKeywords = input().strip().split(',')
  for k in usedKeywords:
    keywords.discard(k)

  print(f'{len(keywords)}\n')
