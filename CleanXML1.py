import re

strList[]

with open('reut2-000.sgm') as f:
	for line in f:
		line = re.sub("(&#\d+;)","",line)
		line = re.sub("[^\x20-\x7f]+","",line)
		strList.append(line)
smg = ''.join(strList)