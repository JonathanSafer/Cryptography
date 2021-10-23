a = 486623425
b = 159866762
x = b
while(a % x != 0 or b % x != 0):
	x -= 1
print(x)