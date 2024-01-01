# Python dictionary with keys having multiple inputs

# dictionary containing longitude and latitude of places
places = {("19.07'53.2", "72.54'51.0"):"Mumbai", \
		("28.33'34.1", "77.06'16.6"):"Delhi"}

print(places)
print('\n')

# Traversing dictionary with multi-keys and creating
# different lists from it
lat = []
long = []
plc = []
for i in places:
 print('lat: ',i[0])
 lat.append(i[0])
 long.append(i[1])
 plc.append(places[i[0], i[1]])

print(lat)
print(long)
print(plc)
