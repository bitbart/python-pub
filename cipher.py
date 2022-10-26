# Container class for priv-key ciphers

import sys
import logging
import secrets
from abc import ABC, abstractmethod
from functools import reduce

def int_of_chr(n):
	return ord(n)-ord('a')

def chr_of_int(n):
	return chr(n + ord('a'))


class Cipher(ABC):

	@abstractmethod
	def gen(self,n):
		pass

	@abstractmethod
	def enc(self,x,k):
		pass

	@abstractmethod
	def dec(self,y,k):
		pass
    
	def exp(self,x0,x1):
		k = self.gen()                         # generate key
		logging.info("k = " + ''.join(str(k)))		
		b = secrets.choice([0,1])              # generate random bit
		y = self.enc(x1 if b else x0,k)        # encrypt xb = x0 if b=0, x1 if b=1
		return (b,y)

	
## Shift cipher in ECB mode with uniform keys and plaintexts of arbitrary length

class ShiftECB(Cipher):

	def gen(self):
		k = secrets.randbelow(26)
		# print("k = " + str(k))
		return k

	def enc(self,x,k):
		return  ''.join(map(lambda n : chr_of_int((int_of_chr(n) + k)%26), x))

	def dec(self,y,k):
		return  ''.join(map(lambda n : chr_of_int((int_of_chr(n) - k)%26), y))


## Shift cipher with non-uniform keys and plaintexts of length 1

class Shift1Unbal(Cipher):

    def gen(self):
        a = secrets.choice([0,1])
        if a==0:
            k=25
        else:
            k = secrets.randbelow(25)
        return k

    def enc(self,x,k):
        assert(len(x)==1),"Plaintext must have length 1"
        return  ''.join(map(lambda n : chr_of_int((int_of_chr(n) + k)%26), x))

    def dec(self,y,k):
        assert(len(x)==1),"Ciphertext must have length 1"    
        return  ''.join(map(lambda n : chr_of_int((int_of_chr(n) - k)%26), y))


## Vigenere cipher with non-uniform keys and plaintexts of length 2

class Vigenere2Unbal(Cipher):
	def gen(self):
		a = secrets.choice([0,1])
		k0 = secrets.randbelow(26)
		if a==0:
			k1 = k0
		else:
			k1 = secrets.randbelow(26)
		return [k0,k1]

	def enc(self,x,k):
		assert(len(x)==2 and len(k)==2)
		y0 = ''.join(map(lambda n : chr_of_int((int_of_chr(n) + k[0])%26), x[0]))
		y1 = ''.join(map(lambda n : chr_of_int((int_of_chr(n) + k[1])%26), x[1]))		
		return y0+y1

	def dec(self,y,k):
		pass


## OTP where the last bit of the key if the XOR of the previous bits

class OTPlastXor(Cipher):

	def __init__(self, n):
		assert(n>0),"n must be greater than 0"
		self.n = n
	
	def gen(self):
		k = []
		for i in range(self.n-1):
			k.append(secrets.choice([0,1]))

		lb = reduce(lambda z, y: z ^ y, k, 0)
		k.append(lb)
		return k

	def enc(self,x,k):
		assert (len(x)==self.n), "Plaintext must have length " + str(self.n)
		assert (len(x)==len(k)), "Plaintexts and key have different lengths"
		assert (reduce(lambda z, y: z and y in ['0','1'], x,True)), "Plaintext not bitstring"
		y = []
		for i in range(len(k)):
			y.append(str(int(x[i]) ^ k[i]))
		y = ''.join(y)
		return y

	def dec(self,y,k):
		pass

	
## TwoTP: two-time pad

class TwoTP(Cipher):

	def __init__(self, n):
		assert(n%2==0),"n must be even"
		self.n = n

	def gen(self):
		k = []
		for i in range(int(self.n/2)):
			k.append(secrets.choice([0,1]))
		k = k + k
		return k

	def enc(self,x,k):
		assert (len(x)==self.n), "Plaintext must have length " + str(self.n)
		assert (len(x)==len(k)), "Plaintexts and key have different lengths"
		assert (reduce(lambda z, y: z and y in ['0','1'], x,True)), "Plaintext not bitstring"
		
		y = []
		for i in range(self.n):
			# y[i] = x[i] ^ k[i]
			y.append(str(int(x[i]) ^ k[i]))
		y = ''.join(y)
		return y

	def dec(self,y,k):
		pass


## Quasi-OTP

class QuasiOTP(Cipher):

	def __init__(self, n):
		self.n = n
		
	def gen(self):
		found = False
		while not found:
			k = []
			for i in range(self.n):
				k.append(secrets.choice([0,1]))
			for bi in k:
				if bi==1:
					found=True
		return k

	def enc(self,x,k):
		assert (len(x)==self.n), "Plaintext must have length " + str(self.n)
		assert (len(x)==len(k)), "Plaintexts and key have different lengths"
		assert (reduce(lambda z, y: z and y in ['0','1'], x,True)), "Plaintext not bitstring"
	
		y = []
		for i in range(self.n):
			y.append(str(int(x[i]) ^ k[i]))
		y = ''.join(y)
		return y

	def dec(self,y,k):
		pass


def main(args):
    logging.basicConfig(format='%(message)s', filename='log', level=logging.INFO)
    P = Vigenere2Unbal()
    (b,y) = P.exp("aa","ab")
    print("b = " + str(b))
    print("y = " + y)    

if __name__ == '__main__':
    main(sys.argv[1:])
