import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

a=input("Please enter the mobile no:")
phone_number=phonenumbers.perse(a)
print(geocoder.description_for_number(phone_number, "en"))
print(carrier.name_for_number(phone_number, "en"))
