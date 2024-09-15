# pytest --hypothesis-show-statistics dict.py

from hypothesis import *
from hypothesis.strategies import *

class MyDict:
    def __init__(self):
        self.l = []

    def insert(self, k, v):
        for i in range(len(self.l)):
            if self.l[i][0] == k:
                self.l[i] = (k,v)
                return
        self.l.append((k,v))

    def remove(self, k):
        for i in range(len(self.l)):
            if self.l[i][0] == k:
                self.l.pop(i)
                return

    def find(self, k):
        for i in range(len(self.l)):
            if self.l[i][0] == k:
                return self.l[i][1]
        return None
    
    def keys(self):
        return [x[0] for x in self.l]

### Unit tests
  
def test_unit1():
     d = MyDict()
     d.insert("a",1)
     d.insert("b",2)
     d.insert("a",3)
     assert d.find("a") == 3
     assert d.find("b") == 2

def test_unit2():
     d = MyDict()
     d.insert("a",1)
     d.insert("b",2)
     d.remove("a")
     assert d.find("a") == None

def test_unit3():
     d = MyDict()
     d.insert("a",1)
     d.insert("b",2)
     d.remove("a")
     assert d.keys() == ["b"]

### Property-based tests

def dup(l):
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i] == l[j]:
                return True
    return False

def test_unit4():
     d = MyDict()
     d.insert("",0)
     d.insert("0",0)
     assert not dup(d.keys())

@given(lists(tuples(integers(),integers())), integers(), integers())
def test_no_dup(l, i, j):
    assume(len(l) > 0)
    i = i % len(l) # index to be copied
    j = j % len(l) # index where l[i] is copied
    l.insert(j,l[i])
    assert dup(l)

# Testing invariants

@given(lists(tuples(text(),integers())))
def test_insert_no_dup(l):
    d = MyDict()
    for i in range(len(l)):
        d.insert(l[i][0],l[i][1])

    assert not dup(d.keys())

# Testing postconditions

@given(lists(tuples(text(),integers())), text(), integers())
def test_insert(l,k,v):
    d = MyDict()
    for i in range(len(l)):
        d.insert(l[i][0],l[i][1])

    d.insert(k,v)
    assert d.find(k) == v
    
@given(lists(tuples(text(),integers())), text())
def test_remove(l,k):
    d = MyDict()
    for i in range(len(l)):
        d.insert(l[i][0],l[i][1])

    d.remove(k)
    assert d.find(k) == None

# Testing metamorphic properties

def eq_dict(d0,d1):
    l0 = sorted(d0.l, key=lambda x: x[0])
    l1 = sorted(d1.l, key=lambda x: x[0])
    return l0 == l1

def test_unit5():
     d0,d1 = MyDict(),MyDict()
     d0.insert("a",0)
     d0.insert("b",1)
     d1.insert("b",1)
     d1.insert("a",0)
     assert eq_dict(d0,d1)

def test_unit6():
     d0,d1 = MyDict(),MyDict()
     d0.insert('',0)
     d0.insert("0",0)
     d1.insert("0",0)
     d1.insert('',0)
     assert eq_dict(d0,d1)

@given(lists(tuples(text(),integers())), text(), integers(), text(), integers())
def test_insert_insert(l,k0,v0,k1,v1):
    assume(k0 != k1)

    d0 = MyDict()
    d1 = MyDict()

    for i in range(len(l)):
        d0.insert(l[i][0],l[i][1])
        d1.insert(l[i][0],l[i][1])

    d0.insert(k0,v0)
    d0.insert(k1,v1)

    d1.insert(k1,v1)
    d1.insert(k0,v0)

    assert eq_dict(d0,d1)

@given(lists(tuples(text(),integers())), text(), text(), text())
def test_remove_remove(l,k0,k1,k2):
    assume(k0 != k1)
    
    d0 = MyDict()
    d1 = MyDict()

    for i in range(len(l)):
        d0.insert(l[i][0],l[i][1])
        d1.insert(l[i][0],l[i][1])

    d0.remove(k0)
    d0.remove(k1)

    d1.remove(k1)
    d1.remove(k0)

    assert d0.find(k2) == d1.find(k2)
