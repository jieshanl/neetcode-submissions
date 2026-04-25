class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # iterate through the intervals list
        # check if the start value of the next interval is greater than 
        # the end value of the previous interval or not

        intervals.sort(key=lambda x: x[0]) # sort the intervals by start value
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1] # the end value of the most recent interval

            if start <= lastEnd: # if overlapped
                output[-1][1] = max(lastEnd, end)
            else:
                output.append([start, end])
        return output
