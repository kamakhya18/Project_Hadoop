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
 print "<form action='mr_status.py' method='POST'>"
 print "<br>"
 print "<br>"
 job_list = commands.getoutput("hadoop job -list all | awk '{print $1}'")
 job_list = job_list.split("\n")
 job_list = job_list[4:]
 if not job_list:
  print "<br>"
  print "<br>"
  print "<br>"
  print "<i>"
  print "<font style='color:white;margin-left:700px;' size='5'>"
  print "No Job Running"
  print "</font>"
  print "</i>"
  print "<br>"
  print "<br>"
  print "<br>"
  print "<br>"
  print "<br>"
  print "<br>"
 else:
  print "<select name='job_id' style='border:none;margin-left:800px;color:blue;text-align:center;padding-left:20px;border-bottom:2px solid white;'>"
  for job in job_list:
   print "<option>"+job+"</option>"
   print "<br>"
  print "</select>"
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
 print "<form action='mr_kill.py' method='POST'>"
 
 print "<br>"
 job_list = commands.getoutput("hadoop job -list | awk '{print $1}'")
 job_list = job_list.split("\n")
 job_list = job_list[2:]
 if not job_list:
  print "<br>"
  print "<br>"
  print "<br>"
  print "<i>"
  print "<font style='color:white;margin-left:700px;' size='5'>"
  print "No Job Running"
  print "</font>"
  print "</i>"
  print "<br>"
  print "<br>"
  print "<br>"
  print "<br>"
  print "<br>"
  print "<br>"
 else:
  print "<select name='job_id' style='border:none;margin-left:800px;color:blue;text-align:center;padding-left:20px;border-bottom:2px solid white;'>"
  for job in job_list:
   print "<option>"+job+"</option>"
   print "<br>"
  print "</select>"
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
 print "<form action='mr_submit.py' method='POST'>"
 print "<br>"
 print "<select name='operation' style='border:none;margin-left:800px;color:blue;text-align:center;padding-left:20px;border-bottom:2px solid white;'>"
 print "<option>aggregatewordcount</option>"
 print "<option>aggregatewordhist</option>"
 print "<option>dbcount</option>"
 print "<option>grep</option>"
 print "<option>join</option>"
 print "<option>multifilewc</option>"
 print "<option>pentomino</option>"
 print "<option>pi</option>"
 print "<option>randomtextwriter</option>"
 print "<option>randomwriter</option>"
 print "<option>sort</option>"
 print "<option>sleep</option>"
 print "<option>secondarysort</option>"
 print "<option>sudoku</option>"
 print "<option>teragen</option>"
 print "<option>terasort</option>"
 print "<option>teravalidate</option>"
 print "<option>wordcount</option>"
 print "<option>pi</option>"
 print "</select>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter arguments' name='in_file' style='border:none;color:blue;text-align:center;padding-left:20px;margin-left:800px;border-bottom:2px solid white;'>"
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


elif option == "priority":
 print "<form action='mr_priority.py' method='POST'>"
 print "<br>"
 job_list = commands.getoutput("hadoop job -list | awk '{print $1}'")
 job_list = job_list.split("\n")
 job_list = job_list[2:]
 if not job_list:
  print "<br>"
  print "<br>"
  print "<br>"
  print "<i>"
  print "<font style='color:white;margin-left:700px;' size='5'>"
  print "No Job Running"
  print "</font>"
  print "</i>"
  print "<br>"
  print "<br>"
  print "<br>"
  print "<br>"
  print "<br>"
  print "<br>"
 else:
  print "<select name='job_id' style='border:none;margin-left:800px;color:blue;text-align:center;padding-left:20px;border-bottom:2px solid white;'>"
  for job in job_list:
   print "<option>"+job+"</option>"
   print "<br>"
  print "</select>"
  print "<br>"
  print "<br>"
  print "<br>"
  print "<br>"
  print "<select name='priority' style='margin-left:800px; padding-left: 20px;'>"
  print "<option>NORMAL</option>"
  print "<br>"
  print "<option>LOW</option>"
  print "<br>"
  print "<option>VERY_LOW</option>"
  print "<br>"
  print "<option>HIGH</option>"
  print "<br>"
  print "<option>VERY_HIGH</option>"
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

elif option == "commission":
 print "<form action='mr_commission.py' method='POST'>"
 print "<br>"
 print "<br>"

 print "<input type='text' name='file_name' placeholder='Enter file name' style='border:none;margin-left:800px;color:blue;text-align:center;padding-left:20px;border-bottom:2px solid white;'>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<input type='hidden' name='ip_jobtracker' value="+ip_jobtracker+">"
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "decommission":
 print "<form action='mr_decommission.py' method='POST'>"
 print "<br>"
 print "<br>"

 print "<input type='text' name='file_name' placeholder='Enter file name' style='border:none;margin-left:800px;color:blue;text-align:center;padding-left:20px;border-bottom:2px solid white;'>"
 
 print "<br>"
 print "<br>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<input type='hidden' name='ip_jobtracker' value="+ip_jobtracker+">"
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "</form>"

else:
 print option


