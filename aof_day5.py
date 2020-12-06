import requests
import numpy as np

cookies = {'session': your_cookie}
r = requests.get('https://adventofcode.com/2020/day/5/input', cookies=cookies)

def fetch_input(request):
	return request.text.split("\n")

def check(boarding_passes):
	##day 5_1
	# valid = []
	# for boarding_pass in boarding_passes:
	# 	valid.append(binary_search(boarding_pass))
	# return max(valid)

	##day 5_2
	boarding_list = np.zeros((128,8), dtype=int)
	for boarding_pass in boarding_passes:
		x,y = binary_search(boarding_pass)
		boarding_list[y][x] = 1
	for i in range(128):
		for j in range(8):
			if 32<i<96 and boarding_list[i][j] == 0:
				return i*8+j
				

def binary_search(boarding_pass):
#				*y F,B
#				*
#				*
#		  		 *****x L,R

	cur_y_min = 0
	cur_y_max = 127
	cur_x_min = 0
	cur_x_max = 7

	##day 5_1
	# for move in boarding_pass:
	# 	if move == "F":
	# 		cur_y_max = (cur_y_max-cur_y_min-1)/2 + cur_y_min
	# 	if move == "B":
	# 		cur_y_min = (cur_y_max-cur_y_min+1)/2 + cur_y_min
	# 	if move == "R":
	# 		cur_x_min = (cur_x_max-cur_x_min+1)/2 + cur_x_min
	# 	if move == "L":
	# 		cur_x_max = (cur_x_max-cur_x_min-1)/2 + cur_x_min
	# return cur_y_min * 8 + cur_x_min

	##day 5_2
	for move in boarding_pass:
		if move == "F":
			cur_y_max = (cur_y_max-cur_y_min-1)/2 + cur_y_min
		if move == "B":
			cur_y_min = (cur_y_max-cur_y_min+1)/2 + cur_y_min
		if move == "R":
			cur_x_min = (cur_x_max-cur_x_min+1)/2 + cur_x_min
		if move == "L":
			cur_x_max = (cur_x_max-cur_x_min-1)/2 + cur_x_min

	return int(cur_x_max),int(cur_y_min)

boarding_passes = fetch_input(r)
print(check(boarding_passes))