#conditional construct
#where we wish to check some condition

total = 349
#discount = 40
"""

#regular if-else

if total >= 500:
    print("flat 40% off")
else:
    print("sorry no discounts")
"""

#ladder if else
"""
if total >100 and total < 200:
    print("flat 10% discount")
elif total >200 and total< 400:
    print("flat 20% discount")
elif total >400 and total < 500:
    print("flat 40% discount")
else:
    print("flat 50% discount")
"""
#nested if else

isInternetConnected = True
isGPSConnected = False

if isInternetConnected:
    print("you can browse the internet")
    if isGPSConnected:
        print("you can navigate using google maps")
else:
    print("connect to gps to navigate using google maps")






