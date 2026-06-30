class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # iterate through the intervals list
        # check if the start value of the next interval is greater than 
        # the end value of the previous interval or not

        # Use the sorting algorithm
        # sort by the start value of each interval
        intervals.sort(key=lambda x: x[0])
        output = [intervals[0]]

        for start, end in intervals:
            lastEnd = output[-1][1]

            if start <= lastEnd:
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output

        # Time Complexity: O(n)
        # Space Complexity: O(n)
            