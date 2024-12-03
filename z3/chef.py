from z3 import *

N = 10 # maximum number of states (= length of a trace)

s = Solver()

x30 = [ Int("x30_%s" % i) for i in range(N) ]
x50 = [ Int("x50_%s" % i) for i in range(N) ]
x80 = [ Int("x80_%s" % i) for i in range(N) ]

# initial state: x30=0, x50=0, x80=80
s.add(x30[0] == 0)
s.add(x50[0] == 0)
s.add(x80[0] == 80)

# bounds on the amount of liquid in each cup (not strictly necessary)
for i in range(N):
    s.add(And(x30[i]>=0,x30[i]<=30,
              x50[i]>=0,x50[i]<=50,
              x80[i]>=0,x80[i]<=80))

# general transition relation state[i] --> state[i+1]
def step(i,src,dst,xsrc,xdst,xoth):
    return And(If(xsrc[i]+xdst[i]<=dst, 
                     And(xsrc[i+1]==0,xdst[i+1]==xdst[i]+xsrc[i]),
                     And(xsrc[i+1]==xsrc[i]-(dst-xdst[i]),xdst[i+1]==dst)),
                xoth[i+1]==xoth[i])

# constrain transition relation for all states
for i in range(N-1):
    m30_50 = step(i,30,50,x30,x50,x80)
    m30_80 = step(i,30,80,x30,x80,x50)
    m50_30 = step(i,50,30,x50,x30,x80)
    m50_80 = step(i,50,80,x50,x80,x30)
    m80_30 = step(i,80,30,x80,x30,x50)
    m80_50 = step(i,80,50,x80,x50,x30)

    # each transition must be of one of the above types
    s.add(Or(m30_50,m30_80,m50_30,m50_80,m80_30,m80_50))

# goal: one of the cups contains 40 units of liquid
goal = [ Or(x50[i]==40,x80[i]==40) for i in range(N) ]

# check if the goal is reachable (for a growing number of steps)
for i in range(N):
    res = s.check(goal[i])
    if res==sat:
        print("sat at step", i)
        m = s.model()
        for j in range(i+1):
            print("x30 =", m.eval(x30[j]),
                  "\tx50 =", m.eval(x50[j]),
                  "\tx80 =", m.eval(x80[j]))
        break

if res!=sat:
    print(res)