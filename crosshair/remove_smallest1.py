# crosshair check --analysis_kind=PEP316 remove_smallest1.py

from typing import List

def remove_smallest(numbers: List[int]) -> None:
    '''
    pre: len(numbers) > 0
    post[numbers]: len(numbers) == 0 or min(numbers) > min(__old__.numbers)
    '''

    smallest = min(numbers)
    
    for n in numbers:
        if n==smallest:
            numbers.remove(n)
            
# Unit tests

def test_unit1():
    l = [1,2,3]
    remove_smallest(l)
    assert l == [2,3]

def test_unit2():
    l = [0,0]
    remove_smallest(l)
    assert l == []

# crosshair check succeeds, but property is false by counterexample [0, 0]