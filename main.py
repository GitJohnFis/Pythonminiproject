name = "Twiggy"
leaves = 0
weather = '☀️' #create the weather in Twiggy's simulated world
print(weather)
daily_weather = ['☀️','☁️','☀️'] # set up the weather forcast for 3 days
print(daily_weather)
for day in daily_weather: # go through every day in the forecast
 if day == '☀️':
  light = 2
 else:
  light = 1
  leaves += light + water # Grow Twiggy with light and water so he gets the benefit of both.
 print(light, end = " ")
 for day in daily_weather:
  if day == '☀️':
   tank = tank + 5 # increase the tank level by five when it's sunny
   print("tank level:", tank)
   print('Gotta drink a lot of water!')
light = 1
cover = 1
wind = 10
wind = wind - (5 * cover)
water = 1
for day in range(3)
leaves = leaves + 1
leaves = leaves + light
leaves = leaves + water
light = light - cover
heat = light * 10
print("Light:", light)
print("Heat:", heat)
if leaves > 8:
 print("Growth spurt!")
if leaves == 3:
 print(name, "is a seedling!")
 
  print("leaves:", leaves)
display_simulation()
