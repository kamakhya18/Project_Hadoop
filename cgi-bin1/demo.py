#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data = cgi.FieldStorage()
ip_namenode = data.getvalue("ip_namenode")
ip_ann = data.getvalue("ip_ann")

os.system("sudo sshpass -p 'redhat' scp -o 'StrictHostKeyChecking no' root@"+ip_namenode+":/hadoopnamenode root@"+ip_ann+":/hadoopnamenode")

status = 0
while status == 0 :
 status = os.system("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_ann+" ping -c 1 "+ip_namenode)

os.system("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_ann+" ifconfig eth0 "+ip_namenode)

#os.system("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_ann+" ifconfig eth0 "+ip_namenode)

os.system("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_ann+" hadoop-daemon.sh start namenode")
