import requests
import numpy as np

cookies = {'session': your_cookie}
r = requests.get('https://adventofcode.com/2020/day/4/input', cookies=cookies)

fields = {
	"ecl":["amb","blu","brn","gry","grn","hzl","oth"],
	"eyr":[2020,2030],
	"byr":[1920,2002],
	"hcl":6,
	"iyr":[2010,2020],
	"hgt":
		{
			"cm":[150,193],
			"in":[59,76]
		},
	"pid":9
	}

def fetch_input(request):
	return request.text.split("\n\n")


def number_of_valid_passports(passports):
	valid_passports = 0
	for passport in passports:
		try:
			valid_passports+=check_validity(passport)
		except:
			pass
	return valid_passports


def check_validity(passport):
	# #day 4_1
	for k in fields.keys():
		if not passport.count(k):
			return 0
	##day 4_2
	for requirement in passport.split("\n"):
		for pair in requirement.split(" "):
			key, value = pair.split(":")[0],pair.split(":")[1]
			if key == "byr":
				if not int(value) in range(1920,2003):
					return 0
			if key == "iyr":
				if not int(value) in range(2010,2021):
					return 0
			if key == "eyr":
				if not int(value) in range(2020,2031):
					return 0
			if key == "hgt":
				if value[-2:] == "cm":
					if not int(value[:-2]) in range(150,194):
						return 0
				if value[-2:] == "in":
					if not int(value[:-2]) in range(59,77):
						return 0
			if key == "hcl":
				if not value[0] == "#" or \
				not len(value) == 7:
					return 0
				for c in value[1:]:
					if not c in '0123456789abcdef':
						return 0
			if key == "ecl":
				if not value in fields["ecl"]:
					return 0
			if key == "pid":
				if not len(value) == 9:
					return 0
				for c in value:
					if not c in "0123456789":
						return 0
	return 1

passports = fetch_input(r)
print(number_of_valid_passports(passports))
