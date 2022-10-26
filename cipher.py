#!/usr/bin/env python

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

	@abstractmethod	
	def string_of_key(self,k):
		pass

	@abstractmethod	
	def key_of_string(self,s):
		pass
	
	def exp(self,x0,x1):
		k = self.gen()                         # generate key
		logging.info("k = " + ''.join(str(k)))		
		b = secrets.choice([0,1])              # generate random bit
		y = self.enc(x1 if b else x0,k)        # encrypt xb = x0 if b=0, x1 if b=1
		return (b,y)


## Uncipher

class Uncipher(Cipher):

	def gen(self):
		k = secrets.randbelow(26)
		return k

	def enc(self,x,k):
		return  x

	def dec(self,y,k):
		return  y

	def string_of_key(self,k):
		return chr_of_int(k)

	def key_of_string(self,s):
		return int_of_chr(s)

	
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

	def string_of_key(self,k):
		return chr_of_int(k)

	def key_of_string(self,s):
		return int_of_chr(s)
	

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


class OTP(Cipher):

	def __init__(self, n):
		self.n = n
		
	def gen(self):
		k = []
		for i in range(self.n):
			k.append(secrets.choice([0,1]))
		return k

	def enc(self,x,k):
		assert (len(x)==self.n), "Plaintext must have length " + str(self.n)
		assert (len(x)==len(k)), "Plaintexts and key have different lengths"
		assert (reduce(lambda z, b: z and b in ['0','1'], x, True)), "Plaintext not bitstring"
	
		y = []
		for i in range(self.n):
			y.append(str(int(x[i]) ^ k[i]))
		y = ''.join(y)
		return y

	def dec(self,y,k):
		assert (len(y)==self.n), "Ciphertext must have length " + str(self.n)
		assert (len(y)==len(k)), "Ciphertext and key have different lengths"
		assert (reduce(lambda z, b: z and b in ['0','1'], y, True)), "Ciphertext not bitstring"
	
		x = []
		for i in range(self.n):
			x.append(str(int(y[i]) ^ k[i]))
		x = ''.join(x)
		return x

	def string_of_key(self,k):
		s = ''.join(map (lambda ki : str(ki), k))
		return s

	def key_of_string(self,s):
		# from string to list of chr
		l = list(filter(lambda i : (i in s and i!="\n"), s))
		# from list of chr to list of int
		k = list(map(lambda ki : int(ki), l))
		return k

	
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


################################################################################
# Frontend
################################################################################

def print_usage():
    print("""\
    Usage:
    cipher scheme -gen n keyfile  generates a key of length n and writes it to keyfile
    cipher scheme -enc keyfile x  encrypts plaintext x with key
    cipher scheme -dec keyfile y  decrypts ciphertext y with key
    cipher scheme -privk x0 x1    indistinguishability experiment on plaintexts x0,x1
    
    where scheme in [Uncipher,ShiftECB,OTP]
    """)

def get_n(args,op):
	if op == "-gen":
		n = int(args[2])
		return n
	elif op in ["-enc","-dec","-privk"]:
		n = len(args[3])
		return n
	else:
		print("Unsupported operation")

def main(args):
	logging.basicConfig(format='%(message)s', filename='log', level=logging.INFO)
	if len(args) < 2:
		print_usage()
		sys.exit(0)

	scheme = args[0]
	op = args[1]
	n = 0            # n=0 when the scheme has no security parameter
	
	if scheme == "Uncipher":
		P = Uncipher()
	elif scheme == "ShiftECB":
		P = ShiftECB()
	elif scheme == "OTP":
		n = get_n(args,op)
		print("n = " + str(n))
		P = OTP(n)
	else:
		print("Unsupported encryption scheme")
		sys.exit(0)

	### Generate key
	if op == "-gen":
		k = P.gen()
		if n==0:
			keyfile = args[2]
		else:
			keyfile = args[3]

		with open(keyfile, 'w') as f:
			s = P.string_of_key(k)
			f.write(s)
			print("k = " + s)

	### Encrypt
	elif op == "-enc":
		keyfile = args[2]
		x = args[3]
		# print("Encrypting " + x + " with key in " + keyfile + "...")
		with open(keyfile, 'r') as f:
			k = P.key_of_string(f.read())
			y = P.enc(x,k)
			print(y)

	### Decrypt
	elif op == "-dec":
		keyfile = args[2]
		y = args[3]	
		# print("Decrypting " + y + " with key in " + keyfile + "...")
		with open(keyfile, 'r') as f:
			k = P.key_of_string(f.read())
			x = P.dec(y,k)
			print(x)

	### Indistinguishability experiment
	elif op == "-privk":
		x0 = args[2]
		x1 = args[3]
		(b,y) = P.exp(x0,x1)
		print("b = " + str(b))
		print("y = " + y)    

	else:
		print("Unsupported operation " + op)
		
if __name__ == '__main__':
    main(sys.argv[1:])
