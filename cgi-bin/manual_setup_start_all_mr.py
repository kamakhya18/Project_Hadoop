#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""


data_uri = open('hadoop.jpg', 'rb').read().encode('base64').replace('\n', '')

data_uri4 = open('continue.jpg', 'rb').read().encode('base64').replace('\n', '')

print "<h1 style='margin:0px; color:yellow;background-color:#D2691E; text-align:center; font-family:verdana; height:90px; width:1500px; background-image:url(data:image/jpg;base64,%s);background-size:120px;background-repeat: no-repeat;padding-left: 40px;' title='Hadoop'> " % data_uri 
print "Hadoop"
print "</h1>"

print "<ul style='list-style-type: none; margin: 0; padding: 0; overflow: hidden; background-color: #333;'>"
print "<li style='float: left;'><a href='../index.html' style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;'>HOME</a></li>"

print "<li style='float: left;'><a  style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../hdfs_cluster.html'>HDFS</a></li>"

print "<li style='float: left;'><a style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../mr_cluster.html'>Map Reduce</a></li>"

print "<li style='float: left;'><a style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../cgi-bin/hive_cluster.py'>HIVE</a></li>"

print "<li style='float: left;'><a style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../login.html'>LOG IN</a></li>"

print "<li style='float:right'><a style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../about.html'>ABOUT</a></li>"

print "</ul>"

data=cgi.FieldStorage()

ip_jobtracker = data.getvalue('ip_jobtracker')

print '<div style="background-color:#FFDAB9; width:100%; height: 150%;">'

inventory=open('/tmp/inventory','r+')

temp_in = inventory.read()

inventory.close()

temp_in = temp_in.replace(ip_jobtracker+"\n","\n")

inventory=open('/tmp/inventory','w+')

inventory.write("[jobtracker]\n"+ip_jobtracker+"\n\n[tasktracker]\n")

inventory.write(temp_in)

inventory.seek(0)

inventory.close()

#mapred-site.xml
f=open("/tmp/mapred-site.xml","w+")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>"+ip_jobtracker+":9001</value>\n</property>\n</configuration>\n")

f.close()

commands.getoutput("sudo ansible-playbook -i /tmp/inventory jobtracker_mr.yml")

commands.getoutput("sudo ansible-playbook -i /tmp/inventory tasktracker_mr.yml")

print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<font size='6' style='margin-left:500px;'>"
print "Map Reduce setup successful"
print "</font>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<form action='../cgi-bin/mr_options1.py' method='POST'>"
print "<input type='hidden' name='ip_jobtracker' value="+ip_jobtracker+">"
print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "</form>"
print "<META HTTP-EQUIV='refresh' content='0; url=mr_options1.py'/>"

print "</div>"
