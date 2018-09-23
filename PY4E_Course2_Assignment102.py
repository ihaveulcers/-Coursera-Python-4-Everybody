name = input('Enter file:')
if len(name) <1 : name = 'mbox-short.txt'
handle = open(name)

counts = dict()

for line in handle:
	line = line.rstrip()
	if line == '':
		continue
	splitedline = line.split()
	if splitedline[0] != 'From' :
		continue
	# split time by :   else we'll have the h:m:s
	time = splitedline[5].split(':')
	hour = time[0]
	counts[hour] = counts.get(hour,0) + 1       #create historgram

list = list()

for key,value in counts.items():
	list.append((key,value))

list.sort()

for hour , count in list:
	print (hour, count)
