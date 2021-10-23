
def decode(text, letterMap):
	result = ""
	for i in range(len(text)):
		if(text[i] == ' '):
			result += ' '
		else:
			result += letterMap[text[i]]
	print(result)

def main():
	cipherText = "lrvmnir bpr sumvbwvr jx bpr lmiwv yjeryrkbi jx qmbm wi bpr xjvni mkd ymibrut jx irhx wi bpr riirkvr jx ymbinlmtmipw utn qmumbr dj w ipmhh but bj rhnvwdmbr bpr yjeryrkbi jx bpr qmbm mvvjudwko bj yt wkbrusurbmbwjk lmird jk xjubt trmui jx ibndt wb wi kjb mk rmit bmiq bj rashmwk rmvp yjeryrkb mkd wbi iwokwxwvmkvr mkd ijyr ynib urymwk nkrashmwkrd bj ower m vjyshrbr rashmkmbwjk jkr cjnhd pmer bj lr fnmhwxwrd mkd wkiswurd bj invp mk rabrkb bpmb pr vjnhd urmvp bpr ibmbr jx rkhwopbrkrd ywkd vmsmlhr jx urvjokwgwko ijnkdhrii ijnkd mkd ipmsrhrii ipmsr w dj kjb drry ytirhx bpr xwkmh mnbpjuwbt lnb yt rasruwrkvr cwbp qmbm pmi hrxb kj djnlb bpmb bpr xjhhjcwko wi bpr sujsru msshwvmbwjk mkd wkbrusurbmbwjk w jxxru yt bprjuwri wk bpr pjsr bpmb bpr riirkvr jx jqwkmcmk qmumbr cwhh urymwk wkbmvb"
	letterFreq = {
		"a": 0.0817,
		"b": 0.0150,
		"c": 0.0278,
		"d": 0.0425,
		"e": 0.1270,
		"f": 0.0223,
		"g": 0.0202,
		"h": 0.0609,
		"i": 0.0697,
		"j": 0.0015,
		"k": 0.0077,
		"l": 0.0403,
		"m": 0.0241,
		"n": 0.0675,
		"o": 0.0751,
		"p": 0.0193,
		"q": 0.0010,
		"r": 0.0599,
		"s": 0.0633,
		"t": 0.0906,
		"u": 0.0276,
		"v": 0.0098,
		"w": 0.0236,
		"x": 0.0015,
		"y": 0.0197,
		"z": 0.0007
	}
	letterTracker = { #initialize all letters in case some don't show up
		"a": 0,
		"b": 0,
		"c": 0,
		"d": 0,
		"e": 0,
		"f": 0,
		"g": 0,
		"h": 0,
		"i": 0,
		"j": 0,
		"k": 0,
		"l": 0,
		"m": 0,
		"n": 0,
		"o": 0,
		"p": 0,
		"q": 0,
		"r": 0,
		"s": 0,
		"t": 0,
		"u": 0,
		"v": 0,
		"w": 0,
		"x": 0,
		"y": 0,
		"z": 0
	}
	letterCount = 0 #we need to track letter count because spaces won't count
	for letter in cipherText:
		#count occurances of each letter
		if(letter != ' '):
			letterTracker[letter]+=1
			letterCount+=1
	for letter in letterTracker:
		#convert occurances to frequencies
		letterTracker[letter] = letterTracker[letter]/letterCount
	#now we have frequencies of each letter in the cipher and expected frequencies
	#we can compare the two by sorting them and comparing the respective indices to convert each letter
	letterMap = {}#we'll use this to map letters in the cipher text to their likely deciphered companion
	sortedLetterFreq = sorted(letterFreq, key=letterFreq.get, reverse=True)
	sortedLetterTracker = sorted(letterTracker, key=letterTracker.get, reverse=True)
	for i in range(len(letterTracker)):
		print(sortedLetterTracker[i], round(letterTracker[sortedLetterTracker[i]], 4),"=> " + sortedLetterFreq[i], letterFreq[sortedLetterFreq[i]])
		letterMap[sortedLetterTracker[i]] = sortedLetterFreq[i]
	decode(cipherText, letterMap)
	#since we converted the values in 'letterTracker' to frequencies, we can directly compare these frequencies to determine a
	#confindence level in each conversion
	#we can then take some of the lowest confidence conversions and try swapping them with their neighbors to see if that makes the text more legible
	#we can also use a dictionary or list of known words to determine how legible the text is

	#because the practice of the basic movements of kata is the focus and mastery of self is the essence of matsubayashi 
	#ryu karate do i shall try to elucidate the movements of the kata according to my interpretation based on forty years 
	#of study it is not an easy task to explain each movement and its significance and some must remain unexplained to give 
	#a complete explanation one would have to be qualified and inspired to such an extent that he could reach the state of 
	#enlightened mind capable of recognizing soundless sound and shapeless shape i do not deem myself the final authority 
	#but my experience with kata has left in doubt that the following is the proper application and interpretation i offer 
	#my theories in the hope that the essence of okinawan karate will remain intact

	#after running the program I was able to decipher the rest of the way manually through context
	#interestingly 'i', 'o', and 'n' got mixed up, probably because a lot of the words ended with "ion"
	# y => b
	# w => u
	# f => p
	# i => o
	# u => f
	# n => i
	# o => n
	# g => y
	# p => g
	# v => x
	# x => q
	# q => z
	# k => w
	# b => k


if __name__ == "__main__":
	main()