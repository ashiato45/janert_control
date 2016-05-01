import sys

r = float(sys.argv[1])
k = float(sys.argv[2])

u = 0
for _ in range(200):
    y = u
    
    e = r - y
    u = k*e
    
    print r, e, 0, u, y
