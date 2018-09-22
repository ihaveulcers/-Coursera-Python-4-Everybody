#romeo.txt
#But soft what light through yonder window breaks
#It is the east AND Juliet is the sun
#Arise fair sun AND kill the envious moon
#Who is already sick and pale with grief


romeo = open('romeo.txt') 
list = list()

#add all word into list, have duplication
for word in romeo:
    list = list + word.split()
    list.sort()

#create an empty list
empty=[]

#add word into empty list to get rid of the duplication
for word in list:
    if word not in empty:
        empty.append(word)

print(empty)
