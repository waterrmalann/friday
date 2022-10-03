from time import time
from assistant.utils.ticker import Ticker

class Scheduler:
    def __init__(self, delay):
        self.delay = delay
        self.queue = {}  # => [(func, unix_time_to_run_at), ]
        self.ticker = Ticker(delay, self.tick)

        self.item_id = -1
    
    def new_id(self):
        self.item_id += 1
        return f"SCHED#{self.item_id}"
    
    def start(self):
        self.ticker.start()

    def tick(self):
        to_delete = []

        for item_id, item in self.queue.items():
            if time() >= item[1]:
                item[0]()
                to_delete.append(item_id)
        
        for item in to_delete:
            self.queue.pop(item)

    def queue_event(self, func: callable, unix_time: int):
        self.queue[self.new_id()] = (func, unix_time)

class EventLoop:
    def __init__(self, delay):
        self.delay = delay
        self.functions = []
        self.ticker = Ticker(delay, self.tick)
    
    def start(self):
        self.ticker.start()
    
    def tick(self):
        for func in self.functions:
            func()
    
    def add_function(self, func: callable):
        self.functions.append(func)