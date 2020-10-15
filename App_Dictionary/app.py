from phonenumbers import geocoder
ch_number = phonenumbers.parse("+919695502434","CH")
geocoder.description_for_number(ch_number,"en")