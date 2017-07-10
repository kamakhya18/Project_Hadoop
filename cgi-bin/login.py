#!/usr/bin/python

import cgi
print "Content-type:text/html"
print ""

data=cgi.FieldStorage()

username=data.getvalue('username')
password=data.getvalue('password')

#print data

if username=='root' and password=='redhat' :
 print 'Authentication successfull\n Redirecting to Project'
 time.sleep(2)
 execfile('hadoop.py')
else:
 print 'Authentication failure'


