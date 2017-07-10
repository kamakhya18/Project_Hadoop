#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

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
