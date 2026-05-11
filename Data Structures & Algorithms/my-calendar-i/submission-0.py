class MyCalendar:
    
    def __init__(self):
        # store all events in a list
        self.events = []

    def book(self, startTime: int, endTime: int) -> bool:
        # time overlap
        for start, end in self.events:
            if startTime < end and endTime > start:
                return False
        self.events.append((startTime, endTime))
        return True

        
# Time Complexity: O(n)
# Space Complexity: O(n)

# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)