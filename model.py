import reverse_geocoder as rg
import pprint

location = (12, 30) # get user location
bandungLocation = (12, 30) # Bandung coordinate
skalaGempa = 7 # gempanya berapa skalanya
ifTsunami = True # apakah akan ada tsunami
 
def reverseGeocode(coordinates):
    result = rg.search(coordinates)
     
    # result is a list containing ordered dictionary.
    pprint.pprint(result)

def getNearestShelter():
    print ("McD Dago")

def stayAtHome():
    print("Tidak perlu ke Shelter")
 
# # Driver function
# if __name__=="__main__":
#      
#     # Coordinates tuple.Can contain more than one pair.
#     coordinates =(-6.875796655127494, 107.62629536051634)
#      
#     reverseGeocode(coordinates)

# modelnya gini kira2
if location == bandungLocation:
    if skalaGempa > 6:
        if ifTsunami == True:
            getNearestShelter()
        else:
            stayAtHome()
    else:
        stayAtHome()
else:
    print ("anda tidak di bandung")
