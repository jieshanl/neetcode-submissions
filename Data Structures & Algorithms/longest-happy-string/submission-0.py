class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # use a MaxHeap

        res, maxHeap = "", []
        for count, char in [(-a, "a"), (-b, "b"), (-c, "c")]:
            if count != 0:
                heapq.heappush(maxHeap, (count, char))

        while maxHeap:
            count, char = heapq.heappop(maxHeap)
            if len(res) > 1 and res[-1] == res[-2] == char:
                if not maxHeap: # what if the second largest count char does NOT exist
                    break
                # else: we do have the second most common char
                count2, char2 = heapq.heappop(maxHeap)
                res += char2
                count2 += 1 # since we poped, we need to "decrement" the count by adding 1 b/c count is negative
                if count2:
                    heapq.heappush(maxHeap, (count2, char2))
            else:
                res += char
                count += 1
            if count:
                heapq.heappush(maxHeap, (count, char))
        return res

    # Time Complexity: O(n)
    # Space Complexity: O(1)
