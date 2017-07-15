#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""


print "<html>"
print "<head>"
print "<title>Hadoop</title>"
print "<link rel='stylesheet' type='text/css' href='login.css/>"
print "</head>"
print "<body>"
data_uri5 = open('../html/css/person.jpg', 'rb').read().encode('base64').replace('\n', '')
data_uri6 = open('../html/css/contact.png', 'rb').read().encode('base64').replace('\n', '')

print "<div style='background-color:black;'>"
print "<ul>"
print "<li style='float:left;'><font size='6'><b style='color:white;'><i>Hadoop</i></b></font></li>"
print "<li><a href='contact.html'><img src='data:image/png;base64,%s' width='25px' style='background-color:white;'></a></li>" %data_uri6
print "<div class='dropdown' >"
print "<button class='dropbtn'><img src='data:image/jpg;base64,%s' width='30px'></button>" %data_uri5
print "<div class='dropdown-content'>"
print "<a href='login.html'>Log In</a>"
print "<a href='#'>Register</a>"
print "</div>"
print "</div>"
print "<li><a href='../index.html'>About</a></li>"
print "<li><a href='../index.html'>Home</a></li>"
print "<li><a href='../cgi-bin/hive_cluster.py'>Hive</a></li>"
print "<li><a href='../cgi-bin/mr_options1.py'>MR</a></li>"
print "<li><a href='../cgi-bin/hdfs_options1.py'>HDFS</a></li>"
print "<div class='dropdown' >"
print "<button class='dropbtn'>Cluster</button>"
print "<div class='dropdown-content'>"
print "<a href='../hdfs.html'>HDFS</a>"
print "<a href='../mr.html'>MR</a>"
print "<a href='../hive.html'>Hive</a>"
print "</div>"
print "</div>"
print "</ul>"
print "</div>"



data_uri = open('../html/hadooplogo.png', 'rb').read().encode('base64').replace('\n', '')
#print '<img src="data:image/jpg;base64,%s">' % data_uri

data_uri1 = open('background1.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri2 = open('refresh.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri3 = open('directory.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri4 = open('continue.jpg', 'rb').read().encode('base64').replace('\n', '')


print "<div>"
print '<img width="2150vw" src="data:image/jpg;base64,%s">' % data_uri
print "</div>"


print '<div style="background-image:url(data:image/jpg;base64,%s); background-size:3000px; background-color:skyblue;">' % data_uri1


data = cgi.FieldStorage()

heartbeat = data.getvalue("heartbeat")

ip_datanode = data.getvalue("ip_datanode")

ip_namenode = data.getvalue("ip_namenode")



print "<pre>"

commands.getoutput("sudo sshpass -p 'redhat' scp root@"+ip_datanode+":/etc/hadoop/hdfs-site.xml /tmp/hdfs-site1.xml")

commands.getoutput("sudo sshpass -p 'redhat' ssh root@"+ip_datanode+" chmod 777 /tmp/hdfs-site1.xml")

f = open("/tmp/hdfs-site1.xml","r+")
temp = f.read()
temp = temp.replace("</configuration>","\n<property>\n<name>dfs.heartbeat.interval</name>\n<value>"+heartbeat+"</value>\n</property>\n</configuration>\n")
f.close()

f = open("/tmp/hdfs-site1.xml","w+")
f.write(temp)
f.close()

commands.getoutput("sudo sshpass -p 'redhat' scp /tmp/hdfs-site1.xml root@"+ip_datanode+":/etc/hadoop/hdfs-site.xml")

commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_datanode+" hadoop-daemon.sh stop datanode")

commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_datanode+" hadoop-daemon.sh start datanode")

print "Heart Beat Interval of "+ip_datanode+" changed to "+heartbeat

print "</pre>"


print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<a style='color:white;text-decoration:none;font-size:30;float:right;' href='../cgi-bin/hdfs_options1.py'>"
print "Back"
print "</a>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "</div>"