my_dict = {"bookingid": 2384,
"booking": {"firstname": "PRAMOD","lastname": "Dutta","totalprice": 432,"depositpaid": False,
"bookingdates": {"checkin": "2022-01-01","checkout": "2022-01-01"},
"additionalneeds": "Lunch"}
}
print(my_dict['bookingid'])
print(my_dict['booking']['bookingdates']['checkin'])
print(my_dict['booking']['bookingdates']['checkout'])
