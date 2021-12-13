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
	print("gcd:", r[i-1])
	print("s:", s[i-1])
	print("t:", t[i-1])
	inverse = t[i-1]
	if(inverse < 0):
		inverse = r[0] + inverse
	print("Inverse of " +str(r[1])+" is:" +str(inverse))

def EA(num1, num2):
	a = num1 if num1 > num2 else num2
	b = num2 if num1 > num2 else num1
	while(b != 0):
		t = b
		b = a % b
		a = t
	print("gcd:", a)
	



def MRT(p):
	s = 512
	r = 0
	u = p - 1
	while(u % 2 == 0):
		u = int(u/2)
		r = r + 1
	for i in range(s):
		a = random.randint(2, p-2)
		print(a)
		print(u)
		print(r)
		z = pow(a, r, p)
		if(z != 1 and z != p-1):
			for j in range(u-1):
				z = pow(z, 2, p)
				print(z)
				if(z == 1):
					print(str(p)+" is composite2")
					return
			if(z != p-1):
				print(str(p)+" is composite1")
				return
	print(str(p)+ " is probably prime")
	return

def powmod_sm(x, hdec, n):
	#equivalent of built in pow(x, h, n)
	h = bin(hdec)[2:]
	r = x
	for i in range(len(h)):
		r = (r * r) % n
		if(h[i] == 1):
			r = (r*x) % n
	print(x, "pow", hdec, "mod", n, "=", r, pow(x,hdec,n))





def main():
	#num1 = int(input("Enter a number for EA: "))
	#num2 = int(input("Enter a number for EA: "))
	#EA(num1, num2)
	#num3 = int(input("Enter first number for EEA: "))
	#num4 = int(input("Enter second number for EEA: "))
	#EEA(num3, num4)
	#num5 = int(input("Enter a number for MRT: "))
	#MRT(num5)
	num6 = int(input("Enter a number for powmod (x): "))
	num7 = int(input("Enter a number for powmod (h): "))
	num8 = int(input("Enter a number for powmod (n): "))
	powmod_sm(num6, num7, num8)




if __name__ == '__main__':
	main()