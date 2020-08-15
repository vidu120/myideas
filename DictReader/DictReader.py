#!/usr/bin/env python3
import os
import csv

with open("result.txt" , "w") as result:
    with open("csv0_file.txt") as family_info:
         file = csv.DictReader(family_info)
         for line in file:
                 _ = result.write("{0} who is a {2} is {1} years old\n".format(line["name"] , line["age"] , line["sex"]))
