import requests
import numpy as np

cookies = {'session':your_cookie}
r = requests.get('https://adventofcode.com/2020/day/6/input', cookies=cookies)

def fetch_input(request):
	return request.text.split("\n\n")


##day 6_1
# def yes_man(answers):
	# total = 0
	# for answer in answers:
	# 	answered = ''
	# 	for each_persons_answer in answer.split("\n"):
	# 			num_of_yes, unique = filter(each_persons_answer, answered)
	# 			total+=num_of_yes
	# 			answered+=unique
	# return total

#day 6_1
# def filter(string, answered):
# 	counter_per_person = 0
# 	for char in answered:
# 		string = string.replace(char,"")
# 		answered = answered.replace(char,"")
# 	for char in string:
# 		counter_per_person+=1
# 		string = string.replace(char, "")
# 		answered+=char
# 	return counter_per_person,answered

#day 6_2
def yes_man(answers):
	total = 0
	for group_answer in all_answers:
		length = len(group_answer.split("\n"))
		collected_answers = ''
		for each_person_answer in group_answer.split("\n"):
			if each_person_answer == "":
				length = length - 1
			collected_answers+=each_person_answer
		cp = list(collected_answers)
		for question in cp:
			if collected_answers.count(question) == length:
				total+=1
				collected_answers = collected_answers.replace(question,"")
	return total

all_answers = fetch_input(r)
print(yes_man(all_answers))