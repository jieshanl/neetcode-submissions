class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Merge Sort - Divide and Conquer

        # 5, 2, 3, 1
        # 5, 2 -> 5 2
        # 3, 1 -> 3 1
        def merge(arr, L, M, R):
            left, right = arr[L:M+1], arr[M+1:R+1] 
            i, j, k = L, 0, 0

            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1
            # Only one of the two while loops below will run
            while j < len(left):
                nums[i] = left[j]
                j += 1
                i += 1
            while k < len(right):
                nums[i] = right[k]
                k += 1
                i += 1

 
        def mergeSort(arr, l, r):
            if l == r:
                return arr

            m = (l + r) // 2
            # call mergeSort recursively on left half
            mergeSort(arr, l, m)
            # call mergeSort recursively on right half
            mergeSort(arr, m + 1, r)
            merge(arr, l, m, r)
            return arr
        
        return mergeSort(nums, 0, len(nums) - 1)