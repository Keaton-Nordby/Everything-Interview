"""
Create a Counter system that keeps track of a number and lets you safely modify it over time.

A value (starts at 0)
Operations that change that value
A record of what happened
Real-World Analogy

Imagine:

Tracking website visits
Counting likes on a post
Keeping score in a game
Monitoring API usage

All of those are basically counters

Increase the number (increment)
Decrease the number (decrement)
Show the current value (get_value)
Reset everything (reset)
Keep a history of actions
"""


class Counter:
    def __init__(self):
        self.curr = 0
        self.history = []
        
            
    def increment(self):
        self.curr += 1
        self.history.append(("increment", self.curr))
        return self.curr
        
    def decrement(self):
        if self.curr == 0:
            raise ValueError("Cannot decrement below 0")
        
        self.curr -= 1
        self.history.append(("decrement", self.curr))
        return self.curr
            
    def reset(self):
        self.curr = 0
        self.history.append(("reset", self.curr))
        return self.curr
    
    
    def get_value(self):
        return self.curr
    
    def get_history(self):
        return list(self.history)
        
        
count = Counter()
print(count.increment())
print(count.increment())
print(count.decrement())
print(count.get_value())
print(count.get_history())

            
                