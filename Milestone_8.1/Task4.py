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

    @staticmethod
    def intersection_static(interval1, interval2):
        if not isinstance(interval1, Interval) or not isinstance(interval2, Interval):
            raise ValueError("Both arguments must be instances of the Interval class.")
        
        if interval1.end < interval2.start or interval2.end < interval1.start:
            return None

        start_intersection = max(interval1.start, interval2.start)
        end_intersection = min(interval1.end, interval2.end)

        return Interval(start_intersection, end_intersection)

    def __and__(self, other_interval):
        return self.intersection_static(self, other_interval)


interval1 = Interval(1, 5)
interval2 = Interval(3, 8)
interval3 = Interval(6, 10)

intersection_result = interval1 & interval2
intersection_result_2 = interval1 & interval3

print("Intersection result:", intersection_result)  # [3, 5]
print("Intersection result (no overlap):", intersection_result_2)  # None