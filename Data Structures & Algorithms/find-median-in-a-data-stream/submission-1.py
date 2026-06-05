class MedianFinder:

    def __init__(self):
        self.data = []

    def addNum(self, num: int) -> None:
        self.data.append(num)

    def findMedian(self) -> float:
        self.data.sort()
        n = len(self.data)
        if (n % 2) == 0:
            median = self.data[n//2] + self.data[n//2 - 1]
            median /= 2.0
            return median
        return self.data[n//2]
        