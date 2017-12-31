# coding=UTF-8
# pylint: disable=invalid-name
'''
heapq
'''
import heapq
print(heapq.__all__)

heap = []
heapq.heappush(heap, 11)
heapq.heappush(heap, 3)
heapq.heappush(heap, 8)
heapq.heappush(heap, 1)
heapq.heappush(heap, 9)
print(heap)

print(heapq.heappop(heap))
print(heap)

l1 = [1, 2, 7, 0, 4, 100]
heapq.heapify(l1)
print(l1)
heapq.heapreplace(l1, "wwwww")
print(l1)

if __name__ == "__main__":
    print("--------------------")
