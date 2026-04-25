class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Use a dictionary/hash map data structure to map the count to num
        # Bucket Sort Trick/Algorithm
        # O(n) time complexity

        count = {}
        # Bucket sort array, index represent the count of num
        # 0, 1, 2, 3, 4, 5, 6 ; len(nums) + 1 
        #[],[1],[2],[3],[],[],[]
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = count.get(num, 0) + 1
        for num, cnt in count.items(): # return us the key-value pair: [(1,1),(2,2),(3,3)]
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res

