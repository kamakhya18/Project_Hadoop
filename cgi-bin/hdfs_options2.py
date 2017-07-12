#!/usr/bin/python

import os,time,string,sys,commands,getpass,cgi

print "Content-type:text/html"
print ""

data=cgi.FieldStorage()
ip_namenode= data.getvalue('ip_namenode')
option = data.getvalue('hdfs_option')

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

if option == "mkdir":
 print "<form action='../cgi-bin/hdfs_mkdir.py' method='POST'>"
 
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
 print "<form action='../cgi-bin/hdfs_upload.py' method='POST'>"
 
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
 print "<form action='../cgi-bin/hdfs_cut.py' method='POST'>"
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
 print "<form action='../cgi-bin/hdfs_ls.py' method='POST'>"
 
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
 print "<form action='../cgi-bin/hdfs_cat.py' method='POST'>"
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
 print "<form action='../cgi-bin/hdfs_touch.py' method='POST'>"
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
 print "<form action='../cgi-bin/hdfs_rmr.py' method='POST'>"
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
 print "<form action='../cgi-bin/hdfs_rmdir.py' method='POST'>"
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
 print "<form action='../cgi-bin/hdfs_count.py' method='POST'>"
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
 print "<form action='../cgi-bin/hdfs_lsr.py' method='POST'>"
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
 print "<form action='../cgi-bin/hdfs_setrep.py' method='POST'>"
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
 print "<form action='../cgi-bin/hdfs_chown.py' method='POST'>"
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
 print "<form action='../cgi-bin/hdfs_chmod.py' method='POST'>"
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
 print "<form action='../cgi-bin/hdfs_chgrp.py' method='POST'>"
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
 print "<form action='../cgi-bin/hdfs_cmd.py' method='POST'>"
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
 print "<form action='../cgi-bin/hdfs_safemode.py' method='POST'>"
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
 print "<form action='../cgi-bin/hdfs_spaceQuota.py' method='POST'>"
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
 print "<form action='../cgi-bin/hdfs_clrSpaceQuota.py' method='POST'>"
 
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
 print "<form action='../cgi-bin/hdfs_nameQuota.py' method='POST'>"
 
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
 print "<form action='../cgi-bin/hdfs_clrNameQuota.py' method='POST'>"
 
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
 print "<form action='../cgi-bin/hdfs_du.py' method='POST'>"
 
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
 print "<form action='../cgi-bin/hdfs_dus.py' method='POST'>"
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
 print "<form action='../cgi-bin/hdfs_decommission.py' method='POST'>"
 
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
 print "<form action='../cgi-bin/hdfs_commission.py' method='POST'>"
 
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

elif option == "fsck":
 print "<form action='../cgi-bin/hdfs_fsck.py' method='POST'>"
 
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

elif option == "permissions":
 print "<form action='../cgi-bin/hdfs_permissions.py' method='POST'>"
 
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

elif option == "report":
 print "<form action='../cgi-bin/hdfs_report.py' method='POST'>"
 
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
 print "<form action='../cgi-bin/hdfs_refreshNodes.py' method='POST'>"
 
 print "<br>"
 print "<br>"
 print "<br>"
 print "<input type='submit' value='Continue' style='background-color:white; color:blue; margin-left:950px; background-image:url(data:image/jpg;base64,%s); background-size:45px; background-repeat: no-repeat; padding-left: 40px;'>" %data_uri4
 print "<br>"
 print "<br>"
 print "<br>"
 print "</form>"

elif option=="hive":
 print "<form action='../cgi-bin/hive_cluster.py' method='POST'>"
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

else:
 print option

print "</div>"

