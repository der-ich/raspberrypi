#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess, re, locale

locale.setlocale(locale.LC_ALL, "")

def freq():
	"""in Hz"""
	freqstr = subprocess.check_output(["vcgencmd", "measure_clock", "arm"]).replace("\n", "").replace("\r", "")
	freqstr2 = re.search(r'.*frequency\(\d*\)=(.*)', freqstr).group(1)
	return locale.format("%d", int(freqstr2), grouping=True) + " Hz"
		
def temp():
	"""in °C """
	tempstr = subprocess.check_output(["vcgencmd", "measure_temp"]).replace("\n", "").replace("\r", "")
	return re.search(r'.*temp=(.*)', tempstr).group(1).replace("'C", " °C")
		
def volt():
	"""in Volt"""
	voltstr = subprocess.check_output(["vcgencmd", "measure_volts"]).replace("\n", "").replace("\r", "")
	voltstr2 = re.search(r'.*volt=(.*)V', voltstr).group(1)
	return  str(float(voltstr2)) + " V"

print(freq())
print(temp())
print(volt())
