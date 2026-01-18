/**
- 플랫폼: 백준
- 문제: [최소 힙](https://www.acmicpc.net/problem/1927)
- 유형: 자료구조, 힙

직접 구현 해보기

# 힙
## 힙이란?
- 완전 이진 트리의 일종. 
- 최소 힙: 값이 가장 작은 값이 가장 높은 우선순위를 가지는 힙
- 최대 힙: 값이 가장 큰 값이 가장 높은 우선순위를 가지는 힙

## 힙의 특징
- 최소 힙: 모든 부모 노드는 그 자식들이 가진 값보다 작거나 같은 값을 가진다.
- 최대 힙: 모든 부모 노드는 그 자식들이 가진 값보다 크거나 같은 값을 가진다.
- 반드시 완전 이진 트리 형태를 유지한다.

## 구현 방법
- 링크드 리스트를 이용할 수도 있지만 여기서는 간편하게 배열로 구현
*/

import Foundation

/**
자연수를 저장할 수 있는 최소 힙

## 인덱스
### 부모 -> 자식
왼쪽 자식의 인덱스 = 부모 인덱스 * 2 + 1
오른쪽 자식의 인덱스 = 부모 인덱스 * 2 + 2

### 자식 -> 부모
부모의 인덱스 = (자식의 인덱스 - 1) / 2
* 그냥 자식인덱스를 2로 나누면, 오른쪽 자식의 부모가 잘못 계산된다.

## 연산
### remove
- 첫 값을 제거하면 된다.
- 다만 연산 후에도 힙이 유지되어야 하므로,
  1. 첫 값과 마지막 값을 swap
  2. 현재 마지막 값(즉, swap하기 전의 첫 값)을 반환
  3. 현재 첫 값(즉, swap하기 전의 마지막 값)에서 시작해 자식을 순회하며 대소 확인해 제 자리 찾기

### insert
- 마지막 원소로 새 값을 추가한다.
- 마지막 원소부터 부모로 올라가면서 대소 확인해 제 자리 찾기
*/
struct Heap {
  private var storage = [Int]()

  let comparator: (Int, Int) -> Bool

  init(comparator: @escaping (Int, Int) -> Bool = { a, b in a < b }) {
    self.comparator = comparator
  }

  var isEmpty: Bool {
    self.storage.isEmpty
  }

  var count: Int {
    self.storage.count
  }

  mutating func insert(_ value: Int) {
    storage.append(value)

    shiftUp(from: count - 1)
  }

  mutating func remove() -> Int? {
    guard !isEmpty else { return nil }

    storage.swapAt(0, count - 1) // 첫 값을 삭제해야 함. 우선 첫 값과 마지막 값을 스왑.

    defer {
      shiftDown(from: 0) // return 후에 수행할 작업. 스왑된 값부터 자식과 비교하면서 제 자리를 찾아줌.
    }

    return storage.removeLast()
  }

  mutating func shiftDown(from index: Int) { // 레벨 수 만큼 비교하므로 O(logN)
    var parent = index // 내려갈 시작점
    while true {
      let left = getLeftChildIndex(parentIndex: parent)
      let right = getRightChildIndex(parentIndex: parent)
      var candidate = parent

      if left < count && comparator(storage[left], storage[candidate]) {
        candidate = left
      }

      if right < count && comparator(storage[right], storage[candidate]) { // 여기서 candidate는 부모이거나 왼쪽 형제. 결국 가장 작은 값을 선택해 아래로 내리게 됨.
        candidate = right
      }

      if candidate == parent { // 마지막에 도달한 경우
        return
      }

      storage.swapAt(parent, candidate)
      parent = candidate // 바뀐 위치를 다시 부모로 잡고 반복
    }
  }

  mutating func shiftUp(from index: Int) {
    var child = index
    var parent = getParentIndex(childIndex: child)
    while child > 0 && comparator(storage[child], storage[parent]) { // 레벨 수 만큼 비교하므로 O(logN)
      storage.swapAt(child, parent)
      child = parent // 바뀐 위치를 다시 자식으로 잡고 반복
      parent = getParentIndex(childIndex: child)
    }
  }

  // MARK: - Utils for handling index
  func getLeftChildIndex(parentIndex: Int) -> Int {
    parentIndex * 2 + 1
  }

  func getRightChildIndex(parentIndex: Int) -> Int {
    parentIndex * 2 + 2
  }

  func getParentIndex(childIndex: Int) -> Int {
    (childIndex - 1) / 2
  }
}

var h = Heap()

let total = Int(readLine() ?? "0") ?? 0
for _ in 0..<total {
  let cmd = Int(readLine() ?? "0") ?? 0
  if cmd == 0 {
    if let popped = h.remove() {
      print(popped)
    } else {
      print(0)
    }

    continue
  }

  h.insert(cmd)
}
