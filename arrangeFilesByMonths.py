#!/usr/bin/env python3

import os
import datetime

def goBackOneDir(current_dir):
    os.chdir(os.path.join(current_dir , ".."))

#This is to go to the /home/vidu120 directory
goBackOneDir(os.getcwd())

#Now we want to organize the mypython directory..
#So to do that let's get the path to that
print("Please input the path to the directory which you want to organize: ")
path = input()
allFiles = os.listdir(path)
os.chdir(path)
for file in allFiles:
    filePath = os.path.join(path , file)
    if os.path.isfile(filePath):
        getCreatedDate = str(datetime.datetime.fromtimestamp(os.path.getmtime(filePath)))
        getCreatedDate = getCreatedDate[5:7]
        if not os.path.exists("M-" + getCreatedDate):
            os.mkdir("M-" + getCreatedDate)
        #Below is the code for moving a file from one directory to another

        #opening both the files the src and the dst
        fileSrc = open(file)

        #This portion for getting into the specific directory and making the same file again
        os.chdir("M-" + getCreatedDate)
        fileDst = open(file , "w")
        fileDst.close()
        fileDst = open(file , "a")
        goBackOneDir(os.getcwd())

        #Copying all lines one by one
        for line in fileSrc:
            _ = fileDst.write(line)

        #closing both the file objects
        fileSrc.close()
        fileDst.close()

        #Finally removing the main copy from the main directory
        os.remove(file)
