# We are going to request the server for the predictions.

#import  packages
import requests

#set url for localhost
url = 'http://localhost:5000/api'

# you can use the url when deployed in the online server
url2 = "http://djangoposts.pythonanywhere.com/api"

#send request
state = input("state")
district = input("district")
market = input("market")
commodity = input("commodity")
variety = input("variety")



r = requests.post(url2,json={'state':str(state),'district':str(district),'market':str(market),'commodity':str(commodity),'variety':str(variety)})

#print result
print("The price of crop is$ {}".format(r.json()))
