from ride_sharing import Ride_sharing
from ride import *
from user import *

pathao = Ride_sharing("Pathao Ride")
rifat = Rider('Rifat khan','rft@gml',33456,'uttora',1500)
pathao.add_rider(rifat)
sifat = Driver('Sifat khan','sft@gml',33125,'abdullahpur')
pathao.add_driver(sifat)
rifat.request_ride(pathao,'Khilkhet','car')
rifat.show_current_ride()
sifat.reach_destination(rifat.current_ride)
print(pathao)