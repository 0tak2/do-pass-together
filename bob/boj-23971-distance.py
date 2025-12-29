def solution(height, width, limitN, limitM):
  # print(f'height: {height}, width: {width}, limitN: {limitN}, limitM: {limitM}')

  # (1 + n) * 최대높이배치수 <= height + n
  # 최대높이배치수 <= (height + n) / (1 + n)
  # 
  # (1 + m) * 최대너비배치수 <= width + m
  # 최대너비배치수 <= (width + m) / (1 + m)
  # 
  # answer = 최대너비배치수 * 최대높이배치수

  maxY = (height + limitN) // (1 + limitN)
  maxX = (width + limitM) // (1 + limitM)

  return maxY * maxX

[h, w, n, m] = map(lambda x: int(x), input().split(' '))
result = solution(h, w, n, m)
print(result)
