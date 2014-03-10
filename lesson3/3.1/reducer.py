import sys

saltesTotal = 0
oldKey = None

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) != 2:
		continue

	thisKey, thisSale = data_mapped

	if oldKey and oldKey != thisKey:
		print("{0}\t{1}".format(oldKey, saltesTotal))
		oldKey = thisKey
		saltesTotal = 0

	oldKey = thisKey
	saltesTotal += float(thisSale)

if oldKey != None:
	print("{0}\t{1}".format(oldKey, saltesTotal))