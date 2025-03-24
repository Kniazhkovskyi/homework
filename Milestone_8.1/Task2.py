class Interval:
    def __init__(self, start, end):
        if not (isinstance(start, (int, float)) and isinstance(end, (int, float))):
            raise ValueError("Both start and end must be numeric values.")
        
        if start > end:
            raise ValueError("Start value must be less than or equal to end value.")
        
        self.start = start
        self.end = end

    def __str__(self):
        return f"[{self.start}, {self.end}]"
    
    def is_overlapping(self, other_interval):
        if not isinstance(other_interval, Interval):
            raise ValueError("The argument must be an instance of the Interval class.")
        
        return not (self.end < other_interval.start or self.start > other_interval.end)


interval1 = Interval(1, 5)
interval2 = Interval(3, 8)
interval3 = Interval(6, 10)

overlap_result1 = interval1.is_overlapping(interval2)
overlap_result2 = interval1.is_overlapping(interval3)

print("Do intervals 1 and 2 overlap?", overlap_result1)  # True
print("Do intervals 1 and 3 overlap?", overlap_result2)  # False