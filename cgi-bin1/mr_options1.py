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


data_uri5 = open('../../html/css/css1/person.jpg', 'rb').read().encode('base64').replace('\n', '')
data_uri6 = open('../../html/css/css1/contact.png', 'rb').read().encode('base64').replace('\n', '')

print "<div style='background-color:black;'>"
print "<ul>"
print "<li style='float:left;'><font size='6'><b style='color:white;'><i>Hadoop</i></b></font></li>"
print "<li><a href='#'><img src='data:image/png;base64,%s' width='25px' style='background-color:white;'></a></li>" %data_uri6
print "<div class='dropdown' >"
print "<button class='dropbtn'><img src='data:image/jpg;base64,%s' width='30px'></button>" %data_uri5
print "<div class='dropdown-content'>"
print "<a href='../../html/Hadoop1/login.html'>Log In</a>"
print "<a href='#'>Register</a>"
print "</div>"
print "</div>"
print "<li><a href='../../html/Hadoop1/index.html'>About</a></li>"
print "<li><a href='../../html/Hadoop1/index.html'>Home</a></li>"
print "<li><a href='hive_cluster.py'>Hive</a></li>"
print "<li><a href='mr_options1.py'>MR</a></li>"
print "<li><a href='hdfs_options1.py'>HDFS</a></li>"
print "<div class='dropdown' >"
print "<button class='dropbtn'>Cluster</button>"
print "<div class='dropdown-content'>"
print "<a href='../../html/Hadoop1/hdfs.html'>HDFS</a>"
print "<a href='../../html/Hadoop1/mr.html'>MR</a>"
print "<a href='../../html/Hadoop1/hive.html'>Hive</a>"
print "</div>"
print "</div>"
print "</ul>"
print "</div>"



data_uri = open('../../html/hadooplogo.png', 'rb').read().encode('base64').replace('\n', '')
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

ip_namenode=data.getvalue("ip_namenode")

ip_jobtracker = data.getvalue("ip_jobtracker")

if not ip_namenode:
 ip_list = commands.getoutput("sudo arp-scan -I docker0 172.17.0.0/24 | grep 172 | awk '{print $1}'")
 ip_list = ip_list.split()
 for i in ip_list:
  jps = commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+i+" jps ")
  if "NameNode" in jps:
   ip_namenode = i
   break

#print ip_namenode

if not ip_jobtracker:
 ip_list = commands.getoutput("sudo arp-scan -I docker0 172.17.0.0/24 | grep 172 | awk '{print $1}'")
 ip_list = ip_list.split()
 for i in ip_list:
  jps = commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+i+" jps ")
  if "JobTracker" in jps:
   ip_jobtracker = i
   break

f=open("/etc/hadoop/core-site.xml","w+")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>fs.default.name</name>\n<value>hdfs://"+ip_namenode+":10002</value>\n</property>\n</configuration>\n")

f.close()

f=open("/etc/hadoop/mapred-site.xml","w+")

f.write("<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<?xml-stylesheet type=\"text/xsl\" href=\"configuration.xsl\"?>\n\n\n\n<configuration>\n<property>\n<name>mapred.job.tracker</name>\n<value>"+ip_jobtracker+":9001</value>\n</property>\n</configuration>\n")

f.close()

print "<form action='mr_options2.py' method='POST'>"
print "<font size='5' style='color:white;'>"
print "<i>"
print "<br>"
print "<br>"
print "<br>"
print "<div style='padding-left:100px;'>"
print "<input type='radio'  name='mr_option' checked='checked' value='list'> Running Jobs"
print "<br>"
print "<input type='radio'  name='mr_option' checked='checked' value='all'> All Jobs"
print "<br>"
print "<input type='radio'  name='mr_option' checked='checked' value='tasktrackers'> Tasktrackers"
print "<br>"
print "<input type='radio'  name='mr_option' checked='checked' value='status'> Status of a job"
print "<br>"
print "<input type='radio'  name='mr_option' checked='checked' value='kill'> Kill a job"
print "<br>"
print "<input type='radio'  name='mr_option' checked='checked' value='submit'> Submit A Job"
print "<br>"
print "<input type='radio'  name='mr_option' checked='checked' value='commission'> Commission Tasktrackers"
print "<br>"
print "<input type='radio'  name='mr_option' checked='checked' value='decommission'> Decommission Tasktrackers"
print "<br>"
print "<input type='radio'  name='mr_option' checked='checked' value='priority'> Change Priority"
print "<br>"
print "<br>"
print "<br>"
print "<input name='ip_namenode' type='hidden' value="+ip_namenode+">"
print "<input type='hidden' name='ip_jobtracker' value="+ip_jobtracker+">"
print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
print "</div>"
print "<br>"
print "<br>"
print "<br>"
print "</i>"
print "</font>"
print "</form>"
print "</div>"
