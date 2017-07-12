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

print "<li style='float: left;'><a style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../login.html'>LOG IN</a></li>"

print "<li style='float:right'><a style='display: block; color: white; text-align: center; padding: 14px 16px; text-decoration: none;' href='../about.html'>ABOUT</a></li>"

print "</ul>"

print '<div style="background-image:url(data:image/jpg;base64,%s); background-size:3000px; background-color:skyblue;">' % data_uri1

data=cgi.FieldStorage()
ip_namenode= data.getvalue('ip_namenode')
ip_jobtracker = data.getvalue('ip_jobtracker')
option = data.getvalue('mr_option')

if option == "list":
 print "<br>"
 print "<br>"
 print commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_jobtracker+" hadoop job -list")
 print "<br>"

elif option == "all":
 print "<br>"
 print "<br>"
 print commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_jobtracker+" hadoop job -list all")
 print "<br>"
 print "<br>"

elif option == "tasktrackers":
 print "<br>"
 print "<br>"
 print commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_jobtracker+" hadoop job -list-active-trackers")
 print "<br>"
 print "<br>"

elif option == "status":
 print "<form action='../cgi-bin/mr_status.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter job id' name='job_id' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<input type='hidden' name='ip_jobtracker' value="+ip_jobtracker+">"
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "kill":
 print "<form action='../cgi-bin/mr_kill.py' method='POST'>"
 
 print "<br>"
 print "<input type='text' placeholder='Enter job id' name='job_id' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<input type='hidden' name='ip_jobtracker' value="+ip_jobtracker+">"
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "submit":
 print "<form action='../cgi-bin/mr_submit.py'>"
 print "<br>"
 print "<input type='text' placeholder='Enter operation' name='operation' style='border:none;margin-left:800px;color:blue;text-align:center;padding-left:20px;border-bottom:2px solid white;'>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Input File Name' name='in_file' style='border:none;color:blue;text-align:center;padding-left:20px;margin-left:800px;border-bottom:2px solid white;'>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Output File Name' name='out_file' style='border:none;color:blue;text-align:center;padding-left:20px;margin-left:800px;border-bottom:2px solid white;'>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<select name='priority' style='margin-left:800px; padding-left: 20px;'>"
 print "<option>Normal</option>"
 print "<br>"
 print "<option>Low</option>"
 print "<br>"
 print "<option>Very Low</option>"
 print "<br>"
 print "<option>High</option>"
 print "<br>"
 print "<option>Very High</option>"
 print "<br>"
 print "</select>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<input type='hidden' name='ip_jobtracker' value="+ip_jobtracker+">"
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "</form>"
 
 print "</div>"

else:
 print option





