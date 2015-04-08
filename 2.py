#!/usr/bin/python
# -*- coding: utf-8 -*-
import re


resulthash = {}
patternIp = re.compile(r'inet .*?:((?<![\.\d])(?:\d{1,3}\.){3}\d{1,3}(?![\.\d]))')
patternNa = re.compile(r'(eth\d+?|tr\d+?|fddi\d+?|ppp\d+?)')
flag = 0;
with open("ifconfig_log.txt",'r') as f:
	line =  f.readline()
	while line:
		resultNa = re.findall(patternNa, line)
		resultIp = re.findall(patternIp, line)
		if resultNa:
			#print resultNa
			tmpNa = resultNa
			resulthash[tmpNa[0]] = 0
			#flag = 1;
		if resultIp:
			#print resultIp
			if resulthash[tmpNa[0]] == 0:
				resulthash[tmpNa[0]] = resultIp[0]

		line =  f.readline()

print resulthash
