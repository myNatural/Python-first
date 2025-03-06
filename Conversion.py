def convert_meters(km):
  meters=km*1000
  return meters
distance=convert_meters(float(input("Enter distance in kilometers:  ")))
print('The distance in meters is:',distance)