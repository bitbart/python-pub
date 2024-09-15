# crosshair check --analysis_kind=PEP316 remove_smallest2.py

from typing import List

def remove_smallest(numbers: List[int]) -> None:
    '''
    pre:  len(numbers) > 0
    post[numbers]: len(numbers) == 0 or min(numbers) > min(__old__.numbers)
    '''

    smallest = min(numbers)
    
    for i in range(len(numbers) -1, -1, -1):
        if numbers[i]==smallest:
            numbers.pop(i) 

# Unit tests

def test_unit1():
    l = [1,2,3]
    remove_smallest(l)
    assert l == [2,3]

def test_unit2():
    l = [12345,12346]
    remove_smallest(l)
    assert l == [12345]

# crosshair check succeeds, property is true