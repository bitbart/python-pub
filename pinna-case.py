from z3 import *

# m = the murder was committed after midnight;
m = Bool('m')

# b = the crime scene is the Batcave;
b = Bool('b')

# i = Prof.\ Scateni is innocent;
i = Bool('i')

# p = the murder weapon is a 3D printer.
p = Bool('p')

# m => not b or i
# not i => p
# (p and b) => m
# b

s = Solver()

s.add(If(m,Not(b),i))
s.add(Implies(Not(i),p))
s.add(Implies(And(p,b),m))
s.add(b)

if s.check(Not(i))==unsat:
    print("Prof. Scateni is innocent")
else:
    print("Prof. Scateni could be guilty")
    print(s.model())    
