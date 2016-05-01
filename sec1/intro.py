from intro_feedback import *

c = Controller(1.25, 0.01)
p = Buffer(50, 10)

#open_loop(p, 1000)
closed_loop(c, p, 1000)
