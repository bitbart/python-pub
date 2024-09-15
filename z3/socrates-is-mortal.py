from z3 import *

Universe = DeclareSort('Universe')

# predicates
Human = Function('Human', Universe, BoolSort())
Mortal = Function('Mortal', Universe, BoolSort())

# constant
socrates = Const('socrates', Universe)

# variables used in forall (must be declared Const)
x = Const('x', Universe)

axioms = [ForAll([x], Implies(Human(x), Mortal(x))), 
          Human(socrates)]

s = Solver()
s.add(axioms)

print(s.check()) # prints sat so axioms are coherent

# classical refutation
s.add(Not(Mortal(socrates)))

if s.check()==unsat:
    print("Socrates is mortal")
else:
    print("Socrates could be immortal")
    print(s.model())    
