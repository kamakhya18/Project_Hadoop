#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""


data_uri = open('hadoop.jpg', 'rb').read().encode('base64').replace('\n', '')
#img_tag = '<img src="data:image/jpg;base64,%s">' % data_uri

data_uri1 = open('background1.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri4 = open('continue.jpg', 'rb').read().encode('base64').replace('\n', '')

print "<h1 style='margin:0px; color:yellow;background-color:#D2691E; text-align:center; font-family:verdana; height:50px; width:2000px; background-image:url(data:image/jpg;base64,%s);background-size:170px;background-repeat: no-repeat; postion:fixed; padding:40px 40px;' title='Hadoop'> " % data_uri 
print "Hadoop"
print "</h1>"

print '<div style="background-image:url(data:image/jpg;base64,%s); background-size:3000px; background-color:skyblue;">' % data_uri1

print "<ul>"
print "<li style='margin:0px; display: block; color: white;text-align: center;padding: 14px 16px;text-decoration: none; width:1000px;  postion:fixed; background-color:royalblue;'>Hive Options</li>"
print "</ul>"


data = cgi.FieldStorage()

query = data.getvalue('query')

# query  = "create table xyz (id int, name string) row format delimited fields terminated by ':' location '/hello1'"
output = commands.getoutput("sudo /hive/bin/hive -S -e \"use adhoc; "+query+";\"")

if not output:
 print "Done"
else:
 print output

print "<br>"
print "<br>"
print "<br>"
print "<a href='../cgi-bin/hive_cluster.py' style='text-decoration:none;'>"
print "Back"
print "</a>"
print "<br>"
print "<br>"
print "<br>"
