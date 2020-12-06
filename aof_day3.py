import requests
import numpy as np
cookies = {'session': your_cookie}
r = requests.get('https://adventofcode.com/2020/day/3/input', cookies=cookies)

def fetch_input():
	inp = []
	row = ''

	for item in r.text:
		if item == "\n":
			pass
		else:
			inp.append(item)
	return inp


##day 3_1
def find_trees(tree_map,right,down):
	cur_y = 0
	number_of_trees = 0
	for cur_x in range(0,len(tree_map),down):
		if tree_map[cur_x][cur_y] == "#":
			number_of_trees+=1
		if cur_y + right >= len(tree_map[0]):
			cur_y=cur_y+right-len(tree_map[0])
		else:
			cur_y+=right
	return number_of_trees

##day 3_2
inp = np.array(fetch_input()).reshape(323,31)
slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]
product_of_trees = 1
for slope in slopes:
	product_of_trees*=find_trees(inp,slope[0],slope[1])
print(product_of_trees)