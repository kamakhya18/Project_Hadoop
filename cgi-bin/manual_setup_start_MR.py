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

data=cgi.FieldStorage()

ip_namenode = data.getvalue('namenode')
namenode_directory = data.getvalue('namenode_directory')
ip_jobtracker=data.getvalue('jobtracker')

if not namenode_directory:
 namenode_directory="hadoopnamenode"

#Inventory file
inventory=open('/tmp/inventory','r+')

temp_in = inventory.read()

inventory.close()

temp = temp_in

temp_in = temp_in.replace(ip_namenode+"\n","\n")

inventory=open('/tmp/inventory','w+')

inventory.write("[namenode]\n"+ip_namenode+"\n\n[datanode]\n")

inventory.write(temp_in)

inventory.write("\n[jobtracker]\n"+ip_jobtracker+"\n\n[tasktracker]\n")

temp = temp.replace(ip_jobtracker+"\n","\n")

inventory.write(temp)

inventory.close()

commands.getoutput("sudo ansible-playbook -i /tmp/inventory all_mr.yml")


#mapred-site.xml
f=open("/tmp/mapred-site.xml","w+")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>"+ip_jobtracker+":9001</value>\n</property>\n</configuration>\n")

f.close()

commands.getoutput("sudo ansible-playbook -i /tmp/inventory jobtracker_mr.yml")

commands.getoutput("sudo ansible-playbook -i /tmp/inventory tasktracker_mr.yml")
print "<br>"
print "<br>"
print "<br>"
print "<font size='5'>"
print "<i>"
print "Map Reduce Cluster setup successful"
print "</i>"
print "</font>"

print "<br>"
print "<br>"
print "<br>"

#print "<META HTTP-EQUIV='refresh' content='1; url=mr_options1.py'/>"

print "<form action='../cgi-bin/mr_options1.py' method='POST'>"
print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
print "<input type='hidden' name='ip_jobtracker' value="+ip_jobtracker+">"
print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
print "</form>"
print "<META HTTP-EQUIV='refresh' content='0; url=mr_options1.py'/>"
