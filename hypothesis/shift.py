# pytest --hypothesis-show-statistics shift.py

from hypothesis import given, assume
from hypothesis.strategies import *

def int_of_chr(n):
	return ord(n)-ord('a')

def chr_of_int(n):
	return chr(n + ord('a'))

def shift_enc(m,k):
    c = [] # cipher text
    for i in range(len(m)):
        c.append(chr_of_int((int_of_chr(m[i]) + k) % 26))
    return ''.join(c)

def shift_dec(c,k):
    m = [] # plain text
    for i in range(len(c)):
        m.append(chr_of_int((int_of_chr(c[i]) - k) % 26))
    return ''.join(m)

### Unit tests

def test_shift1():
    m = "hello"
    k = 3
    c = shift_enc(m,k)
    assert shift_dec(c,k) == m

def test_shift2():
    m = ""
    k = 3
    c = shift_enc(m,k)
    assert shift_dec(c,k) == m

### Property-based tests

@given(characters(min_codepoint=ord('a'),max_codepoint=ord('z')))
def test_chr_int_chr(a):
    assert chr_of_int(int_of_chr(a) == a)

@given(lists(integers(min_value=0, max_value=25)), integers(min_value=0, max_value=25))
def test_dec_enc(x,k):
    m = ''.join([chr_of_int(i) for i in x])
    c = shift_enc(m,k)
    assert shift_dec(c,k) == m

@given(lists(integers(min_value=0, max_value=25)), integers(min_value=0, max_value=25), integers(min_value=0, max_value=25))
def test_enc_inj(x,k1,k2):
    assume(k1 != k2)
    assume(len(x) > 0)
    m = ''.join([chr_of_int(i) for i in x])
    c1 = shift_enc(m,k1)
    c2 = shift_enc(m,k2)
    assert c1 != c2