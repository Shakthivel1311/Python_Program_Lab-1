colors = ["Black", "Red", "Maroon", "Yellow"]
codes = ["000000", "FF0000", "800000", "FFFF00"]

result = []
for i in range(len(colors)):
  result.append({"colorName": colors[i], "colorCode": codes[i]})

print(result)