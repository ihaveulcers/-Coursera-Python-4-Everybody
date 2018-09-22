h = input('enter hour:')
r = input('enter rate:')
hour = float(h)
rate = float(r)
if hour <= 40:
    gross_pay = hour * rate
    print(gross_pay)
else:
    OThour = float(hour - 40)
    gross_pay = (40 * rate) + (OThour*(rate * 1.5))
    print(gross_pay)
