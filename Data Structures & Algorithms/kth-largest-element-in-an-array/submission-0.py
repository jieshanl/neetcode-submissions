class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # use a max heap approach

        # nums is unsorted, if we use a max heap []
        # to heapify nums

        nums = [-1 * num for num in nums]
        heapq.heapify(nums)
        # after heapify: nums = [-2,-3,-1,-5,-4] [-5, -4, -3, -2, -1]

        while nums and k > 0:
            num = heapq.heappop(nums)
            k -= 1
            if k == 0:
                return -num