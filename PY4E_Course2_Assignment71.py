fname = input('enter file name:')
fhand = open(fname)
string = fhand.read()
for x in string:
    x = x.rstrip()
print (string.upper())
