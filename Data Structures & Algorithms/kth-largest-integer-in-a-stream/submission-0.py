class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        if not nums:
            self.heap = []
        heapq.heapify(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        self.heap = nums

        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]