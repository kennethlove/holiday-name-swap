#! /usr/bin/env python

from copy import deepcopy
from random import choice
from time import sleep


initial_data = [
	{
		'name': 'Jane',
		'drawn': False,
		'exclusions': ['Lisa', 'John', 'Anne'],
		'gives_to': None,
	},
	{
		'name': 'John',
		'drawn': False,
		'exclusions': ['Jane'],
		'gives_to': None,
	},
	{
		'name': 'Sam',
		'drawn': False,
		'exclusions': [],
		'gives_to': None,
	},
	{
		'name': 'Lisa',
		'drawn': False,
		'exclusions': [],
		'gives_to': None,
	},
	{
		'name': 'Seth',
		'drawn': False,
		'exclusions': [],
		'gives_to': None,
	},
	{
		'name': 'Tyler',
		'drawn': False,
		'exclusions': ['Anne'],
		'gives_to': None,
	},
	{
		'name': 'Anne',
		'drawn': False,
		'exclusions': ['Tyler'],
		'gives_to': None,
	},
]


def get_givee(giver, data):
	opts = [
		givee for givee in data
		if givee['name'] not in giver['exclusions']
		and givee != giver
		and not givee['drawn']
	]

	if not len(opts):
		# if no options return None to flag that we need to start over
		return None

	return choice(opts)


def run_name_draw():
	data = deepcopy(initial_data)
	for giver in data:
		givee = get_givee(giver, data)

		if givee == None:
			# we need to start over
			return None

		giver['gives_to'] = givee['name']
		givee['exclusions'].append(giver['name'])
		givee['drawn'] = True

	return data


def print_name_draw_with_suspense(data):
	for giver in data:
		print(giver['name'], end='')
		for n in range(0, 5):
			sleep(1)
			print('.', end='')
		print(giver['gives_to'])
		sleep(3)


def print_name_draw_immediate(data):
	for giver in data:
		print(f"{giver['name']}: {giver['gives_to']}")


data = run_name_draw()
while data == None:
	data = run_name_draw()


print_name_draw_immediate(data)