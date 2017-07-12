#!/usr/bin/python

import os,time,string,sys,commands,getpass

print "Content-type:text/html"
print ""

data_uri = open('hadoop.jpg', 'rb').read().encode('base64').replace('\n', '')
#img_tag = '<img src="data:image/jpg;base64,%s">' % data_uri

data_uri1 = open('background1.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri2 = open('refresh.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri3 = open('directory.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri4 = open('continue.jpg', 'rb').read().encode('base64').replace('\n', '')

print '<div style="background-image:url(data:image/jpg;base64,%s); background-color:skyblue;">' % data_uri1

print "<h1 style='margin:0px; color:yellow;background-color:#D2691E; text-align:center; font-family:verdana; height:50px; width:2000px; background-image:url(data:image/jpg;base64,%s);background-size:170px;background-repeat: no-repeat; postion:fixed; padding:40px 40px;' title='Hadoop'> " % data_uri 
print "Hadoop"
print "</h1>"

print "<ul>"
print "<li style='margin:0px; display: block; color: white;text-align: center;padding: 14px 16px;text-decoration: none; width:1000px;  postion:fixed; background-color:royalblue;'> Hive </li>"
print "</ul>"

ip_list = commands.getoutput("sudo arp-scan -I virbr0 192.168.122.0/24 | grep 192 | grep -Ev '192.168.122.93' | awk '{print $1}' > /tmp/ip_list")

ip_list = ip_list.split("\n")

f = open("/etc/hadoop/.bashrc","w+")
 
f.write("# .bashrc\n\n# User specific aliases and functions\n\nalias rm='rm -i'\nalias cp='cp -i'\nalias mv='mv -i'\n\n# Source global definitions\nif [ -f /etc/bashrc ]; then\n\t. /etc/bashrc\nfi\n\nJAVA_HOME=/usr/java/jdk1.7.0_79\nHIVE_PREFIX=/hive\nPATH=$JAVA_HOME/bin:$HIVE_PREFIX/bin:$PATH\nexport PATH\n\n")
 
f.close() 

commands.getoutput("sudo chmod 777 /tmp/hive")

commands.getoutput("sudo chmod 777 /tmp")

if os.system("hive -S -e 'show databases;'") != 0:
 
 #commands.getoutput("sudo wget http://192.168.122.1/hadoopextra/apache-hive-1.2.2-bin.tar.gz")
 
 commands.getoutput("sudo tar -xvzf apache-hive-1.2.2-bin.tar.gz")
 
 commands.getoutput("sudo cp -r  apache-hive-1.2.2-bin /hive")


print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"

print "<form action='../cgi-bin/hive_options1.py' method='POST'>"
print "<input type='text' placeholder='Enter query' name='query' style='margin-left:800px;text-align:center'>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
print "</form>"


print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"

