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
option = data.getvalue('hdfs_option')

if option == "mkdir":
 print "<form action='hdfs_mkdir.py' method='POST'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter directory name' name='directory_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "put":
 print "<form action='hdfs_upload.py' method='POST'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter file name' name='file_src' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter destination' name='file_dest' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter replication factor' name='block_rep' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter block size' name='block_size' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"


elif option == "putf":
 print "<form action='hdfs_putf.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter file name' name='file_src' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter destination' name='file_dest' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter replication factor' name='block_rep' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter block size' name='block_size' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"


elif option == "mv":
 print "<form action='hdfs_cut.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter file name' name='file_src' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter destination' name='file_dest' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "ls":
 print "<form action='hdfs_ls.py' method='POST'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter path' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"



elif option == "text":
 print "<form action='hdfs_cat.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter path' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"


elif option == "touchz":
 print "<form action='hdfs_touch.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter file name' name='file_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"


elif option == "rm":
 print "<form action='hdfs_rmr.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter file name' name='file_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"


elif option == "rmr":
 print "<form action='hdfs_rmdir.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter directory name' name='dir_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"


elif option == "count":
 print "<form action='hdfs_count.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter path' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "lsr":
 print "<form action='hdfs_lsr.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter path' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"


elif option == "setrep":
 print "<form action='hdfs_setrep.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter file name' name='file_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>"
 
 print "<input type='text' placeholder='Replication factor' name='rep_factor' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "chown":
 print "<form action='hdfs_chown.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter path' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Owner name' name='owner_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "chmod":
 print "<form action='hdfs_chmod.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter path' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter permissions' name='permissions' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "chgrp":
 print "<form action='hdfs_chgrp.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter path' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Group name' name='grp_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "cmd":
 print "<form action='hdfs_cmd.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter command' name='command' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "safemode":
 print "<form action='hdfs_safemode.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "Choose safemode state"
 print "<br>"
 
 print "<input type='radio' name='state' value='Enter'>Enter"
 print "<br>"
 
 print "<input type='radio' name='state' value='Leave'>Leave"
 print "<br>"
 
 print "<input type='radio' name='state' value='Get'>Get"
 print "<br>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "set_space_quota":
 print "<form action='hdfs_spaceQuota.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter quota' name='quota' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter directory name' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "clr_space_quota":
 print "<form action='hdfs_clrSpaceQuota.py' method='POST'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter directory name' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "set_name_quota":
 print "<form action='hdfs_nameQuota.py' method='POST'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter quota' name='quota' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter directory name' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "clr_name_quota":
 print "<form action='hdfs_clrNameQuota.py' method='POST'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter directory name' name='path' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "du":
 print "<form action='hdfs_du.py' method='POST'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter directory name' name='dir_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "dus":
 print "<form action='hdfs_dus.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='text' placeholder='Enter directory name' name='dir_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "decommission_nodes":
 print "<form action='hdfs_decommission.py' method='POST'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter directory name' name='file_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "commission_nodes":
 print "<form action='hdfs_commission.py' method='POST'>"
 
 print "<input type='text' placeholder='Enter file name' name='file_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "defsize":
 print "<form action='hdfs_defsize.py' method='POST'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter block size' name='block_size' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "defrep":
 print "<form action='hdfs_defrep.py' method='POST'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter replication factor' name='rep_factor' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "chport":
 print "<form action='hdfs_chport.py' method='POST'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter port no' name='port_no' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "fsck":
 print "<form action='hdfs_fsck.py' method='POST'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter directory name' name='dir_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "chhbt":
 print "<form action='hdfs_chhbt.py' method='POST'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 temp = commands.getoutput("sudo hadoop dfsadmin -report | grep Name | awk '{print $2}'")
 
 temp = temp.split("\n")
 i = 0
 while i < len(temp):
  temp[i]=temp[i][0:temp[i].index(":")]
  i = i + 1
 print "<select name='ip_datanode' style='border:none;margin-left:800px;color:blue;text-align:center;padding-left:20px;border-bottom:2px solid white;'>"
 for node in temp:
  print node
  print "<option>"+node+"</option>"
  print "<br>"
 print "</select>"
 
 print "<br>"
 print "<br>"
 
 print "<input type='text' placeholder='Enter heartbeat interval' name='heartbeat' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "permissions":
 print "<form action='hdfs_permissions.py' method='POST'>"
 
 print "<input type='radio' name='state' value='Enable'>Enable"
 
 print "<input type='radio' name='state' value='Disable'>Disable"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "trash":
 print "<form action='hdfs_trash.py' method='POST'>"
 
 print "<input type='radio' name='state' value='Enable'>Enable"
 
 print "<input type='radio' name='state' value='Disable'>Disable"
 
 print "<input type='text' placeholder='Enter trash interval' name='trash' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<br>"
 
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"


elif option == "report":
 print "<pre>"
 print "<font size='5' style='color:white;'>"
 output = commands.getoutput("sudo hadoop dfsadmin -report ")
 
 print output
 print "</font>"
 print "</pre>" 
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"

elif option == "metasave":
 print "<pre>"
 print "<font size='5' style='color:white;'>"
 commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_namenode+" hadoop dfsadmin -metasave namenode_metadata ")
 output = commands.getoutput("sudo sshpass -p 'redhat' ssh -o 'StrictHostKeyChecking no' root@"+ip_namenode+" cat /var/log/hadoop/root/namenode_metadata")
 print output
 print "</font>"
 print "</pre>" 
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"


elif option == "empty_trash":
 print "<pre>"
 print "<font size='5' style='color:white;'>"
 output = commands.getoutput("sudo hadoop fs -expunge ")
 if not output:
  print "Trash empty or disabled"
 else:
  print output
 print "</font>"
 print "</pre>" 
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"


elif option == "get_quota":
 print "<form action='hdfs_getquota.py' method='POST'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter directory name' name='dir_name' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<br>"
 print "<br>"
 print "<br>" 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option == "refresh_nodes":
 
 print "<pre>"
 output = commands.getoutput("sudo hadoop dfsadmin -refreshNodes ") 
 
 if not output:
  print commands.getoutput("sudo hadoop dfsadmin -report")
 else:
  print output
 print "</pre>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<br>"

elif option=="hive":
 print "<form action='hive_cluster.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<br>"
 print "<br>"
 print "<br>"
 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"
 """

elif option == "ha":
 print "<form action='demo.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter IP ' name='ip_ann' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<br>"
 print "<br>"
 print "<br>"
 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"
 """
elif option == "snn":
 print "<form action='hdfs_snn.py' method='POST'>"
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='text' placeholder='Enter IP of secondary namenode' name='ip_snn' style='border: none; border-bottom: 2px solid white; color: blue; text-align:center; margin-left:800px; padding-left: 20px;'>"
 print "<br>"
 print "<br>"
 print "<input type='hidden' name='ip_namenode' value="+ip_namenode+">"
 
 print "<br>"
 print "<br>"
 print "<br>"
 
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

else:
 print option

print "</div>"

