largest = None
smallest = None

while True:
    svalue = input('enter a number:')
    if svalue == "done":
        break
    try:
        ivalue = int(svalue)
    except:
        print('Invalid input')
        continue

    if largest is None or ivalue > largest :
        largest = ivalue
    if smallest is None or ivalue < smallest :
        smallest = ivalue



print ('Maximum is',largest)
print ('Minimum is',smallest)
