#Extended Euclidean Algorithm

def eea(num1, num2):
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

def main():
	num1 = int(input("Enter num1: "))
	num2 = int(input("Enter num2: "))
	eea(num1, num2)

if __name__ == '__main__':
	main()