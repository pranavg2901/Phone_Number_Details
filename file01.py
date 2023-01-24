import phonenumbers

from phonenumbers import timezone,geocoder,carrier

number = input("Enter Your Number with +__ : ")
pho = phonenumbers.parse(number)
time = timezone.time_zones_for_number(pho)
car = carrier.name_for_number(pho,"en")
gec = geocoder.description_for_number(pho,'en')
print(pho)
print(time)
print(car)
print(gec)
