name = 'mbox-short.txt'
handle = open(name)
senders = dict()

for line in handle:
    if not line.startswith('From '): continue
    line = line.split()
    line = line[1]
    #create an histogram
    senders[line]=senders.get(line,0)+1

topsender = None
sendercount = None

for sender,count in senders.items():
    #1st condition cos zero count at the beginning
    if sendercount is None or count > sendercount:
        topsender = sender
        sendercount = count

print(topsender,sendercount)
