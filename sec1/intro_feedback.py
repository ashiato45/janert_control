import random

class Buffer:
    def __init__(self, max_wip, max_flow):
        self.queued = 0
        self.wip = 0  # Work-In-Progress
        
        self.max_wip = max_wip
        self.max_flow = max_flow
        
    def work(self, u):
        u = max(0, int(round(u)))
        u = min(u, self.max_wip)
        self.wip += u
        
        r = int(round(random.uniform(0, self.wip)))
        #r = min(r, self.queued)
        self.wip -= r
        self.queued += r
        
        r = int(round(random.uniform(0, self.max_flow)))
        r = min(r, self.queued)
        self.queued -= r
        
        return self.queued
        
class Controller:
    def __init__(self, kp, ki):
        self.kp, self.ki = kp, ki
        self.i = 0
        
    def work(self, e):
        self.i += e
        return self.kp*e + self.ki*self.i
        
def open_loop(p, tm=5000):
    def target(t):
        return 5.0
        
    for t in range(tm):
        u = target(t)
        y = p.work(u)
        
        print t, u, 0, u, y

def closed_loop(c, p, tm=5000):
    def setpoint(t):
        if t < 100:
            return 0
        if t < 300:
            return 50
        return 10
   
    y = 0
    for t in range(tm):
        r = setpoint(t)
        e = r - y
        u = c.work(e)
        y = p.work(u)
        
        print t, r, e, u, y
