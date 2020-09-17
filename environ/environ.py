#!/usr/bin/env python3

import os

env1 = os.environ.get("HOME", "Not available")
env2 = os.environ.get("USER" , "Not available")
env3 = os.environ.get("FRUIT" , "Not available")

print(env1 , env2 , env3 )
print(type(dict))
