"""[[ HARD ]]"""
import heapq


class MedianFinder:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.min_heap) == len(self.max_heap):
            heapq.heappush(self.max_heap, -num)
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        else:
            heapq.heappush(self.min_heap, num)
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
        print(self.min_heap, self.max_heap)
        print(self.findMedian())

    def findMedian(self) -> float:
        if len(self.min_heap) > len(self.max_heap):
            return self.min_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2


if __name__ == '__main__':
    mf = MedianFinder()
    mf.addNum(-1)
    mf.addNum(-2)
    mf.addNum(-3)
    mf.addNum(-4)
    mf.addNum(-5)
