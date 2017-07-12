#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""


data_uri = open('hadoop.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri1 = open('background1.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri2 = open('refresh.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri3 = open('directory.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri4 = open('continue.jpg', 'rb').read().encode('base64').replace('\n', '')

print "<h1 style='margin:0px; color:yellow;background-color:#D2691E; text-align:center; font-family:verdana; height:50px; width:2000px; background-image:url(data:image/jpg;base64,%s);background-size:170px;background-repeat: no-repeat; postion:fixed; padding:40px 40px;' title='Hadoop'> " % data_uri 
print "Hadoop"
print "</h1>"

print "<ul style='list-style-type: none; margin: 0; padding: 0; overflow: hidden; background-color: #333;'>"
print "<li style='float: left;'><a href='../index.html' style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;'>HOME</a></li>"

print "<li style='float: left;'><a  style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../hdfs_cluster.html'>HDFS</a></li>"

print "<li style='float: left;'><a style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../mr_cluster.html'>Map Reduce</a></li>"

print "<li style='float: left;'><a style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../hive_cluster.py'>HIVE</a></li>"

print "<li style='float:right'><a style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../about.html'>ABOUT</a></li>"

print "</ul>"

print '<div style="background-image:url(data:image/jpg;base64,%s); background-size:3000px; background-color:skyblue;">' % data_uri1

data = cgi.FieldStorage()

ip_namenode = data.getvalue("ip_namenode")

ip_jobtracker = data.getvalue("ip_jobtracker")

priority = data.getvalue("priority")

in_file = data.getvalue("in_file")

out_file = data.getvalue("out_file")

operation = data.getvalue("operation")

status = commands.getstatusoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_jobtracker+" hadoop jar /usr/share/hadoop/hadoop-examples-1.2.1.jar "+operation+" "+in_file+" "+out_file)

print "<font size='5'>"
if status[0] == 0:
 print commands.getoutput("sudo hadoop fs -text "+out_file+"/part-r-00000")

else:
 print status[1]
print "</font>"

print "<br>"
print "<br>"
print "<br>"
print "<br>"
