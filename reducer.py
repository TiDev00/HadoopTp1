import sys
from collections import OrderedDict

remorByRue = {}

for line in sys.stdin:
	line = line.strip()
	rue, total = line.split("\t", 1)
	try:
		total = int(total)
	except ValueError:
		pass
	try:
		remorByRue[rue] = remorByRue[rue] + total
	except:
		remorByRue[rue] = total
tri = OrderedDict(sorted(remorByRue.items(), key=lambda t: t[1], reverse=True))
for rue in tri.keys():
	print("%s\t%s" % (rue, remorByRue[rue]))
