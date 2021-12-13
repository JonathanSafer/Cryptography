#Project 3: Jonathan Safer
import random

def EEA(num1, num2):
	r = {}
	r[0] = num1 if num1 > num2 else num2
	r[1] = num2 if num1 > num2 else num1
	s = {}
	t = {}
	q = {}
	i = 1
	s[0] = 1
	s[1] = 0
	t[0] = 0
	t[1] = 1
	while r[i] != 0:
		i += 1
		r[i] = r[i-2] % r[i-1]
		q[i-1] = (r[i-2] - r[i])/r[i-1]
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
	a = num1 if num1 > num2 else num2
	b = num2 if num1 > num2 else num1
	while(b != 0):
		t = b
		b = a % b
		a = t
	#print("gcd:", a)
	return a
	



def MRT(p):   #s == k, p == n, u == s  
	s = 512
	r = 0
	u = p - 1
	if(p == 2 or p == 3):
		#print(str(p)+ " is prime")
		return True
	while(u % 2 == 0):
		u //= 2
		r += 1
	for i in range(s):
		a = random.randint(2, p-2)
		z = pow(a, u, p)
		if(z != 1 and z != p-1):
			for j in range(r-1):
				z = pow(z, 2, p)
				if(z == 1):
					#print(str(p)+" is composite")
					return False
			if(z != p-1):
				#print(str(p)+" is composite")
				return False
	#print(str(p)+ " is probably prime")
	return True

def powmod_sm(x, hdec, n):
	#equivalent of built in pow(x, h, n)
	if(hdec == 0):
		return 0
	h = bin(hdec)[3:]
	print(h)
	r = x
	for i in range(len(h)):
		print(h[i])
		r = (r * r) % n
		if(h[i] == '1'):
			r = (r*x) % n
	print(x, "pow", hdec, "mod", n, "=", r)
	return r

def RSAKeyGen():
	p = random.randint(2, pow(2,512))
	while(not MRT(p)):
		p = random.randint(2, pow(2,512))
	q = random.randint(2, pow(2,512))
	while(not MRT(q) or q == p):
		q = random.randint(2, pow(2,512))
	print("Primes are:", p, q)
	n = p * q
	phiN = (p-1) * (q-1)
	e = random.randint(1, phiN -1)
	while(EA(e, phiN) != 1):
		e = random.randint(1, phiN -1)
	d = EEA(e, phiN)
	print("kPub: ", n, e)
	print("kPr:", d)




def main():
	#num1 = int(input("Enter a number for EA: "))
	#num2 = int(input("Enter a number for EA: "))
	#EA(num1, num2)
	#num3 = int(input("Enter first number for EEA: "))
	#num4 = int(input("Enter second number for EEA: "))
	#EEA(num3, num4)
	#num5 = int(input("Enter a number for MRT: "))
	#print(num5, "is prime?", MRT(num5))
	#num6 = int(input("Enter a number for powmod (x): "))
	#num7 = int(input("Enter a number for powmod (h): "))
	#num8 = int(input("Enter a number for powmod (n): "))
	#powmod_sm(num6, num7, num8)

	RSAKeyGen()




if __name__ == '__main__':
	main()