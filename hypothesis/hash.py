from hypothesis import *
from hypothesis.strategies import *

def hash(s, N):
    h = 0
    for c in s:
        h += ord(c)
    return h % N

class HashTable:
    def __init__(self, N):
        self.size = N
        self.l = [ [ ] for i in range(self.size) ]

    def put(self, k, v):
        h = hash(k, len(self.l))
        # self.l[h] = [ (k,v) ]
        lh = self.l[h]
        for i in range(len(lh)):
            if lh[i][0] == k:
                oldv = lh[i][1]
                lh[i] = (k,v)
                return oldv
        lh.append((k,v))
        return None

    def get(self, k):
        h = hash(k, len(self.l))
        lh = self.l[h]
        for kv in lh:
            if kv[0] == k:
                return kv[1]
        return None
    
    def remove(self, k):
        h = hash(k, len(self.l))
        lh = self.l[h]
        for i in range(len(lh)):
            kv = lh[i]
            if kv[0] == k:
                lh.pop(i)
                return kv[1]

        return None


# Unit tests

def test_unit1():
    t = HashTable(10)
    t.put("a",1)
    t.put("b",2)
    assert t.get("a") == 1

def test_unit2():
    t = HashTable(10)
    t.put("a",1)
    t.put("b",2)
    t.put("a",3)
    assert t.get("a") == 3

def test_unit3():
    t = HashTable(10)
    t.put("a",1)
    t.put("b",2)
    t.remove("a")
    assert t.get("a") == None

def test_unit4():
    t = HashTable(10)
    t.put("0Z",2)
    t.put("0",1)
    assert t.get("0Z") == 2

# Property-based tests

@given(lists(tuples(text(),integers())), text(), integers())
def test_put_get(l, k, v):
    assume(k not in [ kv[0] for kv in l ])
    t = HashTable(10)
    t.put(k, v)
    
    for kv in l:
        t.put(kv[0], kv[1])
    
    assert t.get(k) == v