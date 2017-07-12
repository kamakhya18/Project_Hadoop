#!/usr/bin/python

import os,commands

docker = '03eae6414dce\n96493dd26e5d\ne1a3ce8ef2ef\n23dfcf3fb24b\ne31be6c27520'
#docker = commands.getoutput("docker ps -a -q")
docker = docker.split("\n")

for d in docker:
 os.system("docker start "+d)

print "Docker images started"

#Stop all dockers
#docker stop $(docker ps)
