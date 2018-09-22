hour = input('enter hour:')
rate = input('enter rate:')

try:
    h=float(hour)
    r=float(rate)
except:
    print('please enter number')
    quit()

def computepay(h,r):
    if h <= 40:
        pay = h + r
        return  pay
    else:
        pay = (40*r) + ((h-40)*(r*1.5))
        return pay

xp = computepay(h,r)
print(xp)
