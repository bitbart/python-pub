"""
https://learninghypothesis.com/halloween-worksheets-activities-for-older-kids/
"""

from z3 import *

Monster, (dracula,mummy,witch,zombie) = EnumSort('monster', ['Dracula','Mummy','Witch','Zombie'])

Supply, (broom,candy,pumpkin,flashlight) = EnumSort('supply', ['Broom','Candy','Pumpkin','Flashlight'])

fDay = Function('MonsterDay', Monster, IntSort())
fSupply = Function('MonsterSupply', Monster, Supply)

# variables used in forall (must be declared Const)
x,y = Consts(['x','y'], Monster)

s = Solver()

# All the items are purchased
s.add(ForAll([x,y],Implies(x!=y,fSupply(x)!=fSupply(y))))

# No monsters buy in the same day
s.add(ForAll([x,y],Implies(x!=y,fDay(x)!=fDay(y))))

# Possible days = monday, thursday, friday, saturday
s.add(ForAll([x],Or(fDay(x)==1,And(fDay(x)>=4,fDay(x)<=6))))

# 1. Dracula did not go out on Friday
s.add(fDay(dracula)!=5)

# 2. The monster who got candy did not go out on Monday - Thursday
s.add(ForAll([x],Implies(fSupply(x)==candy,And(fDay(x)!=1,fDay(x)!=4))))

# 3. The Witch did not take the broom
s.add(fSupply(witch)!=broom)

# 4. The monster who got pumpkin was not Dracula
s.add(fSupply(dracula)!=pumpkin)

# 5. The mummy went out on Friday or on Saturday
s.add(Or(fDay(mummy)==5,fDay(mummy)==6))

# 6. The monster who got the broom was with Dracula Friday
s.add(ForAll([x],Implies(fSupply(x)==broom,fDay(x)!=5)))

# 7. The pumpkin was purchased on Saturday
s.add(ForAll([x],Implies(fSupply(x)==pumpkin,fDay(x)==6)))

# 8. The Witch was busy on Thursday and Friday
s.add(fDay(witch)!=4,fDay(witch)!=5)

# 9. The Zombie did not buy the item on Monday
s.add(fDay(zombie)!=1)

# 10a. The broom was purchased AFTER the flashlight
# (The flashlight was not purchased on sa)
s.add(ForAll([x,y],Implies(
    And(fSupply(x)==broom,fSupply(y)==flashlight),
    fDay(y)<=fDay(x))))

# 10b. The candy was purchased AFTER the broom
# (The broom was not purchased on sa)
s.add(ForAll([x,y],Implies(
    And(fSupply(x)==candy,fSupply(y)==broom),
    fDay(y)<=fDay(x))))

# 11a. The Mummy was not with Dracula on Friday

# 11b. The Witch did not buy the item on Monday
s.add(fDay(witch)!=1)

if s.check()==unsat:
    print("unsat")
else:
    print(s.model())

