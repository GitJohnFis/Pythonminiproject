name = "Twiggy"
leaves = 0
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
