import os
with open('ipraw.txt', 'r') as f:
	lines = f.readlines()

lines = [line.replace('		', '') for line in lines]

with open('ip.txt', 'w') as f:
	f.writelines(lines)
os.startfile("CloudflareSpeedTest.exe")