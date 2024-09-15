# pytest --hypothesis-show-statistics max3.py

from hypothesis import *
from hypothesis.strategies import integers

def max3(n1,n2,n3):
	if n1>n2:
		if n1>n3:
			return n1
		else:
			return n3
	else:
		if n2>n3:
			return n2
		else:
			return n3 # should be n3

def test_unit1():
     assert max3(1,2,3) == 3

def test_unit2():
     assert max3(3,2,1) == 3

@given(integers(),integers(),integers())
def test_geq(n1,n2,n3):
	z = max3(n1,n2,n3)
	assert z >= n1 and z>=n2 and z>=n3
