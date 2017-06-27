#!/usr/bin/python

import os,socket,getpass,string,commands,sys,time,webbrowser

import cgi

print "Content-type:text/html"
print ""

data=cgi.FieldStorage()

data_uri = open('hadoop.jpg', 'rb').read().encode('base64').replace('\n', '')
#img_tag = '<img src="data:image/jpg;base64,%s">' % data_uri

print "<h1 style='margin:0px; color:yellow;background-color:#D2691E; text-align:center; font-family:verdana; height:90px; background-image:url(data:image/jpg;base64,%s);background-size:120px;background-repeat: no-repeat;padding-left: 40px;' title='Hadoop'> " % data_uri 
print "Hadoop"
print "</h1>"

#time.sleep(2)

#User for Project Startup
user_name=data.getvalue('username')

#Password for user verification
user_pass=data.getvalue("password")



if user_name=="root" and user_pass=="redhat":
  print "<META HTTP-EQUIV='refresh' content='0; url=/menu.html'/>"

else:
  
  print "<ul>"
  print "<li style='margin:0px; display: block; color: white;text-align: center;padding: 14px 16px;text-decoration: none; width:1000px; background-color:black'>Authentication Failure</li>"
  print "</ul>"
  
  data_uri1 = open('wlcmback1.jpg', 'rb').read().encode('base64').replace('\n', '')
  print "<br>"
  print "<br>"
  print "<br>"
  print "<br>"
  print "<br>"
  print "<br>"
  print "<br>"
  print "<br>"
  
  
  print "<div style='background-image:url(data:image/jpg;base64,%s);background-size:250px;background-repeat: no-repeat; width:1200px; height:500px; margin-left:450px; margin-top:0px;'>" % data_uri1 
  
  print "<br>"
  print "<br>"
  print "<META HTTP-EQUIV='refresh' content='2; url=/index.html'/>"

print "</div>"
