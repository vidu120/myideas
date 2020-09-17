#!/usr/bin/env python3
with open("mine") as file:
	for line in file:
		print(line.rstrip("\n"))
