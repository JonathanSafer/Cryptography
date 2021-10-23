def cipher(block, key):
	return (key + 11*block)%256

def CTRencrypt(word, key, iv):
	counter = iv
	result = "CTR: 0x"
	for i in range(len(word)):
		char = word[i]
		encrypted = cipher(counter, key)
		num = ord(char)
		xor = num ^ encrypted
		if(xor <= 15):
			result += "0"
		result += hex(xor)[2:]
		counter += 1
	print(result)

def CFBencrypt(word, key, iv):
	prevBlock = iv
	result = "CFB: 0x"
	for i in range(len(word)):
		encrypted = cipher(prevBlock, key)
		xor = ord(word[i]) ^ encrypted
		prevBlock = xor
		if(xor <= 15):
			result += "0"
		result += hex(xor)[2:]
	print(result)

def OFBencrypt(word, key, iv):
	prevBlock = iv
	result = "OFB: 0x"
	for i in range(len(word)):
		encrypted = cipher(prevBlock, key)
		xor = ord(word[i]) ^ encrypted
		prevBlock = encrypted
		if(xor <= 15):
			result += "0"
		result += hex(xor)[2:]
	print(result)

def ECBencrypt(word, key):
	result = "ECB: 0x"
	for i in range(len(word)):
		encrypted = cipher(ord(word[i]), key)
		if(encrypted <= 15):
			result += "0"
		result += hex(encrypted)[2:]
	print(result)

def CBCencrypt(word, key, iv):
	prevBlock = iv
	result = "CBC: 0x"
	for i in range(len(word)):
		xor = ord(word[i]) ^ prevBlock
		encrypted = cipher(xor, key)
		prevBlock = encrypted
		if(encrypted <= 15):
			result += "0"
		result += hex(encrypted)[2:]
	print(result)


def main():
	key = 8 #key in decimal
	word = input("Enter your word: ")
	iv = 170 #for example, iv of 0xAA == 170
	ctrIV = 168 #for example, left five bits of 0xAA == 168
	CTRencrypt(word, key, ctrIV)
	ECBencrypt(word, key)
	CFBencrypt(word, key, iv)
	CBCencrypt(word, key, iv)
	OFBencrypt(word, key, iv)

main()
