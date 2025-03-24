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

interval = Interval(1, 5)
print(interval)  # [1, 5]