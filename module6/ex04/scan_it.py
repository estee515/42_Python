#!/opt/pyenv/shims/python3

import sys
import re

if len(sys.argv)!=3:
	print("none")
else:
	try:
		count = len(re.findall(sys.argv[1],sys.argv[2]))
		# If count is 0 or an invalid pattern occurred, print "none"
		if count == 0:
			print("none")
		else:
			print(count)
	except re.error:
		print ("none")


