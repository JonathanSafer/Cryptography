#hexor

def hexToBinary(digit):
	digitMap = {
		"0": "0000",
		"1": "0001",
		"2": "0010",
		"3": "0011",
		"4": "0100",
		"5": "0101",
		"6": "0110",
		"7": "0111",
		"8": "1000",
		"9": "1001",
		"a": "1010",
		"b": "1011",
		"c": "1100",
		"d": "1101",
		"e": "1110",
		"f": "1111",
	}
	return digitMap[digit]

def binaryToHex(digits):
	digitMap = {
		"0000": "0",
		"0001": "1",
		"0010": "2",
		"0011": "3",
		"0100": "4",
		"0101": "5",
		"0110": "6",
		"0111": "7",
		"1000": "8",
		"1001": "9",
		"1010": "a",
		"1011": "b",
		"1100": "c",
		"1101": "d",
		"1110": "e",
		"1111": "f",
	}
	return digitMap[digits]

def xor(bit1, bit2):
	if(bit1 == bit2):
		return "0"
	return "1"

def hexor(num1, num2):
	binary1 = hexToBinary(num1)
	binary2 = hexToBinary(num2)
	result = ""
	for i in range(len(binary1)):
		result += xor(binary1[i], binary2[i])
	return binaryToHex(result)

def main():
	num1 = "678e3fc5ed24c239"
	num2 = "4849dcb518233f9a"
	result = ""
	for i in range(len(num1)):
		result += hexor(num1[i], num2[i])
	print(result)



if __name__ == "__main__":
	main()


#for each digit of both numbers (left to right)
#convert both to binary string
#for each bit of binary (left to right)
#compare bits and append onto result string
#convert result to hex
#append hex onto result string
