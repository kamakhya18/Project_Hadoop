#!/usr/bin/python

import os,time,string,sys,commands,getpass

print "Content-type:text/html"
print ""
print "<html>"
print "<head>"
print "<title>HDFS Cluster</title>"
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

print "<form action='../cgi-bin/manual_setup_temp_all.py' method='POST'>"
print "<input type='text' name='ip_namenode' placeholder='Enter IP of namenode'>"
print "<input type='text' name='ip_datanodes' placeholder='Enter datanodes'>"
print "<input type='submit' value='Submit' >"
print "</form>"

print "<a href='manual_setup_all.py' style='width:100px;height:100px;padding-left:500px;float:right;'>"
print "Clear All"
print "</a>"
print "<br>"
print "<br>"
print "<br>"
print "<br>"
print "</div>"
