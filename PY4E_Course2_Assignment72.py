fname = input('Enter file name:')
fhand = open(fname)
total = 0
count = 0
for line in fhand:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    pos = line.find(" ")
    val = line[pos:].rstrip()
    val = float(val)
    count = count + 1
    total = total + val

print ("Average spam confidence:", total/count )
