"""
In the night of Halloweeen, the professors at the Science
Palace reveal their true nature. Professor Abraham Van Helsing, the
famous monster hunter, has collected the following evidence:
1. If Prof. Di Francesco is a mummy, and Prof. Scateni is not a zombie,
then Prof. Carta is a werewolf;
2. If Prof. Carta is a werewolf, then Prof. Pinna is Dracula, or Prof.
Scateni is a zombie;
3. If Prof. Pinna is not Dracula, then Prof. Di Francesco is a mummy;
4. Prof. Scateni is not a zombie.
Prove that Prof. Pinna is Dracula.
"""

from z3 import *

Monster, (Dracula,Mummy,Werewolf,Zombie) = EnumSort('monster', ['Dracula','Mummy','Werewolf','Zombie'])

Prof, (DiFrancesco,Scateni,Carta,Pinna) = EnumSort('prof', ['DiFrancesco','Scateni','Carta','Pinna'])

f = Function('f', Prof, Monster)

# variables used in forall (must be declared Const)
x,y = Consts(['x','y'], Prof)

s = Solver()

# 1. If Prof. Di Francesco is a mummy, and Prof. Scateni is not a zombie,
# then Prof. Carta is a werewolf;
s.add(Implies(And(f(DiFrancesco)==Mummy,f(Scateni)!=Zombie),f(Carta)==Werewolf))

# 2. If Prof. Carta is a werewolf, then Prof. Pinna is Dracula, or Prof. Scateni is a zombie;
s.add(Implies(f(Carta)==Werewolf,Or(f(Pinna)==Dracula,f(Scateni)==Zombie)))

# 3. If Prof. Pinna is not Dracula, then Prof. Di Francesco is a mummy;
s.add(Implies(f(Pinna)!=Dracula,f(DiFrancesco)==Mummy))

# 4. Prof. Scateni is not a zombie.
s.add(f(Scateni)!=Zombie)

# 5. Each Prof is a different monster
s.add(ForAll([x,y],Implies(x!=y,f(x)!=f(y))))

if s.check()==sat:
    print(s.model())  
      
if s.check(Not(f(Pinna)==Dracula))==unsat:
    print("Prof. Pinna is Dracula")

      
