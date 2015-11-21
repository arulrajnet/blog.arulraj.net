:title: Docker Monitoring CPU and Memory Usage
:slug: docker-monitoring-cpu-and-memory-usage
:date: 2015-07-08 11:10:20
:tags: 
:category: Docker
:author: Arul
:lang: en
:status: draft
:summary: 




for line in `docker ps | awk '{print $1}' | grep -v CONTAINER`; do docker ps | grep $line | awk '{printf $NF" "}' && echo $(( `cat /sys/fs/cgroup/memory/docker/$line*/memory.usage_in_bytes` / 1024 / 1024 ))MB ; done


To get list of process running under docker

cat /sys/fs/cgroup/memory/docker/$line*/cgroup.procs

ps -p PID -o %cpu,%mem,cmd

top -c -p PID


names=""; for line in `docker ps | awk '{print $NF}' | grep -v NAMES`; do names=$names" $line"; done; echo $names; docker stats $names;