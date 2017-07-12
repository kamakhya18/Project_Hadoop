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

file_name=data.getvalue("file_name")

ip_namenode = data.getvalue("ip_namenode")


print "<pre>"

print commands.getoutput("sudo sshpass -p 'redhat' scp "+file_name+" root@"+ip_namenode+":"+file_name)

print commands.getoutput("sudo sshpass -p 'redhat' scp root@"+ip_namenode+":/etc/hadoop/hdfs-site.xml /tmp/hdfs-site1.xml")

f = open("/tmp/hdfs-site1.xml","r+")
temp = f.read()
temp = temp.replace("</configuration>","\n<property>\n<name>dfs.hosts</name>\n<value>"+file_name+"</value>\n</property>\n</configuration>")
f.close()
f = open("/tmp/hdfs-site1.xml","w+")
f.write(temp)
f.close()

print commands.getoutput("sudo sshpass -p 'redhat' scp /tmp/hdfs-site1.xml root@"+ip_namenode+":/etc/hadoop/hdfs-site.xml")

print commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_namenode+" hadoop dfsadmin -refreshNodes")

print commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_namenode+"  hadoop dfsadmin -report")

print "</pre>"


print "</div>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<a href='../cgi-bin/hdfs_options1.py'>"
print "Back"
print "</a>"
