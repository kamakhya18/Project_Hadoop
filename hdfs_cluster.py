#!/usr/bin/python

import os,string,socket,getpass,sys,commands
print "Content-type:text/html"
print ""

print "\t\t\tHadoop Cluster Set Up"
print "\t\t\t---------------------"

#Options for setting hadoop cluster
options="""

Press 1. for manual setup
Press 2. for automatic setup

-------------------------------------------------
"""

#Storing option chosen by user
user_choice=raw_input(options)

while user_choice!='1' and user_choice!='2':
 print "\nNot a valid choice\n"
 user_choice=raw_input(options)

if user_choice=='1':
 print "Please Wait........\n"
 time.sleep(1)
 execfile('manual_setup.py')
 
elif user_choice=='2':
 print "Please Wait........\n"
 time.sleep(1)
 execfile('automatic_setup.py')
 
else:
 print "\nNot a valid choice\n"
 

