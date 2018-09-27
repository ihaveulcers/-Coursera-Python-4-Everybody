import re

sum = 0

file = open('regex_sum_138829.txt', 'r')
for line in file:
    #find at least one number in line
    numbers = re.findall('[0-9]+', line)
    if not numbers:
        continue
    else:
        for number in numbers:
            # += means add another value to the variable's value and assigns new value to the varible
            sum += int(number)

print(sum)
