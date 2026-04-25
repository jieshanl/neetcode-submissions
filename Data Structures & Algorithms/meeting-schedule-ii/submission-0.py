"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # use a min heap to store the end times
        # the first available room will be poped and reused, otherwise push a new room
        intervals.sort(key = lambda x: x.start)
        # initialize a min_heap to store each end time
        min_heap = []

        for interval in intervals:
            if min_heap and interval.start >= min_heap[0]: # min_heap[0] means the earliest end time
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end) # we push a new node into min_heap\
        return len(min_heap)