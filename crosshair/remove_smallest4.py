# crosshair check --analysis_kind=PEP316 remove_smallest4.py

from typing import List

def remove_smallest(numbers: List[int]) -> None:
    '''
    pre:  len(numbers) > 0
    post[numbers]: len(numbers) == 0 or min(numbers) > min(__old__.numbers)
    '''

    smallest = min(numbers) 
    i = 0

    while i<len(numbers):
        if numbers[i]==smallest:
            numbers.pop(i)
        i+=1

# Unit tests

def test_unit1():
    l = [1,2,3]
    remove_smallest(l)
    assert l == [2,3]

def test_unit2():
    l = [0,0]
    remove_smallest(l)
    assert l == []