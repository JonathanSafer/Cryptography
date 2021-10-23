#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
	int a = 7;
	int b = 22;
	int letters = 26;
	int aInverse = 0;
	//find a-1
	while(aInverse * a % letters != 1){
		aInverse++;
	}
	cout << aInverse << endl;
	string scramble = "OEXXRWSYHPOS";
	string result = "";
	for(int i = 0; i < scramble.length(); i++){
		int num = int(scramble[i]);
		int shift = num - 65 - b;
		while(shift < 0){
			shift += 26;
		}
		int translate = (shift * aInverse % 26) + 65;
		char newChar = char(translate);
		result.push_back(newChar);
	}
	cout << result << endl;
}