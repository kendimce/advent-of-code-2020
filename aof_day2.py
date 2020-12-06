import requests
cookies = {'session': 'yourcookie'}

#fetch your input for puzzle
r = requests.get('https://adventofcode.com/2020/day/2/input', cookies=cookies)

def fetch_input():
	inp = []
	num = ''
	for i in r.text:
		if i != '\n':
			num+=i
		else:
			inp.append(num)
			num=''
	counter = 0

##day 2_1
def num_of_occurrence(inp):
	for item in inp:
		min_occurrence = int(item.split(" ")[0].split("-")[0])
		max_occurrence = int(item.split(" ")[0].split("-")[1])
		char = item.split(" ")[1][0]
		if item.split(" ")[2].count(char) >= min_occurrence and \
			item.split(" ")[2].count(char) <= max_occurrence:
			counter+=1
	return counter


##day 2_2
def find_character(inp):
	counter = 0
	for item in inp:
		first = int(item.split(" ")[0].split("-")[0])
		second = int(item.split(" ")[0].split("-")[1])
		char = item.split(" ")[1][0]
		if item.split(" ")[2][first-1] == char and item.split(" ")[2][second-1] == char:
			pass
		elif item.split(" ")[2][first-1] == char or item.split(" ")[2][second-1] == char:
			counter+=1
	return counter
