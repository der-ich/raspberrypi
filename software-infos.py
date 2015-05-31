#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess, re, psutil, platform

def uptime():
	"""Linux Uptime"""
	return re.search(r'.*up\s*(.*),\s*\d*\s*user.*', subprocess.check_output(["uptime"])).group(1)

def load():
	"""System Load of the last 1, 5, 15min in %"""
	m = re.search(r'.*load\s*average:\s*(.*)', subprocess.check_output(["uptime"])[1:])
	if m:
		rtn = ""
		for i in m.group(1).replace(", ", " ").replace(",", ".").split(" "):
			rtn += str(int(float(i)*100))+ "% "
		return rtn
	return ""
	
def osname():
	osstr = ""
	for i in platform.dist():
		if i:
			osstr += i + " "
	return osstr + "(" + subprocess.check_output(["uname", "-o"]).replace("\n", "").replace("\r", "") + ")"

def osarch():
	return platform.machine()
	
def oskernelver():
	return platform.release()
	
def cpuusage():
	return int(psutil.cpu_percent())
	
def nodename():
	return platform.node()
	
def intIP():
  """Device IPs"""
	return subprocess.check_output(["hostname", "-I"]).replace("\n","").replace("\r","")

def extIP():
	return subprocess.check_output(["curl", "-s", "icanhazip.com"]).replace("\n","").replace("\r","")

print(uptime())
print(load())
print(osname())
print(osarch())
print(oskernelver())
print(cpuusage())
print(nodename())
print(intIP())
print(extIP())
