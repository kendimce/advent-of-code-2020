import requests

#fetch your input for the puzzle
cookies = {'session': your_cookie}
r = requests.get('https://adventofcode.com/2020/day/1/input', cookies=cookies)

def fetch_input():
	inp = []
	num = ''
	for i in r.text:
		if i != '\n':
			num+=i
		else:
			inp.append(int(num))
			num=''
	return inp

##day 1 solution 2
def solve(inp):
	for i in range(len(inp)):
		for j in range(len(inp)):
			for k in range(len(inp)):
				if inp[i]+inp[j]+inp[k] == 2020:
					print(inp[i], " ", inp[j], " ", inp[i]*inp[j]*inp[k])
