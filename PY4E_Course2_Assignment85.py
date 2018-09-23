fhand = open('mbox-short.txt')
count = 0

for line in fhand:
    if line.startswith('From '):    #find line that starts with 'From'
        email = line.split()        #parse the From line
        print(email[1])
        count = count + 1

print('There were',count, 'lines in the file with From as the first word')


##########################
###    alternatively   ###
##########################

fhand = open('mbox-short.txt')
count = 0

for line in fhand:
    words = line.split()

    #Guardian pattern in a compound statement, skip for blank line
    if len(words) < 1 or line == '' or words[0] !='From':
        continue

    print(words[1])
    count = count + 1

print('There were',count, 'lines in the file with From as the first word')
