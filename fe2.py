from pywebio.output import *
import tesss
skalagempa = 0
from random import randrange
ifTsunami = True

if tesss.getCity() == tesss.bandungLocation:
    style(put_text("Lokasi anda: "+ tesss.getCity() + ", " + tesss.getCountry()), 'color:red')
    skalaGempa = randrange(10)
    if skalaGempa >= 6:
        if ifTsunami == True:
            x = tesss.findClosestShelter(tesss.shelterList, tesss.userLocation)
            style(put_text("Info Gempa: "+ x + " SR"), 'color:black')
            #print(coordinateToLocation(shelterList,x))
            # print(ifLocationSame(shelterList, x))
            style(put_text("Info Gempa: "+ skalaGempa + " SR"), 'color:black')
        else:
            tesss.stayAtHome()
            ##print(skalaGempa)
            style(put_text("Info Gempa: "+ skalaGempa + " SR"), 'color:black')
    else:
        tesss.stayAtHome()
        print(skalaGempa)
else:
    print ("Anda tidak di bandung")
    print (" ")
    print ("Anda berada di: "+tesss.getCity())