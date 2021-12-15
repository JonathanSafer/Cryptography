#Project 3: Jonathan Safer
import random

def EEA(num1, num2):
	r = {}
	r[0] = num2
	r[1] = num1
	s = {}
	t = {}
	q = {}
	i = int(1)
	s[0] = int(1)
	s[1] = int(0)
	t[0] = int(0)
	t[1] = int(1)
	while r[i] != 0:
		i += 1
		r[i] = r[i-2] % r[i-1]
		q[i-1] = (r[i-2] - r[i])//r[i-1]
		s[i] = s[i-2] - (q[i-1] * s[i-1])
		t[i] = t[i-2] - (q[i-1] * t[i-1])
	#print("gcd:", r[i-1])
	#print("s:", s[i-1])
	#print("t:", t[i-1])
	inverse = t[i-1]
	if(inverse < 0):
		inverse = r[0] + inverse
	#print("Inverse of " +str(r[1])+" is:" +str(inverse))
	return inverse

def EA(num1, num2):
	a = num1
	b = num2
	while(b != 0):
		t = b
		b = a % b
		a = t
	#print("gcd:", a)
	return a
	

def tryA(a, p, r, u):
	if(powmod_sm(a, r, p) == 1):
		return False
	for i in range(u):
		if(powmod_sm(a, 2**i * r, p) == p-1):
			return False
	return True

def MRT(p):
	s = 80
	u = 0
	r = p - 1
	if(p == 2 or p == 3):
		#print(str(p)+ " is prime")
		return True
	if(p%2 == 0):
		return False
	while(r % 2 == 0):
		r >>= 1
		u += 1
	for i in range(s):
		a = random.randrange(2, p)
		if(tryA(a, p, r, u)):
			return False
	return True


def powmod_sm(x, hdec, n):
	#equivalent of built in pow(x, h, n)
	if(hdec == 0):
		return 0
	h = bin(hdec)[3:]
	#print(h)
	r = x
	for i in range(len(h)):#square for each digit
		#print(h[i])
		r = (r * r) % n
		if(h[i] == '1'):#if bit is 1, multiply
			r = (r*x) % n
	#print(x, "pow", hdec, "mod", n, "=", r)
	return r

def RSAKeyGen():
	p = random.getrandbits(512)
	while(not MRT(p)): #generate new numbers until one is prime
		p = random.getrandbits(512)
	q = random.getrandbits(512)
	while(not MRT(q) or p == q): #generate new numbers until one is prime and not equal to p
		q = random.getrandbits(512)
	print("Primes are:", p, q)
	n = p * q
	phiN = (p-1) * (q-1) #phiN = phi(n)
	e = random.randint(2, phiN -1)
	while(EA(e, phiN) != 1): #choose and e that has a gcd of 1 with phi(n)
		e = random.randint(2, phiN -1)
	d = EEA(e, phiN) #d is modular inverse of e and phi(n)
	print(e, phiN)
	print("kPub: ", n, e)
	print("kPr:", d)
	return [n, e, d]

def RSAencrypt(n, e, m):
	return powmod_sm(m, e, n)

def RSAdecrypt(n, d, c):
	return powmod_sm(c, d, n)




def main():
	num1 = int(input("Enter first number for EA: "))
	num2 = int(input("Enter second number for EA: "))
	print("gcd of",num1,"and",num2,"=",EA(num1, num2))
	num3 = int(input("Enter first number for EEA: "))
	num4 = int(input("Enter second number for EEA: "))
	print("Inverse of", num3, "mod", num4,"=",EEA(num3, num4))
	num5 = int(input("Enter a number for MRT: "))
	print(num5, "is prime?", MRT(num5))
	num6 = int(input("Enter a number for powmod (x): "))
	num7 = int(input("Enter a number for powmod (h): "))
	num8 = int(input("Enter a number for powmod (n): "))
	print(num6,"^",num7,"mod",num8,"=",powmod_sm(num6, num7, num8))

	message = int(input("Enter a number to be encrypted: "))
	keys = RSAKeyGen()
	c = RSAencrypt(keys[0], keys[1], message)
	print("The encrypted message is:", c)
	print("The decrypted message is:", RSAdecrypt(keys[0], keys[2], c))




if __name__ == '__main__':
	main()