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
	print("gcd: ", r[i-1])
	print("s: ", s[i-1])
	print("t: ", t[i-1])
	inverse = t[i-1]
	if(inverse < 0):
		inverse = r[0] + inverse
	print("Inverse of " +str(r[1])+" is: " +str(inverse))


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
					print(str(p)+" is composit2")
					return
			if(z != p-1):
				print(str(p)+" is composite1")
				return
	print(str(p)+ " is probably prime")
	return

def main():
	#num1 = int(input("Enter first number for EEA: "))
	#num2 = int(input("Enter second number for EEA: "))
	#EEA(num1, num2)
	num3 = int(input("Enter a number for MRT: "))
	MRT(num3)

if __name__ == '__main__':
	main()