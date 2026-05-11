class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # sorted integer array, two integers k & x
        # get the k closest integers to x
        # ex: 2 closest integers to 6
        # utilize the sorted property, since the array is already sorted, the k closest elements must form a contiguous array


        # two pointers

        l, r = 0, len(arr) - 1

        while r - l >= k:
            if abs(x - arr[l]) <= abs(x - arr[r]):
                r -= 1
            else:
                l += 1
        
        return arr[l: r + 1] # the right boundry is exclusive, so r + 1

        # Time Complexity: O(n - k)
        # Space Complexity: O(k)
        
