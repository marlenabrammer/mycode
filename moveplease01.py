#!/usr/bin/env python3

#imports
import shutil
import os

def main():

    #move into this working directory
    os.chdir('/home/student/mycode/')
    #try moving file
    shutil.move('raynor.obj', 'ceph_storage/')

    #pause for input from the user on the filename
    xname = input('What is the new name for kerrigan.obj? ')
    #move the file and rename
    shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

main()
